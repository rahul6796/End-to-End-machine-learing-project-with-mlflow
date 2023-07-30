from src.mlProject.config.configuartion import ConfigurationManager
from src.mlProject.components.data_validation import DataValidation
from src.mlProject.components.model_trainer import ModelTrainer
STAGE_NAME = "data_trainer"


class ModelTrainerPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()