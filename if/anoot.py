import viz
import vizact
import vizinput
import viztask

viz.setMultiSample(4)
viz.fov(60)

viz.go()

av = viz.addAvatar('vcc_male.cfg')

pi = viz.addChild('piazza.osgb')

#mini = viz.addChild('mini.osg')

ss = viz.addChild('sky_day.osgb')

av.state(2)

def change_position():
	for i in [0,1,2,3,4,5,6,7]:
		viz.MainView.move([0,0,i])

def walk():
	global where
	where = [4,0,11]
	av.state(2)
	move = vizact.walkTo(where)
	av.addAction(move)
	if av.getPosition() == where:
		user_input = vizinput.input('Message pre')
		return
	#sp = vizact.spin(0,1,0,180,1)
	#tal = vizact.animation(14)
	#seq = vizact.sequence(move,sp,tal)
	#av.addAction(seq)
	#change_position()
	#viz.MainView.setPosition([ty[0],2,ty[2]-4])

	
#print(mini.getPosition())	
def ii():
	vizact.ontimer2(10,1,walk)
	
def yy():

	yield walk()
	user_input = vizinput.input('Message pre')

#viztask.schedule(yy)

vizact.onkeydown('k',ii)

def getP():
	print((av.getPosition()))

vizact.onkeydown('g',getP)

#print(mini.getPosition())

#print(viz.MainView.getPosition())

#viz.collision(viz.ON)
