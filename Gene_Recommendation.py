# 基于电影类别（genres）的电影推荐
# 类别分隔符 |
import pandas as pd
import numpy as np

import warnings

# 数据集储存的位置
path_20m = '.\dataset\\ml-20m\\'
path_small = '.\dataset\\ml-latest-small\\'

# genres种类
genres = []

# read dataset, merge and preprocess
def merge_data(path=path_small):
    # 原始数据合并
    df_movies = pd.read_csv(path + 'movies.csv')
    df_ratings = pd.read_csv(path + 'ratings.csv')    
    df_merged = pd.merge(df_ratings, df_movies, on = 'movieId')
    df_treated = pd.DataFrame(df_merged.drop(['userId', 'timestamp'], axis=1).groupby('movieId').mean())
    df_treated['number_of_ratings'] = df_merged.groupby('movieId')['rating'].count()
    df_treated = pd.merge(df_treated, df_movies.drop(['title'], axis=1), on='movieId') 
    # print(df_treated.head())

    # 分离得到genres
    global genres
    genres_series = df_treated.genres
    for gene in genres_series:
        genres_array = gene.split('|')
        for g in genres_array:
            if g not in genres:
                genres.append(g)

    return df_treated

# 进行电影df的构造
def df_splited():
    df = merge_data()
    global genres
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
            df[gene][df['movieId'] == movie.movieId] = 1
            
    print(df.head())
    
# 根据用户喜好的类别推荐
def gene_recommend(user_genres):
    for gene in user_genres:


# main
def Gene_main():
    warnings.filterwarnings('ignore')  # 忽略python warning
    df_splited()

if __name__ == '__main__':
    user_genres = ['Action', 'Comedy']
    Gene_main()
    