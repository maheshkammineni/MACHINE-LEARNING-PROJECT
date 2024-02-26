# app.py
import sys
from flask import Flask
from housing.logger import logger
from housing.exception import HousingException

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing_exception = HousingException(e, sys)
        logger.error(HousingException.get_detailed_error_message(e, sys))
        logger.error(housing_exception.error_message)

    logger.info("We're testing the logging module")
    return "Starting Machine Learning Project"

if __name__ == "__main__":
    app.run(debug=True)



