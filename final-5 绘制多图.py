#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import matplotlib.pyplot as plt
import final_0_data

fig=plt.figure()
ax1 = fig.add_subplot(211)  # 2排，每排1张图，第一张图
ax2 = fig.add_subplot(212)  # 2排，每排1张图，第二张图

import matplotlib.dates as mdate
# ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
ax1.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))  # 设置时间标签显示格式
ax2.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))  # 设置时间标签显示格式


import matplotlib.ticker as mtick
ax1.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))
ax2.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

X1 = []
Y1 = []

for (time, cpu) in final_0_data.R1_CPU_TIME:
    X1.append(time)
    Y1.append(cpu)

X2 = []
Y2 = []

for (time, cpu) in final_0_data.R2_CPU_TIME:
    X2.append(time)
    Y2.append(cpu)



R1, = ax1.plot(X1, Y1, linestyle='solid', color='r', label='R1')
R2, = ax2.plot(X2, Y2, linestyle='dashed', color='b', label='R2')

ax1.legend(loc='upper left')
ax2.legend(loc='upper left')

# ##########################添加注释###################################
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.suptitle('路由器CPU利用率')  # 超级标题

# ########################每张图的小标注###############################
ax1.set_title("R1路由器")
ax1.set_xlabel('采集时间')
ax1.set_ylabel('CPU利用率')

ax2.set_title("R2路由器")
ax2.set_xlabel('采集时间')
ax2.set_ylabel('CPU利用率')

# ##########################添加注释###################################
fig.autofmt_xdate()
plt.show()
