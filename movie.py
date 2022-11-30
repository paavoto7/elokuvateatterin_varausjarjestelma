import json
import csv
# Possibly use tabulate

def main():
    load_data()
    action = int(input("Reservation: 1\nModerator: 2\nChoice: "))

    if action == 1:
        dis_movies()
        movie = input("Choose a movie: ")
        reservation(movie)


def load_data():
    global saleja
    saleja = dict()
    with open("database.json", "r") as db:
        for row in db:
            params = json.loads(row)
            saleja[params['name']] = [params["available_seats"], params["movie_name"].lower()]


def add_cinema(nimi, koko):
    ...


def add_movie():
    ...


def reservation(movie: str):
    global saleja
    
    playing = {}
    # Search where the chosen movie is playing
    print("Cinema: Available seats")
    for sali in saleja:
        if movie.lower() in saleja[sali]:
            print(f"{sali}: {saleja[sali][0]}")
    
    seat = input("Pick a cinema: ")
    




def dis_movies():
    with open("movie_catalog.csv", "r") as ctlg:
        reader = csv.reader(ctlg)
        for movie in reader:
            print(f"{movie[0]}: {movie[1]}")


if __name__ == "__main__":
    main()