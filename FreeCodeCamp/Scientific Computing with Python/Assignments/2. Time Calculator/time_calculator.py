def add_time(start, duration):
    # Duration reduced by number of days
    add_hours, add_minutes = map(int, duration.split(":"))
    if add_hours > 24:
        add_days = add_hours // 24
        remaining_hours = add_hours % 24
    else:
        remaining_hours = add_hours

    # Determine AM/PM hours
    start_hours, start_second_part = start.split(":")
    start_minutes, start_meridiem = start_second_part.split()
    start_hours = int(start_hours)
    start_minutes = int(start_minutes)
    # Convert to 24 hour
    if start_meridiem == "PM":
        start_hours += 12

    # Initialise variables
    display_hours = 0
    add_days = 0
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
    # Format time to 12 hours
    if display_hours > 12:
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

    return new_time
# def day_week():
