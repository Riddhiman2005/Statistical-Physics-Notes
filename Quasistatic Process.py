#Python code to generate the P vs V for a Quasi-static Process. Pressure and Volume Inputs to be taken from User.


import matplotlib.pyplot as plt

# Get user input for number of data points
num_points = int(input("Enter the number of data points: "))

# Initialize lists to store pressure (P) and volume (V) data
pressure = []
volume = []

# Collect user input for pressure and volume values
for i in range(num_points):
    p = float(input(f"Enter pressure value at point {i+1}: "))
    v = float(input(f"Enter volume value at point {i+1}: "))
    pressure.append(p)
    volume.append(v)

# Plot the P vs V graph
plt.plot(volume, pressure, marker='o')
plt.xlabel('Volume (V)')
plt.ylabel('Pressure (P)')
plt.title('Quasi-static Process: P vs V')
plt.grid(True)
plt.show()
