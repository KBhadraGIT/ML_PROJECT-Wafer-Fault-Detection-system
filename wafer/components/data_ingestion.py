#Importing dependencies
import pandas as pd
import numpy as np

#Importing required files from the project.
from wafer import utils
from wafer.logger import logging
from wafer.exception import WaferException
from wafer.entity import artifact_entity
from wafer.entity import config_entity

#Required variables


class DataIngestion:
    """
    DESCRIPTION:
    This class will obtain the data for the prediction.
    ---------------------------------------------------
    PARAMETERS:

    """
    
    def __init__(self, data_ingestion_config:config_entity.DataIngestionConfig):
        
        try:
            logging.info(f"{'>>'*20} Data Ingestion {'<<'*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:

        try:
            logging.info("Exporting and reading the data as pandas dataframe.")
            
            #Exporting data
            df:pd.DataFrame = utils.get_data_in_dataframe(file_path = self.data_ingestion_config.file_path)
            
