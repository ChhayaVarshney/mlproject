from flask import Flask, request, render_template
import numpy as np
import pandas as pd 
import os

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

# ✅ Health check route (for GitHub deployment testing)
@application.route('/health')
def health_check():
    model_path = os.path.join('artifacts', 'model.pkl')
    preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

    model_exists = os.path.exists(model_path)
    preprocessor_exists = os.path.exists(preprocessor_path)

    if model_exists and preprocessor_exists:
        return "✅ Deployment successful! Model and preprocessor files found."
    elif not model_exists and not preprocessor_exists:
        return "⚠️ App is running, but model and preprocessor files are missing."
    elif not model_exists:
        return "⚠️ App is running, but model file is missing."
    else:
        return "⚠️ App is running, but preprocessor file is missing."


@application.route('/')
def index():
    return render_template('index.html')

@application.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender = request.form.get('gender'),
            race_ethnicity = request.form.get('race_ethnicity'),
            parental_level_of_education = request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = request.form.get('reading_score'),
            writing_score = request.form.get('writing_score')
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', result = results)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host="0.0.0.0", port=port, debug=True)  # Add debug=True
