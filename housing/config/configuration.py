from housing.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainingConfig,ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig
from housing.util.util import read_yaml_file
from housing.constant import *
from housing.exception import HousingException
from housing.logger import logging
import sys

class Configuration:

    def ___init__(self, config_file_path:str = config_file_path,
                  current_timestamp:str = Current_Timestamp) -> None:
        self.Config_info = read_yaml_file(file_path = config_file_path)
        self.training_pipeline_config = self.get_training_pipeline_config()
        self.timestamp = current_timestamp
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        pass

    def get_data_validation_config(self)-> DataValidationConfig:
        pass

    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass

    def get_model_tariner_config(self) -> ModelTrainingConfig:
        pass

    def get_model_evaluation_config(self)-> ModelEvaluationConfig:
        pass
    def get_model_pusher(self)-> ModelPusherConfig:
        pass
    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(Root_dir,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])

            training_pipeline_config =  TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipeline config :{training_pipeline_config}")
            return training_pipeline_config

        except Exception as e:
            raise HousingException(e,sys) from e


