def count_iterations(problemsize):
    count = 0
    while problemsize > 0:
        problemsize = problemsize // 2
        count += 1
    return count


problemsize = int(input("Enter the problem size: "))
iterations = count_iterations(problemsize)
print(f"The loop ran {iterations} times.")
