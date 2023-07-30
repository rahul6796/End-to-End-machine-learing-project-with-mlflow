from src.mlProject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.mlProject.pipeline.data_validation_pipeline import DataValidationPipeline
from src.mlProject.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.mlProject.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.mlProject.pipeline.model_evaluation import ModelEvaluationPipeline
from src.mlProject.logging import logger

STAGE_NAME = "data ingestion stage"
try:
    logger.info(f"starting {STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
except Exception as e:
    raise e


STAGE_NAME = "data validation stage"
try:
    logger.info(f"starting {STAGE_NAME}")
    data_validation = DataValidationPipeline()
    data_validation.main()
except Exception as e:
    raise e

STAGE_NAME = "data transformation stage"
try:
    logger.info(f"starting {STAGE_NAME}")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
except Exception as e:
    raise e


STAGE_NAME = "model trainer stage"
try:
    logger.info(f"starting {STAGE_NAME}")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
except Exception as e:
    raise e

STAGE_NAME = "model evaluation stage"
try:
    logger.info(f"starting {STAGE_NAME}")
    model_eval = ModelEvaluationPipeline()
    model_eval.main()
except Exception as e:
    raise e