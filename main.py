# this is the main file - run this to start the experience!
# this artifact was created by Przemyslaw Hendel - UP739235
# for CT6APPVR unit 

#importing vizard library files
import viz
import viztask
import vizact
#importing project headers

import Vive
import Actions
import level

# Initialize window
viz.go()
viz.MainView.setEuler([180,0,0])
viz.MainView.setPosition([0,1.3,4])
# Initialize the Vive headset
Vive.InitVive()


sound = viz.addAudio('resources/barber.mp3')
sound.play()
#load the characters
#ground = viz.addChild('ground_grass.osgb')6

#load guitar model
guitar = viz.addChild('resources/guitar.osgb')


luigi = viz.addAvatar('vcc_male.cfg')
luigi.setPosition(-0.3,0,-2.82)
#manuel = viz.addChild('vcc_male2.cfg')
back = luigi.getBone('Bip01 Neck')

viz.link(back,guitar)

#viztask.schedule(Actions.walk(luigi,[-0.48, 0, -1.15234]))
luigi.addAction(vizact.walkTo(	[-0.48, 0, -1.15234],walkSpeed =2.0))
luigi.addAction(vizact.turn(160,220))
luigi.addAction(vizact.animation(15,speed = 2.2))
luigi.addAction(vizact.turn(0,220))
luigi.addAction(vizact.walkTo([-0.5, 0.0, 2],walkSpeed = 1.2))
luigi.addAction(vizact.animation(14,speed=2))
luigi.addAction(vizact.animation(14,speed=2))
luigi.addAction(vizact.walkTo([-2.00277, -0.00000, 3.66770],walkSpeed =2))

#viztask.schedule()
#viztask.schedule(Actions.walk(luigi,[0,0,0]))


#viztask.schedule(walka(luigi))
