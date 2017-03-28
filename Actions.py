"""
This file is responsible for handling events, and animations that are taking place
"""

import vizact

# each function must have a yield on the actions,
#so a scheduled task must finish before another task is being executed
def walk(a, pos):
	walky = vizact.walkTo(pos)
	a.addAction(walky)
	
def walka(a,pos):
	walky = vizact.moveTo(pos)
	yield a.addAction(walky)

def speak(a):
	say = vizact.speak('conversation.wav',scale = 0.004,morph = 'mouth_open')
	yield a.addAction(say)