#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import matplotlib.pyplot as plt
import final_0_data

fig = plt.figure()
ax = fig.add_subplot(111)

import matplotlib.dates as mdate
# ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))  # 设置时间标签显示格式

import matplotlib.ticker as mtick
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

X1 = []
Y1 = []

for (time,cpu) in final_0_data.R1_CPU_TIME:
    X1.append(time)
    Y1.append(cpu)

X2 = []
Y2 = []

for (time, cpu) in final_0_data.R2_CPU_TIME:
    X2.append(time)
    Y2.append(cpu)

# ##########################添加注释###################################
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('路由器CPU利用率')
plt.xlabel('采集时间')
plt.ylabel('CPU利用率')
# ##########################添加注释###################################

fig.autofmt_xdate()

R1, = ax.plot(X1, Y1, linestyle='solid', color='r', label='R1')
R2, = ax.plot(X2, Y2, linestyle='dashed', color='b', label='R2')

r1_legend = ax.legend(handles=[R1], loc='upper left')
r2_legend = ax.legend(handles=[R2], loc='upper right')
ax.add_artist(r1_legend)
ax.add_artist(r2_legend)

plt.show()
