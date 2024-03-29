letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']


def algoritm_in_digits(a, ns):
    ans = []
    while a > (ns - 1):
        ans.append(a % ns)
        a //= ns
    ans.append(a)
    ans.reverse()
    answer = ""
    for i in range(len(ans)):
        if ans[i] < 10:
            answer += str(ans[i])
        elif (ans[i] >= 10) and (ans[i] <= 35):
            answer += str(letters[ans[i] - 10])
        else:
            answer = "Not enough knowledge to translate into this number system. Sorry :("
            break
    return answer


def algoritm_out_digits(a, ns):
    a = str(a)
    answer = 0
    for i in range(len(a)):
        if ('A' <= a[i]) and (a[i] <= 'Z'):
            f = letters.index(a[i])
            f += 10
        else:
            f = int(a[i])
        answer += ns ** ((len(a) - 1) - i) * f
    return answer


def in_digits():
    a = int(input("Enter your number: "))
    n = int(input("Enter the number system into which you are going to translate this number: "))
    print("Your answer:")
    print(algoritm_in_digits(a, n))


def out_digits():
    a = int(input("Enter your number: "))
    n = int(input("Enter the number system from which you are going to translate this number: "))
    print("Your answer:")
    print(algoritm_out_digits(a, n))


def calc_of_numb():
    a = int(input("Enter your first number: "))
    a_ns = int(input("Enter the number system of this number: "))
    b = int(input("Enter your second number: "))
    b_ns = int(input("Enter the number system of this number: "))
    print("In which system do you want to get the answer: ")
    s_nc = int(input())
    if a_ns != 10:
        a = algoritm_out_digits(a, a_ns)
    if b_ns != 10:
        b = algoritm_out_digits(b, b_ns)
    action = input("What action do you want to perform (+,-,*,/): ")
    error = False
    negative = False
    resalt = 0
    match action:
        case "+":
            resalt = a + b
            if s_nc != 10:
                resalt = algoritm_in_digits(resalt, s_nc)
        case "-":
            resalt = a - b
            if s_nc != 10:
                if resalt < 0:
                    resalt *= -1
                    negative = True
                    resalt = algoritm_in_digits(resalt, s_nc)
        case "*":
            resalt = a * b
            if s_nc != 10:
                resalt = algoritm_in_digits(resalt, s_nc)
        case "/":
            if b != 0:
                resalt = a // b
                if s_nc != 10:
                    resalt = algoritm_in_digits(resalt, s_nc)
            else:
                error = True
    if not error:
        if not negative:
            print("Your answer:")
            print(resalt)
        else:
            print("Negative result:", resalt)
    else:
        print("You have some kind of error in the input data. Enter the data again")


def ip_converter_in():
    ip = input("Enter your IP-address: ")
    ip = ip.split(".")
    for i in range(len(ip)):
        ip[i] = int(ip[i])
    n = input("Enter the number system into which you are going to translate this IP-address "
              "(by default, the translation will be made to the binary number system): ")
    if n == "":
        n = 2
    n = int(n)
    answer = ""
    for i in range(len(ip)):
        answer_digit = algoritm_in_digits(ip[i], n)
        if len(answer_digit) < 8:
            answer_digit = "0" * (8 - len(answer_digit)) + answer_digit
        answer += answer_digit
        if i != len(ip) - 1:
            answer += "."
    print("Your answer:")
    print(answer)


def ip_converter_out():
    ip = input("Enter your IP-address: ")
    ip = ip.split(".")
    for i in range(len(ip)):
        ip[i] = int(ip[i])
    n = input("Enter the number system from which you are going to translate this IP-address "
              "(by default, the translation will be made from the binary number system): ")
    if n == "":
        n = 2
    n = int(n)
    answer = ""
    for i in range(len(ip)):
        answer += str(algoritm_out_digits(ip[i], n))
        if i != len(ip) - 1:
            answer += "."
    print("Your answer:")
    print(answer)


def between_digits():
    a = int(input("Enter your number: "))
    a_ns = int(input("Enter the number system of this number: "))
    b_ns = int(input("Enter the number system into which you are going to translate this number: "))
    if a_ns != 10:
        a = algoritm_out_digits(a, a_ns)
    a = algoritm_in_digits(a, b_ns)
    print("Your answer:")
    print(a)


def main_program(point):
    if point > 1:
        print('\n' + '\n')
    print("What are you want?")
    print("1. Convert a number from one number system to another" + '\n' +
          "2. Convert an IP-address from one number system to another" + '\n' +
          "3. Calculate two numbers in different number systems")
    ch = int(input("> "))
    match ch:
        case 1:
            print("1) In (convert from a decimal system to another)")
            print("2) Out (convert from an any number system to decimal)")
            print("3) Between (convert from an any number system to another)")
            ch = int(input("> "))
            match ch:
                case 1:
                    in_digits()
                case 2:
                    out_digits()
                case 3:
                    between_digits()

        case 2:
            print("1) Convert IP-address from decimal to another number system")
            print("2) Convert IP-address from another number system to decimal")
            ch = int(input("> "))
            match ch:
                case 1:
                    ip_converter_in()
                case 2:
                    ip_converter_out()
        case 3:
            calc_of_numb()
        case _:
            print('\n' + "Um, you entered something wrong :(" + '\n' + "Let's try again ;)" + '\n')
            main_program(1)


if __name__ == "__main__":
    s = ''
    flag = 0
    while s != 'N' and s != 'n':
        flag += 1
        main_program(flag)
        print('\n')
        s = input("Do you want to use the program again? [Y/n] ")
    print("Bye! Have a nice day!")
