import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.clearcolor(viz.SKYBLUE)

mySound = viz.addAudio( 'bach_air.mid' ) 

vizact.onkeydown( 'p', mySound.play ) 
vizact.onkeydown( 's', mySound.stop ) 

mySound.loop( viz.ON ) 
#mySound.rate(3) 

myVideo = viz.addVideo('kamodzi.mpg',type = viz.TEXTURE_2D)

#use ball as screen and texture with video 
myScreen = viz.addChild('white_ball.wrl')
mm = viz.addTexQuad()
mm.texture(myVideo)
myScreen.texture( myVideo )
myScreen.setPosition([0.5,2,2])
myScreen.setEuler([-90,90,0])

myVideo.play() 
myVideo.loop() 