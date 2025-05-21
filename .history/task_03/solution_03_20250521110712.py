

aba = {'lesson': [1594663200, 1594666800],
'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
'tutor': [1594663290, 1594663430, 1594663443, 1594666473]}

lesson_start = aba["lesson"][0]
lesson_end = aba["lesson"][1]


for i in range(0, len(aba["pupil"]), 2):
    pupil_start = aba["pupil"][i]
    pupil_finish = aba["pupil"][i+1]
    pupil_start = lesson_start if pupil_start < lesson_start else pupil_start
    pupil_finish = lesson_end if pupil_finish > lesson_end else pupil_finish

    pupil_start = 
    if pupil_start < lesson_start:
        pupil_start = lesson_start


    (aba["pupil"][i],aba["pupil"][i+1])
    print(aba["pupil"][i])
    print(aba["pupil"][i+1])
    


pupil_period = [
    (aba["pupil"][i],aba["pupil"][i+1]) for i in range(0, len(aba["pupil"]), 2) if
     
      ]
print(pupil_period)