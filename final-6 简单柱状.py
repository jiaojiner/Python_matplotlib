#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import matplotlib.pyplot as plt

application = ['http', 'ftp', 'rdp', 'qq']
data = [30, 53, 12, 45]

# plt.bar(application, data, width = 0.5)

color_list = ['r', 'k', '0.5', '#FF00FF']

# 灰度
# HTML颜色

plt.barh(application, data, height=0.5, color=color_list)

# ##########################添加注释###################################
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
plt.title('协议与带宽分布')  # 主题
plt.xlabel('带宽（M/s）')  # X轴注释
plt.ylabel('协议')  # Y轴注释
# ##########################添加注释###################################

plt.show()
