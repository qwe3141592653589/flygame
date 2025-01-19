import pgzrun
import time
import sys

WIDTH = 1000
HEIGHT = 500

screen_spend = 2
cat_down_spend = 5
cat_up_spend = 5
z_spend = 10
time_jiange = 1   

cat = Actor('cat')
bg1 = Actor('bg1')
bg2 = Actor('bg1')
z1 = Actor('z1')
z2 = Actor('z2')
z3 = Actor('z3')
zs = [z1,z2,z3]
for i in zs:
    i.y = 100
z2.y = HEIGHT - 100
z1.x = 1100
z2.x = 1600
z3.x = 2100
bg1.x = 500
bg1.y = 250
bg2.x = 1500
bg2.y = 250
cat.x = 100
cat.y = 150
time1 = time.time()

def draw():
    bg1.draw()
    bg2.draw()
    cat.draw()
    for i in zs:
        i.draw()

def update():
    global screen_spend
    global cat_down_spend
    global z_spend
    global time1,time_jiange
    bg1.x -= screen_spend
    bg2.x -= screen_spend
    for i in zs:
        i.x -= z_spend
        if i.x <= -500:
            i.x = 1100
        if i.colliderect(cat):
            print('死')
            sys.exit()
    if bg1.x < -500:
        bg1.x = 1500
    if bg2.x < -500:
        bg2.x = 1500
    if keyboard.space:
        if not cat.y <= 25:
            cat.y -= cat_up_spend
    else:
        if not cat.y >= 450:
            cat.y += cat_down_spend
        if cat.y >= 450:
            print('死')
            sys.exit()
    time2 = time.time()
    if time2 - time1 >= time_jiange:
        screen_spend += 2
        z_spend += 2
        time1 = time.time()
pgzrun.go()