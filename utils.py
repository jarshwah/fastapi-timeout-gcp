import logging
import logging.config


def configure_logging():
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {"format": "%(asctime)s %(name)-32s %(levelname)-8s %(message)s"}
        },
        "filters": {},
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": logging.INFO,
                "formatter": "standard",
                "filters": [],
            }
        },
        "root": {"handlers": ["console"], "level": logging.INFO},
        "loggers": {"urllib3": {"level": logging.INFO, "handlers": ["console"]}},
    }
    logging.config.dictConfig(config)


def is_valid(domain, path) -> bool:
    # details removed - they involve regex
    return True
