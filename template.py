import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [
    "src/__init__.py",
    'src/components/mood/__init__.py',
    'src/components/quotes/__init__.py',
    'src/components/spotifymusic/__init__.py',
    'src/utilis/__init__.py',
    'src/utilis/common.py',
    'src/common/__init__.py',
    'src/entity/__init__.py',
    'src/entity/config_entity.py',
    'src/config/__init__.py',
    'src/config/configuration.py',
    'src/pipeline/__init__.py',
    'src/logger.py',
    'src/exception.py',
    'templates/index.html',
    'requirements.txt',
    'setup.py',
    'config.yaml',
    'params.yaml',
    'main.py',
    'app.py',
    'setup.py'
]

for files in list_of_files:
    filepath = Path(files)
    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating file directory: {filedir}')

    if (not os.path.exists(filename)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Creating file path: {filepath}')

    else:
        logging.info(f'{filename} already exists')