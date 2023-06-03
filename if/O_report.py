import viz
import vizact
import vizinfo
import viztask
import vizproximity
import sqlite3
import vizmat
import random
import vizfx

viz.setMultiSample(4)
viz.fov(60)

viz.go()

def homeview():
	
	global home_background,bach,pigeons,ad_bg,home_title,op1,op2,op3,dir_button,dpt_button,rpt_button
	
	viz.mouse(viz.OFF)

	viz.MainView.setPosition([0,8,0])
	viz.lookAt([0,0,0])

	home_background = viz.addChild('ground.osgb')

	bach = viz.addAudio('bach_air.mid')
	bach.play()
	bach.loop()

	pigeons = []
	for p in range(50):
	
		x = random.randint(-10,10)
		z = random.randint(-11,13)
	
		pigeon = viz.addChild('pigeon.cfg',cache = viz.CACHE_CLONE)
		pigeon.setPosition([x,0,z])
		pigeon.setScale(1.5,1,1.5)
		pigeon.state(1)
	
		pigeons.append(pigeon)
	
	def pigeonsFeed():

		random_speed = vizact.method.setAnimationSpeed(0,vizact.randfloat(0.7,1.5))
		random_walk = vizact.walkTo(pos=[vizact.randfloat(-11,9),0,vizact.randfloat(-11,13)],walkSpeed = 0.5)
		random_animation = vizact.method.state(vizact.choice([1,3],vizact.RANDOM))
		random_wait = vizact.waittime(vizact.randfloat(5.0,10.0))
		pigeon_idle = vizact.sequence(random_speed,random_walk,random_animation, random_wait, viz.FOREVER)

		for pigeon in pigeons:
			pigeon.addAction(pigeon_idle)

	vizact.ontimer(0,pigeonsFeed)

	ad_bg = viz.add('pit.osgb')
	ad_bg.setPosition([2,0,2])

	home_title = viz.addText('Topic: Pigeons',viz.SCREEN)
	home_title.alignment(viz.ALIGN_LEFT_TOP)
	home_title.setPosition([0.26,0.9,9])
	home_title.font('times new roman')
	home_title.color(viz.ORANGE_RED)

	#home_op1_bg = viz.addTexQuad()
	#home_op1_bg.setScale([5,9,5])
	#home_op1_bg.setPosition([1,0,0])
	#home_op1_bg.lookAt([0,0,0])

	#matrix = vizmat.Transform()
	#matrix.setScale(home_op1_bg.getScale())

	#home_op_tex = viz.addTexture('brick.jpg')
	#home_op_tex.wrap(viz.WRAP_T,viz.REPEAT)
	#home_op_tex.wrap(viz.WRAP_S,viz.REPEAT)

	#home_op1_bg.texmat(matrix)
	#home_op1_bg.texture(home_op_tex)

	op1 = viz.addText('Origin',viz.SCREEN)
	op1.alignment(viz.ALIGN_LEFT_TOP)
	op1.setPosition([0.32,0.7,9])
	op1.font('forte')
	op1.color(viz.YELLOW_ORANGE)
	op1.fontSize(60)

	op2 = viz.addText('Benefits',viz.SCREEN)
	op2.alignment(viz.ALIGN_LEFT_TOP)
	op2.setPosition([0.32,0.5,9])
	op2.font('forte')
	op2.color(viz.YELLOW_ORANGE)
	op2.fontSize(60)

	op3 = viz.addText('Challenges and Solutions',viz.SCREEN)
	op3.alignment(viz.ALIGN_LEFT_TOP)
	op3.setPosition([0.32,0.3,9])
	op3.font('forte')
	op3.color(viz.YELLOW_ORANGE)
	op3.fontSize(60)


	dir_button = viz.addButton()
	dir_button.setPosition(.26,.68)
	dir_button.setScale([2,2,2])

	dpt_button = viz.addButton()
	dpt_button.setPosition(.26,.48)
	dpt_button.setScale([2,2,2])

	rpt_button = viz.addButton()
	rpt_button.setPosition(.26,.28)
	rpt_button.setScale([2,2,2])

	def buttonevent(obj,state):
	
		if obj == dir_button:
			origin()
		elif obj == dpt_button:
			print('you clicked dpt')
		elif obj == rpt_button:
			print('you clicked rpt')

	viz.callback(viz.BUTTON_EVENT,buttonevent)

vizact.onkeydown('m',homeview)

def origin():
	global info
	
	viz.mouse(viz.ON)
	viz.MainView.setPosition([0,2,5])
	viz.lookAt([0,2,0])
	
	home_background.visible(viz.OFF)
	bach.stop()
	for i in pigeons:
		i.visible(viz.OFF)
	ad_bg.visible(viz.OFF)
	
	home_title.visible(viz.OFF)
	op1.visible(viz.OFF)
	op2.visible(viz.OFF)
	op3.visible(viz.OFF)
	
	dir_button.visible(viz.OFF)
	dpt_button.visible(viz.OFF)
	rpt_button.visible(viz.OFF)
	
	info = vizinfo.InfoPanel('Press M to go to Menu',align = viz.ALIGN_RIGHT_BOTTOM)
	info.setTitle('Info')
	
	dpt_setting = viz.addChild('sky_day.osgb')
	
	
	
