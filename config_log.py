import os
import logging


logging.basicConfig(filename='events.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.getLogger("werkzeug").setLevel('WARNING')


logger = logging.getLogger('visie_gustavo')

