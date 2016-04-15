def char_range(char_start, char_end):
    for c in range(ord(char_start), ord(char_end) + 1):
        yield chr(c)


def read_file(file_path, list_lines):
    with open(file_path, 'r') as open_file:
        for line in open_file:
            list_lines.append(line)


def get_stats(list_lines):
    category = 'a'
    stats = {"/a/": 0}

    for x in range(0, len(list_lines)):
        if '/' + category + '/' not in list_lines[x]:
            category = chr(ord(category) + 1)
            stats['/' + category + '/'] = 1
        else:
            stats["/" + category + "/"] += 1

    return stats


def main():
    list_lines = []
    count = 0
    read_file('C:/Users/Todor/Desktop/Training_01.txt', list_lines)
    stats = get_stats(list_lines)

    for pair in stats.items():
        print(pair)


if __name__ == "__main__":
    main()