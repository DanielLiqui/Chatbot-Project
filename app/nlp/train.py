import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))
DATASET_PATH = os.path.join(BASE_DIR, 'dataset_clean.csv')
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'intent_model.joblib')


df = pd.read_csv(DATASET_PATH)

X = df['text']
y = df['intent']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

print(classification_report(y_test, y_pred))

# 6. Сохраняем модель
joblib.dump(pipeline, MODEL_PATH)
print(f"Модель сохранена: {MODEL_PATH}")