import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk and plot the points


while True:

    rw = RandomWalk()
    rw.fill_walk()
    # Set the size of the plotting window
    plt.figure(figsize=(10,6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Blues,edgecolor = 'none', s=1)
    plt.scatter(0, 0, c='green',edgecolor = 'none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',edgecolor = 'none', s=50)
    
    # Remove the axis
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (Y/N): ")
    if keep_running.upper() == "N":
        break
