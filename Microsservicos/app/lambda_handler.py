import logging
from src import main

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Iniciando Lambda...")
    
    try: 
        main()
        
    except Exception as e:
        return e