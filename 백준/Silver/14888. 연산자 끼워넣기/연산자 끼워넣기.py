def dfs(i, now, add, sub, mul, div):
    global min_value, max_value
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i], add, sub, mul, div)
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i], add, sub, mul, div)
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i], add, sub, mul, div)
            mul += 1
        if div > 0:
            div -= 1
            if now < 0:
                dfs(i + 1, -int(-now / data[i]), add, sub, mul, div)
            else:    
                dfs(i + 1, int(now / data[i]), add, sub, mul, div)
            div += 1

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e10
max_value = -1e10

dfs(1, data[0], add, sub, mul, div)

print(max_value)
print(min_value)
