__version__ = "0.1.0"

class CQCalendar:
	def __init__(self, hour=9, minute=0, is_pm=False, minutes_per_tick=1):
		self.hour = hour
		self.minute = minute
		self.is_pm = is_pm
		self.minutes_per_tick = minutes_per_tick
		
	def set_time(self, hour, minute=0, is_pm=False):
		self.hour = hour
		self.minute = minute
		self.is_pm = is_pm
		
	def update(self, ticks=1):
		self.minute += ticks * self.minutes_per_tick
		
		while self.minute >= 60:
			self.minute -= 60
			
			self.advance_hour()
			
	def advance_hour(self):
		if self.hour == 11:
			self.hour = 12
			
			self.is_pm = not self.is_pm
			
		elif self.hour == 12:
			self.hour = 1
			
		else:
			self.hour += 1
			
	def time_string(self):
		return f"{self.hour}:{self.minute:02d} {'PM' if self.is_pm else 'AM'}"