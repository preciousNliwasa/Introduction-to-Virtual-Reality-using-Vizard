import viz
import vizact
import vizinput
import viztask
import pyttsx3

viz.setMultiSample(4)
viz.fov(60)

viz.go()

engine = pyttsx3.init()

av = viz.addAvatar('vcc_male.cfg')

pi = viz.addChild('piazza.osgb')

#mini = viz.addChild('mini.osg')

ss = viz.addChild('sky_day.osgb')

av.state(2)

def walk():
	global where
	where = [4,0,11]
	av.state(2)
	move = vizact.walkTo(where)
	av.addAction(move)
	#av.execute(2)
	#tal = vizact.animation(14)
	
	
	
	#engine.save_to_file('press G on the keyboard to choose places to go from here, brother', "prenli2.wav")
	#engine.runAndWait()

	av.state(14)
	speech = vizact.speak('prenli2.wav', threshold = .001, scale = 0.01, sync = True)
	av.addAction(speech)
	#av.execute(14)
	
	#seq = vizact.sequence(move,speech)
	#av.addAction(seq)
	
	#av.addAction(move)
	#av.clearActions()
	yield viztask.waitKeyDown('g')
	user_input = vizinput.choose('places to go',['Hotel','Hospital','School'])
	
	
	if user_input == 0:
		
		engine.save_to_file('Press U to choose how to go there.', "prenli3.wav")
		engine.runAndWait()
		
		speech2 = vizact.speak('prenli3.wav', threshold = .001, scale = 0.01, sync = True)
		av.addAction(speech2)
		#av.execute(14)
		
		yield viztask.waitKeyDown('u')
		user_input2 = vizinput.choose('Method',['Air','Bike','Car','Train'])
		
		if user_input2 == 2:
			mini = viz.addChild('mini.osg')
			mini.setPosition([3,0,16])

	#change_position()
	ty = viz.MainView.getPosition()
	print(ty)
	#viz.MainView.setPosition([ty[0],2,ty[2]-4])

	
#print(mini.getPosition())	
def ii():
	vizact.ontimer2(10,1,walk)
	
def yy():

	yield walk()
	user_input = vizinput.input('Message pre')

#viztask.schedule(walk)

vizact.onkeydown('k',viztask.schedule,walk)

def getP():
	print((av.getPosition()))

vizact.onkeydown('r',getP)

#print(mini.getPosition())

#print(viz.MainView.getPosition())

#viz.collision(viz.ON)
