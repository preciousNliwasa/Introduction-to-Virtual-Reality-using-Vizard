import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)

viz.go()

sky = viz.addChild('sky_day.osgb')

vizact.onkeydown( 's', viz.window.screenCapture, 'image.bmp' ) 

vizact.onkeydown('b', viz.window.startRecording, 'test.avi' ) 
vizact.onkeydown('e',viz.window.stopRecording ) 