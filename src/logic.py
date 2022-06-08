import pandas as pd
from time import sleep

class Animal():
    
    def __init__(self):
        global df
        df = pd.read_csv("src/data.csv")
        self.max_stat = 100
        self.stats = [df["hungry"][0],df["thirst"][0],df["happiness"][0],df["clean"][0]]


    def write_csv(self):
        df.to_csv("src/data.csv", index=False)


    def edit_csv(self, hungry=100, thirst=100, happiness=100, clean=100):
        df["hungry"][0] = hungry
        df["thirst"][0] = thirst
        df["happiness"][0] = happiness
        df["clean"][0] = clean
        self.write_csv()


    def feed(self):
        if not df["hungry"][0] >= self.max_stat:
            df["hungry"][0] += 15
        else:
            df["hungry"][0] = self.max_stat
            self.write_csv()
        

    def drink(self):
        if not df["thirst"][0] >= self.max_stat:
            df["thirst"][0] += 25
        else:
            df["thirst"][0] = self.max_stat
            self.write_csv()
        

    def clean(self):
        if not df["clean"][0] >= self.max_stat:
            df["clean"][0] += 25
        else:
            df["clean"][0] = self.max_stat
            self.write_csv()


    def heal(self):
        while True:
            if not df["life"][0] >= self.max_stat:
                if sum(self.stats) >= (self.stats - 50):
                    df["life"][0] += 3
                    sleep(5)
            else:
                df["life"][0] = self.max_stat
                self.write_csv()
                return False
