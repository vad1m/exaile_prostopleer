# -*- coding: utf8 -*-
from xl import event
from gui_part import MyPanel
import prostopleer_pref

def get_preferences_pane():
    return prostopleer_pref

def enable(exaile):
	if (exaile.loading):
		event.add_callback(_enable, 'exaile_loaded')
	else:
		_enable(None, exaile, None)

def disable(exaile):
	global panel
	exaile.gui.remove_panel(panel.vbox)

def _enable(eventname, exaile, nothing):
	global panel
	panel = MyPanel(exaile)
