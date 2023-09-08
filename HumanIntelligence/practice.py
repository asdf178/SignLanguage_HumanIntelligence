import os
import numpy as np

path = os.path.join(os.path.dirname(__file__), "static/results/res")

a = np.array([1,2,3])
np.save(path, a)