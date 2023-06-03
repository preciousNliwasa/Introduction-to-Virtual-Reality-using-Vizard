import viz
import vizact

myVideo = viz.addTexture( 'radio_down.gif' ) 

#use ball as screen and texture with video 
myScreen = viz.addChild('white_ball.wrl')
myScreen.texture( myVideo )
myScreen.setPosition([0.5,2,2])
myScreen.setEuler([-90,90,0])

#myVideo.play() 
#myVideo.loop()