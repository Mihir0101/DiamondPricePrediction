import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


# Initialize the data ingestion configuration
@dataclass
class DataIngestionConfig :
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')

# Create a data ingestion class
class DataIngestion :
    def __init__(self) :
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self) :
        logging.info('DATA INGESTION METHOD STARTS')

        try :
            df = pd.read_csv(os.path.join('Notebooks/Data','gemstone.csv'))
            logging.info('DATASET HAS READ AS PANDAS DATAFRAME')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info('TRAIN TEST SPLIT')
            train_set,test_set = train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('INGESTION OF DATA HAS COMPLETED')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e :
            logging.info('ERROR OCCURED IN DATA INGESTION CONFIG') 