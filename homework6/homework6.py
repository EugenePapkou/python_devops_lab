import json
import os
import sys
import yaml

dict_info = {}

s = sys.version
print("Version:", s)
dict_info["Version"] = s

try:
    s = os.environ["VIRTUAL_ENV"].split("/")[7]
    print("Name (alias) of virtual environment:", s)
    dict_info["Name"] = s
    s = os.environ["VIRTUAL_ENV"]
    print("Virtual environment:", s)
    dict_info["virtenv"] = s
except Exception:
    print("Here's no virtual environment")

s = sys.executable
print("Python executable location:", s)
dict_info["exec_loc"] = s

s = os.popen("which pip").read()
print("pip location:", s)
dict_info["pip_loc"] = s

s = os.path.realpath(sys.executable)
print("PYTHONPATH:", s)
dict_info["pyth_path"] = s

s = os.popen("pip list").read()
print("Installed packages: name, version\n", s)
dict_info["pip_list"] = s

s = next(i for i in sys.path if 'site-packages' in i)
print("Site-packages location:", s)
dict_info["site_pack_loc"] = s

s = os.popen("pyenv versions").read()
print("All python versions and environments:\n", s)
dict_info["all_pyenv"] = s

with open("python_info.json", 'a') as json_file:
    json.dump(dict_info, json_file)

with open("python_info.yaml", 'a') as yml_file:
    yaml.dump(dict_info, yml_file, default_flow_style=False)
