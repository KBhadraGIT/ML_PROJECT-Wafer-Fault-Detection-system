#Importing dependencies
import pandas as pd
import numpy as np
import os,sys

#Importing required files from the project.
from wafer.logger import logging
from wafer.exception import WaferException


def get_data_in_dataframe(file_name:str)->pd.DataFrame:
    """
    Description: This function intakes .csv file and return in dataframe format
    =========================================================
    Params:
    file_name: file name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from .csv file: {file_name}.")

        df = pd.read_csv(file_name)
        logging.info(f"Loaded {file_name} as a dataframe")

        _ , columns_dataframe = df.shape
        logging.info(f"Row and columns in loaded dataframe: {df.shape}")
        logging.info(f"Number of columns in loaded dataframe: {columns_dataframe}")
        
        return df
    except Exception as e:
        raise SensorException(e, sys)

    

def write_yaml_file(file_path,data:dict):...

def convert_columns_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:...


def save_object(file_path: str, obj: object) -> None:...


def load_object(file_path: str, ) -> object:...

def save_numpy_array_data(file_path: str, array: np.array):...

def load_numpy_array_data(file_path: str) -> np.array:...