##################################################################### 
# WorldViz Copyright 2011 
# 
# 
# This program demonstrates how to connect two Vizard sessions 
# together using the network feature.  This only requiresthat 
# two machines be in the same network domain but does not 
# require TCP so the computers don't need IP addresses. 
# 
# On each computer, the other user is represented as a robot. When 
# the other person moves around, you'll see the robot go. 
# 
##################################################################### 
##################################################################### 

import viz
import vizact
import vizinput
import steve

viz.setMultiSample(4)
viz.fov(60)
viz.go()

# Use the steve module to represent the other user.
# You will actually have no representation of yourself onyour own monitor.
player_matrix = viz.Matrix()
avatar = steve.Steve()
avatar.setTracker(player_matrix)

# Add the world
maze = viz.addChild('maze.osgb')

#Use a prompt to ask the user the network name of the othercomputer.
target_machine = vizinput.input('Enter thename of the other machine').upper()

#Add a mailbox from which to send messages. This is youroutbox.
target_mailbox = viz.addNetwork(target_machine)

def sendPosition():

    #Retrieve current transform of viewpoint
    mat = viz.MainView.getMatrix()

    #Send position/rotation to target networkobject
    target_mailbox.send(action=updatePlayer, quat=mat.getQuat(), pos=mat.getPosition())

# Start a timer that sends out data over the network everyframe
vizact.ontimer(0,sendPosition)

def updatePlayer(e):
    player_matrix.setPosition(e.pos)
    player_matrix.setQuat(e.quat)

# Listens for any incoming messages
def onNetwork(e):
    if e.sender.upper() == target_machine:
        e.action(e)

# Register network to listen from incoming messages
viz.callback(viz.NETWORK_EVENT, onNetwork)