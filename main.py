from src.mlProject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.mlProject.logging import logger

STAGE_NAME = "data ingestion stage"
try:
    logger.info(f"starting {STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
except Exception as e:
    raise e