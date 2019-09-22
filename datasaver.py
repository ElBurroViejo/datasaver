import yaml
import shutil
from pathlib import Path
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

config_path = Path.home().joinpath("datasaver.yaml")

with open(config_path) as yaml_file:
    config = yaml.load(yaml_file)

source_path = config["source_path"]
destination_path = config["destination_path"]

Path(destination_path).mkdir(exist_ok=True)
for file_type in config["file_types"]:
    Path(destination_path).joinpath(
            f"{file_type}").mkdir(exist_ok=True)

    for file_path in Path(source_path).glob(f"**/*.{file_type}"):
        fuji_folder = file_path.parent.parts[-1]
        file_name = file_path.parts[-1]
        path_to_file = Path(destination_path).joinpath(
            f"{file_type}/{fuji_folder}/{file_name}"
        )
        Path(destination_path).joinpath(
            f"{file_type}/{fuji_folder}").mkdir(exist_ok=True)

        if not Path(path_to_file).exists():
            logging.info(f"moving {file_path}")
            shutil.copy2(file_path, path_to_file)

