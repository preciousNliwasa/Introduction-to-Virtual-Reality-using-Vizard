import viz
import vizmat

viz.setMultiSample(4)
viz.fov(60)
viz.go()

sky = viz.addChild('sky_day.osgb')

pl = viz.addTexQuad()
pl_scale = [60,10,60]
pl.setScale(pl_scale)
pl.setPosition([2,0,6])

matrix = vizmat.Transform()
matrix.setScale(pl_scale)
pl.texmat(matrix)

bricks = viz.addTexture('brick.jpg')
bricks.wrap(viz.WRAP_T,viz.REPEAT)
bricks.wrap(viz.WRAP_S,viz.REPEAT)

pl.texture(bricks)