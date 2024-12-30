import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv("customer_churn.csv")  # Replace with your dataset path

# Check the dataset structure
print(data.head())

# Preprocess data
# Assuming "Churn" is the target column
if data['Churn'].dtype == 'object':  # Encode target column if it's a string
    le = LabelEncoder()
    data['Churn'] = le.fit_transform(data['Churn'])

# Splitting features (X) and target (y)
X = data.drop(columns=['Churn'])
y = data['Churn']

# Handle categorical features in X if any (encoding, one-hot encoding, etc.)
X = pd.get_dummies(X, drop_first=True)  # One-hot encode categorical variables

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Gradient Boosting Classifier
clf = GradientBoostingClassifier(random_state=42)
clf.fit(X_train, y_train)

# Evaluate model
y_pred = clf.predict(X_test)

# Print evaluation metrics
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
