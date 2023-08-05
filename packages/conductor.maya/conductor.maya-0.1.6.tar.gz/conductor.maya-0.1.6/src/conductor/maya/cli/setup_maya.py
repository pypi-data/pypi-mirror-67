#!/usr/bin/env python


import datetime
import os
import subprocess 
import errno
import sys
from email.parser import Parser
# import argparse


"""
Strategy here is 

If location flag set - determine location of maya AND make sure core is there too.
If maya not there - bail
If core not there - search for core with pip
If core not findable - bail

If location flag not set - determine location of maya AND core with pip.
If either unavailable - bail
 
"""


def main():
    print "Setting up Maya module file..."
 
    directory =  sys.argv[1] if len(sys.argv) > 1 else None
    maya_info =  get_package_info("conductor.maya",directory)
    core_info =  get_package_info("conductor.core",directory)

    print maya_info
    print core_info
    

    mod_dir=None
    try:
        mod_dir = get_maya_modules_dir()
    except OSError as ex:
        print ex
        sys.stderr.write(ex.message)
        sys.stdout.write("Can't access any module directory.\n")
        sys.stdout.write("Please note the following information and then consult docs.conductortech.com and search 'setup_maya'.\n")
        
    mod_file = write_module_file(core_info, maya_info, mod_dir)
    sys.stdout.write("conductor.maya package location and version: {} {}.\n".format(*maya_info))
    sys.stdout.write("conductor.core package location and version: {} {}.\n".format(*core_info))
    sys.stdout.write("Wrote module file: {}.\n".format(mod_file))
    msg= """
Thanks for installing Conductor-Maya!
The next time you run Maya you can load the Conductor plugin from the Plugin Manager. 
Windows->Settings/Preferences->Plug-in Manager.
Once loaded, you'll see a Conductor menu in the main menu bar, where you can configure a submission.

For more info, visit https://docs.conductortech.com and search for setup_maya. 
    """
    sys.stdout.write(msg)
    sys.exit(0)
 


def write_module_file(core_info, maya_info, modules_directory=None):

    paths = list(set([core_info[0],maya_info[0]]))
    python_paths = ":".join(paths)
    maya_mod_path = os.path.join(maya_info[0], "conductor", "maya")
    content = "+ conductor {} {}\n".format(maya_info[1], maya_mod_path)
    content += "PYTHONPATH +={}\n".format(python_paths)

    module_file = None
    if modules_directory:
        module_file = os.path.join(modules_directory,"conductor.mod" )
        with open(module_file, "w") as fobj:
            fobj.write(content)
    else:
        sys.stdout.write(content)
        
    return module_file

def get_maya_modules_dir():
    """Get Maya app dir from standard locations, unless overridden."""

    app_dir = os.environ.get("MAYA_APP_DIR")
    if not app_dir:
        home = os.path.expanduser("~")
        platform = sys.platform
        if platform == "darwin":
            tail = "Library/Preferences/Autodesk/maya"
        elif platform in ["win32", "msys", "cygwin"]:
            tail = "Documents\maya"
        else:  # linux
            tail = "maya"    
        app_dir = os.path.join(home, tail)

    mod_dir = os.path.join(app_dir,  "modules")
    ensure_directory(mod_dir)
    return mod_dir


def ensure_directory(directory):
    try:
        os.makedirs(directory)
    except OSError as ex:
        if ex.errno == errno.EEXIST and os.path.isdir(directory):
            pass
        else:
            raise

def get_package_info(name, directory=None):

    # try given directory
 
    relpath =os.path.join(*name.split("."))





    if directory:
        directory = os.path.abspath(os.path.realpath(os.path.expanduser(directory)))
        version_file = os.path.join(directory, relpath, "__version__.py")
        if os.path.isfile(version_file):
            version = get_version(version_file)
            return  (directory, version) 
        else:
            raise ValueError("Can't find version file under the given directory {}".format(version_file))

    # have a look in current directory
    directory = os.getcwd()


    print directory
    print relpath
 
    # version_file = os.path.join(directory, relpath , "__version__.py")
    
    version_file = os.path.join(directory, relpath , "__version__.py")
    if os.path.isfile(version_file):
        version = get_version(version_file)
        return  (directory, version) 
    
    # try pip
    p = subprocess.Popen(["pip", "show", name ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = p.communicate(b"input data that is passed to subprocess' stdin")
    data = Parser().parsestr(output)
    if "Location" in data:
        return (data["Location"], data.get("Version")) 
    else:
        raise ValueError("Can't find Conductor-Maya package in the current directory, or with pip.")



def get_version(version_file):
    about = {"__version__":"any"}
    if os.path.isfile(version_file):
        with open(os.path.join(version_file)) as f:
            exec(f.read(), about)
    return about["__version__"]



if __name__ == '__main__':
    main()

