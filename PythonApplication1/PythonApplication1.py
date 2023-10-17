def average(massive):
    ave = sum(massive) / len(massive)
    return ave


def sort_rows_by_average(matrix):
    averages = [(row, average(row)) for row in matrix]
    for row, avg in averages:
        print(f"average in len {row}: {avg}")
    sorted_averages = sorted(averages, key=lambda x: x[1])
    sorted_matrix = [row for row, _ in sorted_averages]
    return sorted_matrix

matrix = [[21, 46, 879, 5], [81, 26, 368, 567], [7, 4, 9, 13], [4234, 86, 94, 25]]
sorted_matrix = sort_rows_by_average(matrix)
print(sorted_matrix)








