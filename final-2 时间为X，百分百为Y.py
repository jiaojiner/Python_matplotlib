#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import matplotlib.pyplot as plt
import final_0_data
import matplotlib.dates as mdate
import matplotlib.ticker as mtick

fig = plt.figure(figsize=(10, 5), dpi=80)
# figsize：英寸
# dpi为分辨率：点每英寸 dots per inch

ax = fig.add_subplot(211)  # 2排，每排1张图，第一张图

# ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))  # 设置时间标签显示格式
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))  # 格式化Y轴

X = []
Y = []

for (time, cpu) in final_0_data.R1_CPU_TIME:
    X.append(time)
    Y.append(cpu)

fig.autofmt_xdate()  # 自动调整X轴格式

plt.plot(X, Y)  # 制图
plt.show()  # 显示图
