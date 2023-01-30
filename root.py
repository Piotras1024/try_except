import sys


def sqrt(x):
    """Compute square roots using the method of heron of Alexandria.

    Args:
    The number for which the square root is to be computed.

    Returns:
    The square root of x.

    Raises:
    ValueError: if x is negative.
    """

    if x < 0:
        raise ValueError(f"Cannot compute root of negative number {x}")

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(0))
        print(sqrt(-999))
    except ValueError as error:
        print(error, file=sys.stderr)

    print("Program execution continues normally here")


if __name__ == "__main__":
    main()
