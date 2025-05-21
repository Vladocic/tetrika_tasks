

aba = {'lesson': [1594663200, 1594666800],
'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
'tutor': [1594663290, 1594663430, 1594663443, 1594666473]}

lesson_start = aba["lesson"][0]
lesson_end = aba["lesson"][1]
pupil_time_period = []
tutor_time_period = []

for i in range(0, len(aba["pupil"]), 2):
    pupil_start = aba["pupil"][i]
    pupil_finish = aba["pupil"][i+1]
    pupil_start = lesson_start if pupil_start < lesson_start else pupil_start
    pupil_finish = lesson_end if pupil_finish > lesson_end else pupil_finish
    pupil_time_period.append((pupil_start,pupil_finish))


for i in range(0, len(aba["tutor"]), 2):
    tutor_start = aba["tutor"][i]
    tutor_finish = aba["tutor"][i+1]
    tutor_start = lesson_start if tutor_start < lesson_start else tutor_start
    tutor_finish = lesson_end if tutor_finish > lesson_end else tutor_finish
    tutor_time_period.append((tutor_start,tutor_finish))

print(pupil_time_period)
print(tutor_time_period)



for ps,pf in pupil_time_period:
    for ts,tf in tutor_time_period:
        
        print(f'{min(pf,tf) - max(ps,ts)}fff')
        print('f')
        print(aga)