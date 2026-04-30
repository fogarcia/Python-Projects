months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:

        date = input("Date:")

        date = date.strip()

        if "/" in date:

            date = date.replace("/", " ")
            month, day, year = date.split(" ")

            month = int(month)
            day = int(day)
            year = int(year)

            if month in months:
                month = months.index(month) + 1

            if month <= 12 and day <= 31:
                break
            else:
                continue

        elif "," in date:

            date = date.replace(",", "")
            month, day, year = date.split(" ")

            if month in months:
                month = months.index(month) + 1

            month = int(month)
            day = int(day)
            year = int(year)

            if month <= 12 and day <= 31:
                break
            else:
                continue

    except EOFError:
        continue

    except NameError:
        continue

    except ValueError:
        continue

print(f"{year:02}-{month:02}-{day:02}")