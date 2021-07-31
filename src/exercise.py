def main():
    #write your code below this line
    names = []

    while True:
        name = input()

        if name == '':
            break

        names.append(name)
    
    print(names[0])
    print(names[-1])

if __name__ == '__main__':
    main()
