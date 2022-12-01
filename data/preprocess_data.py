import numpy as np
#import scipy.io as sio


def sequencing(path, length=160, stride=10, downsample=1):
    # downsample == 1 -> no downsample
    x = np.load(path) # you can use whatever loading you want
    # for matalb .mat format
    # x = sio.loadmat(path)["data"]
    
    # I assume x has shape (time, dim) ~ example: (1000,3)... 1000 points in time series, 3 channals/sensors
    size = len(x) # 
    # downsampling x
    x = x[::downsample] # (1000,3) -> (1000/downsample, 3)
    # sequencing
    x_sequence = np.array([x[i:i+length] for i in range(0, size - (length - stride + 1), stride)]) # (1000,3) -> (85, 160, 3)
    return np.moveaxis(x_sequence, [0,1,2], [0,2,1]) # (85, 160, 3) -> (85, 3, 160)

# to save data use: np.save("name.npy", data)

def sequencing_input(x, length=160, stride=10, downsample=1):
    size = len(x) # 
    # downsampling x
    x = x[::downsample] 
    # sequencing
    x_sequence = np.array([x[i:i+length] for i in range(0, size - (length - stride + 1), stride)])
    return np.moveaxis(x_sequence, [0,1,2], [0,2,1])