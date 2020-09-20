SECURE = (('s', '$')), (('a', '@')), (('And', '&')),(('o','0')), (('i','1'))

def SecurePassword(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password    


if __name__ == '__main__':
    password = input("Enter a password\n")
    password = SecurePassword(password)
    print(f"your secure password is {password}")