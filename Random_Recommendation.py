# 随机生成N部电影名称
import random
import pandas as pd

# 数据集位置
path_20m = '.\dataset\\ml-20m\\'
path_small = '.\dataset\\ml-latest-small\\'

# 评分标准化
def stand_rate(df):
    i = 4
    while i >= 0:
        df.loc[(df['rating'] > i) & (df['rating'] <= (i + 1)), 'rating'] = i + 1
        i -= 1

    return df

# 生成带评分内容的电影dataframe,采用评分标准化综合考虑rating和number of rating
def generate_movie(data_path=path_small):
    df_movies = pd.read_csv(data_path + 'movies.csv')
    df_ratings = pd.read_csv(data_path + 'ratings.csv')
    df_merged = pd.merge(df_ratings, df_movies, on = 'movieId')
    df_treated = pd.DataFrame(df_merged.drop(['userId', 'timestamp'], axis=1).groupby('movieId').mean())
    df_treated['number_of_ratings'] = df_merged.groupby('movieId')['rating'].count()
    df_treated = pd.merge(df_treated, df_movies, on='movieId') 
    df_treated = stand_rate(df_treated)
    df_treated = df_treated.sort_values(by=['rating', 'number_of_ratings'], ascending=(False,False))
    # print(df_treated)
    return df_treated

# 生成基于正态分布的含n个值的电影列表
def random_list(df, n=4, bias=500):
    # 重新索引
    df = df.reset_index(drop=True)
    
    i = 0
    while i < n:
        i += 1
        chose_index = int(random.gauss(0, bias))
        if chose_index < 0:
            i -= 1
            continue
        else:
            movie_name = df.loc[chose_index, 'title']
            print(i, ') ', movie_name, '\n')


# 随即推荐主函数
def rand_main(n=4):
    df = generate_movie()
    random_list(df, n=n)

if  __name__ == '__main__':
    rand_main()