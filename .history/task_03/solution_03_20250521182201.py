

def appearance(intervals: dict[str, list[int]]) -> int:
    start_lesson = intervals["lesson"][0]
    end_lesson = intervals["lesson"][1]
    total_time = 0

    pupil_time_period = time_period(start_lesson=start_lesson, end_lesson=end_lesson, interaval=intervals["pupil"])
    pupil_time_period = filter_time_period(time_period=pupil_time_period)

    tutor_time_period = time_period(start_lesson=start_lesson, end_lesson=end_lesson, interaval=intervals["tutor"])
    tutor_time_period = filter_time_period(time_period=tutor_time_period)


    for ps,pf in pupil_time_period:
        for ts,tf in tutor_time_period:
            time = min(pf,tf) - max(ps,ts)
            if time > 0:
                total_time += time
    return total_time




def time_period(start_lesson:int, 
                end_lesson:int, 
                interaval:list[int] ) -> list[tuple]:
    return [(max(interaval[i],start_lesson), min(interaval[i+1], end_lesson)) for i in range(0, len(interaval), 2)]



def filter_time_period(time_period:list[tuple])->list[tuple]:
        time_period.sort(key=lambda x: x[0])
        new_period = []
        for period in time_period:
            if not new_period:
                new_period.append(period)
            else:
                last_start, last_end = new_period[-1]
                new_start, new_end = period
                if new_start <= last_end:
                    new_period[-1] = (last_start,max(new_end,last_end))
                else:
                    new_period.append(period)
        return new_period

