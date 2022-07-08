##绘制10点到12点温度变化曲线

from matplotlib import pyplot as plt
import random

#设置x,y轴的值
x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

#设置图片大小
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y)

#调整x轴的刻度
_xtick_labels = ["10:{}".format(i) for i in range(60)]
_xtick_labels += ["11:{}".format(i) for i in range(60)]

#取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation = 45)  #rotatiion旋转的度数

#添加图的描述信息
plt.xlabel("Time")
plt.ylabel("Tempreture(℃)")
plt.title("the change of tempreture from 10am to 12am")

#保存和显示图像
plt.savefig("./2.png")
plt.show()