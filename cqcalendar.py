__version__ = "0.2.0"

class CQCalendar:
	def __init__(self, hour=9, minute=0, is_pm=False, minutes_per_tick=1, day=1, month=1, year=1):
		self.minutes_per_tick = max(1, int(minutes_per_tick))
		
		self.months = [
			("January", 31),
			("February", 28),
			("March", 31),
			("April", 30),
			("May", 31),
			("June", 30),
			("July", 31),
			("August", 31),
			("September", 30),
			("October", 31),
			("November", 30),
			("December", 31),
		]
		
		self.set_time(hour=hour, minute=minute, is_pm=is_pm)
		self.set_date(day=day, month=month, year=year)
		
	def __repr__(self):
		return f"<CQCalendar {self.date_string()} {self.time_string()}>"
		
	def set_time(self, hour=9, minute=0, is_pm=False):
		hour = int(hour)
		minute = int(minute)
		
		if hour < 1: hour = 1
		if hour > 12: hour = 12
		
		if minute < 0: minute = 0
		if minute > 59: minute = 59
		
		self.hour = hour
		self.minute = minute
		self.is_pm = bool(is_pm)
		
	def set_date(self, day=1, month=1, year=1):
		month = int(month)
		day = int(day)
		year = int(year)
		
		month = max(1, min(month, len(self.months)))
		year = max(1, year)
		
		_, days_in_month = self.months[month - 1]
		day = max(1, min(day, days_in_month))
		
		self.day = day
		self.month = month
		self.year = year
		
	def update(self, ticks=1):
		self.minute += int(ticks) * self.minutes_per_tick
		
		while self.minute >= 60:
			self.minute -= 60
			
			self.advance_hour()
			
	def advance_hour(self):
		if self.hour == 11:
			self.hour = 12
			
			self.is_pm = not self.is_pm
			
			if not self.is_pm:
				self.advance_day()
			
		elif self.hour == 12:
			self.hour = 1
			
		else:
			self.hour += 1
			
	def advance_day(self):
		_, days_in_month = self.months[self.month - 1]
		
		self.day += 1
		
		if self.day > days_in_month:
			self.day = 1
			self.advance_month()
			
	def advance_month(self):
		self.month += 1
		
		if self.month > len(self.months):
			self.month = 1
			self.year += 1
			
	def time_string(self):
		return f"{self.hour}:{self.minute:02d} {'PM' if self.is_pm else 'AM'}"
		
	def date_string(self):
		month_name, _ = self.months[self.month - 1]
		return f"{month_name} {self.day}, Year {self.year}"
		
	def datetime_string(self):
		return f"{self.date_string()} at {self.time_string()}"