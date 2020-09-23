# 4-3. Counting to Twenty:
twenty = []
for i in range(1, 21):
    twenty.append(i)
print(twenty)

# 4-4. One Million:
million = []
for number in range(1, 1000001):
    million.append(number)

# 4-5. Summing a Million:
million = [number for number in range(1, 1000001)]
print(max(million))
print(min(million))
print(sum(million))

# 4-6. Odd Numbers:
odds = []
for i in range(1, 21, 2):
    odds.append(i)
print(odds)

# 4-7. Threes:
threes = [i for i in range(3, 31, 3)]
print(threes)

# 4-8. Cubes:
cubes = []
for i in range(1, 11):
    cubes.append(i**3)
print(cubes)

# 4-8. Cubes:
cubes = [i**3 for i in range(1, 11)]
print(cubes)