import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib

# Load QnA dataset
qa_df = pd.read_excel("C:/Users/91949/Downloads/Agricultural QnA Dataset_ (1).xlsx")
qa_df.dropna(inplace=True)

# Create and train pipeline
pipe = make_pipeline(TfidfVectorizer(), LogisticRegression())
pipe.fit(qa_df['Question'], qa_df['Answer'])

# Save model
joblib.dump(pipe, "model.pkl")
print("✅ Model trained and saved as model.pkl")