import viz
import vizact

#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

viz.go()

#Increase the Field of View
viz.MainWindow.fov(60)


livingroom = viz.addChild('InteriorTest2.osgb')

avatar = viz.addAvatar('vcc_male2.cfg')
avatar.setScale(4,4,4)
avatar.setPosition([70,75,240])
avatar.state(6)

speech = vizact.speak('jfk.wav', threshold = .1, scale = 0.7, sync = True)
#Add the action to the avatar
#avatar.addAction(speech)
avatar.execute(6)
#avatar.setEuler([50,0,0])

#viz.MainView.move([620,40,10])

viz.MainView.setPosition([80,80,250])


viz.MainView.setEuler([200,0,0])

#viz.collision(viz.ON)
