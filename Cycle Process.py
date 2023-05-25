#Python code to generate the P vs V for a Closed Cycle. Pressure and Volume inputs to be taken from User.



import matplotlib.pyplot as plt

def closed_cycle():
    num_points = int(input("Enter the number of points: "))
    volumes = []
    pressures = []

    for i in range(num_points):
        V = float(input(f"Enter the volume at point {i+1}: "))
        P = float(input(f"Enter the pressure at point {i+1}: "))
        volumes.append(V)
        pressures.append(P)

    volumes.append(volumes[0])
    pressures.append(pressures[0])

    plt.plot(volumes, pressures, marker='o')
    plt.xlabel("Volume")
    plt.ylabel("Pressure")
    plt.title("P vs V for Closed Cycle")
    plt.show()

closed_cycle()
