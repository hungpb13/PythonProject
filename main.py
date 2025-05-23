# Recursion = a function calls itself from within
# Help with visualize a complex problem into basic steps which can be solved more easily iteratively or recursively

# Iterative
def walk_i(steps):
    for step in range(1, steps + 1):
        print(f"You walk {step} steps")


# Recursive
def walk(steps):
    # Base case
    if steps == 0:
        return

    # Recursive call
    walk(steps - 1)

    print(f"You take step #{steps}")


walk_i(5)
walk(5)

