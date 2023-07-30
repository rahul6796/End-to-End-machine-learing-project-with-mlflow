
from src.mlProject.config.configuartion import ConfigurationManager
from src.mlProject.components.data_validation import DataValidation
from src.mlProject.components.data_transformation import DataTransformation
STAGE_NAME = "data_transformation"


class DataTransformationPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()
