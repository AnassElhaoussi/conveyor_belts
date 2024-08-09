test_cases = int(input())

# Optimal solution

for _ in range(test_cases):
    n, x1, y1, x2, y2 = map(int, input().split())
    
    # Calculate the minimum distance from the edge for each point
    dist1 = min(x1 - 1, n - x1, y1 - 1, n - y1)
    dist2 = min(x2 - 1, n - x2, y2 - 1, n - y2)
    
    # Calculate and print the absolute difference
    print(abs(dist1 - dist2))



    