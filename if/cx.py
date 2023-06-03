import viz 
viz.go() 

#Create Video Camera extension 
video = viz.add('VideoCamera.dle') 

#Connect to next available generic video capture device 
cam = video.addWebcam() 

#Create quad to display video capture data 
quad = viz.addTexQuad(pos=(0,1.8,2),texture=cam) 
