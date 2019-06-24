# 推荐系统主程序
import Movie_Correlation

import os
import time
      
back_or_exit = "Press any buttom to go back to the selection or q to exit.\n"

# 推出文本
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
            print("|      2. Input some movies you likes for the Recommendation；   |\n")
            print("|                                                                |\n")
            print("|      3.                                                        |\n")
            print("|                                                                |\n")
            print("|      4.                                                        |\n")
            print("|                                                                |\n")
            print("|      Press the number to select or q to exit.                  |\n")
            print("|                                                                |\n")
            print("|________________________________________________________________|\n")
        
            menu_select = input()
            if menu_select == 'q':
                print_exit()
                break

            elif menu_select == '1':
                os.system("cls")

                # 主体

                # 结束

                system_open = input(back_or_exit)
                if system_open == 'q':
                    print_exit()
                    break
                else:
                    continue

            elif menu_select == '2':
                os.system("cls")

                # 主体
                print()
                print("Try input some movie you like:")
                input_list = []   # 读取list, 未完成
                search(input_list) # 未完成
                Movie_Correlation.MC_main(input_list)

                # 结束
                system_open = input(back_or_exit)
                if system_open == 'q':
                    print_exit()
                    break
                else:
                    continue
                    
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