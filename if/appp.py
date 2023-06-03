import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.MainView.setPosition([-20,5,-16])

viz.addChild('ground.osgb')
wheel = viz.addChild('wheelbarrow.ive')
tesla = viz.add('cyber.osgb')
tesla.setScale(0.008,0.008,0.008)
viz.MainView.move([0,0,-7])
viz.clearcolor(viz.SKYBLUE)

moveForward = vizact.move(0,0,7,1)

turnRight = vizact.spin(0,1,0,90,1)

#wheel.addAction(moveForward) 
#wheel.addAction(turnRight) 

moveInSquare = vizact.sequence(moveForward,turnRight,4) 

vizact.onkeydown(' ',tesla.addAction,moveInSquare)

vizact.onkeydown('c', tesla.clearActions)