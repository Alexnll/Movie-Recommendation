# 在数据集中搜索用户输入的电影以匹配
# 当用户输入电影名不完全时，进行补完
import pandas as pd
import os

# 电影名文件集
path_20m = '.\dataset\\ml-20m\\movies.csv'
path_small = '.\dataset\\ml-latest-small\\movies.csv'

# 将用户输入的字符串转为list形式
def treat_input():
    text = input("Try input some movie you like separated with \", \", \ninput longer name will help increase the accuracy: \n")
    list_get = text.split(sep=', ')
    return list_get
    
# 在电影目录中找到补完后的结果，若无匹配对象，则返回None
def fill(movie_name_after_treated, data=path_small):
    df_movies = pd.read_csv(data, usecols=['title'])
    # series对象才有str方法，dataframe并无
    filter_data = df_movies[df_movies['title'].str.contains(movie_name_after_treated)]
    for movie_name in filter_data.itertuples():
        name = getattr(movie_name, 'title')
        user_choose = input("Do you mean %s ? Y/N " % name)
        if user_choose == 'Y':
            # os.system('cls')
            return name
            break
        else:
            print()

    return ""  

def search_main(limit=4):
    user_input = treat_input()
    i = 0
    for movie in user_input:
        # 输入电影字符小于limit时，处理为空值，默认设为4
        if len(movie) <= limit:
            print()
            print("The input movie name " + movie + " is too short, ")
            print("so that we just can only jump pass it.")
            user_input[i] = ""
        else:    
            user_input[i] = fill(movie)
        i += 1

    # 去除list中的空值
    l = len(user_input)
    x = 0
    while x < l:
        if user_input[x] == "":
            del user_input[x]
            x -= 1
            l -= 1
        x += 1
        
    os.system('cls')
    return user_input

if __name__ == "__main__":
    user_list = ['Forrest Gump (1994)', 'Pulp Fiction (1994)']
    search_main()