from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline

STAGE_NAME = 'Data Ingestion stage'

try:
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed<<<<<<<\n\n x===========")
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'prepare base model'

try:
      logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started<<<<<<<")
      obj = PrepareBaseModelTrainingPipeline()
      obj.main()
      logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed<<<<<<<\n\n x===========")

except Exception as e:
      logger.exception(e)
      raise e


STAGE_NAME = 'ModelTraining'

try:
      logger.info(f"*******************************")
      logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started<<<<<<<")
      obj = ModelTrainingPipeline()
      obj.main()
      logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed<<<<<<<\n\n x===========")

except Exception as e:
      logger.exception(e)
      raise e