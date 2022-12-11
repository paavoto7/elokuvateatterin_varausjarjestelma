import csv
from getpass import getpass


def register():
    while True:
        username = input("Username: ")
        if len(username) < 4:
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


if __name__ == "__main__":
    # register()
    # login()
    update_reservation("kukka", ["moi"])
