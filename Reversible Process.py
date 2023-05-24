#Python code to generate the P vs V for a Reversible  Proces. Pressure and Volume inputs to be taken from User.



import matplotlib.pyplot as plt

# Get user input
n = int(input("Enter the number of data points: "))

# Initialize lists to store P and V values
P_values = []
V_values = []

# Get P and V values from the user
for i in range(n):
    P = float(input(f"Enter P value {i+1}: "))
    V = float(input(f"Enter V value {i+1}: "))
    P_values.append(P)
    V_values.append(V)

# Plot the P vs V graph
plt.plot(V_values, P_values, 'bo-')
plt.xlabel('Volume (V)')
plt.ylabel('Pressure (P)')
plt.title('P vs V for Reversible Process')
plt.grid(True)
plt.show()
