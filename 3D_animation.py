# coding: utf-8
"""
============
3D animation
============

A simple example of an animated plot... In 3D!
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


def Gen_RandLine(length, dims=2):#有length个(x,y)的点
    lineData = np.empty((dims, length))#np.empty([dims, length])
    lineData[:, 0] = np.random.rand(dims)   # 初始化起点
    for index in range(1, length):
        step = ((np.random.rand(dims) - 0.5) * 0.1)  # 步长
        # 下一步的位置
        lineData[:, index] = lineData[:, index - 1] + step

    return lineData   # 返回一个shape为（3,25）的数组,3维坐标25帧,也可以生成(dims,length)的数组


def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines


# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Fifty lines of random 3-D lines  (长为50的数组，每个元素为shape为3,25的ndarray，最后实际效果就是50条路径)
#这是个生成器，专门产生数据的
data = [Gen_RandLine(25, 3) for index in range(50)]#50个shape为3,25的数组,50条线
print("data",data)

# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
# init
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data] # 每条路径的起始点。每个dat是(3*25)的
print("lines",lines)#5个

# Setting the axes properties
ax.set_xlim3d([0.0, 1.0])
ax.set_xlabel('X')

ax.set_ylim3d([0.0, 1.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 1.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=(data, lines),
                                   interval=50, blit=True)

plt.show()