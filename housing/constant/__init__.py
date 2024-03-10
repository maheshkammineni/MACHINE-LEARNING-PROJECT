import os 

Root_dir = os.getcwd() # to get current work directory

Config_dir =  os.path.join(Root_dir)
config_file_name = "config.yaml"
config_file_path = os.path.join(Root_dir,Config_dir, config_file_name) 

from datetime import datetime

Current_Timestamp = f"{datetime.now().strftime('%Y-%m-%d')}"

# Training pipeline releated variable

TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "atrifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"