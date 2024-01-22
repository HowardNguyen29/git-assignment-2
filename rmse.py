import numpy as np
# import math

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
    # sum_squared_diff = sum((tar[n] - pred[n])**2 for n in range(len(pred)))
    # rmse = (sum_squared_diff/len(pred))**0.5
    squared_diff = np.square(tar - pred)
    mse = np.mean(squared_diff)
    rmse = np.sqrt(mse) # TODO: Implement RMSE Calculation here...
    return rmse



