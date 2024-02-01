k, n = map(int, input().split())


def generate_combinations(k, n, combination=[], results=[]):
    if len(combination) == n:
        results.append(combination.copy())
        return
    
    for i in range(1, k + 1):
        combination.append(i)
        generate_combinations(k, n, combination, results)
        combination.pop()

    return results

combinations = generate_combinations(k, n)
for combo in combinations:
    print(*combo)