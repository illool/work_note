import numpy as np
import cv2
def cv_test():
    img=np.zeros((1024,1024,3),np.uint8)
    pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    pts = pts.reshape((-1,1,2))
    print(pts)
    img = cv2.polylines(img,[pts],True,(0,255,255))
    cv2.imshow("image",img)
    cv2.waitKey(0)

def cv_draw_test():
    np.set_printoptions(threshold='nan')
    # 创建一个宽512高512的黑色画布，RGB(0,0,0)即黑色
    img = np.zeros((512, 512, 3), np.uint8)

    # 画直线,图片对象，起始坐标(x轴,y轴)，结束坐标，颜色，宽度
    cv2.line(img, (0, 0), (311, 511), (255, 0, 0), 10)
    # 画矩形，图片对象，左上角坐标，右下角坐标，颜色，宽度
    cv2.rectangle(img, (30, 166), (130, 266), (0, 255, 0), 3)
    # 画圆形，图片对象，中心点坐标，半径大小，颜色，宽度
    cv2.circle(img, (222, 222), 50, (255.111, 111), -1)
    # 画椭圆形，图片对象，中心点坐标，长短轴，顺时针旋转度数，开始角度(右长轴表0度，上短轴表270度)，颜色，宽度
    cv2.ellipse(img, (333, 333), (50, 20), 0, 0, 150, (255, 222, 222), -1)

    # 画多边形，指定各个点坐标,array必须是int32类型
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    # -1表示该纬度靠后面的纬度自动计算出来，实际上是4

    pts = pts.reshape((-1, 1, 2,))
    # print(pts)
    # 画多条线，False表不闭合，True表示闭合，闭合即多边形
    cv2.polylines(img, [pts], True, (255, 255, 0), 5)

    # 写字,字体选择
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

    # 图片对象，要写的内容，左边距，字的底部到画布上端的距离，字体，大小，颜色，粗细
    cv2.putText(img, "OpenCV", (10, 400), font, 3.5, (255, 255, 255), 2)

    #a = cv2.imwrite("picture.jpg", img)
    cv2.imshow("picture", img)
    cv2.setMouseCallback('picture', OnMouseAction)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

def mouse_event():
    def draw_circle(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            cv2.circle(img, (x, y), 100, (255, 0, 0), -1)

    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', OnMouseAction)
    #cv2.setMouseCallback('image', draw_circle)

    while (1):
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

def OnMouseAction(event,x,y,flags,param):
    if event == cv2.EVENT_FLAG_ALTKEY:
        print("按Alt不放事件")
    elif event==cv2.EVENT_FLAG_CTRLKEY :
        print("按Ctrl不放事件")
    elif flags==cv2.EVENT_FLAG_LBUTTON:
        print("左键拖曳")
    elif event==cv2.EVENT_FLAG_MBUTTON :
        print("中键拖曳")
    elif event == cv2.EVENT_FLAG_RBUTTON:
        print("右键拖曳")
    elif event == cv2.EVENT_FLAG_SHIFTKEY:
        print("按Shift不放事件")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("左键双击")
    elif event == cv2.EVENT_LBUTTONDOWN:
        print("左键按下")
    elif event == cv2.EVENT_LBUTTONUP:
        print("左键弹起")
    elif event == cv2.EVENT_MBUTTONDBLCLK:
        print("中间键双击")
    elif event == cv2.EVENT_MBUTTONDOWN:
        print("中间键按下")
    elif event == cv2.EVENT_MBUTTONUP:
        print("中间键弹起")
    elif event == cv2.EVENT_MOUSEHWHEEL:
        print("横向滚轮滚动")
    elif event == cv2.EVENT_MOUSEMOVE:
        print("鼠标移动")
    elif event == cv2.EVENT_MOUSEWHEEL:
        print("滚轮滚动")
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print("右键双击")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("右键按下")
    elif event == cv2.EVENT_RBUTTONUP:
        print("右键弹起")


if __name__ == '__main__':
    #mouse_event()
    cv_draw_test()
