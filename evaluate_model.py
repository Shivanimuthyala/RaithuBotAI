import pandas as pd
import joblib

# Load model
model = joblib.load("model/model.pkl")

# Load dataset and rename columns
test_df = pd.read_excel("C:/Users/91949/Downloads/Train8_Test1_Dataset.xlsx")
test_df.columns = ['Question', 'Answer']  # Renaming columns
test_df.dropna(inplace=True)

# Evaluate model
correct = 0
for _, row in test_df.iterrows():
    pred = model.predict([row['Question']])[0]
    if pred.strip().lower() == row['Answer'].strip().lower():
        correct += 1

acc = correct / len(test_df)
print(f"✅ Accuracy on test data: {acc:.2%}")
