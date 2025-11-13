# MY VERSION 

moovies_quantity = int(input("How many moovies are there: "))
moovies = []

def register_moovie(quantity):
    try:
        for movie in range(quantity):
            title = input("movie title: ")
            duration = int(input("movie duration: "))
            moovie_info = {
                "title" : title,
                "duration" : duration,
            }
            moovies.append(moovie_info)
    except ValueError:
        print("Enter a valid input")

register_moovie(moovies_quantity)

long = []
medium = []
short = []

def moovie_clasification(moovies):
    try:
        for movie in moovies:
            if movie["duration"] >= 150:
                long.append(movie)
            elif movie["duration"] >= 100:
                medium.append(movie)
            elif movie["duration"] <100:
                short.append(movie)
    except ValueError:
        print("Enter a valid input")        

moovie_clasification(moovies)

# CHATGPT VERSION

def register_movies(quantity):
    movies = []
    for i in range(quantity):
        try:
            title = input(f"Movie {i + 1} title: ")
            duration = int(input("Movie duration (in minutes): "))
            movie_info = {"title": title, "duration": duration}
            movies.append(movie_info)
        except ValueError:
            print("Please enter a valid number for duration.")
    return movies


def classify_movies(movies):
    categories = {"short": [], "medium": [], "long": []}

    for movie in movies:
        duration = movie["duration"]
        if duration >= 150:
            categories["long"].append(movie)
        elif duration >= 100:
            categories["medium"].append(movie)
        else:
            categories["short"].append(movie)

    return categories


def main():
    try:
        quantity = int(input("How many movies are there: "))
        movies = register_movies(quantity)
        classified = classify_movies(movies)

        print("\nShort movies:", classified["short"])
        print("Medium movies:", classified["medium"])
        print("Long movies:", classified["long"])
    except ValueError:
        print("Please enter a valid number for quantity.")


if __name__ == "__main__":
    main()

# SUMMARY OF FEEDBACK

# | **Problem**                                                           | **Fix**                                                                                      | **Why**                                                           |
# | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
# | Functions use **global lists** (`moovies`, `long`, `medium`, `short`) | Return data from each function instead of modifying global variables                         | Avoids side effects, makes the code modular and reusable          |
# | **`try/except`** is used in both functions unnecessarily              | Keep it only where you convert input to `int` (inside `register_movie`)                      | Prevents masking other errors and keeps error handling meaningful |
# | Variable names use **“moovie”** and inconsistent style                | Use correct spelling and `snake_case` naming (`register_movie`, `movie_classification`)      | Improves readability and follows Python conventions (PEP 8)       |
# | Code **runs immediately** without a main function                     | Wrap logic inside `main()` and call it with `if __name__ == "__main__":`                     | Makes your code cleaner, import-safe, and professional            |
# | Unnecessary **parentheses** in `if` conditions                        | Write `if movie["duration"] >= 150:` instead of `if (movie["duration"] >= 150):`             | Cleaner, more Pythonic syntax                                     |
# | Functions **don’t return structured results**                         | Make functions return lists or a dictionary of categories                                    | Easier to use, test, and extend later                             |
# | Raw **lists are printed** directly                                    | Add labels or formatted print statements                                                     | Makes output clearer and user-friendly                            |
# | No **type hints or validation**                                       | Add type hints (e.g., `def classify_movies(movies: list[dict]) -> dict:`) and validate input | Improves clarity and prevents type-related mistakes               |

