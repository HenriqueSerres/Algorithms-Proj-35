def study_schedule(permanence_period, target_time):
    count_students = 0
    try:
        for get_in, get_out in permanence_period:
            if get_in <= target_time and get_out >= target_time:
                count_students += 1
    except TypeError or ValueError:
        return None
    return count_students
