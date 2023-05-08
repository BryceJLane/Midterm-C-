def print_binary_strings(pattern, index):
    if index == len(pattern):
        print(''.join(pattern))
        return

    if pattern[index] == '?':
        for char in '01':
            pattern[index] = char
            print_binary_strings(pattern, index + 1)
            pattern[index] = '?'
    else:
        print_binary_strings(pattern, index + 1)

if __name__ == "__main__":
    example_pattern = ['0', '?', '1', '?']
    print_binary_strings(example_pattern, 0)
