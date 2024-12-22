# import os 
# import sys 
# import logging 

# logging_str = '%(asctime)s: %(levelname)s: %(module)s: %(message)s'
# log_dir = "logs"
# log_filepath = os.path.join(log_dir, "running_logs.log")
# os.makedirs(log_dir, exist_ok=True)


# logging.basicConfig(
#   Level=logging.INFO,
#   format= logging_str,
  
  
#   handlers =[
#     logging.FileHandler(log_filepath),
#     logging.StreamHandler(sys.stdout)
#   ]
# )


# logger = logging.getLogger("TextSummerizerLogger")


import logging
from datetime import datetime

# Example of correct basicConfig
logging.basicConfig(
    level=logging.INFO,  # Use 'level' instead of 'Level'
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(f"log_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
