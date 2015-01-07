import platform

if platform.system() == "Windows":
	from os_apply_config.paths_windows import *
else:
	from os_apply_config.paths_nix import *