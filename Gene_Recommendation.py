# 基于电影类别（genres）的电影推荐
# 类别分隔符 |
import pandas as pd
import numpy as np
import Random_Recommendation

import warnings
import os
import random

# 数据集储存的位置
path_20m = '.\dataset\\ml-20m\\'
path_small = '.\dataset\\ml-latest-small\\'

# read dataset, merge and preprocess
def merge_data(path=path_small):
    # 原始数据合并
    df_movies = pd.read_csv(path + 'movies.csv')
    df_ratings = pd.read_csv(path + 'ratings.csv') 

    df_merged = pd.merge(df_ratings, df_movies, on = 'movieId')
    df_treated = pd.DataFrame(df_merged.drop(['userId', 'timestamp'], axis=1).groupby('movieId').mean())
    df_treated['number_of_ratings'] = df_merged.groupby('movieId')['rating'].count()
    df_treated = pd.merge(df_treated, df_movies, on='movieId') 
    # print(df_treated.head())

    return df_treated

# 分离得到genres，此处的genres后续改进中可作为全局变量，或保存在文本中
def get_genres():
    # genres种类
    genres = []
    df_treated = merge_data()
    genres_series = df_treated.genres
    for gene in genres_series:
        genres_array = gene.split('|')
        for g in genres_array:
            if g not in genres:
                genres.append(g)
    
    return genres

# 进行电影df的构造
# 该函数较耗时，故将构造的dataframe保存
def df_splited():
    df = merge_data()
    genres = get_genres()
    # print(len(genres))
    
    # 添加所有genres的列
    for col in genres:
        df[col] = 0
    # print(df.head())

    for movie in df.itertuples():
        # 某一行的电影的类别list
        movie_genres = movie.genres.split('|')
        # print(movie.movieId)
        # print(df[df['movieId'] == movie.movieId])
        # print(movie_genres)

        # 若某电影包含某类别，则将该列的值赋1
        for gene in movie_genres:
            df.loc[movie.Index, gene] = 1
            
    # print(df.head())
    df.to_csv('.\\dataset\\movie_genres.csv')
    print("Successfully construct.\n")

# 将用户输入的字符串转为list形式
def treat_input():
    text = input("\nTry input some genres you like separated with \", \": \n")
    list_get = text.split(sep=', ')
    genres_list = get_genres()
    for gene in list_get:
        if gene not in genres_list:
            list_get.remove(gene)
            print('\nCan not read ' + gene + '\n')
    return list_get

# 评分标准化
def stand_rate(df):
    i = 4
    while i >= 0:
        df.loc[(df['rating'] > i) & (df['rating'] <= (i + 1)), 'rating'] = i + 1
        i -= 1
    
    return df

# 生成基于正态分布的含n个值的电影列表
def random_list(df, n=4, bias=500):
    i = 0
    while i < n:
        i += 1
        chose_index = int(random.gauss(0, bias))
        if chose_index <= 0:
            i -= 1
            continue
        else:
            movie_name = df.iloc[chose_index-1:chose_index]
            print(i, ') ', movie_name.index[0], '\n')


# 根据用户喜好的类别推荐
def gene_recommend(user_genres, n=4, bias=100):
    # 读取df_splited中生成的dataframe
    movie_genres_matrix = pd.read_csv('.\\dataset\\movie_genres.csv')
    for gene in user_genres:
        print("\n--> Base on the gene: " + gene)
        # 筛选dataframe
        df_filter = movie_genres_matrix.loc[movie_genres_matrix[gene] == 1, ['movieId', 'title', 'rating', 'number_of_ratings', gene]]
        
        # 由于此处难以同时对评分和评分人数进行综合评价，故对rating进行标准化分级，如大于4.5分为5分，4.0~4.5分为4.5分
        df_filter = stand_rate(df_filter)
        # 排序
        df_filter = df_filter.sort_values(by=['rating', 'number_of_ratings'], ascending=(False,False))
        # 重新索引
        df_filter = df_filter.reset_index(drop=True)
        
        i = 0
        while i < n:
            i += 1
            chose_index = int(random.gauss(0, bias))
            if chose_index < 0:
                i -= 1
                continue
            else:
                movie_name = df_filter.loc[chose_index, 'title']
                print(i, ') ', movie_name, '\n')


    clear_screen = input("Clean the screen? Y/N ")
    if clear_screen == "Y":
        os.system("cls")

# main
def Gene_main():
    warnings.filterwarnings('ignore')  # 忽略python warning
    print("All Genres types are showed as follow:\n", get_genres(), '\n')
    
    # 是否构造电影类别矩阵
    constru_matrix = input("Construct new movie genres matrix? Y/N ")
    if constru_matrix == 'Y':
        df_splited()
    
    # 用户输入喜好的类型，进行推荐
    user_genres = treat_input()
    if user_genres != []:
        gene_recommend(user_genres)
    else:
        print("You did not print anything.\n")

if __name__ == '__main__':
    Gene_main()
    