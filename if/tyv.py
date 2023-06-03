import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.clearcolor(viz.SKYBLUE)

env = viz.addEnvironmentMap('pano.jpg')

sky = viz.addCustomNode('skydome.dlc')

av = viz.addAvatar('vcc_female.cfg')
av.setPosition([12,-8,-20])
av.setScale([7,7,7])

av.state(1)

sky.texture(env)

#sky.appearance(viz.ENVIRONMENT_MAP)