def appearance(intervals: dict[str, list[int]]) -> int:
    start_lesson = intervals["lesson"][0]
    end_lesson = intervals["lesson"][1]
    tutor_time_period = []
    total_time = 0

    pupil_time_period = time_period(start_lesson=start_lesson, lesson_end=end_lesson, interaval=intervals["pupil"])


    for i in range(0, len(intervals["pupil"]), 2):
        pupil_start = intervals["pupil"][i]
        pupil_finish = intervals["pupil"][i+1]
        pupil_start = lesson_start if pupil_start < lesson_start else pupil_start
        pupil_finish = lesson_end if pupil_finish > lesson_end else pupil_finish
        pupil_time_period.append((pupil_start,pupil_finish))


    for i in range(0, len(intervals["tutor"]), 2):
        tutor_start = intervals["tutor"][i]
        tutor_finish = intervals["tutor"][i+1]
        tutor_start = lesson_start if tutor_start < lesson_start else tutor_start
        tutor_finish = lesson_end if tutor_finish > lesson_end else tutor_finish
        tutor_time_period.append((tutor_start,tutor_finish))



    for ps,pf in pupil_time_period:
        for ts,tf in tutor_time_period:
            time = min(pf,tf) - max(ps,ts)
            if time > 0:
                total_time += time

    return total_time


    pupil_time_period = time_period(start_lesson=start_lesson, lesson_end=end_lesson, interaval=intervals["pupil"])


def time_period(start_lesson:int, finish_lesson:int, interaval:list[int] ) -> list[tuple]:
    for i in range(0, len(interaval), 2):
        pupil_start = interaval[i]
        pupil_finish = interaval[i+1]
        pupil_start = start_lesson if pupil_start < start_lesson else pupil_start
        pupil_finish = finish_lesson if pupil_finish > finish_lesson else pupil_finish
        pupil_time_period.append((pupil_start,pupil_finish))
        [  (min()     )       for i in range(0, len(interaval), 2)]

    pass