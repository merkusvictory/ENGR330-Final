import serial
import time
import csv

# --- SETTINGS ---
PORT = 'COM18'
BAUD = 115200
FILE = 'data_0D.csv'

# Connect to micro:bit
try:
    ser = serial.Serial(PORT, BAUD)
    print("Connected!")
except:
    print("Could not connect. Check port.")
    exit()

# Ask user for info
x = input("Current X-location on grid (0-4): ")
y = input("Current Y-location on grid (A-E): ")
duration = int(input("How many seconds to record? "))

# Open CSV file to output serial data to
file = open(FILE, 'w', newline='')
writer = csv.writer(file)

# Write header of CSV (replace with your feature names)
writer.writerow(['A', 'B', 'C', 'grid_loc'])

print("\nRecording...\n")

a = None
b = None
c = None

# Main loop to read serial data at a regular interval and write to CSV

while True:
    start = time.time()
    while time.time() - start < duration:
        if ser.in_waiting:
            line = ser.readline().decode().strip()
            print(line)
            parts = line.split(',')

            if len(parts) >= 3:
                a = parts[0]
                b = parts[1]
                c = parts[2]

                try:
                    # modify this based on which features you are using
                    writer.writerow([a, b, c, x+","+y])
                    print(a, b, c)
                    a, b, c = None, None, None
                except:
                    pass  # ignore malformed data
    x = input("Current X-location on grid (0-4), to stop type exit: ")
    y = input("Current Y-location on grid (A-E): ")
    if x == "exit":
        break



print("\nDone reading data. Saved to " + FILE + ". Make sure to copy this over to another file so it doesn't get overwritten next time you record data.")

file.close()
ser.close()