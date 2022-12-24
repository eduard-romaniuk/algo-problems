import tests


def _convert_events(events_list, convert_function):
    return [list(map(convert_function, event)) for event in events_list]


def convert_to_timestamp(events_list):
    def to_minutes(time_str):
        hours, minutes = time_str.split(':')
        return int(hours) * 60 + int(minutes)

    return _convert_events(events_list, to_minutes)


def convert_to_time(events_list):
    def to_time_str(time):
        hours = str(time // 60)
        minutes = str(time % 60).rjust(2, '0')
        return f'{hours}:{minutes}'

    return _convert_events(events_list, to_time_str)


def merge_occupied_time(occupied_time1, occupied_time2):
    i1 = 1
    i2 = 0
    merged = [occupied_time1[0]]

    def merge_into(current):
        last = merged[-1]
        if current[0] >= last[0] and current[1] <= last[1]:
            return
        if current[0] <= last[1] <= current[1]:
            last[1] = current[1]
            return
        merged.append(current)

    while i1 < len(occupied_time1) and i2 < len(occupied_time2):
        if occupied_time1[i1] < occupied_time2[i2]:
            merge_into(occupied_time1[i1])
            i1 += 1
        else:
            merge_into(occupied_time2[i2])
            i2 += 1

    while i1 < len(occupied_time1):
        merge_into(occupied_time1[i1])
        i1 += 1

    while i2 < len(occupied_time2):
        merge_into(occupied_time2[i2])
        i2 += 1
    return merged


def occupied_to_free(occupied_time, meeting_duration):
    free_time = []

    for i in range(1, len(occupied_time)):
        free_time_start = occupied_time[i - 1][1]
        free_time_end = occupied_time[i][0]
        if free_time_end - free_time_start < meeting_duration:
            continue
        free_time.append([free_time_start, free_time_end])

    return free_time


def calendar_to_occupied_time(calendar, working_hours):
    return convert_to_timestamp([['00:00', working_hours[0]]] + calendar + [[working_hours[1], '24:00']])


# Time O(c1 + c2)
# Space O(c1 + c2)
# where c1 and c2 are numbers of meetings in calendars
def calendar_matching(calendar1, working_hours1, calendar2, working_hours2, meeting_duration):
    occupied_time = merge_occupied_time(
        calendar_to_occupied_time(calendar1, working_hours1),
        calendar_to_occupied_time(calendar2, working_hours2)
    )
    free_time = occupied_to_free(occupied_time, meeting_duration)
    return convert_to_time(free_time)


tests.test(calendar_matching)
