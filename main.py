# this is the main file - run this to start the experience!
# this artifact was created by Przemyslaw Hendel - UP739235
# for CT6APPVR unit 

#importing vizard library files
import viz
import viztask
import vizact

#importing project headers
import Vive
import level
import time

# Initialize window
viz.go()
viz.update( viz.UPDATE_TIMERS )
# for editing while the vive is not being used/initialization commented out
# comment this out if you want to use the Vive/Oculus/TrinusVR(SteamVR emulation)
viz.MainView.setEuler([180,0,0])
viz.MainView.setPosition([0,1.3,4])

def Pause():
	#postprocess - greyscale
	import vizfx.postprocess
	from vizfx.postprocess.color import GrayscaleEffect
	effect = GrayscaleEffect()
	
	#gray_effect = BlendEffect(None,effect),blend=0.0)
	while True:
		print viz.MainView.getPosition()
		# if viewport yaw between 160-180
		if viz.MainView.getEuler() >= [170.0, -0.0, 0.0] and viz.MainView.getEuler() <= [180.0, -0.0, 0.0]:
			vizfx.postprocess.removeEffect(effect)
		# if viewport yaw between 160-180
		elif viz.MainView.getEuler() >= [-180.0, -0.0, 0.0] and viz.MainView.getEuler() <= [-170.0, -0.0, 0.0]:
			vizfx.postprocess.removeEffect(effect)
		else:
			vizfx.postprocess.addEffect(effect)
			
			
			
# puts the function on a different thread to allow the while loop to run as the scene keeps going
viz.director(Pause)

# Initialize the Vive headset
#Vive.InitVive()
	
# load and play the binaural recording
sound = viz.addAudio('resources/barber.mp3')
sound.play()

# load guitar model
guitar = viz.addChild('resources/guitar.osgb')

# load the avatars and set starting position
luigi = viz.addAvatar('vcc_male.cfg')
luigi.setPosition(-0.3,0,-2.82)

# manuel = viz.addChild('vcc_male2.cfg')
# link the guitar to the back model
back = luigi.getBone('Bip01 Neck')
link = viz.link(back,guitar)

# luigi walking in, closing the door, and 'talking' to the user
luigi.addAction(vizact.walkTo(	[-0.48, 0, -1.15234],walkSpeed =2.0))
luigi.addAction(vizact.turn(160,220))
luigi.addAction(vizact.animation(15,speed = 2.2))
luigi.addAction(vizact.turn(0,220))
luigi.addAction(vizact.walkTo([-0.5, 0.0, 2],walkSpeed = 1.2))
luigi.addAction(vizact.turn(30,220))
luigi.addAction(vizact.animation(14,speed=2))
luigi.addAction(vizact.animation(14,speed=2))
luigi.addAction(vizact.turn(0,220))
luigi.addAction(vizact.walkTo([-2, -0.00000, 6.02116],walkSpeed =2))
luigi.addAction(vizact.animation(3,speed=0.7))
luigi.addAction(vizact.turn(160,220))
luigi.addAction(vizact.walkTo([-0.5, 0.0, 2],walkSpeed = 2))

def walkNturn():
	while True:
		# yield waits until a task is finished before progressing to the next one
		yield viztask.addAction(luigi, vizact.walkTo([2.4, 0, 2.57996],walkSpeed = 2))
		yield viztask.addAction(luigi, vizact.turn(-45,220))
		
		# change the position and rotation of the linked guitar
		link.setOffset([-0.5,0.05,-0])
		link.setEuler([-45,0,70])
		yield viztask.waitTime(13)
		upperarm = luigi.getbone('Bip01 L UpperArm')
		upperarm.lock()
		upperarm.setEuler(0,0,0)
		
		forearm = luigi.getBone('Bip01 L Forearm')
		forearm.lock()
		forearm.setEuler(0,0,-120)
		#forearm.setPosition(0.6,-0.1,0)
		hand = luigi.getBone('Bip01 L Hand')
		hand.lock()
		hand.setEuler(0,180,45)
		
		yield viztask.addAction(luigi, vizact.animation(4,speed = 0.1))
		
		
viztask.schedule(walkNturn())






#viztask.schedule()
#viztask.schedule(Actions.walk(luigi,[0,0,0]))
#viztask.schedule(walka(luigi))
