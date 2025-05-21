def appearance(intervals: dict[str, list[int]]) -> int:
    start_lesson = intervals["lesson"][0]
    end_lesson = intervals["lesson"][1]
    tutor_time_period = []
    total_time = 0

    pupil_time_period = time_period(start_lesson=start_lesson, end_lesson=end_lesson, interaval=intervals["pupil"])
    tutor_time_period = time_period(start_lesson=start_lesson, end_lesson=end_lesson, interaval=intervals["tutor"])


    for ps,pf in pupil_time_period:
        for ts,tf in tutor_time_period:
            time = min(pf,tf) - max(ps,ts)
            if time > 0:
                total_time += time

    return total_time


    pupil_time_period = time_period(start_lesson=start_lesson, lesson_end=end_lesson, interaval=intervals["pupil"])


def time_period(start_lesson:int, end_lesson:int, interaval:list[int] ) -> list[tuple]:
    return [(max(interaval[i],start_lesson), min(interaval[i+1], end_lesson)) for i in range(0, len(interaval), 2)]

