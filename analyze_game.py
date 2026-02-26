import sys



def read_game(file_name):

    lines = []

    with open(file_name, "r") as f:
        for line in f:
            line = line.strip()

            if line == "" or line.startswith("#"):
                continue

            lines.append(line)

    half = len(lines) // 2

    A = []
    for row in lines[:half]:
        A.append(list(map(int, row.split())))

    # second half -> Player B
    B = []
    for row in lines[half:]:
        B.append(list(map(int, row.split())))

    return A, B



def dominant_strategy_A(A):

    num_rows = len(A)
    num_cols = len(A[0])

    for r in range(num_rows):

        always_better = True

        for other in range(num_rows):

            if r == other:
                continue

            for c in range(num_cols):

                if A[r][c] < A[other][c]:
                    always_better = False

        if always_better:
            return r

    return None



def dominant_strategy_B(B):

    num_rows = len(B)
    num_cols = len(B[0])

    for c in range(num_cols):

        always_better = True

        for other in range(num_cols):

            if c == other:
                continue

            for r in range(num_rows):

                if B[r][c] < B[r][other]:
                    always_better = False

        if always_better:
            return c

    return None



def find_nash_equilibrium(A, B):

    rows = len(A)
    cols = len(A[0])

    result = []

    for i in range(rows):
        for j in range(cols):

            best_for_A = max(A[r][j] for r in range(rows))
            A_is_happy = (A[i][j] == best_for_A)

            best_for_B = max(B[i])
            B_is_happy = (B[i][j] == best_for_B)

            if A_is_happy and B_is_happy:
                result.append((i, j))

    return result



def main():

    if len(sys.argv) < 2:
        print("Usage: python analyze_game.py <file>")
        return

    A, B = read_game(sys.argv[1])

    print("\nGame Analysis\n")

    dA = dominant_strategy_A(A)
    dB = dominant_strategy_B(B)

    print("Dominant Strategy:")
    print("Player A:", dA if dA is not None else "None")
    print("Player B:", dB if dB is not None else "None")

    equilibria = find_nash_equilibrium(A, B)

    print("\nNash Equilibrium:")
    if len(equilibria) == 0:
        print("None")
    else:
        for eq in equilibria:
            print(eq)


if __name__ == "__main__":
    main()
