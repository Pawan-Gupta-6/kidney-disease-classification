import os
from pathlib import Path
import logging
#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
project_name = 'cnnClassifier'

list_of_file = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constans/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirments.txt",
    "setup.py",
    "research/trials.txt",
    "templates/index.html"
    
]


for filepath in list_of_file:
    filepath=Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file:{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file:{filepath}")


    else:
        logging.info(f"{filename} is already exist")            

