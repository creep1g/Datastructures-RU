def factorsone(n):
    results = []
    for k in range(1,n+1):
        if n % k == 0:
            results.append(k)
    return results

def factorstwo(n):
    for k in range(1,n+1):
        if n % k == 0:
            yield k


print(factorsone(100))
yielded = factorstwo(100)

for i in yielded:
    print(i, end=" ")
