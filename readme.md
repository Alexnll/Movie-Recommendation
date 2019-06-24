# 基于movielens数据集的推荐系统构建
### 目标：
1. 对新用户基于电影热门度的推荐
2. 基于类别的电影热门度推荐
3. 基于用户个人评分的推荐
4. 基于机器学习的推荐
5. 列表搜索
6. 用户信息记录
### 2. 已完成内容
##### 1. 数据集
采用MOovieLes的ml-latest-small进行推荐系统的构建，并在ml-20m的大数据集上进行测试
##### 2. 构建基于电影相似度的推荐系统
- Movie_Correlation.py
通过每部电影的平均评分和被评分次数，计算电影间的相关性，用皮尔逊相关系数以表征
皮尔逊积相关系数（PPMCC/r/Pearson's）：用于度量两个变量X和Y之间的相关程度（线性相关），其值介于-1与1之间。
### Final
- main.py
主界面程序编写，基于命令行。
后期可使用GUI库进行优化。
### 用户信息记录

### 数据集保存位置
ml-latest-small: .\dataset\ml-latest-small\
ml-20m: .\dataset\\ml-20m\

### 数据集下载
> https://grouplens.org/datasets/movielens/