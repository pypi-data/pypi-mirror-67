# __all__ = ["ColoredFormatterFactory"]

import os, re
import logging
import logging.config

# from fairways.conf import settings
from fairways.decorators import use

CONF_KEY = "LOGGING"

@use.config(CONF_KEY)
def set_conf(logging_conf):
    if not logging_conf:
        logging_conf = DEFAULT_CONF
    logging.config.dictConfig(logging_conf)

_loggers = {}

def getLogger(name=None, level=logging.INFO):        
    # handler = logging.StreamHandler()
    # if formatter:
    #     handler.setFormatter(formatter)
    root_log = _loggers.get(name)
    if root_log is None:
        root_log = logging.getLogger(name)
        root_log.setLevel(level)
        _loggers[name] = root_log
    # root_log.addHandler(handler)
    root_log = _loggers.get(name)
    if level != logging.INFO:
        root_log.setLevel(level)
    return root_log

DEFAULT_CONF = {
    'version': 1,
    'disable_existing_loggers': False,
    "handlers": {
        "console": {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'color'            
        },
        # "rmq": {
		# 	'level': 'DEBUG',
		# 	'class': 'python_logging_rabbitmq.RabbitMQHandler',
		# 	'host': 'localhost',
		# 	'port': 5672,
		# 	'username': 'guest',
		# 	'password': 'guest',
		# 	'exchange': 'log',
		# 	'declare_exchange': False,
		# 	'connection_params': {
		# 		'virtual_host': '/',
		# 		'connection_attempts': 3,
		# 		'socket_timeout': 5000
		# 	},
		# 	'fields': {
		# 		'source': 'MainAPI',
		# 		'env': 'production'
		# 	},
		# 	'fields_under_root': True            
        # }
    },

    "formatters": {
        "standard": {
            "format": "%(name)s->>> %(levelname)-8s %(asctime)s %(message)s"
        },
        "color": {
            "()": "fairways.helpers.ColoredFormatterFactory",
            "format_template": "%(name)s->>> %(log_color)s%(levelname)-8s%(reset)s %(log_color)s%(message)s",
            "datefmt": None,
            "reset": True,
            "log_colors": {
                'DEBUG':    'cyan',
                'INFO':     'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'red,bg_white',
            },
            "secondary_log_colors": {},
            "style": '%'
        }
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
            "formatter": "color"
        },
        # "rmq": {
        #     "handlers": ["rmq"]
        # }
    }
}


# logging.config.dictConfig(DEFAULT_CONF)