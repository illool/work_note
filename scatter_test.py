# coding: utf-8

"""
scatter example
author: illool@163.com
"""

#导入必要的模块
import numpy as np
import matplotlib.pyplot as plt
#产生测试数据
x = np.arange(1,10)
y = x
fig = plt.figure()
ax1 = fig.add_subplot(111)
#设置标题
ax1.set_title('Scatter Plot')
#设置X轴标签
plt.xlabel('X')
#设置Y轴标签
plt.ylabel('Y')
#画散点图
lValue = x
cValue = ['r','y','g','b','r','y','g','b','r']
mValue = [u'.',u',',u'o',u'v',u'^',u'<',u'>',u'1',u'p']
for _mValue, _cValue,_lValue, _x, _y in zip(mValue, cValue,lValue, x, y):
    ax1.scatter(_x,_y,c=_cValue,s=_lValue,linewidths=_lValue,marker=_mValue)
#设置图标
plt.legend('x1')
plt.show()
