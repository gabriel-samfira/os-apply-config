import os

ROOT_DIR = "C:\\tripleo"

DEFAULT_TEMPLATES_DIR = os.path.join(ROOT_DIR, 'libexec', 'os-apply-config', 'templates')
DEFAULT_OS_CONFIG_FILES_PATH = os.path.join(ROOT_DIR, 'lib', 'os-collect-config', 'os_config_files.json')
# for compatibility
OS_CONFIG_FILES_PATH_OLD = DEFAULT_OS_CONFIG_FILES_PATH

DEFAULT_OUTPUT = os.path.join(os.environ.get("SYSTEMDRIVE", "C:"), os.sep)


def _has_exec_ext(path):
    path = path.lower()
    extensions = os.environ.get("PATHEXT", "").split(os.pathsep)
    for i in extensions:
        if path.endswith(i.lower()):
            return (True, i.lower())
    return (False, "")

def sanitize_file(path):
    path = path.lower()
    ok, ext = _has_exec_ext(path)
    if ok:
        return path.rstrip(ext)
    return path

def is_executable(path):
    ok, ext = _has_exec_ext(path)
    return ok