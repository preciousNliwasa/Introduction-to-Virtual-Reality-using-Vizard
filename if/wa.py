import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

#This code adds a ground for them to stand on.
ground = viz.addChild('ground.osgb')

#This code adds the avatars and sets them in a neutral state
male = viz.addAvatar('vcc_male.cfg')
female = viz.addAvatar('vcc_female.cfg')
female.setPosition([0,0,7])
female.setEuler([180,0,0])

female.state(1)
male.state(1)

#Move the viewpoint to see both avatars clearly 
viz.MainView.setPosition([-6,1.8,3.5])
viz.MainView.setEuler([90,0,0])

#This number equals the number of seconds the shouting animationtakes  
SHOUT_DURATION = female.getduration(3)

def heDances():

	male_turn_around = vizact.turn(90)
	male.addAction(male_turn_around)
    #male.addAction( vizact.animation(5) )
    #This line creates an animation in which the male avatar moves 
    #to the point (0,0,6).
    #walk_over = vizact.walkTo([0,0,-6])
    #This line calls that animation
    #male.addAction(walk_over)
    
	

def sheShouts():

    female.addAction( vizact.animation(3) )
    vizact.ontimer2(SHOUT_DURATION, 0, heDances)

#This keypress will call the function sheShouts
vizact.onkeydown('1', sheShouts)