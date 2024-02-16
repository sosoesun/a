import turtle as t
from random import randint

#배경설정
background = t.Turtle()
background2 = t.Turtle()
background.ht() 
background.speed(1000)
background.penup()
background.goto(-250,-250)
background.pendown()
for i in range(4):
    background.forward(500)
    background.left(90)
background2.ht()
background2.penup()    
background2.goto(-250,-280)
generation = 1
background2.write(f"제 {generation}세대",font=10)



t1 =t.Turtle()
t1.shape("turtle")
t1.color("GREEN")




best = 100000
best_gene=[randint(1,4) for i in range(20)]

while(1):   
    t1.penup()
    t1.goto(-250,-250)
    t1.pendown()
    t1.speed(5)
    gene_list = []

    #돌연변이
    for i in range(2):
        moving_men = randint(1,4)
        gene_list.append(moving_men)
        if moving_men == 1:
            t1.right(90)
        elif moving_men == 2:
            t1.left(90)
        elif moving_men == 3:
            t1.right(180)
        elif moving_men ==4:
            pass
        if t1.heading() == 90 and t1.ycor() > 245 or t1.heading() == 180 and t1.xcor() < -245 or t1.heading() == 270 and t1.ycor() < -245 or t1.heading() == 0 and t1.xcor() > 245: 
            pass
        else:
            t1.forward(50)

    #유전자 계승
    for i in range(18):
        select_gene = randint(0,19)
        gene_list.append(best_gene[select_gene])
        if select_gene == 1:
            t1.right(90)
        elif select_gene == 2:
            t1.left(90)
        elif select_gene == 3:
            t1.right(180)
        elif select_gene ==4:
            pass
        if t1.heading() == 90 and t1.ycor() > 245 or t1.heading() == 180 and t1.xcor() < -245 or t1.heading() == 270 and t1.ycor() < -245 or t1.heading() == 0 and t1.xcor() > 245: 
            pass
        else:
            t1.forward(50)

    background2.clear()
    generation += 1
    background2.write(f"제 {generation}세대,{t1.distance(250,250)},{best_gene}",font=10)

    if t1.distance(250,250) < best:
        best_gene = gene_list.copy()
        
    t1.clear()       
