import turtle
import random
import time



screen = turtle.Screen()
screen.setup(height=500, width=600)
#Form cho người dùng nhập vào dự đoán
guess = screen.textinput(prompt="Dự đoán con rùa nào chiến thắng?", title="Nhập vào màu rùa (đỏ, nâu, xanh dương, xanh lá cây, cam, hồng)")

#List colors chứa màu của từng con rùa
colors = ["red", "brown", "blue", "green", "orange", "pink"]
turtle_speeds =[10,15,20,25,30,5]

#Tọa độ x của các con ,rùa
x = -250
#Tọa độ y của con rùa
ys = [-80,-40,0,40,80,120]

#Biến lưu trữ bút vẽ cho từng con rùa
all_turtles = []

#Nếu có con rùa nào có tọa độ x > 250 thì run = False
run = True


but_ve_dich = turtle.Turtle()
but_ve_dich.penup()
but_ve_dich.goto(250, -150)
but_ve_dich.left(90)
but_ve_dich.pendown()
but_ve_dich.forward(300)
but_ve_dich.hideturtle()


        
#Khởi tạo các bút vẽ cho từng con rùa
for i in range(6):
    but_ve = turtle.Turtle()
    but_ve.shape("turtle")
    but_ve.color(colors[i])
    but_ve.penup()
    but_ve.goto(-250, ys[i])
    all_turtles.append(but_ve)
    
    
#Mỗi bước chạy mỗi con rùa sẽ chọn một tốc độ ngẫu nhiên trong list_speed
id_con_rua_thang_cuoc = []
buoc_di_cua_rua = [0,0,0,0,0,0]
start = time.time()

def random_walk(all_turtles):
    global run
    global id_con_rua_thang_cuoc
    i = 0
    for but_ve in all_turtles:
        buoc_di = random.choice(turtle_speeds)
        buoc_di_cua_rua[i] += buoc_di
        but_ve.forward(buoc_di)
      
        #Nếu con rùa có tọa độ x >= 250 thì run = False
        #turtle.xcor() trả về tọa độ bút vẽ tại thời điểm được gọi
        if but_ve.xcor() >= 250:
            id_con_rua_thang_cuoc.append(i)
            
            stop = time.time()      
            print("Thời gian rùa chạy là: ",stop - start)
            run = False
        i += 1
         
#Lặp lại các bước chạy cho đến khi run = False
 
while run == True:
    random_walk(all_turtles)
    
print("Màu con rùa thắng cuộc là: ", colors[id_con_rua_thang_cuoc])



#Chương trình kết thúc khi click chuột vào màn hình
screen.exitonclick()


turtle.done()