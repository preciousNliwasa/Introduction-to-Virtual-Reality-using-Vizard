import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

# Load texture
pic = viz.addTexture('lake3.jpg')
pic.wrap(viz.WRAP_T, viz.CLAMP_TO_BORDER)
pic.wrap(viz.WRAP_S, viz.MIRROR)

sky = viz.addChild('sky_day.osgb')

# Create surface to wrap the texture on 
quad = viz.addTexQuad() 
quad.setPosition([-.75, 2, 3]) #put quad inview 

# Wrap texture on quad 
quad.texture(pic)

# Create new texquad 
quad2 = viz.addTexQuad() 
quad2.setPosition([.75, 2, 3]) 
quad2.texture(pic)

import vizmat 
matrix = vizmat.Transform() 
# Scale down texture by scaling up the texquad's texturecoordinates 
matrix.setScale([1.5,1.5,1]) 
matrix.setTrans([-.25,-.25,1])
quad2.texmat(matrix) 


# Make background wall
WALL_SCALE = [10, 3, 1]

wall = viz.addTexQuad()
wall.setPosition( [0, 2, 3] )
wall.zoffset(1) #avoid zfighing, make wall appear behind pictures
wall.setScale( WALL_SCALE )

# Apply nice repeating brick texture
matrix = vizmat.Transform()
matrix.setScale( WALL_SCALE )
wall.texmat( matrix )

bricks = viz.addTexture('uy.png')
bricks.wrap(viz.WRAP_T, viz.REPEAT)
bricks.wrap(viz.WRAP_S, viz.REPEAT)

wall.texture(bricks)

viz.collision(viz.OFF)