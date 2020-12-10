import logging

import azure.functions as func
import random, string

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    letter_one = random.choice(string.ascii_letters)
    letter_two = random.choice(string.ascii_letters)
    letter_three = random.choice(string.ascii_letters)
    letter_four = random.choice(string.ascii_letters)
    letter_five = random.choice(string.ascii_letters)
    letters = letter_one + letter_two + letter_three + letter_four + letter_five
    return letters
