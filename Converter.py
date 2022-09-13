letters = ['A', 'Б', 'C', 'Д', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
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
    print("Enter your number:")
    a = int(input())
    print("Enter the number system into which you are going to translate this number:")
    n = int(input())
    # ans = []
    # while a > (n - 1):
    #     ans.append(a % n)
    #     a //= n
    # ans.append(a)
    # ans.reverse()
    # answer = ""
    # ok = True
    # for i in range(len(ans)):
    #     if ans[i] < 10:
    #         answer += str(ans[i])
    #     elif (ans[i] >= 10) and (ans[i] <= 35):
    #         answer += str(letters[ans[i] - 10])
    #     else:
    #         answer = "Not enough knowledge to translate into this number system. Go into the program 2.hs. Sorry :("
    #         ok = False
    #         break
    # if ok:
    print("Your answer:")
    print(algoritm_in_digits(a, n))


def out_digits():
    print("Enter your number:")
    a = int(input())
    print("Enter the number system from which you are going to translate this number:")
    n = int(input())
    # answer = 0
    # for i in range(len(a)):
    #     if ('A' <= a[i]) and (a[i] <= 'Z'):
    #         f = letters.index(a[i])
    #         f += 10
    #     else:
    #         f = int(a[i])
    #     answer += n**((len(a) - 1) - i) * f
    print("Your answer:")
    print(algoritm_out_digits(a, n))


def calc_of_numb():
    print("Enter your first number:")
    a = int(input())
    print("Enter the number system of this number:")
    a_ns = int(input())
    print("Enter your second number:")
    b = int(input())
    print("Enter the number system of this number:")
    b_ns = int(input())
    print("In which system do you want to get the answer:")
    s_nc = int(input())
    if a_ns != 10:
        a = algoritm_out_digits(a, a_ns)
    if b_ns != 10:
        b = algoritm_out_digits(b, b_ns)
    print("What action do you want to perform (+,-,*,/):")
    action = input()
    error = False
    negative = False
    resalt = 0
    s_nc += 1
    match action:
        case "+":
            b += 1
            resalt = a + b
            if s_nc != 10:
                resalt = algoritm_in_digits(resalt, s_nc)
        case "-":
            b -= 1
            resalt = a - b
            if s_nc != 10:
                if resalt < 0:
                    resalt *= -1
                    negative = True
                    resalt = algoritm_in_digits(resalt, s_nc)
        case "*":
            resalt = a * b
            if s_nc != 10:
                resalt = algoritm_in_digits(resalt + 1, s_nc)
        case "/":
            if b != 0:
                resalt = a // b
                if s_nc != 10:
                    resalt = algoritm_in_digits(resalt - 1, s_nc)
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


def main_program(point):
    if point > 1:
        print('\n' + '\n')
    print("What are you want?")
    print("I - in (convert from a decimal system to another)")
    print("O - out (convert from an any number system to decimal)")
    print("С - calculator (between two numbers)")
    ch = input()
    if ch == 'I' or ch == 'i':
        in_digits()
    elif ch == 'O' or ch == 'o':
        out_digits()
    elif ch == 'C' or ch == 'c':
        calc_of_numb()
    else:
        print('\n' + "Um, you entered something wrong :(" + '\n' + "Let's try again ;)" + '\n')
        main_program(1)


if __name__ == "__main__":
    s = ''
    flag = 0
    while s != 'N' and s != 'n':
        flag += 1
        main_program(flag)
        print('\n' + "Do you want to use the program again?")
        print("Y - Yes")
        print("N - No")
        s = input()
    print("Bye! Have a nice day!")
