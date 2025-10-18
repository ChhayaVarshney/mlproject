from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import os
import sys
import traceback
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# ✅ Add src/ to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

logger.debug("DEBUG: Starting imports")

try:
    from pipeline.predict_pipeline import CustomData, PredictPipeline
    logger.debug("DEBUG: Imports successful")
except Exception as e:
    logger.error("ERROR: Import failed")
    logger.exception(e)

application = Flask(__name__)
logger.debug("DEBUG: Flask app created")

@application.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        logger.debug("DEBUG: /predictdata POST request received")
        try:
            form_data = request.form.to_dict()
            logger.debug(f"Form Data: {form_data}")

            # If using CustomData and PredictPipeline:
            # data = CustomData(**form_data)
            # pred_df = data.get_data_as_data_frame()
            # pipeline = PredictPipeline()
            # result = pipeline.predict(pred_df)

            return render_template('home.html', result="Fake prediction OK")

        except Exception as e:
            logger.exception("ERROR during prediction processing")
            return render_template('home.html', result=f"Error occurred: {e}")


@application.route('/')
def index():
    return "App is running.", 200

@application.route('/healthcheck')
def healthcheck():
    return "OK", 200



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host="0.0.0.0", port=port, debug=True)  # Add debug=True

