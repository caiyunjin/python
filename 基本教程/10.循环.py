# while
a = 1
sum = 0
while a <= 100:
    # 偶数和
    if a % 2 == 0:  # if not bool(a % 2) 奇数和
        sum += a
    a += 1
print(sum)

# for in
for item in "python":
    print(item)

for i in range(10):
    print(i)

for _ in range(10):  #
    print("python")

# break 跳出循环

# continue
for i in range(1, 10):
    if i % 5 == 0:
        print(i)

for i in range(1, 10):
    if i % 5 != 0:
        continue
    print(i)

# 嵌套循环
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, "*", j, "=", i * j, end="\t")
    print()

# 二重循环

for i in range(1, 10):
    for j in range(1, 11):
        if j % 2 == 0:
            # break
            continue
        print(j, end="\t")
    print()
