import viz
import vizact
import vizinfo
import viztask
import vizproximity
import sqlite3
import vizmat
import random
import vizfx
import vizinput

viz.setMultiSample(4)
viz.fov(60)

viz.phys.enable()

viz.go()

info_menu = vizinfo.InfoPanel('Press C to initiate the couple walk \n Press S to visualise car sensor \n Press Q to drive car after initiating the car sensor')
info_menu.addSeparator()
info_menu.setTitle('Information')

lodge = viz.addChild('it.osgb')
lodge.setScale([0.5,0.5,0.5])

pad1 = lodge.getChild('Pad Pad 1 [227786]')
surface = lodge.getChild('Surface  [179767]')
wall = lodge.getChild('Basic Wall Generic - 200mm [225595]')
wall2 = lodge.getChild('Basic Wall Generic - 200mm [321386]')

sky = viz.addEnvironmentMap('sky.jpg')

vine2 = viz.addTexture('Soil.jpg')
vine2.wrap(viz.WRAP_T,viz.REPEAT)
vine2.wrap(viz.WRAP_S,viz.REPEAT)

matrix3 = vizmat.Transform()
matrix3.setScale(wall.getScale())

wall.texmat(matrix3)
wall.texture(vine2)

#wall.texture(sky)
#wall.appearance(viz.ENVIRONMENT_MAP)

wall2.texture(sky)
wall2.appearance(viz.ENVIRONMENT_MAP)

matrix = vizmat.Transform()
matrix.setScale(pad1.getScale())

matrix2 = vizmat.Transform()
matrix2.setScale(surface.getScale())

home_op_tex = viz.addTexture('brick.jpg')
home_op_tex.wrap(viz.WRAP_T,viz.REPEAT)
home_op_tex.wrap(viz.WRAP_S,viz.REPEAT)

pad1.texmat(matrix)
pad1.texture(home_op_tex)

surface.texmat(matrix2)
surface.texture(home_op_tex)


world = viz.addChild('sky_day.osgb')
world.collidePlane()
#world.setScale([40,40,40])
	
	
hotel = viz.addChild('hotel.osgb')
hotel.setScale([0.045,0.045,0.045])
hotel.setPosition([0,0,20])

plane_hotel = hotel.getChild('Plane001')
plane_hotel.visible(viz.OFF)

road_hotel = hotel.getChild('Road')
road_hotel.visible(viz.OFF)

street_building = viz.addChild('street_building.osgb')
street_building.collidePlane()
street_building.setScale([0.015,0.015,0.015])
street_building.setPosition([-50,-4,47])

vizact.onkeydown('f', viz.MainView.setPosition,[0,0,0.1],viz.REL_GLOBAL)

vizact.onkeydown('b', viz.MainView.setPosition,[0,0,-0.1],viz.REL_GLOBAL)

vizact.onkeydown('r', viz.MainView.setPosition,[0.1,0,0],viz.REL_GLOBAL)

vizact.onkeydown('l', viz.MainView.setPosition,[-0.1,0,0],viz.REL_GLOBAL)

vizact.onkeydown('u', viz.MainView.setPosition,[0,0.1,0],viz.REL_GLOBAL)

vizact.onkeydown('d', viz.MainView.setPosition,[0,-0.1,0],viz.REL_GLOBAL)
#viz.collision(viz.ON)

sophia = viz.addAvatar('sophia.osgb')
sophia.setPosition([15,0,7])
sophia.setScale(0.015,0.015,0.015)
sophia.state(1)

frank = viz.addAvatar('Frank.osgb')
frank.setPosition([13,-1.95,1])
frank.setScale(0.20,0.20,0.20)
#frank.state(1)


#bank = viz.addChild('bank.osgb')
#bank.setScale([0.02,0.02,0.02])
#bank.setPosition([70,0,40])

zuko = viz.addChild('zuko.osgb')
zuko.setPosition([60,0,0])
zuko.setScale([4,4,4])

lodge2 = viz.addChild('lodge2.osgb')
lodge2.setPosition([91,0,4])
lodge2.setScale([0.0008,0.0008,0.0008])

plane_lodge = lodge2.getChild('Plane001')
plane_lodge.visible(viz.OFF)

texture_part = lodge2.getChild('Paint - Cadmium Yellow')

textu2 = viz.addTexture('Stone.jpg')
textu2.wrap(viz.WRAP_T,viz.REPEAT)
textu2.wrap(viz.WRAP_S,viz.REPEAT)

