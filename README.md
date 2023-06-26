# Guess the song
*A small project by Andrew Wiltshire, for school*

# Note
yes, the code sucks. could've utilised JSON more, used bcrypt to encrypt passwords, MongoDB for the user database...

But usually i dont code in python without a framework (discord.py). maybe I'll rewrite this in node.js

Also, please dont run this in IDLE. I know it will be difficult on the school computers but it wont operate as intended in IDLE

# Requirements
- Python 3 (Python 3.10 was used to create this)
- windows, mac, or any linux distro that supports the `cls` command
- It is recommended to add python to `PATH`

That's it- no python packages are used here, other than the built-in ones

# How to play
A random song name and artist are chosen. 

The artist and the first letter of each word in the song title are displayed.

The user has two chances to guess the name of the song. 

If the user guesses the answer correctly the first time, they score 3 points. If the user guesses the answer correctly the second time they score 1 point. The game repeats.

The game ends when a player guesses the song name incorrectly the second time.
