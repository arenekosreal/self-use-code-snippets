# Come from this and I modified to make it work on my system:
# https://stackoverflow.com/a/5839291/14209295
import pkg_resources
from subprocess import call
packages = list()
for dist in pkg_resources.working_set:
    if dist.project_name.startswith("-")==False:
        packages.append(dist.project_name)
call("pip install --upgrade " + ' '.join(packages), shell=True)
