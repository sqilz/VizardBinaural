# this is the main file - run this to start the experience!
# this artifact was created by Przemyslaw Hendel - UP739235
# for CT6APPVR unit 

#importing vizard library files
import viz
import viztask

#importing project headers
import artefact
import Vive
import Actions

# Initialize window
viz.go()
# Initialize the Vive headset
#Vive.InitVive()

#load the characters
ground = viz.addChild('ground_grass.osgb')
luigi = viz.addChild('vcc_male.cfg')
#manuel = viz.addChild('vcc_male2.cfg')

#viztask.schedule(loadLevel())

viztask.schedule(Actions.walk(luigi,[2,0,2]))
viztask.schedule(Actions.walk(luigi,[0,0,0]))
viztask.schedule(Actions.speak(luigi))
#viztask.schedule(walka(luigi))
