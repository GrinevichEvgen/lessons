arr = ['a', 'b', 'c', 'd']
str = ''
for i in range(len(arr)):
    str += arr[i]
reserved = ''.join(reversed(str))
print(reserved)