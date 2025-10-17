from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import os
import sys
import traceback

# ✅ Add src/ to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

print("DEBUG: Starting imports", flush=True)

try:
    from pipeline.predict_pipeline import CustomData, PredictPipeline
    print("DEBUG: Imports successful", flush=True)
except Exception as e:
    print("ERROR: Import failed", flush=True)
    traceback.print_exc()

application = Flask(__name__)
print("DEBUG: Flask app created", flush=True)

@application.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        print("DEBUG: /predictdata POST route reached", flush=True)
        try:
            # Uncomment below once the pipeline is stable
            # data = CustomData(
            #     gender=request.form.get('gender'),
            #     race_ethnicity=request.form.get('race_ethnicity'),
            #     parental_level_of_education=request.form.get('parental_level_of_education'),
            #     lunch=request.form.get('lunch'),
            #     test_preparation_course=request.form.get('test_preparation_course'),
            #     reading_score=request.form.get('reading_score'),
            #     writing_score=request.form.get('writing_score')
            # )

            # pred_df = data.get_data_as_data_frame()
            # predict_pipeline = PredictPipeline()
            # results = predict_pipeline.predict(pred_df)
            # return render_template('home.html', result=results)

            print("DEBUG: Prediction skipped", flush=True)
            return render_template('home.html', result="Fake prediction OK")

        except Exception as e:
            print("ERROR: Exception in /predictdata", flush=True)
            traceback.print_exc()
            return render_template('home.html', result=f"Error: {e}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host="0.0.0.0", port=port)
