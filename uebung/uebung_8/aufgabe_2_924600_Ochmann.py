import numpy as np


def brownian_motion(n, num_time_steps):
    """Simple Brownian motion simulation.
    """
    # Start with n particles (startposition inside square)

    # Shape (n, 2) --> n particles with coordinates x, y
    particles = np.sqrt(n) * (np.random.random((n, 2)) - 0.5)
    
    
    
    # Simulate movement over num_time_steps
    for i in range(num_time_steps):
        particles += 2 * np.random.random() - 1
    
    
    
    """x and y AVG"""
    x=particles[:,0]
    y=particles[:,1]
    print(f"Mittelwert x:{np.mean(x)}")
    print(f"Mittelwert y:{np.mean(y)}")
    """Distance"""
    max_x = np.max(x)
    max_y = np.max(y)
    print(f"Der am weiten entfernte punkt ist: (X={max_x},Y={max_y})")

pass




brownian_motion(1000,1000)
