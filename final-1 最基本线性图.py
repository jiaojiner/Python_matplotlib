#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import matplotlib.pyplot as plt
import random

X = [i for i in range(9)]
# Y = [i for i in range(9)]
Y = [random.randint(0, 9) for i in range(9)]

plt.plot(X,Y)
plt.savefig('result1.png')
plt.show()
