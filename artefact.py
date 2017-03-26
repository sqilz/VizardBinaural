import viz
import viztask

viz.go()

viz.setMultiSample(4)
viz.fov(60)

def loadLevel():
	
	yield viztask.waitTime(2)
	#a = viz.addChild('lab.osgb')
	gallery = viz.addChild('barber_shop.osgb')
	sound = viz.addAudio('barber.mp3')
	sound.play()

	# setting starting camera position and rotation
	viz.MainView.setEuler([180,0,0])
	viz.MainView.setPosition([0,1.3,4])

	#	references the door in the barber_shop.osgb
	door = gallery.getChild('door')
	door.setCenter([-5,0,0])
	spin = vizact.spin(0,0,1, -90)
	door.addAction(spin)

	# Add a crosshair fixed to the view 
	crosshair = viz.add('beachball.osgb',pos=(0,0,0.1),euler = [0,-90,0], scale = [0.02,0.01,0.01])
	texture = viz.addTexture('crosshair.png')
	crosshair.texture(texture);
	crosshair.setReferenceFrame(viz.RF_VIEW)

	luigi = viz.add('vcc_male.cfg') 

	#chair = viz.add('Chair.osgb', pos= (0,0,0), scale= [0.01,0.01,0.01])
	#guitar = viz.add('guitar.osgb', pos=(0,1,0))
	#door = viz.add('door.osgb',pos = (0,0,4))
	#bag = viz.add('bag.osgb', pos = (0,2,0))
	#phone = viz.add('phone.osgb', pos =(0,0,0))
	#The code below should print out: 
	#Elapsed time: 2.4 seconds 

	def mytimer(num):
		
		print viz.ElapsedTimer()
			
		print 'Elapsed time: {:.1f} seconds'.format(viz.elapsed())

		
	viz.callback(viz.TIMER_EVENT,mytimer)
	viz.starttimer(0,2.4)
	
viztask.schedule(loadLevel())

text3D = viz.addText('Text',pos=[-1.5,2,4])