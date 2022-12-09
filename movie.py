import json
import csv

# Possibly use tabulate


def main():
    global saleja
    saleja = dict()
    load_data()
    action = int(input("Reservation: 1\nModerator: 2\nChoice: "))

    if action == 1:
        display_movies()
        movie = input("Choose a movie: ")
        reservation(movie)


def load_data():
    global saleja
    saleja.clear()
    with open("database.json", "r") as db:
        dat = json.load(db)
        # print(dat)
        for sali in dat:
            saleja[sali["name"]] = [
                sali["seat_count"],
                sali["movies"],
            ]
        #print(saleja)
        print(saleja["g33ood"])

        """reader = csv.reader(db)
        next(reader)
        #saleja[fields['name']] = [fields["available_seats"], fields["movie_name"].lower()]
        for row in reader:
            saleja[row[0]] = [int(row[1]), int(row[2]), row[3]]
        print(saleja)"""


def add_cinema(nimi, koko):
    ...


def add_movie():
    ...


def reservation(movie: str):
    global saleja

    playing = {}
    # Search where the chosen movie is playing
    print("Cinema: Time: Available seats")
    for sali in saleja:
        cin = saleja[sali]
        name = list(cin[1].values())

        for i in range(len(name)):
            if movie.lower() == name[i]["movie_name"].lower():
                time = list(cin[1].keys())[i]
                print(f"{sali}: {time}: {name[i]['available_seats']}")
                playing[sali] = time

    while True:
        cinema = input("Pick a cinema: ")
        seat = int(input("How many seats? "))

        chosen = playing[cinema]

        if saleja[cinema][1][chosen]["available_seats"] >= seat:
            saleja[cinema][1][chosen]["available_seats"] -= seat
            break
        else:
            print("Not enough seats, choose again.")
            continue


def write_data():
    global saleja
    with open("database.json", "w") as out:
        fieldnames = ["name", "seat_count", "available_seats", "movie_name"]
        for nimi in saleja:
            ...


def display_movies():
    with open("movie_catalog.csv", "r") as ctlg:
        reader = csv.reader(ctlg)
        for movie in reader:
            print(f"{movie[0]}: {movie[1]}")


def update():
    global saleja
    """Update the movies if enough time has passed.
    Update the seats if movie ended."""


if __name__ == "__main__":
    main()
