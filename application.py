# from flask import Flask, request, render_template
# import numpy as np
# import pandas as pd
# import os
# import sys
# import traceback
# import logging

# logger = logging.getLogger()
# handler = logging.StreamHandler(sys.stdout)
# formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)

# # ✅ Add src/ to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# logger.debug("DEBUG: Starting imports")

# try:
#     from pipeline.predict_pipeline import CustomData, PredictPipeline
#     logger.debug("DEBUG: Imports successful")
# except Exception as e:
#     logger.error("ERROR: Import failed")
#     logger.exception(e)

# application = Flask(__name__)
# logger.debug("DEBUG: Flask app created")

# @application.route('/predictdata', methods=['GET', 'POST'])
# def predict_datapoint():
#     if request.method == 'GET':
#         return render_template('home.html')
#     else:
#         logger.debug("DEBUG: Reached /predictdata POST route")
#         try:
#             form_data = request.form.to_dict()
#             logger.debug(f"Form data received: {form_data}")

#             # TEMP: Comment out actual model code for debugging
#             # data = CustomData(**form_data)
#             # pred_df = data.get_data_as_data_frame()
#             # pipeline = PredictPipeline()
#             # result = pipeline.predict(pred_df)

#             return render_template('home.html', result="Fake prediction OK")
#         except Exception as e:
#             logger.exception("Exception occurred in /predictdata POST route")
#             return render_template('home.html', result=f"Error occurred: {e}")



# @application.route('/')
# def index():
#     return "App is running.", 200

# @application.route('/healthcheck')
# def healthcheck():
#     return "OK", 200

from flask import Flask, request, render_template
import os
import sys
import logging

# Basic logging config for EB
logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Add src to path (keep it here even though it's not used for now)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

application = Flask(__name__)
logger.debug("DEBUG: Flask app initialized")

@application.route('/')
def index():
    logger.debug("DEBUG: Index route called")
    return "App is running.", 200

@application.route('/healthcheck')
def healthcheck():
    logger.debug("DEBUG: Healthcheck pinged")
    return "OK", 200

@application.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    logger.debug("DEBUG: GET or POST /predictdata reached")
    if request.method == 'GET':
        logger.debug("DEBUG: Serving home.html template")
        return render_template('home.html')
    else:
        try:
            form_data = request.form.to_dict()
            logger.debug(f"DEBUG: Received form data: {form_data}")
            return f"Received: {form_data}", 200
        except Exception as e:
            logger.exception("ERROR: In POST /predictdata")
            return f"Internal Server Error: {e}", 500

@application.route('/testtemplate')
def test_template():
    return render_template('home.html')



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host="0.0.0.0", port=port, debug=True)  # Add debug=True
