"""
By: UesleiDev 2022
-> Wtf, i did this (ITS SOOOOOOOOO CRAZY).
-> I'm working in this for 5 hours, then this can be upgraded in the future.'
"""

import re

class TJAParser(object):
	def __init__(self, object):
		self.taiko = {"info": {}, "events": []}
		self.tjaFile = open(str(object) + ".tja").read()
		self.tja = self.tjaFile.split("\n")
		self.pos = 0
		self.eventPos = 0
		self.inStart = False
		self.getEvents = False
		self.getNotes = False
		self.ended = False
		self.notes = []
		self.eventsCount = 0
		
	def TJAKey(self, key):
		keyTitle = key.split(":")[0]
		self.taiko["info"][keyTitle.lower()] = key.replace(keyTitle + ":", "")
	
	def TJAIgnore(self, key):
		if "//" in key or "/" in key: # For comments xD
			return False
		elif key == "" or len(key) == 0:
			return False
		elif key == "#START":
			self.inStart = True
			self.getEvents = True
			self.taiko["notes"] = []
			self.eventPos = self.pos
			return False
		elif key == "#END":
			self.ended = True
			return False
		return True
		
	def TJAEvent(self, key):
		rKey = key.replace("#", "")
		sKey = rKey.split(" ")
		
		if rKey[0:7] == "BARLINE":
			return
		if rKey[0:11] == "GOGOSTART":
			return
		if rKey[0:7] == "GOGOEND":
			return
		if rKey[0:6] == "SCROLL":
			return
			
		self.taiko["events"].append(
			{
				sKey[0].lower(): sKey[1]
			}
		)
		
		self.eventsCount += 1
	
	def TJAIsEvent(self, key):		
		if "#" in key.strip() and "#START" not in key.strip():
			if "#END" in key.strip():
				self.getEvents = False
				self.getNotes = True
				return False
			return True
		
		return False
	
	def skip(self):
		if self.pos < len(self.tja):
			self.pos += 1
	
	def skipEvent(self):
		if self.eventPos < len(self.tja):
			self.eventPos += 1
			
	def Parse(self):
		while self.pos < len(self.tja):
			if self.TJAIgnore(self.tja[self.pos]) and not self.inStart:
				self.TJAKey(self.tja[self.pos])
				
			if self.getEvents and self.inStart:
				if self.TJAIsEvent(self.tja[self.eventPos]):
					self.TJAEvent(self.tja[self.eventPos])
					self.skipEvent()
				else:
					self.skipEvent()
					
			self.skip() # I love this bro.
			
		if self.getNotes:
			self.ParseNotes()
	
	def ParseNotes(self):
		for e in self.tja:
			if(bool(re.match('^[0-9]', e))):
				self.notes.append(e.replace(",", ""))
		
		for note in self.notes:
			for i, num in enumerate(note):
				self.taiko["notes"].append(
					{
						"beat": i * float(self.taiko["info"]["bpm"]),
						"note": num
					}
				)
		
		print(self.taiko) # See the JSOON

#	-> Example:		
parser = TJAParser("KappaSays")
parser.Parse()