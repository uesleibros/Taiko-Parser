import re

NOTE_TYPES = {
	"0": "blank", # Blank notes, not be generated
	"1": "don",
	"2": "ka",
	"3": "daiDon",
	"4": "daiKa",
	"5": "drumroll",
	"6": "daiDrumroll",
	"7": "ballon",
	"8": "blank", # Blank notes, not be generated
	"9": "ballon",
	"A": "daiDon",
	"B": "daiKa"
}

COURSE_TYPES = {
	"0": "easy",
	"1": "normal",
	"2": "hard",
	"3": "oni",
	"4": "ura",
	"edit": "ura"
}

class TJAParser(object):
	def __init__(self, object):
		self.taiko = {"meta": {}}
		self.tjaFile = open(str(object) + ".tja").read()
		self.tja = self.tjaFile.split("\n")
		self.pos = 0
		self.inStart = False
		self.getNotes = False
		self.ended = False
		self.notes = []
		
	def TJAConvertVAR(self, key):
		if not bool(re.findall(r"[a-zA-Z]", key)) and self.TJAIgnore(key):
			return float(key)
		
		return key
		
	def TJAKey(self, key):
		keyTitle = key.split(":")[0]
		self.taiko["meta"][keyTitle.lower()] = self.TJAConvertVAR(key.replace(keyTitle + ":", ""))
	
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
	
	def skip(self):
		if self.pos < len(self.tja):
			self.pos += 1
			
	def Parse(self):
		while self.pos < len(self.tja):
			if type(self.tja[self.pos]) == str and self.TJAIgnore(self.tja[self.pos]) and not self.inStart:
				self.TJAKey(self.tja[self.pos])
		
			self.skip()
      
		self.ParseNotes()
	
	def TJAChangeJSON(self):
		self.taiko["meta"]["course"] = COURSE_TYPES[str(int(self.taiko["meta"]["course"]))]
	
	def ParseNotes(self):
		self.TJAChangeJSON()
		for e in self.tja:
			if(bool(re.match('^[0-9]', e))):
				self.notes.append(e.replace(",", ""))
		
		for note in self.notes:
			for i, num in enumerate(note):
				self.taiko["notes"].append(
					{
						"id": i,
						"bpm": abs(self.taiko["meta"]["bpm"]),
						"bpmMS": 60000 / self.taiko["meta"]["bpm"],
						"ms": self.taiko["meta"]["offset"] * -1000 + self.taiko["meta"]["offset"],
						"style": int(num),
						"name": NOTE_TYPES[num]
					}
				)
		
parser = TJAParser("chart")
parser.Parse()
