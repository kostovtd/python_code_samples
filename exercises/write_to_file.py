def write_to_file(file_name, user_input):
    with open(file_name.join('.txt'), 'a') as open_file:
        open_file.write(user_input)


def main():
    file_name = input("Enter file name:")
    user_input = input("Enter something:")
    write_to_file(file_name, user_input)


if __name__ == "__main__":
    main()