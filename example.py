from awanitron.log4s3.myhandler import S3RotatingFileHandler

import sys
import traceback
import logging
import logging.config
import logging.handlers


LOGGING = {
  'version': 1,
  'disable_existing_loggers': True,
    'formatters': {
    'verbose': {
      'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
      'simple': {
        'format': '%(levelname)s %(asctime)s %(message)s'
        },
      },
    'handlers': {
      'file':{
        'level': 'ERROR',
        'class': 'awanitron.log4s3.myhandler.S3RotatingFileHandler',
          'formatter': 'simple',
            'filename': '/tmp/bottle.txt',
              'mode': 'a',
              'maxBytes': 128,
                'backupCount' : 100,
                'aws_key' : r'SOMEKEY'
                'aws_secret' : r'SOMESECRET',
                'aws_urlbase' :  r'http://maheshmapr.s3.amazonaws.com/logsetc'
                  },
      'console':{
        'level': 'INFO',
          'class': 'logging.StreamHandler',
            'formatter': 'simple',
            }
      },
    'loggers': {
      'awanitron': {
        'handlers': ['file','console'],
          'level': 'INFO',
          }
      }
    }


logging.config.dictConfig(LOGGING)

awanitron = logging.getLogger('awanitron')

awanitron.error("Begin") ;
