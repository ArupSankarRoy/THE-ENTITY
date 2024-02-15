import sys , os
from entity_main_package.logger import logging
from entity_main_package.exception import AppException
from entity_main_package.components.data_ingestion import DataIngestion
from entity_main_package.components.data_validation import DataValidation
from entity_main_package.components.model_trainer import ModelTrainer
from entity_main_package.entity.config_entity import (DataIngestionConfig , 
                                                 DataValidationConfig , 
                                                 ModelTrainerConfig)

from entity_main_package.entity.artifacts_entity import (DataIngestionArtifact ,
                                                     DataValidationArtifact , 
                                                     ModelTrainerArtifact)
import yaml

class TrainPipeline:
    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()
    
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from URL")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise AppException(e, sys)
        
    def start_data_validation(self ,data_ingestion_artifact:DataIngestionArtifact )-> DataValidationArtifact:
        try:
            logging.info("Entered the start_data_validation method of TrainPipeline class")
            logging.info("Getting the data from URL")
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config= self.data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_validation_artifact

        except Exception as e:
            raise AppException(e , sys)

    def start_model_trainer(self)-> ModelTrainerArtifact:
        try:
            model_trainer=ModelTrainer(
                model_trainer_config=self.model_trainer_config
            )
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        except Exception as e:
            raise AppException(e , sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            if data_validation_artifact.validation_status == True:
                # Define the paths
                path = 'artifacts/data_ingestion/feature_store/data.yaml'
                path1 = 'artifacts/data_ingestion/feature_store/train/images'
                path2 = 'artifacts/data_ingestion/feature_store/valid/images'

                # Load the data from data.yaml
                with open(path, 'r') as file:
                    data = yaml.safe_load(file)

                # Update the paths
                data['train'] = path1
                data['val'] = path2

                # Save the updated data back to data.yaml
                with open(path, 'w') as file:
                    yaml.dump(data, file, default_flow_style=False)
                model_trainer_artifact = self.start_model_trainer()
            else:
                raise Exception('Your data is not in correct format')
               
        except Exception as e:
            raise AppException(e , sys)
        


