import os

ROOT_DIR = "C:\\tripleo"

DEFAULT_TEMPLATES_DIR = os.path.join(ROOT_DIR, 'libexec', 'os-apply-config', 'templates')
DEFAULT_OS_CONFIG_FILES_PATH = os.path.join(ROOT_DIR, 'lib', 'os-collect-config', 'os_config_files.json')
# for compatibility
OS_CONFIG_FILES_PATH_OLD = DEFAULT_OS_CONFIG_FILES_PATH