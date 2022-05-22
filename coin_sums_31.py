
ways = 0
cost = 200

p200 = 0
p100 = 0
p50 = 0
p20 = 0
p10 = 0
p5 = 0
p2 = 0
p1 = 0

p200 = cost // 200
rem = cost - (p200 * 200)
if rem > 0:
    # then fill with p100
    p100 = rem // 100



denoms = [200, 100, 50, 20, 10, 5, 2, 1]

for ix in len(denoms):

