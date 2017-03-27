import viz
import time
import viztask
import vizact

def loadLevel():
	#delay loading of the level, so the instructions can be showed
	yield viztask.waitTime(2)
	gallery = viz.addChild('barber_shop.osgb')
	gallery.hint(viz.OPTIMIZE_INTERSECT_HINT)
	gallery.disable(viz.SHADOW_CASTING)
	sound = viz.addAudio('barber.mp3')
	luigi = viz.add('vcc_male.cfg') 
	sound.play()
	Events(luigi)
	
	#	references the door in the barber_shop.osgb
	door = gallery.getChild('door')
	door.setCenter([-5,0,0])

	#spin = vizact.spin(0,0,1, -90)
	#door.addAction(spin)

	# Add a crosshair fixed to the view 
	crosshair = viz.add('beachball.osgb',pos=(0,0,0.1),euler = [0,-90,0], scale = [0.02,0.01,0.01])
	texture = viz.addTexture('crosshair.png')
	crosshair.texture(texture);
	crosshair.setReferenceFrame(viz.RF_VIEW)

	

	#chair = viz.add('Chair.osgb', pos= (0,0,0), scale= [0.01,0.01,0.01])
	#guitar = viz.add('guitar.osgb', pos=(0,1,0))
	#door = viz.add('door.osgb',pos = (0,0,4))
	#bag = viz.add('bag.osgb', pos = (0,2,0))
	#phone = viz.add('phone.osgb', pos =(0,0,0))
	#The code below should print out: 
	#Elapsed time: 2.4 seconds 

	def mytimer(num):
		print 'Elapsed time: {:.1f} seconds'.format(viz.elapsed())
	viz.callback(viz.TIMER_EVENT,mytimer)
	viz.starttimer(0,2.4)
	


text3D = viz.addText('Text',pos=[-1.5,2,4])
import time

"""
def Events(luigi):
	start = time.time()
	#time.clock()    
	elapsed = 0
	seconds = 273
	while elapsed < seconds:
		elapsed = time.time() - start
		print "loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed) 
		#time.sleep(1) 
		#Event 1
		if elapsed > 3:
			walk = vizact.walkTo([5,0,5])
			luigi.addAction(walk)
"""