import csv
from getpass import getpass


def register():
    while True:
        username = input("Username: ")
        if len(username) < 4 or username == "admin":
            print("Too short.")
            continue
        else:
            break

    while True:
        password = getpass()
        password2 = getpass("Repeat password: ")

        if len(password) < 4:
            print("Too short.")
            continue
        elif password != password2:
            print("Passwords don't match.")
            continue
        else:
            break

    with open("credidentials.csv", "a") as cred:
        cred.write(f"{username},{password},[reservation]\n")
    return username


def login():
    with open("credidentials.csv", "r") as credidentials:
        creds = dict()
        reader = csv.reader(credidentials)
        for line in reader:
            creds[line[0]] = {"password": line[1], "reservation": line[2]}

        while True:
            username = input("Username: ")
            if username not in creds:
                print("Wrong username, try again.")
                continue
            else:
                break

        while True:
            password = getpass()
            if password != creds[username]["password"]:
                print("Invalid password, try again.")
                continue
            else:
                break
        print("Login successful!")
        return username


def update_reservation(name, res):
    with open("credidentials.csv", "r") as into:
        reader = csv.reader(into)
        new = list()
        for line in reader:
            if name == line[0]:
                line[2] = res
            new.append(line)
        with open("credidentials.csv", "w") as out:
            outter = csv.writer(out)
            outter.writerows(new)


def print_reservation():
    with open("credidentials.csv", "r") as reservations:
        reader = csv.reader(reservations)
        next(reader)
        print(f"| Username | Cinema | Time | Movie | Seat(s) |")
        print("----------------------------------------------")
        for line in reader:
            res = line[2].strip("[]").replace("'", "").split(", ")
            try:
                print(f"| {line[0]} | {res[0]} | {res[1]} | {res[2]} | {res[3]} |")
                print("----------------------------------------------")
            except IndexError:
                continue


if __name__ == "__main__":
    print("Try: python3 movie.py")
