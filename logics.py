def print_arr(mas):
    for row in mas:
        print(*row)


def empty_list(mas):
    list = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                list.append(num)
    return list


def get_number_from_index(i, j):
    return i * 4 + j + 1


