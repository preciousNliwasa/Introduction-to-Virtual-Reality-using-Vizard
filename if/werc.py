import viz

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.addChild('playground.wrl')
viz.clearcolor(viz.SKYBLUE)

viz.MainView.collision( viz.ON )

viz.MainView.setPosition( [5, 1.82, -15] )

viz.MainView.gravity(30)