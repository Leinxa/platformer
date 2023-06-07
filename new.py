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
for m in range(3):
    duplicate(bg,x=size_bg*(m+1))
    duplicate(bg,x=-size_bg*(m+1))


player= PlatformerController2d(y=1,scale_y=1.5,color=color.white,texture='assets/cat.gif',jump_height=2)
ground= Entity(model='quad',y=-4,x=-0.5,scale_x=10,collider="box",color=color.yellow)
ground2= Entity(model='quad',y=-4,x=27,scale_x=10,collider="box",color=color.yellow)
wall= Entity(model='quad', scale=(1,5), x=5,y=-2, collider="box",color=color.azure)
finish = Entity(model='quad',color=color.red,scale=(1,3),x=30,y=-1.5, collider="box")
level = Entity(model='quad',color=color.red,scale=(3,1),x=2,y=-2, collider="box")
levelMove = Entity(model='quad',color=color.red,scale=(3,1),x=9,y=1, collider="box")
levelMove2 = Entity(model='quad',color=color.red,scale=(3,1),x=14,y=1, collider="box")
dead = Entity(model="quad",scale=(60,1),x=0,y=-9, collider="box")
def update():
    global speed,speed2,dx,dx2
    dx+=speed*time.dt
    dx2+=speed2*time.dt
    if abs(dx)>2:
        speed*=-1
        dx=0
    if abs(dx2)>3:
        speed2*=-1
        dx2=0
    levelMove.x += speed * time.dt
    levelMove2.x += speed2 * time.dt

    if player.intersects(finish).hit:
        print('Congrats')
        video_sound.play()
    if player.intersects(dead).hit:
        print('Dead')
        player.x = 0
        player.y = 0

music = Entity(model='quad',x=-20,texture="assets/hapi.mp4")
video_sound = loader.loadSfx("assets/hapi.mp4")
music.texture.synchronizeTo(video_sound)

speed=1
speed2=2
dx=0
dx2=0
camera.add_script(SmoothFollow(target=player,offset=[2,0,-10],speed=1))
app.run()
