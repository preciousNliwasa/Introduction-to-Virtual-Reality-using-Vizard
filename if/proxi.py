import viz
import vizinfo
import vizact
import vizproximity
import viztask
import vizinput

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.clearcolor(viz.SKYBLUE)

viz.mouse(viz.OFF)

info_ = vizinfo.InfoPanel('Press S on the keyboard to view sensors ',align = viz.ALIGN_RIGHT_BOTTOM)
info_.setTitle('About Simulation')

viz.MainView.move([-2,4,-8])
viz.lookAt([0,0,0])

world = viz.addChild('ground.osgb')
add_world = viz.addChild('sky_day.osgb')

crate = viz.addChild('crate.osgb')
crate.setScale([0.8,0.8,0.6])
crate.collidePlane()

me = viz.addAvatar('vcc_male2.cfg')
me.state(6)

girl = viz.addAvatar('vcc_female.cfg')
girl.setPosition([-4,0,9])
girl.addAction(vizact.turn(180))

girl_sensor = vizproximity.Sensor(vizproximity.Box(size = [1.8,4,1.5],center = [0,0,0]),source = girl)

target = vizproximity.Target(me)

manager = vizproximity.Manager()

manager.addSensor(girl_sensor)
manager.addTarget(target)

#Toggle debug shapes with keypress 
vizact.onkeydown('s',manager.setDebug,viz.TOGGLE)

def walk_to():

	global info
	
	info = viz.pick(1)
	
	if info.valid and info.object == world:
		
		move = vizact.walkTo([info.point[0],0,info.point[2]])
		me.runAction(move)
		if (girl_sensor in manager.getSensors()) == True:
			pass
		else:
			girl_follow()
			
		viztask.schedule(ask)
		viztask.schedule(drive)
		
	print(info.object == world)
	print(mini_sensor in manager.getSensors())
		
vizact.onmousedown(viz.MOUSEBUTTON_LEFT,walk_to)

def girl_follow():
	
	move = vizact.walkTo([info.point[0],0,info.point[2]-1])
	girl.runAction(move)

def ask():
	
	global mini_sensor,mini
	
	yield vizproximity.waitEnter(girl_sensor)
	
	my_input = vizinput.choose('A car to travel with the girl',['mini','tesla','bugati'])
	
	if my_input == 0:
		mini = viz.addChild('mini.osg')
		mini.setPosition([-2,0,-3.5])
		
		manager.removeSensor(girl_sensor)
		
		mini_sensor = vizproximity.Sensor(vizproximity.Box([2.7,3,4],center = [0,0,0]),source = mini)
		
		manager.addSensor(mini_sensor)
		
		
def drive():
	
	yield vizproximity.waitEnter(mini_sensor)
		
	my_input2 = vizinput.choose('Drive ?',['yes','no'])
	
	if my_input2 == 0:
		
		me.setScale([0,0,0])
		girl.setScale([0,0,0])
		manager.removeTarget(target)
		manager.removeSensor(mini_sensor)
		new_target = vizproximity.Target(mini)
		manager.addTarget(new_target)
		
def mini_drive():
	
	info2 = viz.pick(1)
	
	if info2.valid and info2.object == world:
		move = vizact.moveTo([info2.point[0],0,info2.point[2]],speed = 1)
		mini.runAction(move)
		au = viz.addAudio('meek.mp3')
		au.play()
		au.loop(viz.ON)
		#mini.playsound('meek.mp3')
		
		# sound = mini.playsound('prenli.wav',viz.STOP)
		# vizact.onkeydown('k',sound.play,viz.LOOP)
		
vizact.onmousedown(viz.MOUSEBUTTON_RIGHT,mini_drive)
	
#vizact.onkeydown('l', viz.MainView.setPosition,[0,0,0.1],viz.REL_LOCAL)

vizact.onkeydown('f', viz.MainView.setPosition,[0,0,0.1],viz.REL_GLOBAL)

vizact.onkeydown('b', viz.MainView.setPosition,[0,0,-0.1],viz.REL_GLOBAL)

vizact.onkeydown('r', viz.MainView.setPosition,[0.1,0,0],viz.REL_GLOBAL)

vizact.onkeydown('l', viz.MainView.setPosition,[-0.1,0,0],viz.REL_GLOBAL)

#viz.collision(viz.ON)
