largest = 0
for i in range(1, 100):
    for j in range(1, 100):
        n = i * j
        s1 = str(n)
        s2 = s1[::-1]
        if s1 == s2:
            largest = max(largest, n)
        
print(largest)
