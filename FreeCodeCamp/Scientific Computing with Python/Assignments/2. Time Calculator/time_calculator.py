def add_time(start, duration, start_day=None):
    # Duration reduced by number of days
    add_hours, add_minutes = map(int, duration.split(":"))
    if add_hours > 24:
        add_days = add_hours // 24
        remaining_hours = add_hours % 24
    else:
        remaining_hours = add_hours
        add_days = 0
    # Determine AM/PM hours
    start_hours, start_second_part = start.split(":")
    start_minutes, start_meridiem = start_second_part.split()
    start_hours = int(start_hours)
    start_minutes = int(start_minutes)
    # Convert to 24 hour
    if start_meridiem == "PM":
        start_hours += 12

    # Initialise variable
    display_hours = 0
    # Add minutes
    total_minutes = start_minutes + add_minutes
    if total_minutes > 60:
        display_minutes = total_minutes % 60
        display_hours = 1
    else:
        display_minutes = total_minutes
    # Add hours
    display_hours += start_hours + remaining_hours
    if display_hours > 24:
        add_days += 1
        display_hours %= 24
    # Format midnight
    if display_hours == 24:
        display_hours -= 24
        display_meridiem = "AM"
        add_days += 1
    # Format time to 12 hours
    elif display_hours > 12:
        display_hours -= 12
        display_meridiem = "PM"
    else:
        display_meridiem = "AM"

    # If 1 day, (next day)
    if add_days == 1:
        display_days_later = " (next day)"
    # If >1 day, (n days later)
    elif add_days > 1:
        display_days_later = f" ({add_days} days later)"
    else:
        display_days_later = ""

    # Combine all together
    new_time = (f"{display_hours}:{"{:02d}".format(display_minutes)} "
                f"{display_meridiem}{display_days_later}")

    # Add the day if argument available
    if start_day is not None:
        day = day_week(start_day, add_days)
        new_time += " " + day

    return new_time


def day_week(start_day, add_days=0):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday", "Sunday"]
    day_number = days.index(start_day) + add_days
    if day_number + 1 > 7:
        return days[day_number % len(day_number)]
    else:
        return days[day_number]
