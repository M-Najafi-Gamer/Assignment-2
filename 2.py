while True:
    h = int(input('pls enter hour: '))
    if h<0:
        print('error!!!\npls enter a positive number )')
    else:
        break

while True:
    m = int(input('pls enter minute: '))
    if m<0 or m>59:
        print('error!!!\npls enter a number in range (0,59)')
    else:
        break

while True:
    s = int(input('pls enter second: '))
    if s<0 or s>59:
        print('error!!!\npls enter a number in range (0,59)')
    else:
        break

print(f'Your time is: {str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}')

time_to_second = (h*3600) + (m*60) + s

print('your time in type of second is:',time_to_second)