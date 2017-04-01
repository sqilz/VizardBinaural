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
x = level.level()



# Initialize window
viz.go()
viz.update( viz.UPDATE_TIMERS )
# for editing while the vive is not being used/initialization commented out
# comment this out if you want to use the Vive/Oculus/TrinusVR(SteamVR emulation)
viz.MainView.setEuler([180,0,0])
viz.MainView.setPosition([0,1.3,4])

# Initialize the Vive headset
#Vive.InitVive()
	
#load and play the binaural recording
sound = viz.addAudio('resources/barber.mp3')
sound.play()

# load guitar model
guitar = viz.addChild('resources/guitar.osgb')

# load the avatars and set starting position
luigi = viz.addAvatar('vcc_male.cfg')
luigi.setPosition(-0.3,0,-2.82)

#manuel = viz.addChild('vcc_male2.cfg')
# link the guitar to the back model
back = luigi.getBone('Bip01 Neck')
viz.link(back,guitar)

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
luigi.addAction(vizact.walkTo([-2.00277, -0.00000, 3.66770],walkSpeed =2))

#viztask.schedule()
#viztask.schedule(Actions.walk(luigi,[0,0,0]))
#viztask.schedule(walka(luigi))
