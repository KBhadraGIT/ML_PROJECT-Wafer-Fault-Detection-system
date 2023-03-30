#Imorting dependencies
import os,sys
from datetime import datetime

#Importing required files from the project.
from wafer.exception import WaferException
from wafer.logger import logging


#Global variables:

FILE_NAME = "wafer.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"


class TrainingPipelineConfig:
    """
    Description: 

    This will create a folder name artifact within it timestamp based folders will be created
    that will contain output file of each and every components of the training pipeline.
    """
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception as e:
            logging.error(WaferException(e, sys))
            raise WaferException(e, sys)    


#The above created class TrainingPipelineConfig will be used as object by each and every class.
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir , "data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2

        except Exception as e:
            logging.error(WaferException(e, sys))
            raise WaferException(e, sys)

class DataValidationConfig:...

class DataTransformationConfig:...

class ModelTrainerConfig:...


class ModelEvaluationConfig:...

class ModelPusherConfig:...