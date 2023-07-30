from src.mlProject.config.configuartion import ConfigurationManager
from src.mlProject.components.data_validation import DataValidation
from src.mlProject.components.model_trainer import ModelTrainer
from src.mlProject.components.model_evaluation import ModelEvaluation
STAGE_NAME = "model_evaluation"

class ModelEvaluationPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_evaluation_config()
        model_eval = ModelEvaluation(config=model_eval_config)
        model_eval.log_into_mlflow()