matrix4 = vizmat.Transform()
matrix4.setScale(texture_part.getScale())

texture_part.texmat(matrix4)
texture_part.texture(textu2)

piazzaSound = viz.addAudio('piazza.mp3')
piazzaSound.play()
piazzaSound.loop()

mini = viz.addChild('mini.osg')
mini.setPosition([40,0,3])

mini2 = viz.addChild('mini.osgb')
mini2.setPosition([46,17,39])

guy = viz.addAvatar('vcc_male2.osgb')
guy.setScale([1,1,1])
guy.setPosition([7.5,-0.2,0])
guy.collidePlane()
#guy.state(5)
guy.addAction(vizact.turn(90))

def guy_dance():
	guy.addAction(vizact.animation(5))

vizact.ontimer(0,guy_dance)

girl = viz.addAvatar('vcc_female.cfg')
girl.setScale([1,1,1])
girl.setPosition([7.5,-0.2,1])
girl.collidePlane()
girl.addAction(vizact.turn(180))
girl.speed(2)

def girl_cheer():
	girl.addAction(vizact.animation(3))

vizact.ontimer(0,girl_cheer)

pigeons = []
for p in range(30):
	
	x = random.randint(25,44)
	z = random.randint(2,10)
	
	pigeon = viz.addChild('pigeon.cfg',cache = viz.CACHE_CLONE)
	pigeon.setScale(1,1,1)
	pigeon.setPosition([x,0,z])
	pigeon.state(1)
	
	pigeons.append(pigeon)
	
def pigeonsFeed():

    random_speed = vizact.method.setAnimationSpeed(0,vizact.randfloat(0.7,1.5))
    random_walk = vizact.walkTo(pos=[vizact.randfloat(25,44),0,vizact.randfloat(2,15)],walkSpeed = 0.1)
    random_animation = vizact.method.state(vizact.choice([1,3],vizact.RANDOM))
    random_wait = vizact.waittime(vizact.randfloat(5.0,10.0))
    pigeon_idle = vizact.sequence(random_speed,random_walk,random_animation, random_wait, viz.FOREVER)

    for pigeon in pigeons:
        pigeon.addAction(pigeon_idle)

vizact.ontimer(0,pigeonsFeed)

another_guy = viz.addAvatar('vcc_male.cfg')
another_guy.setPosition([50,0,3])
another_guy.state(1)

another_lady = viz.addAvatar('vcc_female.cfg')
another_lady.setPosition([50,0,5])
another_lady.addAction(vizact.turn(180))

def walk_to():
	
	global info
	
	info = viz.pick(1)
	
	if info.valid and info.object == lodge:
		
		move = vizact.walkTo([info.point[0],0,info.point[2]])
		another_guy.runAction(move)
		girl_follow()
	print(info.point)

def couple_walk():
	
	vizact.onmousedown(viz.MOUSEBUTTON_LEFT,walk_to)
	
vizact.onkeydown('c',couple_walk)

def girl_follow():	
	
	move = vizact.walkTo([info.point[0],0,info.point[2]-1])
	another_lady.runAction(move)
	
def drive_mode():
	
	MOVE_SPEED = 5 
	TURN_SPEED = 60	

	view = viz.MainView 
	#view.collision(viz.ON)

	def updatecar():
		if viz.key.isDown(viz.KEY_UP):
			view.move([0,0,MOVE_SPEED*viz.elapsed()],viz.BODY_ORI)
		elif viz.key.isDown(viz.KEY_DOWN):
			view.move([0,0,-MOVE_SPEED*viz.elapsed()],viz.BODY_ORI)
		elif viz.key.isDown(viz.KEY_RIGHT):
			view.setEuler([TURN_SPEED*viz.elapsed(),0,0],viz.BODY_ORI,viz.REL_PARENT)
		elif viz.key.isDown(viz.KEY_LEFT):
			view.setEuler([-TURN_SPEED*viz.elapsed(),0,0],viz.BODY_ORI,viz.REL_PARENT)
		
		mini.setPosition(view.getPosition())
		mini.setEuler(view.getEuler(viz.BODY_ORI))
		mini.setPosition([0.35,-1.2,0.2],viz.REL_LOCAL)

	def drivemini():
		piazzaSound.stop()
		aka = viz.addAudio('aka.mp3')
		aka.play()
		aka.loop()
		vizact.ontimer(0,updatecar)
	
	vizact.onkeydown('q',drivemini)

	def mousemove(e):
		euler = view.getEuler(viz.HEAD_ORI)
		euler[0] += e.dx*0.1
		euler[1] += -e.dy*0.1
		euler[1] = viz.clamp(euler[1],-85.0,85.0)
		view.setEuler(euler,viz.HEAD_ORI)

	viz.callback(viz.MOUSE_MOVE_EVENT,mousemove)

	viz.mouse(viz.OFF)
	viz.mouse.setVisible(False)

	vizact.onmousedown(viz.MOUSEBUTTON_LEFT,view.reset,viz.HEAD_ORI)
	vizact.onmousedown(viz.MOUSEBUTTON_RIGHT,view.reset, viz.BODY_ORI |viz.HEAD_POS)
	vizact.onmousedown(viz.MOUSEBUTTON_RIGHT,updatecar)
	
