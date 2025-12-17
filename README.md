# CQCalendar
CQCalendar is a lightweight, tick-based time and calendar system for Python games and simulations.

***

## How to Create a Calendar for Your Game
```
import cqcalendar

calendar = cqcalendar.CQCalendar(hour=9, minutes=0, is_pm=False, minutes_per_tick=1)
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
