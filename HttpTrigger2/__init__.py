import logging

import azure.functions as func
import random

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    digit_one = str(random.randint(0,9))
    digit_two = str(random.randint(0,9))
    digit_three = str(random.randint(0,9))
    digit_four = str(random.randint(0,9))
    digit_five = str(random.randint(0,9))
    digits = digit_one + digit_two + digit_three + digit_four + digit_five   
    return digits