
def solution(arr):
    # create a stack
    s = list()
    flag = 1
    l1 = ['(', '{', '[']
    l2 = [')', '}', ']']

    for i in range(0, len(arr)):
        if len(arr) % 2 != 0 or arr[i] in l2 and i == 0:
            return False

        elif arr[i] in l1:
            s.append(arr[i])

        else:
            el = s.pop()

            if arr[i] == ')' and (el == '{' or el == '['):
                flag = 0

            elif arr[i] == '}' and (el == '(' or el == '['):
                flag = 0

            elif arr[i] == ']' and (el == '{' or el == '('):
                flag = 0

    if flag == 1 and len(s) == 0:
        return True
    else:
        return False





def main():
    # sample test case
    arr = ['(', ')']
    result = solution(arr)
    print(f"{result}")


if __name__ == '__main__':
    main()
