import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.clearcolor(viz.SKYBLUE)

#add the avatar and set his position and orientation
male = viz.addAvatar('vcc_male.cfg', pos=(0,0,4), euler=(180,0,0) )

#These keys will call various animations using the <avatar>.addAction()command. 
#vizact.onkeydown('1', male.addAction, vizact.animation(1))
#vizact.onkeydown('2', male.addAction, vizact.animation(2))
vizact.onkeydown('3', male.addAction, vizact.animation(3))

vizact.onkeydown('1', male.state, 1)
vizact.onkeydown('2', male.state, 2)
#vizact.onkeydown('3', male.state, 3)

#change the speed of the animation 
vizact.onkeydown('4', male.speed, 2)

vizact.onkeydown('5', male.speed, .5)

#blend two animations 
def blendAnimations():

    male.blend(4, .2)
    male.blend(10, .8)

vizact.onkeydown('6', blendAnimations)

#execute a single animation that does not repeat 
vizact.onkeydown('7', male.execute, 6)

#stop an animation 
vizact.onkeydown('8', male.stopAction, 3)

vizact.onkeydown('9', male.stopAnimation, 3)
