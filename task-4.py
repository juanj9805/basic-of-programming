# MY VERSION

from helpers import input_quantity_info,ID_generator,input_name

songs_quantity = int(input("How many songs do you want to register: "))

def register_songs(quantity):
    songs_info = []
    for song in range(quantity):
        song_ID = time.time()
        song_title = input("What is the song title: ")
        song_genre = input("What is the musical genre: ")
        song_info = {
            "ID":song_ID,
            "title":song_title,
            "genre":song_genre 
            }
        
        songs_info.append(song_info)
    return songs_info

# print(register_songs(songs_quantity))

def unique_genres(songs_info):
    genres = []
    unique_genres = set(genres)
    for song in songs_info:
        genre = song["genre"]    
        genres.append(genre)
    return unique_genres

print(unique_genres(register_songs()))

# CHATGPT VERSION

# import time
# import uuid

# def register_songs(quantity):
#     """Registers a number of songs with title and genre."""
#     songs_info = []
#     for i in range(quantity):
#         print(f"\n--- Song {i + 1} ---")
#         song_ID = uuid.uuid4()  # safer unique ID
#         song_title = input("What is the song title: ").strip()
#         song_genre = input("What is the musical genre: ").strip()
        
#         song_info = {"ID": song_ID, "title": song_title, "genre": song_genre}
#         songs_info.append(song_info)
#     return songs_info


# def unique_genres(songs_info):
#     """Extracts unique genres from a list of song dictionaries."""
#     genres = [song["genre"] for song in songs_info]
#     unique_genres_set = set(genres)
#     return unique_genres_set


# def main():
#     songs_quantity = int(input("How many songs do you want to register: "))
#     songs = register_songs(songs_quantity)
#     print("\nUnique genres:", unique_genres(songs))


# if __name__ == "__main__":
#     main()

# SUMMARY OF IMPROVEMENTS

# | **Problem**                                                                                               | **Fix**                                                                                  | **Why**                                                                   |
# | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
# | You’re using `songs_quantity` inside `register_songs()` instead of the **function parameter** `quantity`. | Change `for song in range(songs_quantity):` → `for song in range(quantity):`             | It breaks the idea of reusable functions — you’re ignoring the parameter. |
# | You generate an **ID** using `time.time()`, which can produce **duplicates** if inputs are very fast.     | Use `time.time_ns()` (nanoseconds) or Python’s built-in `uuid` library (`uuid.uuid4()`). | Ensures truly unique IDs.                                                 |
# | In `unique_genres()`, you create a list, then convert it to a set **on every loop iteration**.            | Move `unique_genres = set(genres)` *outside* the loop.                                   | Creating the set each time wastes resources and is logically redundant.   |
# | Variable `unique_genres` inside the function **shadows** the function name.                               | Rename it, e.g., `unique_genres_set = set(genres)`                                       | Prevents confusion and potential naming conflicts.                        |
# | You don’t validate inputs (e.g., blank title or genre).                                                   | Add basic input checks or `.strip()` to clean input strings.                             | Prevents empty or messy data.                                             |
# | No docstrings or comments.                                                                                | Add short docstrings above each function explaining its purpose.                         | Improves readability and professionalism.                                 |
# | `register_songs()` prints nothing when collecting — might confuse users.                                  | Add progress messages like `print(f"--- Song {i+1} ---")`                                | Gives feedback during data entry.                                         |
