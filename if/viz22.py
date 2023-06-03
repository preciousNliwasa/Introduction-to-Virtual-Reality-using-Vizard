import viz

#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

viz.go()

#Increase the Field of View
viz.MainWindow.fov(60)

viz.go()

#ground = viz.add('sky_day.osgb')

#ground.collidePlane()


mo = viz.addChild('office.osgb')
#viz.MainView.setPosition([41.8,13.33,17])

#avatar = viz.addAvatar('vcc_female.cfg')
#avatar.setScale(600,600,600)
#avatar.setPosition([9072,97,4578])
#avatar.state(5)
#avatar.execute(5)

viz.MainView.setPosition([8468,825,4000])


viz.MainView.setEuler([200,0,0])


#viz.collision(viz.ON)
