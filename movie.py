import csv
import json
import random
import string
import sys
from datetime import datetime

from account_system import login, print_reservation, register, update_reservation

# Possibly use tabulate

# The UI and choices
def main():
    global saleja
    saleja = dict()
    load_data()
    action = int(input("1. Login\n2. Register\nChoice: "))

    if action == 1:
        username = login()
        if username == "admin":
            admin = True
        else:
            admin = False

    if action == 2:
        username = register()
        admin = False

    # User mode
    if admin == False:
        try:
            # Display the movies
            load_movies()
            movie = input("Choose a movie: ")
            # Reserve a movie seat
            res = reservation(movie)
            # Write the data into the "database"
            write_data()
            # Save the reservation to the account "database"
            update_reservation(username, res)
            sys.exit("Thank you for reservation!")
        except KeyboardInterrupt:
            sys.exit("\nThank you for choosing us!")

    # Admin mode
    if admin == True:
        print("Administrator mode activated")
        while True:
            try:
                choice = input(
                    "1. Add cinema | 2. Add a movie\n3. Delete a movie | 4. See reservations\n5. See playing movies | 6. Quit\nNumber: "
                )
                if choice == "1":
                    add_cinema()
                elif choice == "2":
                    movie_mod("add")
                elif choice == "3":
                    print_playing()
                    movie_mod("delete")
                elif choice == "4":
                    print_reservation()
                elif choice == "5":
                    print_playing()
                elif choice == "6":
                    write_data()
                    sys.exit("Logged out!")

            except KeyboardInterrupt:
                write_data()
                sys.exit("\nLogged out!")


# Rerserving a seat in a selected show
def reservation(movie: str):
    global saleja

    playing = {}
    ord_num = 1
    # Search where the chosen movie is playing
    print("Cinema: Time: Available seats")
    for sali in saleja:

        names = list(saleja[sali]["movies"].values())
        keys = list(saleja[sali]["movies"].keys())

        for i in range(len(names)):
            if movie.lower() in names[i]["movie_name"].lower():
                time = keys[i]
                print(f"{ord_num}. {sali}: {time}: {names[i]['available_seats']}")
                playing[f"{ord_num}. {sali}"] = time
                ord_num += 1

    # Picking the cinema
    while True:
        cinema = input("Pick a cinema(number): ")
        seat = int(input("How many seats? "))

        for key in playing:
            if cinema[0].lower() in key[0].lower():
                chosen = playing[key]
                cinema = key[3:]
                print("Ticket code:")
                print(
                    "".join(random.choices(string.ascii_letters + string.digits, k=10))
                )
                break

        if saleja[cinema]["movies"][chosen]["available_seats"] >= seat:
            saleja[cinema]["movies"][chosen]["available_seats"] -= seat

            movie_name = saleja[cinema]["movies"][chosen]["movie_name"]
            return [cinema, chosen, movie_name, seat]
        else:
            print("Not enough seats, choose again.")
            continue


# Loading the data to memory
def load_data():
    global saleja
    saleja.clear()
    with open("database.json", "r") as db:
        saleja = json.load(db)


# Adding a cinema
def add_cinema():
    global saleja
    cinema_name = input("The name of the new cinema: ")
    seat_count = int(input("The seat count: "))

    saleja[cinema_name] = {
        "seat_count": seat_count,
        "movies": {time: data for (time, data) in populate(seat_count)},
    }


# Add or modify a movie
def movie_mod(action):
    global saleja
    for sali in saleja:
        print(sali)

    new = input("Which cinema: ")
    movie = input("Which movie: ")
    time = input("At what time: ")

    max_seats = saleja[new]["seat_count"]

    if action == "add":
        # Check if new movie in catalog
        load_movies(movie)

        saleja[new]["movies"][time] = {
            "movie_name": movie,
            "available_seats": max_seats,
        }

        saleja[new]["movies"] = dict(sorted(saleja[new]["movies"].items()))

    elif action == "delete":
        saleja[new]["movies"].pop(time)


def write_data():
    global saleja
    with open("database.json", "w") as out:
        json.dump(saleja, out, indent=4)
        out.write("\n")


# Print or return all the playing movies
def load_movies(movie_name=None):
    with open("movie_catalog.csv", "r+") as ctlg:
        reader = csv.reader(ctlg)

        if movie_name == None:
            for movie in reader:
                print(f"| {movie[0]} | {movie[1]} |")
                print("----------------------------------------------")

        else:
            movies = [movie[0] for movie in reader][1:]
            if movie_name not in movies:
                ctlg.write(movie_name)
                ctlg.write("\n")


def print_playing():
    global saleja
    for sali in saleja:
        print(f"| {sali} |")
        for time in saleja[sali]["movies"]:
            print(f"| {time} | {saleja[sali]['movies'][time]['movie_name']} |")
        print("--------------------------------")


# Implement automatic mechanism to change movies if enough time
def update():
    global saleja
    time_now = f"{datetime.now().hour}:{datetime.now().minute:02d}"
    test_time = "20"

    for cinema in saleja:
        for time in saleja[cinema]["movies"]:
            if int(time[:2]) <= int(test_time):
                print(time[:2])
                # Use the populate function


# Populating the new cinemas randomly
def populate(seat_count):
    movies = list()
    # Read the available movies into a list
    with open("movie_catalog.csv", "r") as lista:
        reader = csv.reader(lista)
        for movie in reader:
            movies.append(movie[0])

    # Yield the values back to the dictionary comprehension
    for i in range(5):
        time = random.randint(0, 24)
        movie = {
            "movie_name": movies[random.randint(1, 4)],
            "available_seats": seat_count,
        }
        yield time, movie


if __name__ == "__main__":
    main()