mini_sensor = vizproximity.Sensor(vizproximity.Box([4,4,4]),source = mini)
target = vizproximity.Target(another_guy)

manager = vizproximity.Manager()

manager.addSensor(mini_sensor)
manager.addTarget(target)

vizact.onkeydown('s',manager.setDebug,viz.TOGGLE)

def proximity_event():
	
	yield vizproximity.waitEnter(mini_sensor)
	
	user_input = vizinput.choose('drive around ? ',['Yes','No'])
	
	if user_input == 0:
		drive_mode()
		another_guy.visible(viz.OFF)
		another_lady.visible(viz.OFF)
		
	else:
		pass

viztask.schedule(proximity_event)

WALL_SCALE = [15,12,5]

wall5 = viz.addTexQuad()
wall5.setPosition( [63,0,15] )
wall5.zoffset(1) #avoid zfighing, make wall appear behind pictures
wall5.setScale(WALL_SCALE)

# Apply nice repeating brick texture
matrix5 = vizmat.Transform()
matrix5.setScale(WALL_SCALE)
wall5.texmat(matrix5)

bricks = viz.addTexture('wood.jpg')
bricks.wrap(viz.WRAP_T, viz.REPEAT)
bricks.wrap(viz.WRAP_S, viz.REPEAT)

wall5.texture(bricks)

piccW = viz.addTexQuad()
piccW.setPosition( [59,4.5,15] )
piccW.setScale([3,2,3])

picc = viz.addTexture('picc.png')

piccW.texture(picc)


piccW2 = viz.addTexQuad()
piccW2.setPosition( [63,4.5,15] )
piccW2.setScale([3,2,3])

picc2 = viz.addTexture('picc2.png')

piccW2.texture(picc2)

piccW3 = viz.addTexQuad()
piccW3.setPosition( [67,4.5,15] )
piccW3.setScale([3,2,3])

picc3 = viz.addTexture('picc4.png')

piccW3.texture(picc3)


piccW4 = viz.addTexQuad()
piccW4.setPosition( [59,2,15] )
piccW4.setScale([3,2,3])

picc4 = viz.addTexture('picc5.png')

piccW4.texture(picc4)

piccW5 = viz.addTexQuad()
piccW5.setPosition( [63,2,15] )
piccW5.setScale([3,2,3])

picc5 = viz.addTexture('picc6.png')

piccW5.texture(picc5)

piccW6 = viz.addTexQuad()
piccW6.setPosition( [67,2,15] )
piccW6.setScale([3,2,3])

picc6 = viz.addTexture('picc8.png')

piccW6.texture(picc6)

#video = viz.add('VideoCamera.dle') 

#cam = video.addWebcam() 

#quad = viz.addTexQuad(pos=(63,3,25),texture=cam) 
#quad.setScale([6,4,6])

WALL_SCALEL = [15,12,5]

wallL = viz.addTexQuad()
wallL.setPosition( [63,0,25] )
wallL.zoffset(1) #avoid zfighing, make wall appear behind pictures
wallL.setScale(WALL_SCALEL)

# Apply nice repeating brick texture
matrixL = vizmat.Transform()
matrixL.setScale(WALL_SCALEL)
wallL.texmat(matrixL)

bark = viz.addTexture('bark.jpg')
bark.wrap(viz.WRAP_T, viz.REPEAT)
bark.wrap(viz.WRAP_S, viz.REPEAT)

wallL.texture(bark)