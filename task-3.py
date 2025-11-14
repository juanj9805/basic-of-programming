# MY VERSION
from helpers import input_quantity_info,ID_generator

def gym_points(points):
    days = int(input("How many days do you train: "))
    points = { "ID": ID_generator(),
    "days":days,
    "points":points
    }
    return points

def week_asistance(weeks):
    asistance = []
    try:
        for week in range (weeks):
            days = input_quantity_info("days")
            if days >0 and days<8:
                if days >=5:
                    asistance.append(gym_points(10))
                    print("ganaste 10 puntos")
                elif days >=3:
                    asistance.append(gym_points(5))
                    print("ganaste 5 puntos")
                elif days <3:
                    asistance.append(gym_points(2))
                    print("ganaste 2 puntos")
    except ValueError:
                print("Something went wrong")
    return asistance                        

print(week_asistance(input_quantity_info("weeks")))

# def weeks_total_points(weeks):
#     week_points = weeks.
# weeks_total_points(weeks)
# CHATGPT VERSION

# from datetime import datetime

# POINTS = {
#     "high": 10,
#     "medium": 5,
#     "low": 2
# }

# def week_assistance(weeks: int) -> list[dict]:
#     """Registers weekly training performance and awards points."""
#     assistance = []

#     for week in range(1, weeks + 1):
#         try:
#             days = int(input(f"Week {week}: How many days did you train (1–7)? "))

#             if 5 <= days <= 7:
#                 earned_points = POINTS["high"]
#             elif 3 <= days < 5:
#                 earned_points = POINTS["medium"]
#             elif 1 <= days < 3:
#                 earned_points = POINTS["low"]
#             else:
#                 print("⚠️ Please enter a number between 1 and 7.")
#                 continue

#             record = {
#                 "id": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 "week": week,
#                 "days": days,
#                 "points": earned_points
#             }
#             assistance.append(record)
#             print(f"✅ You earned {earned_points} points this week!\n")

#         except ValueError:
#             print("❌ Invalid input. Please enter a number.\n")

#     return assistance


# def main():
#     try:
#         weeks = int(input("How many weeks do you train: "))
#         records = week_assistance(weeks)

#         # Total points summary
#         total_points = sum(record["points"] for record in records)
#         print("\n🏁 Training Summary:")
#         for record in records:
#             print(f"Week {record['week']}: {record['days']} days → {record['points']} points")
#         print(f"\nTotal points earned: {total_points}")

#     except ValueError:
#         print("❌ Please enter a valid number for weeks.")

# if __name__ == "__main__":
#     main()

# SUMMARY OF IMPROVEMENTS 

# | **Problem**                                                     | **Fix**                                                                         | **Why**                                                          |
# | --------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
# | The function **depends on global input** (`weeks` from outside) | Pass `weeks` as a parameter (you already do it) and call it cleanly in `main()` | Keeps the function reusable and clean                            |
# | **Repeated code** when creating and appending dictionaries      | Create the dictionary once and change only the point value dynamically          | Reduces redundancy and makes code easier to maintain             |
# | **Magic numbers** (`5`, `3`, `10`, `5`, `2`) are scattered      | Use named constants or a mapping                                                | Increases clarity and flexibility                                |
# | The **error handler** (`except ValueError`) does nothing        | Add a print or a retry mechanism inside the exception block                     | Helps users understand what went wrong                           |
# | **No validation** if `days` is outside 1–7 range                | Add `else` branch to handle invalid input                                       | Prevents wrong or missed data                                    |
# | **No separation between logic and I/O**                         | Move `input()` calls outside or into a higher-level function                    | Makes function testable (can pass days directly later)           |
# | **Timestamp readability**                                       | Use a formatted timestamp (`strftime`) instead of raw `time.time()`             | Easier to read and debug                                         |
# | **Hardcoded prints in function**                                | Print after the function returns or only for errors                             | Keeps the function pure (it should only process and return data) |
# | **No summary of results**                                       | Add a total-points counter and show a summary at the end                        | Improves user feedback                                           |

