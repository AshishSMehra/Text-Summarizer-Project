import os
import urllib.request as request
import zipfile
from textsummerizer.logging import logger
from textsummerizer.utils.common import get_size
from pathlib import Path
from textsummerizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        Downloads the file from the source URL if it doesn't already exist locally.
        """
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} downloaded! with the following info: \n{headers}")
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
        except Exception as e:
            logger.error(f"Error occurred while downloading the file: {e}")
            raise

    def validate_file(self):
        """
        Validates if the downloaded file is a valid ZIP file.
        Returns True if valid, False otherwise.
        """
        if zipfile.is_zipfile(self.config.local_data_file):
            logger.info(f"The file {self.config.local_data_file} is a valid ZIP file.")
            return True
        else:
            logger.error(f"The file {self.config.local_data_file} is not a valid ZIP file.")
            return False

    def extract_zip_file(self):
        """
        Extracts the ZIP file into the specified directory if it is valid.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        try:
            # Validate the ZIP file
            if not self.validate_file():
                logger.error("Extraction aborted due to invalid ZIP file.")
                return
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f"Extracted {self.config.local_data_file} to {unzip_path}")
        except zipfile.BadZipFile as e:
            logger.error(f"Bad ZIP file error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error occurred while extracting the ZIP file: {e}")
            raise
