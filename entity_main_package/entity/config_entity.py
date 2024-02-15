import os
from dataclasses import dataclass
from datetime import datetime
from entity_main_package.constant.training_pipeline import *

@dataclass
class TrainingPipelineConfig:
    artifacts_dir : str = ARTIFACTS_DIR

training_pipeline_config : TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    # I'm downloading the data in data_ingestion folder
    data_ingestion_dir : str = os.path.join(
        training_pipeline_config.artifacts_dir , DATA_INGESTION_DIR_NAME # artifacts/data_ingestion
    )
    feature_store_file_path : str = os.path.join(
        data_ingestion_dir , DATA_INGESTION_FEATURE_STORE_DIR # artifacts/data_ingestion/feature_store
    )
    data_download_url : str = DATA_DOWNLOAD_URL

@dataclass
class DataValidationConfig:
    data_validation_dir = os.path.join(
        training_pipeline_config.artifacts_dir , DATA_VALIDATION_DIR_NAME
    )
    data_status_file_dir = os.path.join(
        data_validation_dir , DATA_VALIDATION_STATUS_FILE
    )
    required_file_list = DATA_VALIDATION_ALL_REQUIRED_FILES

@dataclass
class ModelTrainerConfig:
    model_trainer_dir = os.path.join(
        training_pipeline_config.artifacts_dir , MODEL_TRAINER_DIR_NAME
    )
    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME
    no_epochs = MODEL_TRAINER_NO_EPOCHS
    batch_size = MODEL_TRAINER_BATCH_SIZE