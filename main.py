# 推荐系统主程序
import Movie_Correlation
import search_movie
import Random_Recommendation

import os
import time
      
back_or_exit = "Press any buttom to go back to the selection or q to exit.\n"

# 退出文本
def print_exit():
    print()
    print("Thank you.")
    print("Successfully exit.")
    time.sleep(1)

if __name__ == "__main__":
    os.system("cls")
    # 开始界面
    print(" ________________________________________________________________ \n")
    print("|                                                                |\n")
    print("|                               Hello!                           |\n")
    print("|                                                                |\n")
    print("|          Welcome to the Movie Recommendation System            |\n")
    print("|                                                                |\n")
    print("|        This system is based on the dataset: movielens          |\n")
    print("|                                                                |\n")
    print("|    Dataset source: https://grouplens.org/datasets/movielens/   |\n")
    print("|                                                                |\n")
    print("|                  System builder: Chen Zhangxuan                |\n")
    print("|                                                                |\n")
    print("|            Press any buttom to continue or q to exit           |\n")
    print("|                                                                |\n")
    print("|________________________________________________________________|\n")

    system_open = input()
    if system_open == 'q':
        print_exit()
    
    else:
        # 选择界面
        while True:
            os.system("cls")
            print(" ________________________________________________________________ \n")
            print("|                                                                |\n")
            print("|  You can:                                                      |\n")
            print("|                                                                |\n")
            print("|      1. See some high-rating movies on MovieLens randomly;     |\n")
            print("|                                                                |\n")
            print("|      2. Input some movies you like for the Recommendation；    |\n")
            print("|                                                                |\n")
            print("|      3. Input some tags or generes you like;                   |\n")
            print("|                                                                |\n")
            print("|      4. Login in to see your personal recommendation list,     |\n")
            print("|         or rate some movies;                                   |\n")
            print("|                                                                |\n")
            print("|      Press the number to select or q to exit.                  |\n")
            print("|________________________________________________________________|\n")
        
            menu_select = input()
            # 在选择界面退出
            if menu_select == 'q':
                print_exit()
                break
            # 选择1 (已完成)
            elif menu_select == '1':
                os.system("cls")

                # 主体
                print()
                print('We will randomly recommend some movie for you now.')
                time.sleep(1)
                while True:
                    print()
                    Random_Recommendation.rand_main(n=4)  # 随机生成函数
                    print()
                    OK_or_not = input('Do these movies OK for you? Y/N ')
                    if OK_or_not == 'Y':
                        break

                # 结束
                system_open = input(back_or_exit)
                if system_open == 'q':
                    print_exit()
                    break
                else:
                    continue
            # 选择2 （已完成）
            elif menu_select == '2':
                os.system("cls")

                # 主体
                print()
                treated_list = search_movie.search_main() # 使用户输入电影列表，并在数据集中进行匹配，名称补完
                if len(treated_list) == 0:
                    print("Nothing match.")
                else:
                    Movie_Correlation.MC_main(treated_list)

                # 结束
                system_open = input(back_or_exit)
                if system_open == 'q':
                    print_exit()
                    break
                else:
                    continue
            # 选择3     
            elif menu_select == '3':
                os.system("cls")

                # 主体


                # 结束
                system_open = input(back_or_exit)
                if system_open == 'q':
                    print_exit()
                    break
                else:
                    continue
            # 选择4
            elif menu_select == '4':
                os.system("cls")

                # 主体


                # 结束
                system_open = input(back_or_exit)
                if system_open == 'q':
                    print_exit()
                    break
                else:
                    continue

            else:
                print()
                print("There is no this choice, please select again.")
                time.sleep(1)