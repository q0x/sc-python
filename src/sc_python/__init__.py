import os
import logging.config
import yaml

LOG = logging.getLogger(__name__)

def configure_logging():
    logging_config_filename = os.getenv('LOGGING_CONFIG_FILE','logging.yaml')
    try:
        with open(logging_config_filename, 'r', encoding='utf8') as logging_config_file:
            logging_config = yaml.safe_load(logging_config_file)
            logging.config.dictConfig(logging_config)
    except (FileNotFoundError, ValueError):
        logging_format = '%(asctime)s %(name)s %(levelname)s %(message)s'
        logging.basicConfig(level=logging.INFO, format=logging_format)
        LOG.warning('Unable to read logging config "%s". Using defaults.', 
                    logging_config_filename, exc_info=1)
        
configure_logging()