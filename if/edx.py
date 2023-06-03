﻿import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.clearcolor(viz.SKYBLUE)

soccerball = viz.addChild('soccerball.osgb')
basketball = viz.addChild('basketball.osgb') 
volleyball = viz.addChild('volleyball.osgb')

soccerball.setPosition([-0.5,2,1.5])
basketball.setPosition([0,2,1.5])
volleyball.setPosition([0.5,2,1.5])

arrow = viz.addChild('arrow.wrl')
arrow.setScale([0.1,0.1,0.1])
arrow.visible(viz.OFF)