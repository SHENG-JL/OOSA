import numpy as np

def random_data():
    # Generate an array of random numbers
    data = np.random.random(100)
    return data

def min_value(data):
    # Find the minimum value in the data
    return np.min(data)


if __name__ == '__main__':
    # Generate random data
    random_data = random_data()

    # Get the minimum value from the data
    minnumber = min_value(random_data)

    # Print the data and the minimum value
    print("Generated Data:", random_data)
    print("Minimum Value:", minnumber)

