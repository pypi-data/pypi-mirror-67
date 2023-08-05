from enum import Enum
import os
from os.path import join
import shutil
import datetime
from pprint import pprint
import sys
from .ds import ds
import torch
from torch.utils.tensorboard import SummaryWriter

sys.path.insert(0, '..')


def shape(*args):
    for idx, item in enumerate(args):
        print(idx, getattr(item, 'shape', 'No Shape Defined'))


class AL_ENVS(Enum):
    COLAB = 0
    LOCAL = 1


conf = {}


def datasets(func, transforms=None):
    return getattr(conf['AL_DATASETS'], func, lambda x: "Method not fuond!")(transforms)


def set_tb_log_dir_with_history(log_dir_path, datetime_format="%Y%m%d-%H%M%S"):
    """
        For each new experiment, create a new directory with current
        datetime to store tensorboard logs.
    """
    log_dir = os.path.join(
        log_dir_path, datetime.datetime.now().strftime(datetime_format))

    if os.path.isdir(log_dir):
        raise "Directory name clashes with old logs."
    else:
        print(
            'Info: New directory will be created and setup for tensorboard.')
        os.makedirs(log_dir, exist_ok=True)


def set_tb_log_dir_with_no_history(log_dir_path):
    """
        For each new experiment, discard old logs, and use the same path again.
    """
    log_dir = os.path.join(
        log_dir_path)

    print('Info: Removing old logs, and setup log directory for tensorboard.')
    rm_logs(log_dir)
    os.makedirs(log_dir, exist_ok=True)


def set_defaults(settings={}, print_settings=True):
    """
        Set varilable in the order of presedence.
        1. There are defaults for everything.
        2. settings dict override defaults.
        3. Environment Overrides settings.

    """
    global conf
    print("Info: Setting up defalut log directory for tensorboard.")
    AL_EXPERIMENT = os.environ.get(
        'AL_EXPERIMENT', settings.get('AL_EXPERIMENT', 'default-experiment'))
    AL_ENV = os.environ.get(
        'AL_ENV', settings.get('AL_ENV', None))
    AL_BASE_PATH = os.environ.get(
        'AL_BASE_PATH', settings.get('AL_BASE_PATH', './'))
    AL_DEFAULT_LOG_DIR = os.environ.get(
        'AL_DEFAULT_LOG_DIR', settings.get('AL_DEFAULT_LOG_DIR', join(AL_BASE_PATH, AL_EXPERIMENT, 'logs')))
    AL_DEFAULT_DATA_DIR = os.environ.get(
        'AL_DEFAULT_DATA_DIR', settings.get('AL_DEFAULT_DATA_DIR', join(AL_BASE_PATH, AL_EXPERIMENT, 'data')))
    AL_EXPERIMENT_DIR = os.environ.get(
        'AL_EXPERIMENT_DIR', settings.get(
            'AL_EXPERIMENT_DIR', join(AL_BASE_PATH, AL_EXPERIMENT)))

    if AL_ENV is None:
        try:
            import google.colab
            AL_ENV = AL_ENVS.COLAB
        except:
            AL_ENV = AL_ENVS.LOCAL
        assert isinstance(
            AL_ENV, AL_ENVS), "Environment must be of type AL_ENVS"

    AL_LOG_MODE = os.environ.get('AL_LOG_MODE', 'history')
    if AL_LOG_MODE == 'history':
        set_tb_log_dir_with_history(AL_DEFAULT_LOG_DIR)
    else:
        set_tb_log_dir_with_no_history(AL_DEFAULT_LOG_DIR)

    _ = {
        'AL_ENV': AL_ENV,
        'AL_DEFAULT_LOG_DIR': AL_DEFAULT_LOG_DIR,
        'AL_DEFAULT_DATA_DIR': AL_DEFAULT_DATA_DIR,
        'AL_BASE_PATH': AL_BASE_PATH,
        'AL_LOG_MODE': AL_LOG_MODE,
        'AL_ENV': AL_ENV,
        'AL_DATASETS': ds(AL_DEFAULT_DATA_DIR),

        'device': "cuda" if torch.cuda.is_available() else "cpu",
        'tensorboard': SummaryWriter(log_dir=AL_DEFAULT_LOG_DIR)
    }

    conf = _
    if print_settings:
        pprint(_)
    return _


def is_colab():
    """
        A function for testing weather the current environment is colab
        ----
        Parameters
            - None
        Return
            - Boolean
    """
    return conf['AL_ENV'] == AL_ENVS.COLAB


def rm_logs(log_path):
    if os.path.isdir(log_path):
        shutil.rmtree(log_path)
        return True
    return False


def load_model(experiment_path):
    """
        Load model from default model location with name.
        ----
        Parameters
            - str: experiment_name
        Return
            - nn.Module: net
            - tuple    : (train_set, test_set)
    """
    pass


def store_model(net, dataset_state):
    """
        Store the given model at default model location.
        ----
        Parameters
            - None
        Return
            - Boolean
    """
    pass
