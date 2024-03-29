﻿import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.clearcolor(viz.SKYBLUE)

MOVE_SPEED = 5 
TURN_SPEED = 60

car = viz.addChild('mini.osg')
ground = viz.addChild('piazza.osgb')
sk = viz.addChild('sky_day.osgb')

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
		
	car.setPosition(view.getPosition())
	car.setEuler(view.getEuler(viz.BODY_ORI))
	car.setPosition([0.35,-1.2,0.2],viz.REL_LOCAL)

def drivemini():
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