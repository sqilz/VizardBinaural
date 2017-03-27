# sets up the Vive HMD
# no controllers needed for this artifact, therefore not initialized
import viz
import steamvr

def InitVive():
	viz.setMultiSample(8)
	# Setup SteamVR HMD
	hmd = steamvr.HMD()
	if not hmd.getSensor():
		sys.exit('SteamVR HMD not detected')

	navigationNode = viz.addGroup()
	viewLink = viz.link(navigationNode, viz.MainView)
	viewLink.preMultLinkable(hmd.getSensor())

	# setting starting camera position and rotation of the view
	navigationNode.setEuler(180,0,0)
	navigationNode.setPosition(0,0,4)
