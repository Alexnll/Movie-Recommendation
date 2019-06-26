# 随机生成N部电影名称
import random
import pandas as pd

# 数据集位置
path_20m = '.\dataset\\ml-20m\\'
path_small = '.\dataset\\ml-latest-small\\'

# 生成带评分内容的电影dataframe,此处忽略评分人数带来的误差
def generate_movie(data_path=path_small):
    df_movies = pd.read_csv(data_path + 'movies.csv', usecols=['movieId', 'title'])
    df_ratings = pd.read_csv(data_path + 'ratings.csv', usecols=['movieId', 'rating'])
    df_merged = pd.merge(df_ratings, df_movies, on = 'movieId')
    df_treated = pd.DataFrame(df_merged.groupby('title')['rating'].mean()).sort_values('rating', ascending=False)
    # print(df_treated)
    return df_treated

# 生成基于正态分布的含n个值的电影列表
def random_list(df, n=4):
    i = 0
    while i < n:
        i += 1
        chose_index = int(random.gauss(0, 500))
        if chose_index <= 0:
            i -= 1
            continue
        else:
            movie_name = df.iloc[chose_index-1:chose_index]
            print(i, ') ', movie_name.index[0], '\n')


# 随即推荐主函数
def rand_main(n=4):
    df = generate_movie()
    random_list(df, n=n)

if  __name__ == '__main__':
    rand_main()