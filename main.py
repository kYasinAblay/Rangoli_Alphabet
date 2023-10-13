import math

list_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

def traverse_numeric(size):
    middle_line_letter_count = (size*2) - 1
    #middle_line_hyphen_count = middle_line_letter_count - 1
    total_char_count_line = (2 * middle_line_letter_count) - 1
    total_column_count = (size*2)-1

    process_alphabet = list_alphabet[:size]
    need_alphabet = process_alphabet[::-1]

    data = [["-"] * total_char_count_line for _ in range(total_column_count)]
    row_index = 0
    midpoint = math.ceil(total_char_count_line/2)-1
    backward = total_column_count-1

    for n in range(size):
        point = 0
        Is_Increase = True
        midpoint_calc_index = midpoint - (n*2)
        while True:
            item = need_alphabet[point]

            if point == 0 and n == 0:
                data[row_index][midpoint] = item
                data[backward][midpoint] = item
                break

            #string_result = "-".join(need_alphabet[point])
            data[row_index][midpoint_calc_index] = item
            if row_index != (total_column_count//2):
                data[backward][midpoint_calc_index] = item

            # Gezi mekanizması
            if Is_Increase:
                if point != n:
                 point += 1
                else:
                   Is_Increase = False
                   point -= 1
            else:
                point -= 1
                if point < 0:
                    break
            midpoint_calc_index += 2

        row_index += 1
        backward -= 1
    string_result = ""
    for arr in data:
        string_result += "".join(arr)+"\n"
    print(string_result)
    #print("\n".join(data))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    traverse_numeric(26)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
