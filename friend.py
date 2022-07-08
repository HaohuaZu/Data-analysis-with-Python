#绘制你和同桌两个人男女朋友数量变化
# coding=utf-8
from matplotlib import pyplot as plt

y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]

x = range(11,31)

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y_1,label="me",color="blue")
plt.plot(x,y_2,label="friend",color="#DB7093",linestyle="--")

#设置x轴刻度，可能密集或者稀疏一些
_xtick_labels = ["age{}".format(i) for i in x]
plt.xticks(x,_xtick_labels)
# plt.yticks(range(0,9))

#绘制网格
plt.grid(alpha=0.4,linestyle=':')

#添加图例
plt.legend(loc="upper left")

#图像保存
plt.savefig("./t1.png")
#可以保存为.svg格式，矢量图

#展示
plt.show()