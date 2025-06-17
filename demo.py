from us_visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()
# from us_visa.logger import logging

# logging.info("Welcom to my project")
# import sys
# from us_visa.exception import USvisaException
# try:
#     a=2/0
# except Exception as e:
#     raise USvisaException(e,sys)

# import os
# mongo_db_url = os.getenv('MONGODB_URL')
# print(mongo_db_url)
