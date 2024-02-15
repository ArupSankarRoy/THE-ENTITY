import os,sys
from ultralytics import YOLO
import yaml
from entity_main_package.logger import logging
from entity_main_package.exception import AppException
from entity_main_package.entity.config_entity import ModelTrainerConfig
from entity_main_package.entity.artifacts_entity import ModelTrainerArtifact



class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            path = 'artifacts/data_ingestion/feature_store/data.yaml'
            current_dir = os.getcwd()
            converted_dir = os.path.normpath(current_dir).replace(os.sep, '/')

            # Run YOLO command
            command = f"cd '{converted_dir}/' && yolo task=detect mode=train model={self.model_trainer_config.weight_name} data={path} epochs={self.model_trainer_config.no_epochs}"
            os.system(command)

            # Check if the 'runs' directory is created
            if not os.path.exists('runs'):
                print('runs not had created')

            # Create 'yolov8' directory
            os.makedirs('yolov8', exist_ok=True)

            # Use absolute paths for the 'cp' commands
            source_file = os.path.abspath('runs/detect/train/weights/best.pt')
            os.system(f"cp {source_file} yolov8/")

            # Create model_trainer_dir if it doesn't exist
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)

            # Copy the trained model to model_trainer_dir
            os.system(f"cp {source_file} {os.path.abspath(self.model_trainer_config.model_trainer_dir)}/")

            # Remove 'runs' directory
            os.system("rm -rf runs")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov8/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise AppException(e, sys)