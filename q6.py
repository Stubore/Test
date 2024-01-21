Maths = int(input('Maths'))
Science = int(input('Science'))
Computer = int(input('Computer'))
English = int(input('English'))
Total_mark = Maths + Science + Computer + English
Percentange =  Total_mark / 4
if Percentange > 70:
    print('Distinction')
elif Percentange > 60:
    print('First Division')
elif Percentange > 40:
    print('Second Division')
else:
    print('Fail')
