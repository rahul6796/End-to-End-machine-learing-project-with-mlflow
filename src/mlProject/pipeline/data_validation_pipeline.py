from src.mlProject.config.configuartion import ConfigurationManager
from src.mlProject.components.data_validation import DataValidation

STAGE_NAME = "data_validation"


class DataValidationPipeline:

    def __init__(self):
        pass

    @staticmethod
    def main():
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()