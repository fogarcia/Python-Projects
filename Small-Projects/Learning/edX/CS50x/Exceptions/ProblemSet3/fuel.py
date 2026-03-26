while True:
    try:

        fuel = input("Fraction: ")

        fuel = fuel.split("/")

        n = int(fuel[0])
        d = int(fuel[1])

        if round(n/d * 100) > 100:
            continue
        elif n < 0 or d < 0:
            continue
        elif n/d == 1 or round(n/d * 100) == 99:
            print("F")
            break
        elif n/d == 0 or round(n/d * 100) == 1:
            print("E")
            break
        else:
            print(f"{round(n/d * 100)}%")
            break

    except ValueError:
        continue
    except ZeroDivisionError:
        continue