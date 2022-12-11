import csv
import json
import random
from datetime import datetime
import sys

# Possibly use tabulate

# The UI and choices
def main():
    global saleja
    saleja = dict()
    load_data()
    action = int(input("Reservation: 1\nModerator: 2\nChoice: "))

    if action == 1:
        load_movies()
        movie = input("Choose a movie: ")
        reservation(movie)
        write_data()

    if action == 2:
        try:
            choice = input(
                "1. Add cinema | 2. Add a new movie\n3. See reservations | 4. Quit\nNumber: "
            )
            if choice == "1":
                add_cinema()
            elif choice == "2":
                add_movie
            elif choice == "3":
                ...
            elif choice == "4":
                write_data()
                sys.exit("Thank you for using!")
        except KeyboardInterrupt:
            write_data()
            sys.exit("Thank you!")


        write_data()


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


# Ading movies to the cinemas manually
def add_movie():
    global saleja
    for sali in saleja:
        print(sali)

    new = input("Which cinema: ")
    movie = input("Which movie: ")
    # Check if new movie in catalog
    load_movies(movie)
    time = input("At what time: ")

    max_seats = saleja[new]["seat_count"]
    saleja[new]["movies"][time] = {"movie_name": movie, "available_seats": max_seats}

    saleja[new]["movies"] = dict(sorted(saleja[new]["movies"].items()))


# Rerserving a seat in a selected show
def reservation(movie: str):
    global saleja

    playing = {}
    # Search where the chosen movie is playing
    print("Cinema: Time: Available seats")
    for sali in saleja:

        names = list(saleja[sali]["movies"].values())
        keys = list(saleja[sali]["movies"].keys())

        for i in range(len(names)):
            if movie.lower() == names[i]["movie_name"].lower():
                time = keys[i]
                print(f"{sali}: {time}: {names[i]['available_seats']}")
                playing[sali] = time

    # Picking the cinema
    while True:
        cinema = input("Pick a cinema: ")
        seat = int(input("How many seats? "))

        chosen = playing[cinema]

        if saleja[cinema]["movies"][chosen]["available_seats"] >= seat:
            saleja[cinema]["movies"][chosen]["available_seats"] -= seat
            break
        else:
            print("Not enough seats, choose again.")
            continue


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
                print(f"{movie[0]}: {movie[1]}")

        else:
            movies = [movie[0] for movie in reader][1:]
            if movie_name not in movies:
                ctlg.write(movie_name)
                ctlg.write("\n")


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
