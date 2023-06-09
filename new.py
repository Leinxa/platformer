from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app=Ursina()
def input(key):
    if key=='space':
        from ursina.prefabs.ursfx import ursfx
        ursfx([(0.0, 1.0), (0.11, 0.5), (0.25, 0.5), (0.35, 0.5), (1.0, 0.0)], volume=0.75, wave='triangle', pitch=-1, speed=2.7)
camera.orthographic=True
camera.fov = 10

size_bg=13
bg = Entity(model="quad",scale=(size_bg,9),texture='assets/1.png',z=1)
for m in range(4):
    duplicate(bg,x=size_bg*(m+1))
    duplicate(bg,x=-size_bg*(m+1))


player= PlatformerController2d(y=1,scale_y=1.5,color=color.white,texture='assets/cat.gif',jump_height=2)
ground= Entity(model='quad',y=-4,x=-0.5,scale_x=10,collider="box",color=color.yellow)
wall= Entity(model='quad', scale=(1,5), x=5,y=-2, collider="box",color=color.azure)
ground2 = Entity(model='quad',color=color.yellow,scale=(3,1),x=36,y=2, collider="box")
round2 = Entity(model='quad',color=color.yellow,scale=(3,1),x=45,y=2, collider="box")
trap = Entity(model='quad',color=color.yellow,scale=(3,1),x=39,y=2, collider="box")
finish = Entity(model='quad',color=color.red,scale=(3,1),x=42,y=2, collider="box")
level = Entity(model='quad',color=color.red,scale=(3,1),x=2,y=-2, collider="box")
levelMove = Entity(model='quad',color=color.red,scale=(3,1),x=9,y=1, collider="box")
levelMove2 = Entity(model='quad',color=color.red,scale=(3,1),x=14,y=1, collider="box")
levelMove3 = Entity(model='quad',color=color.red,scale=(5,1),x=24,y=0, collider="box")
levelMove4 = Entity(model='quad',color=color.red,scale=(3,1),x=30,y=-1, collider="box")
dead = Entity(model="quad",scale=(200,1),x=0,y=-9, collider="box")
def update():
    global speed,speed2,speed3,speed4,dx,dx2,dx3
    dx+=speed*time.dt
    dx2+=speed2*time.dt
    dx3+=speed4*time.dt
    if abs(dx)>2:
        speed*=-1
        dx=0
    if abs(dx2)>3:
        speed2*=-1
        dx2=0
        if abs(dx3)>3:
            speed4*=-1
            dx3=0
    levelMove.x += speed * time.dt
    levelMove2.x += speed2 * time.dt
    levelMove4.y += speed2 * time.dt
    levelMove3.rotation_z += speed3 * time.dt

    if player.intersects(finish).hit:
        print('Congrats')
        video_sound.play()
    if player.intersects(dead).hit:
        print('Dead')
        player.x = 0
        player.y = 0
    if player.intersects(trap).hit:
        trap.x= -200

music = Entity(model='quad',x=-20,texture="assets/hapi.mp4")
video_sound = loader.loadSfx("assets/hapi.mp4")
music.texture.synchronizeTo(video_sound)
speed3=40
speed=1
speed2=2
speed4=1
dx=0
dx2=0
dx3=0
camera.add_script(SmoothFollow(target=player,offset=[2,0,-10],speed=1))
app.run()