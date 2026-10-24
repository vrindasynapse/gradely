
import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Create sample student data
np.random.seed(42)
number_of_students = 500

study_hours = np.random.uniform(0, 8, number_of_students)
attendance = np.random.uniform(40, 100, number_of_students)
previous_marks = np.random.uniform(20, 100, number_of_students)
assignment_score = np.random.uniform(0, 100, number_of_students)

# 2. Generate sample final marks
noise = np.random.normal(0, 5, number_of_students)

final_marks = (
    2.5 * study_hours
    + 0.20 * attendance
    + 0.35 * previous_marks
    + 0.15 * assignment_score
    + noise
)

final_marks = np.clip(final_marks, 0, 100)

# 3. Store the data in a table
data = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "previous_marks": previous_marks,
    "assignment_score": assignment_score,
    "final_marks": final_marks
})

# 4. Save student data
data.to_csv("students.csv", index=False)
print("Gradely: Student dataset created!")

# 5. Select inputs and target
X = data[
    ["study_hours", "attendance",
     "previous_marks", "assignment_score"]
]

y = data["final_marks"]

# 6. Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. Train the machine-learning model
model = LinearRegression()
model.fit(X_train, y_train)

# 8. Test the model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"R-squared Score: {r2:.3f}")

# 9. Save the trained model
with open("student_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Gradely: Model saved successfully!")
print("Next step: Create app.py")
