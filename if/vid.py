import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)

viz.go()

av = viz.addAvatar('vcc_male.cfg')

pi = viz.addChild('piazza.osgb')

mini = viz.addChild('mini.osg')

ss = viz.addChild('sky_day.osgb')

av.state(2)

def change_position():
	for i in [0,1,2,3,4,5,6,7]:
		viz.MainView.move([0,0,i])

def walk():
	global where
	where = [0,0,5]
	av.state(2)
	move = vizact.walkTo(where)
	av.addAction(move)
	change_position()
	
#print(mini.getPosition())	

vizact.onkeydown('w',viz.MainView.setPosition,[0,0,1],viz.REL_LOCAL)

def getP():
	print((viz.MainView.getPosition()))

vizact.onkeydown('g',getP)

#print(mini.getPosition())

#print(viz.MainView.getPosition())

#viz.collision(viz.ON)
