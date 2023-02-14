def input_or_file() -> bool:
    """Selecting a text input method."""
    print('"0" - for standard input;')
    print('"1" - for input from a text file;')
    select: str = input('--> ')
    tuple_select: tuple = ('0', '1', 'exit')
    select_return: bool = False
    while True:
        if select not in tuple_select:
            print(f'You entered "{select}", please enter "0" or "1".')
            select: str = input('--> ')
        elif select == '1':
            select_return: bool = True
            break
        elif select == '0':
            break
        elif select == 'exit':
            quit()
    return select_return


def input_text() -> list:
    """
    Reads text from the input and strips it of spaces.
    Returns a list of elements.
    """
    list_for_txt: list = list()
    while True:
        string: str = input().replace(' ', '')
        if string.strip() == '':
            break
        else:
            list_for_txt.extend(list(string))
    return list_for_txt


def file_text() -> list:
    """
    Reads text from a file and strips it of spaces.
    Returns a list of elements.
    """


def handler_list_elem(list_elem: list) -> list:
    """
    The handler for the received list of elements.
    Returns the end result.
    """
    list_elem_copy: list = list_elem.copy()
    string: str = ''.join(list_elem)
    string_non_full: str = ''.join(sorted(list(set(list_elem_copy))))
    list_elem.clear()
    for i in string_non_full:
        list_elem.append(string.count(i))
    print(list_elem)
    list_elem_copy.clear()
    list_elem_copy.append([])
    list_elem_copy[0].extend(string_non_full)
    list_elem_copy.append([])
    for i in range(1, max(list_elem) + 1):
        for j in range(len(string_non_full)):
            if list_elem[j] > 0:
                list_elem_copy[i].append('@')
                list_elem[j] = list_elem[j] - 1
            else:
                list_elem_copy[i].append(' ')
        list_elem_copy.append([])
    list_elem_copy.pop()
    list_elem.clear()
    list_elem = list(reversed(list_elem_copy))
    return list_elem


def output_result(list_elem: list) -> None:
    """
    Outputs the result to the console and a file with the .txt format.
    """
    for elem in list_elem:
        print(*elem)

def main() -> None:
    """The main logic of work."""
    option: bool = input_or_file()
    if option:
        list_elem: list = input_text()
    else:
        list_elem: list = file_text()
    result: list = handler_list_elem(list_elem)
    output_result(result)

if __name__ == '__main__':
    main()