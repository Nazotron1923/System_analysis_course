import pandas as pd
import numpy as np
import scipy.linalg as la


def t_0(x):
    return 0.5


def t_1(x):
    return -1.0 + 2.0 * x


def t_2(x):
    return 1.0 - 8.0 * x + 8.0 * (x**2)


new_df = pd.read_csv('norm_table.csv', index_col='Unnamed: 0')
A = []
for i in range(45):
    row_lin = [t_0(new_df['x11'].iloc[i]), t_1(new_df['x11'].iloc[i]), t_2(new_df['x11'].iloc[i]),
                    t_0(new_df['x12'].iloc[i]), t_1(new_df['x12'].iloc[i]),t_2(new_df['x12'].iloc[i]),
                    t_0(new_df['x21'].iloc[i]), t_1(new_df['x21'].iloc[i]), t_2(new_df['x21'].iloc[i]),
                    t_0(new_df['x22'].iloc[i]), t_1(new_df['x22'].iloc[i]), t_2(new_df['x22'].iloc[i]),
                    t_0(new_df['x31'].iloc[i]), t_1(new_df['x31'].iloc[i]), t_2(new_df['x31'].iloc[i]),
                    t_0(new_df['x32'].iloc[i]), t_1(new_df['x32'].iloc[i]), t_2(new_df['x32'].iloc[i]),
                    t_0(new_df['x33'].iloc[i]), t_1(new_df['x33'].iloc[i]), t_2(new_df['x33'].iloc[i])
             ]
    A.append(row_lin)


matrix_A = np.array(A)


b = list(new_df['Y2'])
len(b)


b_vec = np.array(b)

np.linalg.matrix_rank(matrix_A)

U = la.lstsq(matrix_A, b_vec)