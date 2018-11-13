import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import mpl_toolkits.mplot3d.art3d
from matplotlib import colors as mcolors

def test1():
    x, y = np.mgrid[-2:2:20j, -2:2:20j]
    z = x * np.exp(-x ** 2 - y ** 2)
    print(x)
    print(y)
    print(z)
    ax = plt.subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap=plt.cm.coolwarm, alpha=0.1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()

def test2():
    fig = plt.figure()
    ax = mpl_toolkits.mplot3d.Axes3D(fig)
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    print(type(X))
    print(type(Y))
    X, Y = np.meshgrid(X, Y)
    print(X)
    print(Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    print(Z)
    # 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    plt.show()

def cc(arg):
    #print(mcolors.to_rgba(arg, alpha=0.1))
    return mcolors.to_rgba(arg, alpha=0.1)

def draw_polygon():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # 正文体顶点和面
    verts = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 0, 1)]
    faces = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [1, 2, 6, 5], [2, 3, 7, 6], [0, 3, 7, 4]]
    # 四面体顶点和面
    #verts = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 0, 1)]
    #faces = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
    # 获得每个面的顶点
    poly3d = [[verts[vert_id] for vert_id in face] for face in faces]
    print(poly3d)
    # print(poly3d)
    # 绘制顶点
    x, y, z = zip(*verts)
    ax.scatter(x, y, z)
    # 绘制多边形面
    ax.add_collection3d(mpl_toolkits.mplot3d.art3d.Poly3DCollection(poly3d, color='m',facecolors=cc('g'),linewidths=0.5, linestyles=':'))
    #ax.add_collection3d(mpl_toolkits.mplot3d.art3d.Poly3DCollection(poly3d,facecolors=[1,0,0],color='k',linewidths=0.5, linestyles=':',alpha=0.1))
    #ax.add_collection3d(mpl_toolkits.mplot3d.art3d.Line3DCollection(poly3d, colors='y',linewidths=0.1, linestyles=':'))
    ax.set_xlabel('X')
    ax.set_xlim3d(-0.5, 1.5)
    ax.set_ylabel('Y')
    ax.set_ylim3d(-0.5, 1.5)
    ax.set_zlabel('Z')
    ax.set_zlim3d(-0.5, 1.5)
    plt.show()

if __name__ == '__main__':
    draw_polygon()
