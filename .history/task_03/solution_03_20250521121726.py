
intervals = {'lesson': [1594702800, 1594706400],
        'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]}



def appearance(intervals: dict[str, list[int]]) -> int:
    start_lesson = intervals["lesson"][0]
    end_lesson = intervals["lesson"][1]
    total_time = 0

    pupil_time_period = time_period(start_lesson=start_lesson, end_lesson=end_lesson, interaval=intervals["pupil"])
    tutor_time_period = time_period(start_lesson=start_lesson, end_lesson=end_lesson, interaval=intervals["tutor"])
    
    print(pupil_time_period)

    for ps,pf in pupil_time_period:
        for ts,tf in tutor_time_period:
            time = min(pf,tf) - max(ps,ts)
            if time > 0:
                total_time += time
    print(total_time)
    return total_time




def time_period(start_lesson:int, 
                end_lesson:int, 
                interaval:list[int] ) -> list[tuple]:
    return [(max(interaval[i],start_lesson), min(interaval[i+1], end_lesson)) for i in range(0, len(interaval), 2)]



period = [(1594702800, 1594704500), (1594702800, 1594704542), 
          (1594704512, 1594704515), (1594704514, 1594704545), 
          (1594704564, 1594704582), (1594704581, 1594704582)]

def filter_time_period(time_period:list[tuple])->list[tuple]:
        time_period.sort(key=lambda x: x[0])
        new_period = []
        for period in time_period:
            if period not in new_period:
                  new_period.append(period)
            else:
                 last_start, last,end = 
        pass

appearance(intervals)


