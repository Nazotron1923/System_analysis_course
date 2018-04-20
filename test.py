from pulp import *
import time
import math
import pandas as pd
import numpy as np


def t_0(x):
    return 1.0


def t_1(x):
    return -1.0 + 2.0 * x


def t_2(x):
    return 1.0 - 8.0 * x + 8.0 * math.pow(x, 2.0)

# new_df = pd.read_csv('table_51_b.csv', index_col='Unnamed: 0')
new_df = pd.read_csv('norm_table.csv', index_col='Unnamed: 0')
# new_df = pd.DataFrame([], index=df.index, columns=df.columns)
#
#
# def normilize(x, MIN_p, MAX_p):
#     return (x - MIN_p) / (MAX_p - MIN_p)
#
#
# for col in df.columns:
#     MAX_one = max(df[col])
#     MAX = [MAX_one for i in range(45)]
#
#     MIN_one = min(df[col])
#     MIN = [MIN_one for i in range(45)]
#
#     ser = pd.Series(np.array(list(map(normilize, df[col], MIN, MAX))), index=df.index)
#     new_df[col] = ser
# min_b1 = min(new_df.Y1)
# min_b2 = min(new_df.Y2)
# min_b3 = min(new_df.Y3)
# min_b4 = min(new_df.Y4)
#
# max_b1 = max(new_df.Y1)
# max_b2 = max(new_df.Y2)
# max_b3 = max(new_df.Y3)
# max_b4 = max(new_df.Y4)
#
# b1 = (max_b1 + min_b1)/2
# b2 = (max_b2 + min_b2)/2
# b3 = (max_b3 + min_b3)/2
# b4 = (max_b4 + min_b4)/2
#
# b = []
#
# for i in range(45):
#     min_b = min(new_df[['Y1', 'Y2', 'Y3', 'Y4']].iloc[i])
#     max_b = max(new_df[['Y1', 'Y2', 'Y3', 'Y4']].iloc[i])
#     b.append((min_b + max_b)/2)
#
# bo = np.array(b)
# boo = pd.Series(bo, index=new_df.index)
# new_df['b_row'] =  pd.Series(bo, index=new_df.index)
#
# b_1 = np.array([0.5 for i in range(45)])
# b11 = pd.Series(b_1, index=new_df.index)
# new_df['b_col'] =  pd.Series(b11, index=new_df.index)






start = time.time()

lx11_1 = pulp.LpVariable("lx11_1")
lx11_2 = pulp.LpVariable("lx11_2")
lx11_3 = pulp.LpVariable("lx11_3")

lx12_1 = pulp.LpVariable("lx12_1")
lx12_2 = pulp.LpVariable("lx12_2")
lx12_3 = pulp.LpVariable("lx12_3")

lx21_1 = pulp.LpVariable("lx21_1")
lx21_2 = pulp.LpVariable("lx21_2")
lx21_3 = pulp.LpVariable("lx21_3")

lx22_1 = pulp.LpVariable("lx22_1")
lx22_2 = pulp.LpVariable("lx22_2")
lx22_3 = pulp.LpVariable("lx22_3")

lx31_1 = pulp.LpVariable("lx31_1")
lx31_2 = pulp.LpVariable("lx31_2")
lx31_3 = pulp.LpVariable("lx31_3")

lx32_1 = pulp.LpVariable("lx32_1")
lx32_2 = pulp.LpVariable("lx32_2")
lx32_3 = pulp.LpVariable("lx32_3")

lx33_1 = pulp.LpVariable("lx33_1")
lx33_2 = pulp.LpVariable("lx33_2")
lx33_3 = pulp.LpVariable("lx33_3")









l_facke = pulp.LpVariable("l_facke", lowBound=0)


y = []

for i in range(90):
    str_n = str('y') + str(i)
    y.append(pulp.LpVariable(str_n, lowBound=0))



problem = pulp.LpProblem('0',pulp.LpMinimize)

