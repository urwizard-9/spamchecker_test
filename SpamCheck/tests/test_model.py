# test_model.py
import os
import joblib
# 모델 파일 절대경로
MODEL_PATH = r"C:\Users\lemon\Desktop\aiPipeLinePractice\SpamCheck\ml\artifacts\spam_model.joblib"

def test_trained_model_exists():
    assert os.path.exists(MODEL_PATH)

def test_model_can_predict():
    model = joblib.load(MODEL_PATH)
    pred1 = model.predict(["free prize click now"])[0]
    pred2 = model.predict(["hello professor"])[0]
    assert pred1 in ["spam", "ham"]
    assert pred2 in ["spam", "ham"]