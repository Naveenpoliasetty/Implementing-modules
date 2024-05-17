import os
import logging
from pathlib import Path

package_name = 'mongodb_connect'

list_of_files = [
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongocrud.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "tests/integration/int.py"
    "init__setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "expirement/expirements.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir!= "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if not filepath.exists() or (os.path.getsize(filepath) == 0):
        with filepath.open('w') as f:
            pass  # create an empty file