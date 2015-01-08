import os

DEFAULT_TEMPLATES_DIR = '/usr/libexec/os-apply-config/templates'
DEFAULT_OS_CONFIG_FILES_PATH = '/var/lib/os-collect-config/os_config_files.json'
OS_CONFIG_FILES_PATH_OLD = '/var/run/os-collect-config/os_config_files.json'

DEFAULT_OUTPUT = os.sep

def sanitize_file(path):
	"""
	Does nothing on *nix
	"""
    return path

def is_executable(path):
    return os.path.isfile(path) and os.access(path, os.X_OK)