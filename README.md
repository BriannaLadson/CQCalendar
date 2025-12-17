# CQCalendar
CQCalendar is a lightweight, tick-based time and calendar system for Python games and simulations.

***

## How to Create a Calendar for Your Game
```
import cqcalendar

calendar = cqcalendar.CQCalendar(hour=9, minute=0, is_pm=False, minutes_per_tick=1, day=1, month=1, year=1)
```

***
## Time

### How to Display Current Time
```
print(calendar.time_string())
```

### How to Change Time
```
calendar.set_time(hour=12, minute=0, is_pm=True)
```

### How to Increment Time
```
calendar.update(ticks=10)
```

***
## Date

### How to Display Current Date
```
print(calendar.date_string())
```

### How to Change Date
```
calendar.set_date(day=31, month=12, year=1)
```

***
## Misc.

### How to Display Current Date and Time
```
print(calendar.datetime_string())
```
