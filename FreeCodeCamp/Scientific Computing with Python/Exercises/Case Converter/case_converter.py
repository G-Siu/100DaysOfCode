# Learn Python List Comprehension By Building a Case Converter Program
# Name: G Siu
# Date created: 22nd December 2023
# Date modified: 22nd December 2023

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')


def main():
    print(convert_to_snake_case('IAmAPascalCasedString '))


if __name__ == '__main__':
    main()
