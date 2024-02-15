
# 'MAIN DIRECTORY' IS ARTIFACTS_DIR, (IT IS CREATED AUTOMATICALLY WHEN CODE IS RUN)
ARTIFACTS_DIR : str = 'artifacts' # This is is the directory that stored all the generated files in every stage.


# INSIDE ARTIFACTS_DIR WE HAVE DATA_INGESTION_DIR 
DATA_INGESTION_DIR_NAME : str = 'data_ingestion' # See the flowchart

# AFTER UNZIPPING THE DATA_INGESTION_DIR THE EXTRACTED DATA WILL STORED INSIDE DATA_INGESTION_FEATURE_STORE_DIR,
DATA_INGESTION_FEATURE_STORE_DIR : str = 'feature_store' # See the flowchart

DATA_DOWNLOAD_URL : str = "https://drive.google.com/file/d/1ECfl3dtYyfivY8kYPq7RHUBTjC-2vf61/view?usp=share_link" # See the flowchart


'''
DATA VALIDATION RELATED CONTENT START WITH DATA_VALIDATION VAR NAME
'''
DATA_VALIDATION_DIR_NAME : str = 'data_validation'
DATA_VALIDATION_STATUS_FILE : str = 'status.txt' # This contains if ['train' , 'valid' , 'data.yaml'] these all three present in 'data_validation' dir or not
                                                 # Contains True or False Value
DATA_VALIDATION_ALL_REQUIRED_FILES = ['train' , 'valid' , 'data.yaml']

'''
MODEL TRAINER RELARED CONTENT START WITH MODEL_TRAINER VAR NAME
'''
MODEL_TRAINER_DIR_NAME : str = 'model_trainer'
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME : str = 'yolov8n.pt'
MODEL_TRAINER_NO_EPOCHS : int = 1
MODEL_TRAINER_BATCH_SIZE : int = 16