from math import sqrt


n = int(input())
n = sqrt(n)

if n < 0:
    print('a')
else:
    print('b')

# rychlost - 8 instrukcii -> konstantna casova zlozitost


n = int(input())
total = 0
for i in range(n):
    for j in range(n):
        total += n

print(total)

# rychlost - 4 + 3*n**2  instrukcii -> konstantna casova zlozitost
