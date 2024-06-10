input_raw_text = open("input.txt")
input_text = input_raw_text.readlines()
symbols = ["@","*", "$", "#", "+", "-", "%", "/", "=", "&"]
part_numbers = []

line_length = len(input_text[0])
line_amount = len(input_text)

def check_part_number(lines, char_pos):
    for line in lines:
        for x in range(3):
            char_position = char_pos+x-1
            if char_position < line_length-1 and char_position > 0:
                if any(x in line[char_position] for x in symbols):
                    return True
                else:
                    pass
    return False


for line in range(line_amount):
    current_line = input_text[line]
    number = ""
    is_new_number = False
    is_part_number = False

    for char in range(line_length-1):
        print(char)
        if current_line[char].isnumeric():
            is_new_number = True
            number += str(current_line[char])
            if is_part_number == False:
                if line == line_amount-1:
                    if check_part_number([current_line, input_text[line-1]], int(char)):
                        is_part_number = True
                else:
                    if check_part_number([current_line, input_text[line-1], input_text[line+1]], int(char)):
                        is_part_number = True

        if is_new_number == True:
            if not current_line[char].isnumeric() or char == line_length-2:
                if is_part_number == True:
                    part_numbers.append(int(number))
                    is_part_number = False
                number = ""
                is_new_number = False
            
print(part_numbers)
print(sum(part_numbers))