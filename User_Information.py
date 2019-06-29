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

# 评分范围
rating_range = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

class user:
    
    __user_Id = None
    __rating_df = None  # 储存用户对某部电影的评分
    __star_list = None # star列表
    __path_this_user = None # 用户文件储存的位置

    # 初始化对象，注册或登录
    def __init__(self, Sign_in_or_up):
        # 注册账户
        if Sign_in_or_up == 'up': 
            self.__account_generated()

        # 登录账户
        elif Sign_in_or_up == 'in':
            read_Id = input('Please print your user Id: ')
            self.__sign_in(read_Id)
        # 错误输入，尝试阻止对象的初始化
        else:
            print('Wrong input. Please try again.')

    # 当路径不存在时，创建路径
    def __mkdir_if_not_exist(self, path):
        if os.path.exists(path) == False:
            os.makedirs(path)

    # 初始化一个新的userId, 并生成一个以Id为名字的csv保存rating信息，生成一个以Id为名字的txt保存star_list信息
    # id为六位数
    def __account_generated(self):
        length = 6 # 六位数
        user_list = os.listdir(path_user)
        # 随机生成新id
        while True:
            r_id = str(random.randint(math.pow(10, 5), math.pow(10, 6)-1))
            if r_id not in user_list:
                self.__user_Id = r_id
                break
        print('This is your id, pleasure remember: ', self.__user_Id, '\n')
        
        # 生成以id命名的文件夹以保存该用户的csv和txt文件
        self.__path_this_user = path_user + '\\' + self.__user_Id
        self.__mkdir_if_not_exist(self.__path_this_user)
        
        # 生成空rating的df
        self.__rating_df = pd.DataFrame(columns=['userId', 'movieId', 'title', 'rating'])
        # 新建csv文件
        self.__rating_df.to_csv(self.__path_this_user + '\\' + self.__user_Id + '.csv')
        # 生成新的star列表
        self.__star_list = []
        # 新建txt文件
        with open(self.__path_this_user + '\\' + self.__user_Id + '.txt', 'wb') as f:
            pass
    
    # 登录
    def __sign_in(self, print_Id):
        if Id in os.listdir(path_user):
            # 读取账户Id
            self.__user_Id = print_Id
            self.__path_this_user = path_user + '\\' + self.__user_Id
            # 读取电影列表
            self.__rating_df = pd.read_csv(self.__path_this_user + '\\' + self.__user_Id + '.csv')
            # 读取star列表

        else:
            print("The id printed does not exist. Please sign again.\n")
            # 销毁对象



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

    # 查看自己的id
    def show_id(self):
        print("Your user Id is: ", self.__user_Id)
        return self.__user_Id

    # 查看自己以打分或以star但未打分的电影
    def see_list(self):
        # 展示star list
        if len(self.__star_list) != 0:
            print('\nYour star list is showed as follow: ')
            for movie_name in self.__star_list:
                print('--> ', movie_name)
            print('\nEnd.\n')
        # 展示rating list
        

    # 销毁当前账户
    def delete_account(self):
        choose = input("You sure you want to delete your account? Y/N")
        if choose == 'Y':
            for fi in os.listdir(self.__path_this_user):
                os.remove(self.__path_this_user + '\\' + fi)
            os.rmdir(self.__path_this_user)
            print('\nSuccessfully delete your account: ' + self.__user_Id + '. You can not use this account to sign in again.')


    # 根据自己的打分电影列表进行电影推荐
    # 基于用户的协同过滤
    def recom_movie(self):
        pass


if __name__ == '__main__':
    read = input('print in or up: ')
    trial_login = user(read)

