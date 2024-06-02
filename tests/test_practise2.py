def test_find_duplicates():
    # Initialize an empty dictionary to store character counts
    # char_count = {}
    # string ="osnjno"
    # # Count occurrences of each character in the string
    # for char in string:
    #     if char in char_count:
    #         char_count[char] += 1
    #     else:
    #         char_count[char] = 1
    #
    # # Initialize a variable to count duplicates
    # duplicates_count = 0
    #
    # # Print characters with counts greater than 1 (duplicates)
    # print("Duplicates:")
    # for char, count in char_count.items():
    #     if count > 1:
    #         print(f"'{char}': {count}")
    #         duplicates_count += 1
    #
    # # Print total count of duplicates
    # print("Total duplicates count:", duplicates_count)

    str=('nayaa'
         'n')
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)) :
        if str[i] != str[len(str) - i - 1]:
                print("nope")
    print("Palindrome")