from loguru import logger

from src.commands.BaseCommand import BaseCommand
from src.core.Config import Config

import requests
import sys


class ValidateApiCommand(BaseCommand):

    def __init__(self):
        self.status = 'status'
        self.headers = {
            "Accept": "application/json"
        }

    def execute(self):

        logger.info("VALIDATING API AVAILABILITY")

        try:
            status_req = requests.get(f"{Config.config['target']['url_status']}/{self.status}", headers=self.headers)
        except Exception as e:
            sys.exit(logger.error(f"There was an error for request  : {e.args}"))

        if status_req.status_code is not 200:
            sys.exit(logger.error(f"API {Config.config['target']['url_status']}/{self.status} "
                                  f"status code {status_req.status_code}"))

        else:
            logger.success(f"API status code : 200")

            if status_req.json()['status'] != "ok":
                sys.exit(logger.error(f"API not available"))
            else:
                logger.success(f"API availability : OK")

        # TODO
        # validate /api/koha API availability
