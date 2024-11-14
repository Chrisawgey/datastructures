def count_iterations(problemsize):
    count = 0
    while problemsize > 0:
        problemsize = problemsize // 2
        count += 1
    return count

# Problem sizes to test
problem_sizes = [1000, 2000, 4000, 10000, 100000]

# Iterate through each problem size and display the number of iterations
for size in problem_sizes:
    iterations = count_iterations(size)
    print(f"Problem size: {size}, Iterations: {iterations}")
