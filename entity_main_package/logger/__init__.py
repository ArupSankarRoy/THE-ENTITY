# The idea is to create, log/01_29_2024_15_35_53.log 

import logging
import os
from datetime import datetime
from from_root import from_root

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_folder_path = os.path.join(from_root() , 'log')

if not os.path.exists(log_folder_path):
    os.makedirs(log_folder_path , exist_ok=True)

LOG_FILE_PATH = os.path.join(log_folder_path , LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)




