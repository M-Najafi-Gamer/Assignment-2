s = int(input('pls enter the time you want(second): '))

m = s//60
new_s = s%60

h = 0

if m>59:
    h = m//60
    new_min = m%60
    print(f'{str(h).zfill(2)}:{str(new_min).zfill(2)}:{str(new_s).zfill(2)}')
else:
    print(f'{str(h).zfill(2)}:{str(m).zfill(2)}:{str(new_s).zfill(2)}')