# made with python 3.10.5
import json
import os
import random
import time
from os import path
import getpass
from typing import List

"""
I don't know if there is an easier way to do this, but this system that i designed resets the screen,
while printing all strings passed in the list parameter. (defaulting to bus)

Designed by me, might turn it into a python package.
"""

title = [
    "---------------------------------------------",
    "Welcome to Guess The Song",
    "A small project by Andrew Wiltshire",
    "---------------------------------------------",
    ""
]

bus = title  # default value of bus is title because the title will be shown at the beginning


# Recommended to run in regular OS terminal client
def clearScreen(text=bus):
    if os.name == "nt":  # If on Windows, use the cls command (clears screen)
        os.system("cls")
    else:  # otherwise, use the clear command (also clears screen, on Mac and linux)
        os.system("clear")

    for item in text:
        print(item)


clearScreen()
directory = path.join(__file__, "..")

# Enums
HIGH_SCORE = "highscore"
PASSWORD = "password"


# JSON is something I struggle with (I usually use MongoDB in node.js) so this code probably sucks
class User:
    # Avoid having to read the actual JSON file as much as possible
    full_obj: json = None
    obj: json = None

    username = ""
    score = 0
    gameOver = False

    def __init__(self):
        self.auth()
        bus.clear()
        for l in title:
            bus.append(l)
        self.deserialize()

    def deserialize(self):
        with open(path.join(directory, "./data/users.json"), "r") as f:
            self.full_obj = json.load(f)
            self.obj = self.full_obj[self.username]

    def serialize(self):
        with open(path.join(directory, "./data/users.json"), "w") as f:
            self.full_obj[self.username] = self.obj
            json.dump(self.full_obj, f, indent=4)

    def auth(self, index: int = 0):
        index += 1
        with open(path.join(directory, "./data/users.json"), "r") as f:
            data = json.load(f)
            if index == 1:
                print("Log in or create an account")
            else:
                clearScreen(bus + ["Incorrect credentials. Try again", " ", "Log in or create an account"])

            username = input("username: ")
            try:
                u = data[username]
                bus.append("Log in")
                bus.append(f"username: {username}")
                clearScreen()
                p = getpass.getpass("password: ")
                if p != u[PASSWORD]:
                    bus.clear()
                    clearScreen()
                    self.auth(index)
                self.username = username
                return data


            except KeyError:
                bus.append("Create account")
                bus.append(f"username: {username}")
                p = getpass.getpass("password: ")
                with open(path.join(directory, "./data/users.json"), "w") as wf:
                    data[username] = {}
                    data[username]["password"] = p
                    data[username]["highscore"] = 0
                    json.dump(data, wf, indent=4)
                self.username = username
                bus.clear()
                return data


user = User()
bus = title
clearScreen()

# JSON is better but I don't care.
f = open(path.join(directory, "./data/songs.txt"))  # doesn't matter what the working directory is
lines = f.read().splitlines()

gameOver = False

score = 0


