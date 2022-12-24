from dataclasses import dataclass


@dataclass
class Event:
    start: str
    end: str


@dataclass
class Calendar:
    events: list[Event]
    working_hours: Event


def time_to_minutes(time_str: str) -> int:
    hours, minutes = time_str.split(':')
    return int(hours) * 60 + int(minutes)


def minutes_to_time(time: int) -> str:
    hours = str(time // 60).rjust(2, '0')
    minutes = str(time % 60).rjust(2, '0')
    return f'{hours}:{minutes}'


def get_all_occupied_time_blocks(calendars: list[(list[(str, str)], (str, str))]) -> list[(int, int)]:
    end_of_day = 24 * 60
    occupied_time = []

    for events, working_hours in calendars:
        working_hours_start, working_hours_end = working_hours
        occupied_time.append([0, time_to_minutes(working_hours_start)])
        occupied_time.append([time_to_minutes(working_hours_end), end_of_day])
        for event_start, event_end in events:
            occupied_time.append([time_to_minutes(event_start), time_to_minutes(event_end)])

    return occupied_time


def merge_occupied_time(occupied_time: list[(int, int)]) -> list[(int, int)]:
    occupied_time.sort()
    merged_occupied_time = [occupied_time[0]]

    for time_slot in occupied_time[1:]:
        latest_time_slot = merged_occupied_time[-1]
        if time_slot[0] <= latest_time_slot[1] <= time_slot[1]:
            latest_time_slot[1] = time_slot[1]
            continue
        merged_occupied_time.append(time_slot)

    return merged_occupied_time


def occupied_to_free(occupied_time: list[(int, int)], meeting_duration: int) -> list[(str, str)]:
    free_time = []

    for i in range(1, len(occupied_time)):
        free_time_start = occupied_time[i - 1][1]
        free_time_end = occupied_time[i][0]
        if free_time_end - free_time_start < meeting_duration:
            continue
        free_time.append([minutes_to_time(free_time_start), minutes_to_time(free_time_end)])

    return free_time


def find_free_slots(calendars: list[Calendar], meeting_duration: int) -> list[Event]:
    occupied_time = get_all_occupied_time_blocks(calendars)
    occupied_time = merge_occupied_time(occupied_time)
    return occupied_to_free(occupied_time, meeting_duration)


# result = find_free_slots(
#     calendars=[
#         ([('9:00', '10:30'), ('12:00', '13:00'), ('16:00', '18:00')], ('9:00', '20:00')),
#         ([('10:00', '11:30'), ('12:30', '14:30'), ('14:30', '15:00'), ('16:00', '17:00')], ('10:00', '18:30'))
#     ],
#     meeting_duration=30
# )
# print(f'Result: {result}')
