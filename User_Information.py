# 用于用户的登录与注册
# 保存用户的评分信息于csv中
# 读取用户信息并于总数据集合并
# 注意用户每次只能对一部电影保存一次评分，新的评分将会覆盖旧评分
# 评分范围为0.5 ~ 5.0 stars
import numpy as np
import pandas as pd

# 数据集地址
path_20m = '.\\dataset\\ml-20m\\'
path_small = '.\\dataset\\ml-latest-small\\'

# 用户信息保存地址
path_user = '.\\new_user\\'

class user:
    __user_Id = None
    __rating_list = None   # 储存用户对某部电影的评分

    # 初始化用户的账户iD，密码，以及一个空的字典列表
    def __init__(self, login_or_sign):
        # 注册账户
        if login_or_sign == 'login':
            self.__user_Id = __account_generated()
            self.__rating_list = {} 
        # 登录账户
        elif login_or_sign == 'sign':
            read_Id = input('Please print your user Id: ')
            self.__sign_in(read_Id)

    # 初始化一个新的userId, 并生成一个以Id为名字的csv保存信息
    def __account_generated(self):
        pass

    # 登陆时读取该用户的电影列表
    def __read_dict(self, Id):
        pass
    
    # 登录
    def __sign_in(self, Id):
        # 读取账户Id
        self.__user_Id = Id
        # 读取电影列表
        self.__rating_list

    # 搜索电影，或加入star列表
    def movie_search(self, movie_name):
        pass

    # 为电影打分
    def movie_rating(self, movie_name, rate):
        pass

    # 查看自己以打分或以star但未打分的电影
    def see_dict(self):
        pass

    # 根据自己的打分电影列表进行电影推荐
    # 基于用户的协同过滤
    def recom_movie(self):
        pass

if __name__ == '__main__':
    trial_login = user('login')
    trial_sign = user('sign')