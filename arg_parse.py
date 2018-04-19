import argparse
'''In this project we have already set integer values and taking a command from user to do arithmetic operations like addition, subtraction, multiplication and division, module.
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--operation", help="operation", \
                        choices=["add", "subtract", "multiply","module","division"])

    args = parser.parse_args()
    n1 = 25
    n2 = 50

    print 'Number 1: ', n1
    print 'Number 2: ', n2
    print(args.operation)


    result = None
    if args.operation == "add":
        result=n1+n2
    elif args.operation == "subtract":
        result=n1-n2
    elif args.operation == "multiply":
        result=n1*n2
    elif args.operation == "module":
        result= n1%n2
    elif args.operation == "division":
        result = n1 / n2

    print 'Result: ',result