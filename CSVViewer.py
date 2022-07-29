import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import csv
csv_file = open("CSVs/SaveData.csv","r",encoding="ms932",errors="",newline="")
#リスト形式にする
f = csv.reader(csv_file,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#辞書形式
#f = csv.DictReader(csv_file)
#f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
print(header)
fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')

x = []
y = []
z = []
6
for row in f:
    #rowはList
    #row[0]で必要な項目を取得することができる
    #print(row)
    x.append(float(row[0]))
    y.append(float(row[1]))
    z.append(float(row[2]))
print(x)
print(y)
ax.scatter(x, y, z)
plt.show()