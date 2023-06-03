import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

piazza = viz.addChild('piazza.osgb')

female = viz.addAvatar('vcc_female.cfg')
female.setPosition([0,0,3])
female.setEuler([180,0,0])
female.state(12)

#Get a handle to the Neck bone 
neck = female.getBone('Bip01 Neck')
neck.lock() #Disableautomatic animation so that we can manually animate it

#Lock the head bone so that manual movement of the neckbone also moves the child head bone
female.getBone('Bip01 Head').lock() 

#Used to rotate the torso when the viewpoint moves to theside of the avatar
torso = female.getBone('Bip01 Spine1')
torso.lock()

gh = '''def faceView():
    #Make head look at viewpoint
    viewPOS = viz.MainView.getPosition()
    neck.lookAt( viewPOS, mode=viz.AVATAR_WORLD ) #points the head and neck at theviewpoint

#call function that updates Avatar orientation every frame
vizact.ontimer(0, faceView)'''

def faceView():
    #Make head look at viewpoint
    viewPOS = viz.MainView.getPosition()
    neck.lookAt( viewPOS, mode=viz.AVATAR_WORLD ) #points the head and neck at the viewpoint

    #Get neck orientation to see if we need to translate torso
    neckOrientation = neck.getEuler( viz.AVATAR_LOCAL )

    #Move torso so that the neck does not twist too much
    if neckOrientation[0] < -90 and neckOrientation[0] > -180: # -90 to -180
        #Viewpoint in avatar's left-back yaw quadrant
        torso.setEuler( [neckOrientation[0] + 90, 0, 0], viz.AVATAR_LOCAL )
        #Point head back at view because it is child object and was moved by torso rotation
        neck.lookAt( viewPOS, mode=viz.AVATAR_WORLD )

    elif neckOrientation[0] > 90 and neckOrientation[0] < 180: #90 to 180
        #Viewpoint in avatar's right-back yaw quadrant
        torso.setEuler( [neckOrientation[0] - 90, 0, 0], viz.AVATAR_LOCAL )
        #Point head back at view because it is child object and was moved by torso rotastion
        neck.lookAt( viewPOS, mode=viz.AVATAR_WORLD )

#call function that updates Avatar orientation every frame
vizact.ontimer(0, faceView)