import viz

#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

viz.go()

#Increase the Field of View
viz.MainWindow.fov(60)
 

piazza = viz.addChild('house.osgb')

avatar = viz.addAvatar('vcc_female.cfg')
avatar.setScale(3800,3800,3800)
avatar.setPosition([59728,-200,36018])
avatar.state(5)
avatar.execute(5)
#avatar.setEuler([50,0,0])

#viz.MainView.move([62000,4000,10000])

viz.MainView.setPosition([63392,5551,45020])


viz.MainView.setEuler([200,0,0])

#viz.collision(viz.ON)
