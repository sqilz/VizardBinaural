
import viz
viz.go()
a = viz.addTexQuad()
video = viz.addVideo('resources/catvid.mpg')
video.play()
video.loop()

a.texture(video)

ground = viz.addChild('ground.osgb')