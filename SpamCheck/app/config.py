# app/config.py
import os

MODEL_MODE = "ml" # "ml"

# __file__ 기준 경로: Windows/Linux/Render 모두 동작
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # SpamCheck/
LOCAL_MODEL_PATH = os.path.join(BASE_DIR, "ml", "artifacts", "spam_model.joblib")

# MODEL_URI = "runs:/a7e81f6583f247a680d21e97eabac0b9/model"
MODEL_URI = "models:/spam-model@champion"
MLFLOW_TRACKING_URI = "sqlite:///" + os.path.join(BASE_DIR, "mlflow.db")