def palindrome(str):
    user_input = input("Enter a word: ")
    u_input = user_input.replace(" ", "")
    u_input = u_input.lower()
    if u_input == u_input[::-1]:
        return True
    else:
        return False

def main():
    return


if __name__ == '__main__':
    main()