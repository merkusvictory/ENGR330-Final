# import libraries for data analysis and machine learning
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import serial

# load training data
try:
    df = pd.read_csv('training_data.csv')
except FileNotFoundError:
    print("Collect data first")
    exit()

# Expect columns: Temperature, Light, Sound, Label
# modify this line based on your actual column names in the CSV
expected_cols = ['A', 'B', 'C', 'grid_loc']

missing = [c for c in expected_cols if c not in df.columns]
if missing:
    print(f"CSV is missing columns: {missing}. Available: {list(df.columns)}")
    exit()

# modify this based on which features you are using
# X is the feature set (input), y is the label (output that we will predict)
X = df[['A', 'B', 'C']]
y = df['grid_loc']

# Train KNN
knn = KNeighborsClassifier(n_neighbors=11) # this is the k parameter that we can tune
knn.fit(X, y)
print("Model Trained Successfully!")

# Getting stream of data from microbit
PORT = 'COM18'
BAUD = 115200
try:
    ser = serial.Serial(PORT, BAUD)
    print("Connected!")
except:
    print("Could not connect. Check port.")
    exit()

# Infinitely getting data from microbit
while True:

    if ser.in_waiting:
        line = ser.readline().decode().strip()
        parts = line.split(',')

        if len(parts) >= 3:
            a = parts[0]
            b = parts[1]
            c = parts[2]

        try:
            # modify this based on which features you are using
            print("Input: ",a,b,c)
            input_data = pd.DataFrame([[a,b,c]], columns=['A', 'B', 'C'])

            # get predicted value based on input data
            prediction = knn.predict(input_data)

            print(f"--> Prediction: {prediction[0].upper()}")

            # sending prediction to microbit
            ser.write(prediction[0].upper().encode('utf-8'))
        except:
            pass  # ignore malformed data