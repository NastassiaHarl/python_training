def trim_and_repeat(text, offset=0, repetitions=1):
    return f'{text[offset:] * repetitions}'

print(trim_and_repeat("python", repetitions=3))



def is_palindrome(world):
    return world == world[::-1]

print(is_palindrome('woloW'))



def guess_number(number):
    if number == 42:
        return 'You win!'
    return 'Try again!'

print(guess_number(42))


def normalize_url(adress):
    if adress[:8] == 'https://':
        return adress
    else:
        if adress[:7] == 'http://':
            return f"https://{adress[7:]}"
        else:
            return f"https://{adress}"

print(normalize_url('http://ai.fi'))

def print_numbers(numbers):
    i = 4
    while i >= numbers:
        print(i)
        i = i - 1
    print('finished!')

print_numbers(1)

def print_numbers(last_number):
    i = 1
    while i <= last_number:
        print(i)
        i = i + 1
    print('finished!')

print_numbers(3)

def multiply_numbers_from_range(start, finish):
    i = start
    multiply = 1
    while i <= finish:
        multiply = multiply * i
        i = i + 1
    return multiply

print(multiply_numbers_from_range(2, 3))



def join_numbers_from_range(numbers, times):
    result = ''
    i = numbers
    while i <= times:
        result = result + str(i)
        i = i + 1
    return result

print(join_numbers_from_range(5, 10))

def repeat(text, times):
    result = ''
    i = 1
    while i <= times:
        result = result + text
        i = i + 1
    return result

def print_reversed_word_by_symbol(word):
    i = len(word) - 1
    while i >= 0:
        print(word[i])
        i = i - 1

# word = 'Hexlet'
print_reversed_word_by_symbol('Hexlet')

def print_name_by_symbol(name):
    i = 0
    while i < len(name):
        print(name[i])
        i = i + 1

name = 'Arya'
print_name_by_symbol(name)

def count_chars(string, char):
    lowerstring = string.lower()
    index = 0
    count = 0
    while index < len(lowerstring):
        if lowerstring[index] == char:
            # Считаем только подходящие символы
            count = count + 1
        # Счётчик увеличивается в любом случае
        index = index + 1
    return count
print(count_chars('HexlEt', 'e'))

def reverse_string(string, index):
    index = 0
    string = ''

    while index >= 0:
        current_char = string[index]
        reversed_string = reversed_string + current_char
        # То же самое через интерполяцию
        # reversed_string = f"{reversed_string}{current_char}"
        index = index - 1

    return reversed_string

reverse_string('Game Of Thrones') # 'senorhT fO emaG'
# Проверка нейтрального элемента
reverse_string('') # ''

def my_substr(string, numbers):
    return f"{string[:numbers]}"

print(my_substr('If I look back I am lost', 7))

def my_substr(string, length):
    result_string = ''
    index = 0
    while index < length:
        result_string = result_string + string[index]
        index = index + 1

    return result_string