def play(num: int = None, index: int = 1):
    clearScreen()
    if num is None:
        num = random.randrange(0, 11, 2)

    name = lines[num]
    artist = lines[num + 1]

    l = name.upper().split(" ")
    first_letters = []
    for i in l:
        first_letters.append(i[0])

    print(f"--------------------\nName?:\t{' '.join(first_letters)}\nArtist:\t{artist}\n--------------------")
    ans = input("\nSong Name: ").lower()
    if ans == name.lower():
        if index == 1:
            bus.append(
                f"----------------------------------------------\n{name:<25} | {artist:>15} 🟢\n----------------------------------------------")
            clearScreen(["You are"])
            time.sleep(0.25)
            clearScreen(["You are."])
            time.sleep(0.25)
            clearScreen(["You are.."])
            time.sleep(0.25)
            clearScreen(["You are..."])
            time.sleep(0.25)
            clearScreen(["You are"])
            time.sleep(1)
            clearScreen(["You are CORRECT! +3 points"])
            time.sleep(0.25)
            clearScreen(["You are CORRECT! +3 points", "Well done"])
            user.score += 3
            time.sleep(0.75)
        else:
            bus.append(
                f"----------------------------------------------\n{name:<25} | {artist:>15} 🟡\n----------------------------------------------")
            clearScreen(["You are"])
            time.sleep(0.25)
            clearScreen(["You are."])
            time.sleep(0.25)
            clearScreen(["You are.."])
            time.sleep(0.25)
            clearScreen(["You are..."])
            time.sleep(0.25)
            clearScreen(["You are"])
            time.sleep(1)
            user.score += 1
            clearScreen(["You are Correct! +1 point"])
            time.sleep(0.25)
            clearScreen(["You are Correct! +1 point", "Persistence is key"])
            time.sleep(0.75)
    else:
        if index == 1:
            clearScreen(["You are"])
            time.sleep(0.25)
            clearScreen(["You are."])
            time.sleep(0.25)
            clearScreen(["You are.."])
            time.sleep(0.25)
            clearScreen(["You are..."])
            time.sleep(0.25)
            clearScreen(["You are"])
            time.sleep(1)
            clearScreen(["You are INCORRECT!"])
            time.sleep(0.25)
            clearScreen(["You are INCORRECT!", "Try again"])
            time.sleep(0.75)
            play(num, 2)

        else:
            bus.append(
                f"----------------------------------------------\n{name:<25} | {artist:>15} 🔴\n----------------------------------------------")
            clearScreen(["You are"])
            time.sleep(0.25)
            clearScreen(["You are."])
            time.sleep(0.25)
            clearScreen(["You are.."])
            time.sleep(0.25)
            clearScreen(["You are..."])
            time.sleep(0.25)
            clearScreen(["You are"])
            time.sleep(1)
            clearScreen(["You are INCORRECT!"])
            time.sleep(0.25)
            clearScreen(["You are INCORRECT!", "Again."])
            time.sleep(1)
            user.gameOver = True


def menu(plays=0, new_highscore=False):
    print("---------------------------------------------")
    if (plays > 0):
        s = f"""{"Score: " + str(user.score):<11}{"HighScore: " + str(user.obj[HIGH_SCORE]):>25}"""
        if new_highscore:
            s = " ".join([s, "(NEW!)"])
        print(s)
        print("\nWhat would you like to do next?")
        print("P: Play again")
        print("L: Leaderboard")
        print("Q: Quit")
    else:
        print(f"""{"HighScore: " + str(user.obj[HIGH_SCORE]):>43}\n""")
        print("P: Play")
        print("L: Leaderboard")
        print("Q: Quit (don't even think about it)")
    print("---------------------------------------------")
    inp = input(">> ").lower()
    if inp == "p":
        pass
    if inp == "l":
        leader()
    if inp == "q":
        quit()


def leader():
    clearScreen()
    user.deserialize()  # ensure the loaded dict is up to date
    res = sorted(user.full_obj.items(), key=lambda items: -items[1][HIGH_SCORE])

    print("---------------------------------------------")

    i = 0
    for pl in res:
        i += 1
        if i <= 5 or pl[0] == user.username:
            if (pl[1][HIGH_SCORE] > 0):
                print(f"{i}: {pl[0]:<20}{pl[1][HIGH_SCORE]:>18}")
    print("---------------------------------------------")
    getpass.getpass("Enter to go back to menu... ")
    clearScreen()
    menu()


_ = 0
new_highscore = False
while True:
    menu(_, new_highscore)
    user.score = 0
    user.gameOver = False
    bus.clear()
    while not user.gameOver:
        play()
        if user.score > user.obj[HIGH_SCORE]:
            user.obj[HIGH_SCORE] = user.score
            user.serialize()
            new_highscore = True

    _ += 1
    clearScreen(["GAME."])
    time.sleep(0.25)
    clearScreen(["GAME. OVER.\n"])
    time.sleep(1)
