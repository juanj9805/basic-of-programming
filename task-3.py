# 3. Gimnasio “Solo Leveling Fit” — Motivación + Bono

# Pedir cuántos días entrenó esta semana.

#     ≥ 4 días → "¡Excelente disciplina!" + gana 1 punto de energía
#     2 o 3 → "Bien, pero puedes dar más"
#     0 o 1 → "No aflojes, tú puedes mejorar"

# Mostrar mensaje y si aplica, los puntos ganados.

# MY VERSION

trainingDays = int(input("How many days do you train this week: "))

def message (days):
    if days >= 4:
        return "Excellent discipline, You just earn an energy point "
    elif days == 2 or 3:
        return "Great, But you could give more "
    elif days == 0 or 1:
        return "Don't give up, You could improve "
    else:
        return "Something went wrong"
    
print(message(trainingDays))

# CHATGPT VERSION

training_days = int(input("How many days did you train this week? "))

def motivation_message(days):
    """Return a motivational message based on the number of training days."""
    if days < 0:
        return "Invalid number of days."
    elif days >= 4:
        return "Excellent discipline! You’ve earned 1 energy point."
    elif 2 <= days <= 3:
        return "Good job, but you can push yourself a little more!"
    elif days <= 1:
        return "Don’t give up! You can improve next week."
    else:
        return "Something went wrong."

print(motivation_message(training_days))

# SUMMARY OF IMPROVEMENTS

# | Problem                               | Fix                                                  |
# | ------------------------------------- | ---------------------------------------------------- |
# | Logical error (`elif days == 2 or 3`) | Corrected with `2 <= days <= 3`                      |
# | Inconsistent grammar                  | Cleaned up and corrected                             |
# | No validation                         | Added negative number handling                       |
# | Naming style                          | Changed `message` → `motivation_message` for clarity |
# | Code readability                      | Added docstring and consistent variable naming       |

""" A docstring (short for documentation string) is a special kind of comment in Python used to describe what a function, class, or module does. """