# 查看数据集并进行预处理
# 实现基于用户的协同过滤
import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import warnings

# 数据集储存的位置
data_path = '.\dataset\\'
path_20m = '.\dataset\\ml-20m\\'
path_small = '.\dataset\\ml-latest-small\\'