import os , sys
import shutil
from entity_main_package.logger import logging
from entity_main_package.exception import AppException
from entity_main_package.entity.config_entity import DataValidationConfig
from entity_main_package.entity.artifacts_entity import (DataIngestionArtifact,DataValidationArtifact)

# DataIngestionArtifact this returns,
# class DataIngestionArtifact:
#    data_zip_file_path : str
#    feature_store_path : str
# this  feature_store_path : str i need so i can check in that path the files are avilable in that directory or not ?


class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise AppException(e, sys) 
        


    
    def validate_all_files_exist(self)-> bool:
        try:
            validation_status = None

            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)

            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.data_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.data_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status


        except Exception as e:
            raise AppException(e, sys)
        


    
    def initiate_data_validation(self) -> DataValidationArtifact: 
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(
                validation_status=status)

            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data validation artifact: {data_validation_artifact}")

            if status:
                os.system(f"rm {self.data_ingestion_artifact.data_zip_file_path}") # Removing data.zip file

            return data_validation_artifact

        except Exception as e:
            raise AppException(e, sys)