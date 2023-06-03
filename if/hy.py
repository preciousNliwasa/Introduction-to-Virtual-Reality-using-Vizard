import viz
import vizact
import vizshape

viz.setMultiSample(4)
viz.fov(60)
viz.go()

#Add environment model
day = viz.addChild('sky_day.osgb')

#Add grid
grid = vizshape.addGrid()
grid.color(viz.GRAY)

#Add a world axis with X,Y,Z labels
world_axes = vizshape.addAxes()
X = viz.addText3D('X',pos=[1.1,0,0],color=viz.RED,scale=[0.3,0.3,0.3],parent=world_axes)
Y = viz.addText3D('Y',pos=[0,1.1,0],color=viz.GREEN,scale=[0.3,0.3,0.3],align=viz.ALIGN_CENTER_BASE,parent=world_axes)
Z = viz.addText3D('Z',pos=[0,0,1.1],color=viz.BLUE,scale=[0.3,0.3,0.3],align=viz.ALIGN_CENTER_BASE,parent=world_axes)

#Change navigation style to pivot
import vizcam
cam = vizcam.PivotNavigate(center=[0,1.8,0],distance=5)
cam.rotateRight(-30)
cam.rotateUp(15)

mamaPigeon = viz.addAvatar('pigeon.cfg')
mamaPigeon.setPosition([1,0,3])
mamaPigeon.setEuler([90,0,0])

mamaPigeon_axes = vizshape.addAxes(parent = mamaPigeon, pos=[0,0.4,0],scale=[0.2,0.2,0.2])

#Create a walking action 
walk1 = vizact.walkTo([2,0,4])
walk2 = vizact.walkTo([1,0,3])
turn = vizact.turn(90)
walkSequence = vizact.sequence(walk1,walk2,turn)

#Apply the walking action to mamaPigeon when the spacebaris pressed
vizact.onkeydown(' ',mamaPigeon.addAction,walkSequence)

childPigeon = viz.addAvatar('pigeon.cfg', scale=[0.8,0.8,0.8])
childText = viz.addText3D('Child',pos=[0,0.4,0],scale=[0.1,0.1,0.1],parent=childPigeon,align=viz.ALIGN_CENTER_BASE)
worldPigeon = viz.addAvatar('pigeon.cfg', scale=[0.8,0.8,0.8])
worldText = viz.addText3D('World',pos=[0,0.4,0],scale=[0.1,0.1,0.1],parent=worldPigeon,align=viz.ALIGN_CENTER_BASE)

childPigeon.setPosition([0,0,-1])
worldPigeon.setPosition([0,0,-1])

childPigeon.setParent(mamaPigeon)

# default argument of getPosition is viz.ABS_PARENT 
print("childPigeon's positionoffset from parent:", childPigeon.getPosition())
print("worldPigeon's positionoffset from parent:", worldPigeon.getPosition())

# Get the position in viz.ABS_GLOBAL not the default,viz.ABS_PARENT
print("childPigeon's global position:", childPigeon.getPosition(viz.ABS_GLOBAL))
print("worldPigeon's global position:", worldPigeon.getPosition(viz.ABS_GLOBAL))

crate = viz.addChild('crate.osgb',pos=[-1,0.25,2], scale=[0.5,0.5,0.5])

childPigeon.setPosition([-1,0.5,2.15], viz.ABS_GLOBAL)
worldPigeon.setPosition([-1,0.5,1.85])

childPigeon.setPosition([-1,0,0])
childPigeon.setEuler([-45,0,0])

cam.setCenter([1,0,3.5])
cam.setDistance(6)
cam.rotateRight(-60)
cam.rotateUp(15)

#move childPigeon relative to his local system when 'l'is pressed 
vizact.onkeydown('l', childPigeon.setPosition,[0,0,0.1],viz.REL_LOCAL)

#move childPigeon relative to his parent system when 'p'is pressed 
vizact.onkeydown('p', childPigeon.setPosition,[0,0,0.1],viz.REL_PARENT)

#move childPigeon relative to the world system when 'w'is pressed
vizact.onkeydown('w', childPigeon.setPosition,[0,0,0.1],viz.REL_GLOBAL)