problem += l_facke, "Функция цели"
for i in range(45):
    problem += y[i] == lx11_1 * t_0(new_df['x11'].iloc[i]) + lx11_2 * t_1(new_df['x11'].iloc[i]) + lx11_3 * t_2(new_df['x11'].iloc[i]) + \
                       lx12_1 * t_0(new_df['x12'].iloc[i]) + lx12_2 * t_1(new_df['x12'].iloc[i]) + lx12_3 * t_2(new_df['x12'].iloc[i]) + \
                       lx21_1 * t_0(new_df['x21'].iloc[i]) + lx21_2 * t_1(new_df['x21'].iloc[i]) + lx21_3 * t_2(new_df['x21'].iloc[i]) + \
                       lx22_1 * t_0(new_df['x22'].iloc[i]) + lx22_2 * t_1(new_df['x22'].iloc[i]) + lx22_3 * t_2(new_df['x22'].iloc[i]) + \
                       lx31_1 * t_0(new_df['x31'].iloc[i]) + lx31_2 * t_1(new_df['x31'].iloc[i]) + lx31_3 * t_2(new_df['x31'].iloc[i]) + \
                       lx32_1 * t_0(new_df['x32'].iloc[i]) + lx32_2 * t_1(new_df['x32'].iloc[i]) + lx32_3 * t_2(new_df['x32'].iloc[i]) + \
                       lx33_1 * t_0(new_df['x33'].iloc[i]) + lx33_2 * t_1(new_df['x33'].iloc[i]) + lx33_3 * t_2(new_df['x33'].iloc[i]) + l_facke - new_df['b_row'].iloc[i] >= 0, str(i+1)

for i in range(45):
    problem += y[i] == (-lx11_1) * t_0(new_df['x11'].iloc[i]) - lx11_2 * t_1(new_df['x11'].iloc[i]) - lx11_3 * t_2(new_df['x11'].iloc[i]) + \
                       (-lx12_1) * t_0(new_df['x12'].iloc[i]) - lx12_2 * t_1(new_df['x12'].iloc[i]) - lx12_3 * t_2(new_df['x12'].iloc[i]) + \
                       (-lx21_1) * t_0(new_df['x21'].iloc[i]) - lx21_2 * t_1(new_df['x21'].iloc[i]) - lx21_3 * t_2(new_df['x21'].iloc[i]) + \
                       (-lx22_1) * t_0(new_df['x22'].iloc[i]) - lx22_2 * t_1(new_df['x22'].iloc[i]) - lx22_3 * t_2(new_df['x22'].iloc[i]) + \
                       (-lx31_1) * t_0(new_df['x31'].iloc[i]) - lx31_2 * t_1(new_df['x31'].iloc[i]) - lx31_3 * t_2(new_df['x31'].iloc[i]) + \
                       (-lx32_1) * t_0(new_df['x32'].iloc[i]) - lx32_2 * t_1(new_df['x32'].iloc[i]) - lx32_3 * t_2(new_df['x32'].iloc[i]) + \
                       (-lx33_1) * t_0(new_df['x33'].iloc[i]) - lx33_2 * t_1(new_df['x33'].iloc[i]) - lx33_3 * t_2(new_df['x33'].iloc[i]) + l_facke + new_df['b_row'].iloc[i] >= 0, str(i + 46)







problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Прибыль:")
print (value(problem.objective))
stop = time.time()
print ("Время :")
print(stop - start)

# df = pd.read_csv('test.csv', index_col='Unnamed: 0')
# new_df = pd.DataFrame([], index=df.index, columns=df.columns)
#
#
# def normilize(x, MIN_p, MAX_p):
#     return (x - MIN_p) / (MAX_p - MIN_p)
#
#
# for col in df.columns:
#     MAX_one = max(df[col])
#     MAX = [MAX_one for i in range(45)]
#
#     MIN_one = min(df[col])
#     MIN = [MIN_one for i in range(45)]
#
#     ser = pd.Series(np.array(list(map(normilize, df[col], MIN, MAX))), index=df.index)
#     new_df[col] = ser
# min_b1 = min(new_df.Y1)
# min_b2 = min(new_df.Y2)
# min_b3 = min(new_df.Y3)
# min_b4 = min(new_df.Y4)
#
# max_b1 = max(new_df.Y1)
# max_b2 = max(new_df.Y2)
# max_b3 = max(new_df.Y3)
# max_b4 = max(new_df.Y4)
#
# b1 = (max_b1 + min_b1)/2
# b2 = (max_b2 + min_b2)/2
# b3 = (max_b3 + min_b3)/2
# b4 = (max_b4 + min_b4)/2
# for i in range(45):
#     min_b = min(new_df[['Y1', 'Y2', 'Y3', 'Y4']].iloc[i])
#     max_b = max(new_df[['Y1', 'Y2', 'Y3', 'Y4']].iloc[i])
#     b.append((min_b + max_b)/2)

# bo = np.array(b)
# boo = pd.Series(bo, index=new_df.index)
# new_df['b_row'] =  pd.Series(bo, index=new_df.index)

# b1 = np.array([0.5 for i in range(45)])
# b11 = pd.Series(b1, index=new_df.index)
# new_df['b_col'] =  pd.Series(b11, index=new_df.index)
