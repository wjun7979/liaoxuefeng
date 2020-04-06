# -*- coding: utf-8 -*-
# 日志
import logging
logging.basicConfig(level=logging.INFO, filename='logger.log', filemode='a', 
                    format='%(asctime)s - %(name)s - %(levelname)s : %(message)s')
logger = logging.getLogger(__name__)

s = '0'
n = int(s)
logger.info('n = %d' % n)
print(10 / n)
