from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT = '-e .'

__version__= "0.0.1"
REPO_NAME = "Implementing-modules"
PKG_NAME="Mongo-Connect"
AUTHOR_USER_NAME = "NaveenPoliasetty"
AUTHOR_EMAIL = "iamnaveenpoliasetty@gmail.com"

def get_require(file_name)->List[str]:
    requirements = []
    with open(file_name) as f:
        requirements = f.readlines()
        requirements =[req.replace("\n",'')for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name=PKG_NAME,
    verison=__version__,
    author=AUTHOR_USER_NAME,
    description='A python package for connecting with database',
    url=F'https://github.com{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        "Bug Tracker": f"https://github.com{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=find_packages(where='src'),
    intstall_requires=get_require('./requirements_dev.txt'),
)