def appearance(intervals: dict[str, list[int]]) -> int:
    start_lesson = intervals["lesson"][0]
    lesson_end = intervals["lesson"][1]
    pupil_time_period = []
    tutor_time_period = []
    total_time = 0

    time_period(start_lesson=, finish_lesson=, intraval=)


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


def time_period(start_lesson:int, finish_lesson:int, intraval:list[int] ) -> list[tuple]:
    pass