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
	navigationNode.setEuler(0,0,0)
	navigationNode.setPosition(-1.5,0.3,3.2)

# setting starting camera position and rotation
	viz.MainView.setEuler([180,0,0])
	viz.MainView.setPosition([0,1.3,4])
