import numpy as np
from scipy import linalg 
import time
import matplotlib.pyplot as plt
import pandas as pd

def time_solve_lineq(n):
    a = np.random.randint(1, 2*n, size=(n, n))
    b = np.random.randint(1,n, size =n)
    try:
        start = time.time()
        linalg.solve(a,b)
        end = time.time()
        return end - start
    except np.linalg.LinAlgError:
        return time_solve_lineq(n)

X = np.linspace(1000 , 10000 , 25 , dtype=np.int32)
# # plt.plot(X , time_solve_lineq(x) for x in X)
# Y =np.array([time_solve_lineq(x) for x in X])
# plt.plot(X, Y, marker= '.', linestyle='--' )
# plt.xscale('log')
# plt.yscale('log')
# plt.show()

count_of_variables = np.logspace(1,15,15,base=2,dtype=np.int32)
times_of_solves = np.array([time_solve_lineq(x) for x in count_of_variables])

ratios = np.array([None]*len(times_of_solves))
for i in range(len(times_of_solves) -1):
    ratios[i + 1] = times_of_solves[i+1]/times_of_solves[i]

logs = np.array([None]*len(times_of_solves))
for i in range(1, len(times_of_solves)):
    logs[i] = np.log2(ratios[i])

df = pd.DataFrame()
df['count_of_variables'] = count_of_variables.tolist()
df["times_of_solves"] = times_of_solves.tolist()
df['ratios'] = ratios.tolist()
df['logs'] = logs.tolist()
print(df)
df.to_csv('wyniki_czasu2.csv')
