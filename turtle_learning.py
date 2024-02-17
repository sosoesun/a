import turtle as t
from random import randint
from time import sleep

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

background.penup()
background.goto(200,200)
background.pendown()
background.fillcolor("RED")
background.begin_fill()
for i in range(4):
    background.forward(50)
    background.left(90)

background.end_fill()


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

sleep(10)
while(1):   
    t1.penup()
    t1.goto(-250,-250)
    t1.pendown()
    t1.speed(50)
    gene_list = []
    best_gene2 = best_gene.copy()

    #돌연변이
    for i in range(2):
        moving_men = randint(1,4)
        gene_list.append(moving_men)
        if moving_men == 1:
            t1.setheading(0)
        elif moving_men == 2:
            t1.setheading(90)
        elif moving_men == 3:
            t1.setheading(180)
        elif moving_men ==4:
            t1.setheading(270)
        if t1.heading() == 90 and t1.ycor() > 245 or t1.heading() == 180 and t1.xcor() < -245 or t1.heading() == 270 and t1.ycor() < -245 or t1.heading() == 0 and t1.xcor() > 245: 
            pass
        else:
            t1.forward(50)

    #유전자 계승
    for i in range(18):
        select_gene = best_gene2.pop(randint(0,19-i))
        gene_list.append(select_gene)
        if select_gene == 1:
            t1.setheading(0)
        elif select_gene == 2:
            t1.setheading(90)
        elif select_gene == 3:
            t1.setheading(180)
        elif select_gene ==4:
            t1.setheading(270)
        if t1.heading() == 90 and t1.ycor() > 245 or t1.heading() == 180 and t1.xcor() < -245 or t1.heading() == 270 and t1.ycor() < -245 or t1.heading() == 0 and t1.xcor() > 245: 
            pass
        else:
            t1.forward(50)

    background2.clear()
    generation += 1
    background2.write("제 {}세대,목표까지의 거리:{:.1f}\n\n 보유유전자:{}".format(generation,t1.distance(250,250),gene_list),font=10)

    #최적의 유전자 저장
    if t1.distance(250,250) < best+10:
        best_gene = gene_list.copy()
        best = t1.distance(250,250)
        print(best_gene,gene_list,best_gene2,best)
    
    #최악의 유전자 돌연변이 제거
    if t1.distance(250,250) > best+200:
        if gene_list[0] in best_gene in best_gene:
            best_gene.remove(gene_list[0])
            best_gene.append(randint(1,2))
    
    t1.clear()

    if t1.distance(250,250) < 25:
        break



background2.goto(-10,100)
background2.write("도착!",font=40)
background2.goto(-200,0)
background2.write("최종 유전자:{}".format(best_gene),font=10) 
sleep(1000)          
