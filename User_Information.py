# 用于用户的登录与注册
# 保存用户的评分信息于csv中
# 读取用户信息并于总数据集合并
# 注意用户每次只能对一部电影保存一次评分，新的评分将会覆盖旧评分
# 评分范围为0.5 ~ 5.0 stars
import numpy as np
import pandas as pd

class user:

    # 初始化用户的账户iD，密码，以及一个空的字典列表
    def __init__(self, userId, password):
        self.user_Id = userId
        self.password = password
        self.rating_list = {}          # 储存用户对某部电影的评分

    def



# 初始化一个新的userId，并随机生成一个password
def  account_generated():
    pass