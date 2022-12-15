import csv
import json
import random
import string
import sys
import datetime

from account_system import login, print_reservation, register, update_reservation

# The UI and choices
def main():
    global saleja
    saleja = dict()
    load_data()
    while True:
        try:
            action = input("1. Login\n2. Register\n3. Quit\nChoice: ").strip().lower()
            if action == "3" or action == "quit":
                sys.exit("Quitting.")
            break
        except ValueError:
            print("Please input 1, 2 or 3.")
            continue
        except KeyboardInterrupt:
            sys.exit("Quitting.")

    if action == "1" or action == "login":
        username = login()
        if username == "admin":
            admin = True
        else:
            admin = False

    elif action == "2" or action == "register":
        username = register()
        admin = False

    else:
        sys.exit("Invalid input.")

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
    elif admin == True:
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
    if not playing:
        print("Movie not playing or not found.")
        return

    while True:
        try:
            cinema = input("Pick a cinema(number): ")
            seat = int(input("How many seats? "))
        except ValueError:
            print("Invalid input")
            return

        for key in playing:
            if cinema[0].lower() in key[0].lower():
                chosen = playing[key]
                cinema = key[3:]
                print("Ticket code:")
                print(
                    "".join(random.choices(string.ascii_letters + string.digits, k=10))
                )
                break

        if "chosen" not in locals():
            print("Cinema not found, try again.")
            continue

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
    try:
        seat_count = int(input("The seat count: "))
    except ValueError:
        print("Invalid input.")
        return

    saleja[cinema_name] = {
        "seat_count": seat_count,
        "movies": {time: data for (time, data) in populate(seat_count)},
    }

    saleja[cinema_name]["movies"] = dict(sorted(saleja[cinema_name]["movies"].items()))


# Add or modify a movie
def movie_mod(action):
    global saleja
    for sali in saleja:
        print(sali)

    new = input("Which cinema: ")
    movie = input("Which movie: ")
    time = input("At what time: ")

    try:
        max_seats = saleja[new]["seat_count"]
    except KeyError:
        print("Invalid theather name")
        return

    if action == "add":
        # Check if new movie in catalog
        load_movies(movie)

        saleja[new]["movies"][time] = {
            "movie_name": movie.title(),
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


# Print all the playing movies or write missing movie
def load_movies(movie_name=None):
    with open("movie_catalog.csv", "r+") as ctlg:
        reader = csv.reader(ctlg)

        # Prin movies
        if movie_name == None:
            for movie in reader:
                print(f"| {movie[0]} |")
                print("----------------------------------------------")

        # Write the movies into the catalog file
        else:
            movies = [movie[0].lower() for movie in reader][1:]
            if movie_name.lower() not in movies:
                ctlg.write(f"{movie_name.title()}\n")


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

        time_now = datetime.datetime.now()
        movie_start = time_now + datetime.timedelta(
            hours=random.randint(0, 24), minutes=random.randint(0, 60)
        )
        movie_end = movie_start + datetime.timedelta(
            hours=random.randint(1, 2), minutes=random.randint(0, 60)
        )

        movie = {
            "movie_name": movies[random.randint(1, len(movies) - 1)],
            "available_seats": seat_count,
        }
        yield f"{movie_start.strftime('%H:%M')}-{movie_end.strftime('%H:%M')}", movie


if __name__ == "__main__":
    main()
