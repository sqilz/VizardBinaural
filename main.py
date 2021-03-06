﻿# this is the main file - run this to start the experience!
# this artifact was created by Przemyslaw Hendel - UP739235
# for CT6APPVR unit 

#importing vizard library files
import viz
import viztask
import vizact

#importing project headers
import Vive
import level

# Initialize window
viz.go()
viz.update( viz.UPDATE_TIMERS )

# for editing while the vive is not being used/initialization commented out
# comment this out if you want to use the Vive/Oculus/TrinusVR(SteamVR emulation)
#viz.MainView.setEuler([180,0,0])
#viz.MainView.setPosition([0,1.3,4])

# Initialize the Vive headset
Vive.InitVive()

def pause():
	#postprocess - greyscale
	import vizfx.postprocess
	from vizfx.postprocess.color import GrayscaleEffect
	effect = GrayscaleEffect()
	
	# applies a grey viewport postprocess dependant on the viewport rotation on Y axis
	while True:
		#print viz.MainView.getPosition()
	
		# if viewport yaw between 160-180
		if viz.MainView.getEuler() >= [170.0, -0.0, 0.0] and viz.MainView.getEuler() <= [180.0, -0.0, 0.0]:
			vizfx.postprocess.removeEffect(effect)
		# if viewport yaw between 160-180
		elif viz.MainView.getEuler() >= [-180.0, -0.0, 0.0] and viz.MainView.getEuler() <= [-170.0, -0.0, 0.0]:
			vizfx.postprocess.removeEffect(effect)
		else:
			vizfx.postprocess.addEffect(effect)
			
# puts the function on a different thread to allow the while loop to run as the scene keeps going
viz.director(pause)

# load and play the binaural recording
sound = viz.addAudio('resources/barber.mp3')
sound.play()

# load guitar model
guitar = viz.addChild('resources/guitar.osgb')

# load the avatars and set starting position
manuel = viz.addAvatar('vcc_male.cfg')
manuel.setPosition(-0.3,0,-2.82)

luigi = viz.addChild('vcc_male2.cfg')
luigi.setPosition([-2, 0, 6])

# link the guitar to the back model
back = manuel.getBone('Bip01 Neck')
link = viz.link(back,guitar)

# manuel walking in, closing the door, and 'talking' to the user
manuel.addAction(vizact.walkTo(	[-0.48, 0, -1.15234], walkSpeed = 2.0))
manuel.addAction(vizact.turn(160,220))
manuel.addAction(vizact.animation(15, speed = 2.2))
manuel.addAction(vizact.turn(0,220))
manuel.addAction(vizact.walkTo([-0.5, 0.0, 2], walkSpeed = 1.2))
manuel.addAction(vizact.turn(30,220))
manuel.addAction(vizact.animation(14, speed = 2))
manuel.addAction(vizact.animation(14, speed = 2))
manuel.addAction(vizact.turn(0,220))
manuel.addAction(vizact.walkTo([-2, -0.00000, 6.02116], walkSpeed = 2))
manuel.addAction(vizact.animation(3, speed = 0.7))
manuel.addAction(vizact.turn(160,220))
manuel.addAction(vizact.walkTo([-0.5, 0.0, 2], walkSpeed = 2))

# handling actions of luigi
def luigiActions():
		yield viztask.waitTime(53)
		yield viztask.addAction(luigi, vizact.walkTo([-0, 0, 4]))
		yield viztask.addAction(luigi, vizact.walkTo([-1, 0, 3],turnInPlace = True))
		yield viztask.addAction(luigi, vizact.walkTo([0, 0, 2]))
		yield viztask.addAction(luigi, vizact.turn(0,220))
		yield viztask.addAction(luigi, vizact.animation(4))
		
luigiact = viztask.schedule(luigiActions)

def luigiStatusCheck():
	a = True
	while luigiact.alive():
		if luigi.getAnimationTime(4) >= 12 and a == True:
			import vizfx.postprocess
			from vizfx.postprocess.blur import FragmentBlurEffect
			effect = FragmentBlurEffect(distance=4)
			vizfx.postprocess.addEffect(effect)
			a = False
		elif luigi.getAnimationTime(4) >=18:
			viz.quit()
viz.director(luigiStatusCheck)
def walkAndAnimate():
	while True:
		
		# yield waits until a task is finished before progressing to the next one
		# walks to the left side of the user, by the bench
		yield viztask.addAction(manuel, vizact.walkTo([2.4, 0, 2.57996], walkSpeed = 2))
		yield viztask.addAction(manuel, vizact.turn(-45,220))
		
		# change the position and rotation of the linked guitar		
		link.setOffset([-0.5,0.05,-0])
		link.setEuler([-45,0,70])
		
		# pauses animations for 13 seconds so the guitar playing animation is in sync with audio
		yield viztask.waitTime(13)
		
		# locking of bones and setting their positions/rotations so left arm of 'manuel' will 'play' the guitar
		upperarm = manuel.getbone('Bip01 L UpperArm')
		upperarm.lock()
		upperarm.setEuler(0,0,0)
		
		forearm = manuel.getBone('Bip01 L Forearm')
		forearm.lock()
		forearm.setEuler(0,0,-120)
		
		hand = manuel.getBone('Bip01 L Hand')
		hand.lock()
		hand.setEuler(0,180,45)

		#luigi.addAction(vizact.animation(4,speed =1))		
		for num in range(0,11):
			yield viztask.addAction(manuel, vizact.animation(4))
	
		#unlocks bones
		upperarm.unlock()
		forearm.unlock()
		hand.unlock()
		
		# kill task when done
		animationTask.kill()
		
# queue up the function as a task
animationTask = viztask.schedule(walkAndAnimate())

def checkTaskStatus():
	while animationTask.alive():
		# had to do this otherwise it doesn't work because vizard libraries don't allow checking for stuff finishing
		# dummy event
		ANIMATION_TASK_ALIVE = viz.getEventID('ANIMATION_TASK_ALIVE')
	else:
		# when the animationTask finishes carry on from here because vizards libraries are bad 
		# and the execution doesnt carry on from the place where the function was called like it should - animationTask
		# queuing the animation of clapping that 
		
		link.setOffset([0,0,0])
		link.setEuler([0,0,0])
		
# runs function on a new thread
viz.director(checkTaskStatus)

