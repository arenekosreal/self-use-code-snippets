import pkg_resources
from subprocess import call
packages = list()
for dist in pkg_resources.working_set:
    if dist.project_name.startswith("-")==False:
        packages.append(dist.project_name)
call("pip install --upgrade " + ' '.join(packages), shell=True)