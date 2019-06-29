# 查看数据集并进行预处理
# 实现基于物品的协同过滤
# 采用皮尔逊积相关系数表征电影之间的相关性
import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn  as sns
import os

import warnings

# 数据集储存的位置
data_path = '.\dataset\\'
path_20m = '.\dataset\\ml-20m\\'
path_small = '.\dataset\\ml-latest-small\\'

# read dataset and merge them together
def merge_data(path = path_small):
    df_ratings = pd.read_csv(path +  'ratings.csv')
    df_movies = pd.read_csv(path + 'movies.csv')
    # print("movies: \n", df_movies.head())
    # print("ratings: \n", df_ratings.head())

    # link the two dataframe with column "movieId"
    df_merged = pd.merge(df_ratings, df_movies, on = 'movieId')
    # print("merged data: \n", df_merged.head())
    
    # print("mean rating: %f" % df_merged['rating'].mean())
    # print("dataset infomation: \n", df_merged.info())
    
    return df_merged

# 构建包含每部电影平均评分和被评分次数的dataframe，用以观察数据
# 返回电影平均评分以及被评分数据的dataframe
def construct_r(df):
    # 每部电影的平均分数
    ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
    # 添加每部电影评分次数的columns
    ratings['number_of_ratings'] = df.groupby('title')['rating'].count()
    # print(ratings.head())
    # print()
    # print(ratings.info())
    # print()

    # ratings['rating'].hist(bins=50)   # bins表示图中显示的列数
    # ratings['number_of_ratings'].hist(bins=50)
    # 电影评分与被评分次数之间的散点图
    #sns.jointplot(x='rating', y='number_of_ratings', data=ratings)

    # plt.show()

    return ratings

# 构建基于电影相似度的推荐系统
def construct_RS(df_merged, ratings, user_list, setting_number=100):
    # 构建电影矩阵用以计算相关性
    # 电影之间相关性越高，越相似
    # 矩阵中呈现较多空值
    movie_matrix = df_merged.pivot_table(index='userId', columns='title', values='rating')
    # print("movie matrix: \n", movie_matrix.head())
    # print()
    
    # 查看评分人数最多的电影
    # print("the highest rating movies: \n", ratings.sort_values('number_of_ratings', ascending=False).head())
    # print()
    
    # 基于用户看过的电影
    for movie in user_list:
        if movie == "":
            continue
        else:
            print()
            print("--> " + "Based on the movie " + movie)

            movie_user_rating = movie_matrix[movie]
            # print(movie, ': \n', movie_user_rating.head())
            # print()

            # 用corrwith功能统计两个dataframe对象间两两相关的关系
            similar_movie = movie_matrix.corrwith(movie_user_rating)
            # print("similar_movie: \n", similar_movie.head())
            # print()

            # 删除表中的缺失值并转化为dataframe对象
            corr_movie = pd.DataFrame(similar_movie, columns=['Correlation'])
            corr_movie.dropna(inplace=True)
            # print("corr_movie: \n", corr_movie.head())
            # print()

            # 设置评分次数阈值
            # 利用join方法在corr_movie中加入ratings的number of ratings列
            corr_movie = corr_movie.join(ratings['number_of_ratings'])
            # print("corr_movie: \n", corr_movie.head())
            # print()
            corr_movie_after_treated = corr_movie[corr_movie['number_of_ratings'] > setting_number].sort_values(by='Correlation', ascending=False)        
            # 去除第一行（即该电影本身）
            corr_movie_after_treated.drop(index=[movie], inplace=True)
            # print("corr_movie after treated: \n", corr_movie_after_treated.head())
            print("Recommended list: \n", corr_movie_after_treated.head())
            print()

            # 是否保存
            #save = input("Do you want to save the " + "recommended movies based on " + movie + " as .csv? Y/N ")
            #if save == 'Y':
            #    similar_movie.to_csv(data_path + 'Recommendation based on ' + movie + '.csv')
        
    clear_screen = input("Clean the screen? Y/N ")
    if clear_screen == "Y":
        os.system("cls")



# 主程序
def MC_main(user_list, setting_number=100):
    warnings.filterwarnings('ignore')  # 忽略python warning
    df_merged = merge_data(path_small)
    ratings = construct_r(df_merged)
    construct_RS(df_merged=df_merged, ratings=ratings, user_list=user_list, setting_number=setting_number)

if __name__ == '__main__':
    # 用户看过的电影
    user_list = ['Forrest Gump (1994)', 'Pulp Fiction (1994)']
    MC_main(user_list)