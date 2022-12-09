import random
from datetime import datetime
import json
import csv


class Sali:
    def __init__(self, name, seat_count, available_seats, movie_name="Default"):
        self.name = name
        self.seat_count = seat_count
        self.available_seats = available_seats
        #self.time = f"{datetime.now().hour}:{datetime.now().minute:02d}"
        
        self.movie(movie_name)

    
    def movie(self, elokuva):
        with open("movie_catalog.csv", "r") as catalog:
            if elokuva == "Default":
                ...
            else:  
                self.movie_name = elokuva
    
    def __str__(self) -> str:
        return f"{self.name}"


if __name__ == "__main__":
    with open("database.json", "r") as dbr:
        #x = json.load(dbr)
        #print(x)


        """for row in dbr:
            x = json.loads(row)
            n = Sali(**x)
            n.seat_count = random.randint(10,100)
            print(n.seat_count)"""


    with open("database.json", "a") as db:
        s = Sali("good", 44, 5, "Toy Story")
        print(s.__dict__)
        #db.write(json.dumps(s.__dict__))
        json.dump(s.__dict__, db, indent=4)
        db.write("\n")
        """fieldnames = ["name", "seat_count", "available_seats", "movie_name"]
        writer = csv.DictWriter(db, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(10):
            writer.writerow(s.__dict__)"""