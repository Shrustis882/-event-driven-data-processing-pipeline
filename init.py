import logging
import azure.functions as func

def main(mytimer: func.TimerRequest):
    logging.info("Daily report function executed")
