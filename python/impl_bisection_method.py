def square_root_bisection(num, tol=0.01, max_iter=10):
    if num < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )

    if num == 0 or num == 1:
        print(f"The square root of {num} is {num}")
        return num

    a, b = (0, num) if num > 1 else (num, 1)

    for i in range(0, max_iter):
        mid = (a + b) / 2
        mid_squared = mid**2

        if abs(mid - num**0.5) <= tol:
            print(f"The square root of {num} is approximately {mid}")
            return mid

        if mid_squared < num:
            a = mid
        else:
            b = mid

    print(f"Failed to converge within {max_iter} iterations")
    return None


square_root_bisection(0.001, 1e-7, 50)
square_root_bisection(225, 1e-7, 10)
