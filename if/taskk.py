import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

#Add a room.
dojo = viz.addChild('dojo.osgb')

#move the viewpoint
viz.MainView.move([0,0,-5])

#Add some avatars and place them in the room.
male = viz.addAvatar('vcc_male.cfg')
female = viz.addAvatar('vcc_female.cfg')
female.setPosition([-2,0,0])
female.setEuler([90,0,0])
male.setPosition([2,0,0])
male.setEuler([-90,0,0])

#Animate them.
male.state(1)
female.state(1)

#Add some text.
question_text = viz.addText('Hit spacebar to start', viz.SCREEN)
question_text.setScale([.4,.4,.4])
question_text.setPosition([.35,.75,0])
question_text.setBackdrop(viz.BACKDROP_OUTLINE)

#Import the viztask module. 
import viztask

FG = '''
#Create a task.
def myTask():
    #Wait for a keypress.
    yield viztask.waitKeyDown( ' ' )
    #Animate the female.
    female.state( 5 )
    #Wait for a second.
    yield viztask.waitTime( 1 )
    #Make the male walk and wait forhim to finish the action.
    yield viztask.addAction( male,  vizact.walkTo( [-1,0,0] ) )
    #Make the male dance.
    male.state( 4 ) 
#Schedule the task.
viztask.schedule( myTask() )'''

#Import the viztask module. 
import viztask
#Create a task.
def myTask():
    #As long as the task is running. . .
    while True:
        question_text.message( 'Hit the spacebar to begin.' )
        #Wait fora keypress.
        yield viztask.waitKeyDown( ' ' )
        #Animatethe female.
        female.state( 5 )
        #Wait fora second.
        yield viztask.waitTime( 1 )
        #Make themale walk and wait for him to finish the action.
        yield viztask.addAction( male,  vizact.walkTo( [-1,0,0] ) )
        #Make themale dance.
        male.state( 5 )
        #Wait fora sub task to finish.
        yield mySubTask()
        #Give themale a new animation.
        male.state(9)
        #Give thefemale a new animation and wait for it to finish.
        yield viztask.addAction( female, vizact.animation(6) )
        #Make themale run.
        male.addAction( vizact.walkTo( [2,0,-1],2.5,90,11 ) )

#Schedule the task.
viztask.schedule( myTask() )
def mySubTask():
    #Until this function returns a valueor is killed. . .
    while True:
        #Set thetext's message.
        question_text.message( 'Do they keep dancing? (y/n)' )
        #Wait foreither 'y' or 'n' key to be pressed
        d = yield viztask.waitKeyDown( ['y','n'] )
        #If thekeystroke is an 'n'. . .
        if d.key == 'n':
            question_text.message('')
            #End the task.
            return