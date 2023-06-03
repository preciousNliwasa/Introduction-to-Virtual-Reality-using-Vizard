import viz
import vizshape

viz.go(viz.FULLSCREEN | viz.STEREO_HORZ)

video = viz.addVideo('indedi.mp4')

leftsphere = vizshape.addSphere(flipFaces=True)
leftsphere.texture(video)
rightsphere = vizshape.addSphere(flipFaces=True)
rightsphere.texture(video)

#Play and loop the video
video.play() 
video.loop() 

#Make sure spheres appear at infinite distance
#This allows other objects to be rendered in front
leftsphere.disable(viz.DEPTH_TEST)
leftsphere.drawOrder(-100)
rightsphere.disable(viz.DEPTH_TEST)
rightsphere.drawOrder(-100)

#Keep spheres centered around main view
viz.link(viz.MainView,leftsphere,mask=viz.LINK_POS)
viz.link(viz.MainView,rightsphere,mask=viz.LINK_POS)

#Setup a panorama camera navigation
import vizcam
vizcam.PanoramaNavigate()

# assign spheres to left/right eyes
leftsphere.renderToEye(viz.LEFT_EYE)
rightsphere.renderToEye(viz.RIGHT_EYE)

# apply shifts to sphere texture coordinates
# to account for video in top/down format
textmat = viz.Transform()
# left sphere
textmat.setScale(1.0, 0.5, 1.0)
textmat.setPosition(0, 0.5, 0)
leftsphere.texmat(textmat)
# right sphere
textmat.setScale(1.0, 0.5, 1.0)
textmat.setPosition(0, 0.0, 0)
rightsphere.texmat(textmat)