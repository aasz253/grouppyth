def multiplication_table(n=10):
    """Print the n x n multiplication table from 1 to n."""
    print(f"\nMultiplication Table (1 to {n})")
    print("=" * 50)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:>5}", end="")
        print()


if __name__ == "__main__":
    size = int(input("Enter the size of the table (e.g. 10): ") or 10)
    multiplication_table(size)
