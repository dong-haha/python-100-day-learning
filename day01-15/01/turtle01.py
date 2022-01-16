import turtle
# 坐标原点为画布中心的坐标轴, 坐标原点上有一只面朝x轴正方向小乌龟

# 设置画布的宽(单位像素), 高, 背景颜色
turtle.screensize(800, 600, "green")


# 画笔控制命令
turtle.pensize(4)
turtle.pencolor('red')
turtle.speed(2)
 # 绘制图形的填充颜色
turtle.fillcolor('red')
# 隐藏箭头显示
turtle.hideturtle()


# 画笔运动命令
## 移动
turtle.forward(100)
turtle.backward(50)
turtle.goto(400, 400)
## 角度
turtle.right(60)
turtle.left(60)

turtle.penup()
turtle.pendown()

turtle.mainloop()