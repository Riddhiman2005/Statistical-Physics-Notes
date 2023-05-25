#Python code to generate the P vs V for a Cycle Process. Pressure and Volume inputs to be taken from User.



import matplotlib.pyplot as plt

def plot_cycle_process():
    num_stages = int(input("Enter the number of stages in the cycle process: "))
    
    pressures = []
    volumes = []
    
    # Input pressure and volume values for each stage
    for i in range(num_stages):
        pressure = float(input(f"Enter pressure at stage {i+1}: "))
        volume = float(input(f"Enter volume at stage {i+1}: "))
        pressures.append(pressure)
        volumes.append(volume)
    
    # Plotting the P-V diagram
    plt.plot(volumes, pressures, marker='o')
    plt.xlabel('Volume')
    plt.ylabel('Pressure')
    plt.title('P-V Diagram for Cycle Process')
    plt.grid(True)
    plt.show()

# Calling the function to generate the P-V diagram
plot_cycle_process()

