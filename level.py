import viz
import vizact
import viztask
import time


gallery = viz.addChild('resources/barber_shop.osgb')
gallery.hint(viz.OPTIMIZE_INTERSECT_HINT)
gallery.disable(viz.SHADOW_CASTING)
door = gallery.getChild('door')

door.setCenter([-5,0,0])

	#ha = vizact.sequence(openDoor,wait,closeDoor)

def openDoor(door):
	action1 = vizact.spinTo(axisAngle=[0,0,-1,60],speed=120)
	yield door.addAction(action1)
	
def closeDoor(doorObject):
	action2 = vizact.spinTo(axisAngle=[0,0,-1,0],speed=120)
	yield doorObject.add(action2)


viztask.schedule(openDoor(door))

viztask.schedule(closeDoor(door))
