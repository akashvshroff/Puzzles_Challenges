def conflicting_times(t1, t2):
    """
    Determines if 2 times are overlapping
    """
    t1, t2 = sorted((t1, t2))
    assert (t1[0] <= t2[0])
    if t1[1] >= t2[0]:  # first end greater than second
        return True
    return False


def num_class_room(schedule: list) -> int:
    """
    Given an array of time intervals (start, end) for classroom lectures
    (possibly overlapping), find the minimum number of rooms required.
    For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
    """
    if not schedule:
        return 0
    meeting_rooms = [schedule[0]]
    remaining_times = schedule[1:]
    for time in remaining_times:
        conflict = True
        for occupied in meeting_rooms:
            if not conflicting_times(time, occupied):
                conflict = False
                break
        if conflict:
            meeting_rooms.append(time)
    return len(meeting_rooms)


assert num_class_room([]) == 0
assert num_class_room([(30, 75), (0, 50), (60, 150)]) == 2
assert num_class_room([(30, 75), (0, 50), (10, 60), (60, 150)]) == 3
assert num_class_room([(60, 150)]) == 1
assert num_class_room([(60, 150), (150, 170)]) == 2
assert num_class_room([(60, 150), (60, 150), (150, 170)]) == 3
