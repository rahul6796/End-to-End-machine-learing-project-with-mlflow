import os
import urllib.request as request
import zipfile

import pandas as pd

from src.mlProject.entity.config_entity import ModelTrainerConfig
from src.mlProject.logging import logger
from src.mlProject.utils.common import get_size
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import joblib


class ModelTrainer:

    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_d = pd.read_csv(self.config.train_data_path)
        test_d = pd.read_csv(self.config.test_data_path)

        x_train = train_d.drop([self.config.target_column], axis=1)
        x_test = test_d.drop([self.config.target_column], axis=1)
        y_train = train_d[self.config.target_column]
        x_test = test_d[self.config.target_column]

        lr = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=42,
        )

        lr.fit(x_train, y_train)
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
