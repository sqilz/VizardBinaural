import viz
import vizact
import viztask
import time
import vizshape

#loading the scene
gallery = viz.addChild('resources/barber_shop.osgb')
door = gallery.getChild('door')

# level settings for the hmd - taken from the vizard vive example
gallery.hint(viz.OPTIMIZE_INTERSECT_HINT)
gallery.disable(viz.SHADOW_CASTING)

# setting door center to fix the pivot/rotation point
door.setCenter([-5,0,0])
#load the tV model and set its position and rotation
tv = viz.addChild('resources/monitor2.osgb')

tv.setPosition(0,2.5,-2.2)
tv.setEuler(0,40,0)

# video texture
video = viz.addVideo('resources/catvid.mpg')
video.play()
video.volume(1)


#creating a plane that holds the video texture
screen = vizshape.addPlane([0.9,0.55,0.9],axis = vizshape.AXIS_Z)
screen.setEuler(45,0,0)
screen.texture(video)

#link the plane to the tv model
viz.link(tv,screen,offset = [0,0.22,0.24])

# for exporting osgb file into other file formats - useful
# gallery.save('model/shop.fbx')

#this function opens the door
def openDoor(door):
	action1 = vizact.spinTo(axisAngle=[0,0,-1,60],speed=120)
	yield door.addAction(action1)
		
#this function closes the door
def closeDoor(doorObject):
	action2 = vizact.spinTo(axisAngle=[0,0,-1,0],speed=30)
	yield doorObject.add(action2)

#schedule door open/close that matches the sound from the binaural recording
viztask.schedule(openDoor(door))
viztask.schedule(closeDoor(door))


		
