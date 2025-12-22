from numpy import *
from numpy import dot 
from numpy.linalg import norm 
import numpy as np 
import pandas as pandas
import math
import matplotlib.pyplot as plt

def cosine_distance(a, b):
    return 1 - cosine_similarity(a, b)

def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b)) # angle between the vectors

def find_end_points(point, angle, length): # purpose is to find end points to plot the function
    '''
    point - Tuple (x, y)
    angle - Angle you want your end point at in degrees.
    length - Length of the line you want to plot.

    Will plot the line on a 10 x 10 plot.
    '''

    x, y = point # unpacking / deconstructing
    
    # take point as an argument then polar -> cartesian 
    endy = length * math.sin(math.radians(angle))
    endx = length * math.cos(math.radians(angle))

    return (endx, endy)

column_header = ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10']
row_header = ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10']
doc_term = array([
    # D0   D1   D2   D3   D4   D5   D6   D7   D8   D9   D10  D11   (a 2D numpy array)
    [0.1, 0.1, 0.0, 0.1, 0.2, 0.0, 0.1, 0.9, 0.9, 0.3, 0.0, 0.8],
    [0.1, 0.1, 0.0, 0.1, 0.0, 0.0, 0.1, 0.9, 0.0, 0.3, 0.0, 0.8],
    [0.0, 0.0, 0.9, 0.0, 0.3, 0.1, 0.7, 0.0, 0.2, 0.7, 0.5, 0.5],
    [0.0, 0.0, 0.9, 0.1, 0.0, 0.1, 0.9, 0.3, 0.8, 0.4, 0.1, 0.4],
    [0.0, 0.0, 0.0, 0.0, 0.5, 0.9, 0.3, 0.7, 0.4, 0.6, 0.0, 0.3],
    [0.5, 0.6, 0.0, 0.7, 0.3, 0.3, 0.9, 0.1, 0.0, 0.0, 0.0, 0.3],
    [0.0, 0.0, 0.8, 0.0, 0.6, 0.6, 0.0, 0.1, 0.4, 0.9, 0.3, 0.1],
    [0.35, 0.4, 0.0, 0.5, 0.5, 0.1, 0.7, 0.1, 0.5, 0.3, 0.8, 0.1],
    [0.3, 0.3, 0.0, 0.2, 0.8, 0.7, 0.7, 0.8, 0.0, 0.6, 0.8, 0.0],
    [0.0, 0.0, 0.5, 0.0, 0.2, 0.0, 0.0, 0.1, 0.0, 0.4, 0.5, 0.3]
])

# all are python lists
cos_similarity_list = []
pd_cols_cos_similarity = []
cos_distance_list = []
pd_cols_cos_distance = []

for i in range(0, 11):
    for j in range(0, 11):
        cos_value = cosine_similarity(doc_term[:,[i]], doc_term[:,[j]]) # here [j] or [i] instead of i or j is due to preserving array dimensions in numpy
        cos_distance = 1 - cos_value
        cos_distance_list.append(asscalar(around(cos_distance, decimals = 3)))
        cos_similarity_list.append(asscalar(around(math.degrees(math.acos(min(max(cos_value, -1.0), 1.0))), decimals=1)))
    pd_cols_cos_similarity.append(cos_similarity_list)
    pd_cols_cos_distance.append(cos_distance_list)
    cos_similarity_list = []
    cos_distance_list = []

# lists -> pandas df

df_cos_sim = pd.DataFrame(pd_cols_cos_similarity, columns = column_header, index = row_header)
print(df_cos_sim)

df_cos_dis = pd.DataFrame(pd_cols_cos_distance, columns=column_header, index=row_header)
print(df_cos_dis)

fig = plt.figure()
ax = plt.subplot(111)
ax.set_ylim([0, 1.75])
ax.set_xlim([0, 1.75])

ref_doc = 0 # choosing D0 as reference document (will be comparing against this)
for i in range(0, 11):
    X, Y = find_end_points([0, 0], df_cos_sim.iloc[ref_doc][i], norm(doc_term[:, [i]])) # will return X, Y coordinates of the end point
    ax.plot(X, Y)
    ax.annotate("", xy=(X[1], Y[1]), xytext=(0, 0), arrowprops=dict(arrowstyle="->")) # Draws arrow from (0, 0) to endpoint (X[1], Y[1])
    ax.text(X[1], Y[1], "D" + str(ref_doc) + "-" + "D" + str(i) + "-(" + str(df_cos_sim.iloc[ref_doc][i]) + u"\u00b0" + ")") # adds labeling
fig.show()

query = "D" + str(ref_doc)
rank_order = df_cos_sim.sort_values(query) # sorts documents by their similarity to D0
print ("\n\nDocument Rank for the query ", query)
print(rank_order[query])
