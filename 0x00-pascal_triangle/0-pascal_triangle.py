def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    # Generate the subsequent rows of Pascal's triangle
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Each row starts with 1
        for j in range(1, len(prev_row)):
            # Calculate the middle values
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # Each row ends with 1
        triangle.append(new_row)

    return triangle
