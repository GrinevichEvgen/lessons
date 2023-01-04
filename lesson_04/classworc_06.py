n =7
m =35

for current in range(n, m+1):
    for x in range(2, current):
        if current % x ==0:
            is_primary = False
            break

if is_primary:
           primary_count+=1
        print(current)

