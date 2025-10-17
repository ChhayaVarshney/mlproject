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
        logger.debug("DEBUG: /predictdata POST route reached")
        try:
            # data = CustomData(...)
            # pred_df = data.get_data_as_data_frame()
            # predict_pipeline = PredictPipeline()
            # results = predict_pipeline.predict(pred_df)
            # return render_template('home.html', result=results)

            logger.debug("DEBUG: Prediction skipped")
            return render_template('home.html', result="Fake prediction OK")

        except Exception as e:
            logger.exception("ERROR: Exception in /predictdata")
            return render_template('home.html', result=f"Error: {e}")

@application.route('/healthcheck')
def healthcheck():
    return "OK", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host="0.0.0.0", port=port)
