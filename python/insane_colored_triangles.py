def triangle(row):
    row = [0 if c == "R" else 1 if c == "G" else 2 for c in row]
    reduce = [3**i + 1 for i in range(11)][::-1]
    for length in reduce:
        while len(row) >= length:
            row = [
                row[i]
                if row[i] == row[i + length - 1]
                else 2 * (row[i] + row[i + length - 1]) % 3
                for i in range(len(row) - length + 1)
            ]
    return "R" if row[0] == 0 else "G" if row[0] == 1 else "B"
