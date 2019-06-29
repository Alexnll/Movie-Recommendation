# 用于用户的登录与注册
# 保存用户的评分信息于csv中
# 读取用户信息并于总数据集合并
# 注意用户每次只能对一部电影保存一次评分，新的评分将会覆盖旧评分
# 评分范围为0.5 ~ 5.0 stars
import numpy as np
import pandas as pd

import random
import math
import os

import search_movie

# 数据集地址
path_20m = '.\\dataset\\ml-20m\\'
path_small = '.\\dataset\\ml-latest-small\\'

# 用户信息保存地址
path_user = '.\\new_user'

class user:
    __user_Id = None
    __rating_list = None  # 储存用户对某部电影的评分，储存格式，'row1': {'movieId': , 'title': , 'rating': }
    __star_list = None # star列表

    # 初始化用户的账户iD，密码，以及一个空的字典列表
    def __init__(self, Sign_in_or_up):
        # 注册账户
        if Sign_in_or_up == 'up': 
            self.__account_generated()

        # 登录账户
        elif Sign_in_or_up == 'in':
            read_Id = input('Please print your user Id: ')
            self.__sign_in(read_Id)

    # 初始化一个新的userId, 并生成一个以Id为名字的csv保存rating信息，生成一个以Id为名字的txt保存star_list信息
    # id为六位数
    def __account_generated(self):
        length = 6 # 六位数
        user_list = os.listdir(path_user)
        while True:
            user_id = random.randiant(math.pow(10, 5), math.pow(10, 6)-1)
            if user_id not in user_list:
                self.__user_Id = user_id
                break
        print('This is your id, pleasure remember: ', id, '\n')

        # 新建csv文件
        self.__rating_list = {}
        movie_df = pd.DataFrame.from_dict(self.__rating_list, orient='index',columns=['movieId', 'title', 'rating'])
        movie_df.to_csv(path_user + '\\' + id + '.csv')

        # 新建txt文件
        self.__star_list = []
    
    # 登录
    def __sign_in(self, Id):
        # 读取账户Id
        self.__user_Id = Id
        # 读取电影列表
        movie_df = pd.read_csv(path_user + '\\' + id + '.csv')
        self.__rating_list = movie_df.to_dict('index')
        # 读取star列表

    # 搜索电影，或加入star列表
    def movie_search(self, movie_name):
        # 搜索电影
        name = search_movie.fill(movie_name)
        
        if name != '':
            # 加入star list
            add_to_list = input('Do you want to add this movie into your star list? Y/N ')
            if add_to_list == 'Y':
                if name not in self.__star_list:
                    self.__star_list.append(name)
                    print('Successfully append.\n')
                    # 添加到txt中

                else:
                    print('The movie' + name + ' has already your star list.\n')
        else:
            print('Can not find the movie matching ' + movie_name + '.\n')

    # 为电影打分
    def movie_rating(self, movie_name, rate):
        pass

    # 查看自己以打分或以star但未打分的电影
    def see_dict(self):
        print(self.__star_list)
        print(self.__rating_list)

    # 根据自己的打分电影列表进行电影推荐
    # 基于用户的协同过滤
    def recom_movie(self):
        pass


if __name__ == '__main__':
    trial_login = user('login')
    trial_sign = user('sign')