# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Module for handling SDK dependencies required during Ensemble iterations."""
import os
from typing import Optional

from azureml import _async
from azureml.core import Run
from azureml.exceptions import AzureMLException

from azureml.automl.core.shared import logging_utilities
from azureml.automl.runtime import ensemble_base
from azureml.automl.runtime._offline_automl_run import _OfflineAutoMLRun
from azureml.train.automl import _logging  # type: ignore
from azureml.train.automl._azureautomlsettings import AzureAutoMLSettings
from azureml.train.automl.exceptions import ConfigException


class EnsembleHelper(object):
    """
    Helper class for ensembling previous AutoML iterations.

    This helper class is used for handling SDK dependencies used during Ensemble iterations (like model downloading)


    :param automl_settings -- The settings for this current experiment
    :param ensemble_run_id -- The id of the current ensembling run
    :param experiment_name -- The name of the current Azure ML experiment
    :param workspace_name --  The name of the current Azure ML workspace where the experiment is run
    :param subscription_id --  The id of the current Azure ML subscription where the experiment is run
    :param resource_group_name --  The name of the current Azure resource group
    """

    DEFAULT_DOWNLOAD_MODELS_TIMEOUT_IN_SEC = 5 * 60  # 5 minutes

    def __init__(self,
                 automl_settings: AzureAutoMLSettings,
                 ensemble_run_id: str,
                 experiment_name: str,
                 workspace_name: str,
                 subscription_id: str,
                 resource_group_name: str,
                 current_run: Optional[_OfflineAutoMLRun] = None):
        """Create an Ensemble pipeline out of a collection of already fitted pipelines.

        :param automl_settings -- The settings for this current experiment
        :param ensemble_run_id -- The id of the current ensembling run
        :param experiment_name -- The name of the current Azure ML experiment
        :param workspace_name --  The name of the current Azure ML workspace where the experiment is run
        :param subscription_id --  The id of the current Azure ML subscription where the experiment is run
        :param resource_group_name --  The name of the current Azure resource group
        :param current_run --  The current run
        """
        # input validation
        if automl_settings is None:
            raise ConfigException.create_without_pii("automl_settings parameter should not be None")

        if ensemble_run_id is None:
            raise ConfigException.create_without_pii("ensemble_run_id parameter should not be None")

        if experiment_name is None:
            raise ConfigException.create_without_pii("experiment_name parameter should not be None")

        if subscription_id is None:
            raise ConfigException.create_without_pii("subscription_id parameter should not be None")

        if resource_group_name is None:
            raise ConfigException.create_without_pii("resource_group_name parameter should not be None")

        if workspace_name is None:
            raise ConfigException.create_without_pii("workspace_name parameter should not be None")

        self._automl_settings = automl_settings
        self._ensemble_run_id = ensemble_run_id
        self._experiment_name = experiment_name
        self._subscription_id = subscription_id
        self._resource_group_name = resource_group_name
        self._workspace_name = workspace_name
        self._current_run = current_run

        parent_run_id_length = self._ensemble_run_id.rindex("_")
        self._parent_run_id = self._ensemble_run_id[0:parent_run_id_length]

        # for potentially large models, we should allow users to override this timeout
        if hasattr(self._automl_settings, "ensemble_download_models_timeout_sec"):
            # TODO: Can this be converted into a real attribute?
            self._download_models_timeout_sec = \
                self._automl_settings.ensemble_download_models_timeout_sec
        else:
            self._download_models_timeout_sec = self.DEFAULT_DOWNLOAD_MODELS_TIMEOUT_IN_SEC

    def download_fitted_models_for_child_runs(self, logger, child_runs, model_remote_path):
        """Override the base implementation for downloading the fitted pipelines in an async manner.

        :param logger -- logger instance
        :param child_runs -- collection of child runs for which we need to download the pipelines
        :param model_remote_path -- the remote path where we're downloading the pipelines from
        """
        with _async.WorkerPool() as worker_pool:
            task_queue = _async.TaskQueue(worker_pool=worker_pool,
                                          _ident="download_fitted_models",
                                          _parent_logger=logger)
            index = 0
            tasks = []
            for run in child_runs:
                task = task_queue.add(ensemble_base.EnsembleBase._download_model,
                                      run,
                                      index,
                                      model_remote_path,
                                      logger)
                tasks.append(task)
                index += 1
            try:
                task_queue.flush(source=task_queue.identity, timeout_seconds=self._download_models_timeout_sec)
            except AzureMLException as e:
                msg = "Failed to download {} models within {} seconds."
                msg += "Proceeding with only {} models"
                logging_utilities.log_traceback(e, logger, is_critical=False)
                logger.warning(msg.format(len(tasks),
                                          self._download_models_timeout_sec,
                                          len(list(task_queue.results))))
            return [task.wait() for task in tasks if task.done()]

    def get_ensemble_and_parent_run(self):
        """Return a tuple (ensemble_run_instance, parent_run_instance)."""

        if isinstance(self._current_run, _OfflineAutoMLRun):
            return self._current_run, None

        # we'll instantiate the current run from the environment variables
        ensemble_run = Run.get_context()
        parent_run = Run(ensemble_run.experiment, self._parent_run_id)

        return ensemble_run, parent_run

    def get_logger(self):
        """Return a logger instance."""
        log_file_name = 'ensemble.log' if not os.path.exists(self._automl_settings.debug_log) else \
            self._automl_settings.debug_log
        logger = _logging.get_azureml_logger(automl_settings=self._automl_settings, parent_run_id=self._parent_run_id,
                                             child_run_id=self._ensemble_run_id, log_file_name=log_file_name)

        return logger
