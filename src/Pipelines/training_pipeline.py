import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.Components.data_ingestion import DataIngestion
from src.Components.data_transformation import DataTransformation
from src.Components.model_trainer import ModelTrainer

if __name__ == '__main__' :
    
    # Data Ingestion
    data_ingestor = DataIngestion()
    train_data,test_data = data_ingestor.initiate_data_ingestion()
    print(train_data,test_data)

    # Data Transformation
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)
    print(train_arr,test_arr,_)

    # Model Training
    model_trainer = ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)
