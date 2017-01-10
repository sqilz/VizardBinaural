import viz
viz.go()
#a = viz.addChild('lab.osgb')
#gallery = viz.addChild('gallery.osgb')
sound =viz.addAudio('barber.mp3')
sound.play()

# Add a crosshair fixed to the view 
crosshair = viz.add('beachball.osgb',pos=(0,0,0.1),euler = [0,-90,0], scale = [0.02,0.01,0.01])
texture = viz.addTexture('crosshair.png')
crosshair.texture(texture);
crosshair.setReferenceFrame(viz.RF_VIEW)


chair = viz.add('Chair.osgb', pos= (0,0,0), scale= [0.01,0.01,0.01])