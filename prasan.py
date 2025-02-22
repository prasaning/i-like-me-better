import time
import sys
import os
from playsound import playsound
import threading
import keyboard

def clear_console():
    """Clear the console screen based on the operating system."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def set_terminal_title(title):
    """Sets the terminal window title."""
    sys.stdout.write(f"\033]0;{title}\007")
    sys.stdout.flush()

def type_in_blue(text, speed=0.05):
    """Types out text in light blue with animation."""
    for char in text:
        sys.stdout.write(f"\033[94m{char}")
        sys.stdout.flush()
        time.sleep(speed)
    print()

def type_art_slowly(art, char_speed=0.05, line_delay=0.2):
    """Types out ASCII art with animation effect, one character at a time."""
    for char in art:
        sys.stdout.write(f"\033[94m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(char_speed)
    print()

def play_song():
    """Plays the song in the background."""
    playsound("song.mp3")

song_thread = threading.Thread(target=play_song, daemon=True)
song_thread.start()

set_terminal_title("prasan.py")
clear_console()

start_time = time.time()

lyrics = [
    (8.5, "To be young and in love in New York City"),
    (13.5, "To not know who I am, but still know that \nI'm good long as you're here with me"),
    (18.9, "To be drunk and in love in New York City"),
    (23, "Midnight into morning coffee"),
    (25.5, "Burning through the hours talking\n"),
    (28.5, "Damn,\n\nI like me better when I'm with you"),
    (34.5, "I like me better when I'm with you"),
    (39.5, "I knew from the first time"),
    (42.5, "I'd stay for a long time 'cause"),
    (45.5, "I like me better when"),
    (47.5, "I like me better when I'm with you"),
]

ascii_art = """
       .....           .....
   ,ad8PPPP88b,     ,d88PPPP8ba,
  d8P"      "Y8b, ,d8P"      "Y8b
 dP'           "8a8"           `Yd
 8(              "              )8
 I8                             8I
  Yb,                         ,dP
   "8a,                     ,a8"
     "8a,                 ,a8"
       "Yba             adP" 
         `Y8a         a8P'
           `88,     ,88'
             "8b   d8"
              "8b d8"
               `888'
                 "
"""

for timestamp, line in lyrics:
    time.sleep(max(0, timestamp - (time.time() - start_time)))
    type_in_blue(line, speed=0.05)

time.sleep(2)
type_art_slowly(ascii_art, char_speed=0.005, line_delay=0.2)
print(f"\033[94m---------------------------------------")

elapsed_time = time.time() - start_time
print(f"\033[94mProcess Done exited after {elapsed_time:.2f} seconds")
print(f"\033[94mPress any key to continue ...")

keyboard.wait()
song_thread.join()
