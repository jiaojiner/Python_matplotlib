#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import matplotlib.pyplot as plt
import final_0_data
import matplotlib.dates as mdate
import matplotlib.ticker as mtick


fig = plt.figure()
ax = fig.add_subplot(111)

ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))  # 设置时间标签显示格式

ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))  # 格式化Y轴

X = []
Y = []

for (time, cpu) in final_0_data.R1_CPU_TIME:
    X.append(time)
    Y.append(cpu)

fig.autofmt_xdate()

# ##########################添加注释###################################
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
plt.title('路由器CPU利用率')  # 主题
plt.xlabel('采集时间')  # X轴注释
plt.ylabel('CPU利用率')  # Y轴注释
# ##########################添加注释###################################

# ##########################添加注释###################################
# font_path = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf')
# plt.title('路由器CPU利用率',fontproperties=font_path)#主题
# plt.xlabel('采集时间',fontproperties=font_path)#X轴注释
# plt.ylabel('CPU利用率',fontproperties=font_path)#Y轴注释
# ##########################添加注释###################################

R1 = ax.plot(X, Y, '-', color='r', label='R1')
# 线的格式与颜色

ax.legend(loc='lower right')
# 下面的方法可以在把多个标记在不同位置展示
# r1_legend = ax.legend(handles=[R1], loc='upper right')
# ax.add_artist(r1_legend)
plt.show()
