# 8. Empresa “TecnoPlus” — Evaluación compuesta

# El usuario ingresa dos notas (0.0 - 5.0):

#     Prueba técnica (70%)
#     Prueba lógica (30%)

# Cálculo: nota_final = (tecnica * 0.7) + (logica * 0.3)

# Condiciones:

#     nota_final ≥ 3 → “Aprobado”
#     2 ≤ nota_final < 3 → “Revisión”
#     < 2 → “Reprobado”

# Validar que las notas estén en rango.

# MY VERSION

prueba_tecnica = 0.7
prueba_logica = 0.3

def total_grade(test1,test2):
    total_grade = (test1 * prueba_tecnica) +(test2 * prueba_logica)
    return total_grade

def validation (total):
    if(total >= 3):
        return "Approved"
    elif(total >= 2):
        return "Review"
    else:
        return "Rejected"
    
total = total_grade(0,5)

print(validation(total))


# CHATGPT VERSION

# Constants (good practice to define at top)
PRUEBA_TECNICA = 0.7
PRUEBA_LOGICA = 0.3

def total_grade(test1: float, test2: float) -> float:
    """Calculate the total grade based on technical and logic test weights."""
    if not (0 <= test1 <= 5) or not (0 <= test2 <= 5):
        return "Error: Scores must be between 0 and 5."
    
    total = (test1 * PRUEBA_TECNICA) + (test2 * PRUEBA_LOGICA)
    return round(total, 2)  # Round for cleaner output

def validation(total: float) -> str:
    """Return evaluation result based on total grade."""
    if isinstance(total, str):
        return total  # handles error message
    if total >= 3:
        return "Approved"
    elif total >= 2:
        return "Review"
    else:
        return "Rejected"

# Example
total = total_grade(4.0, 2.5)
print(f"Final grade: {total}")
print(validation(total))


# SUMMARY OF IMPROVEMENTS

# | Problem                                   | Fix                                                               |
# | ----------------------------------------- | ----------------------------------------------------------------- |
# | **Hardcoded weights** not clearly defined | Added constants `PRUEBA_TECNICA` and `PRUEBA_LOGICA` in uppercase |
# | **No input validation**                   | Added checks to ensure grades are between 0 and 5                 |
# | **Messy decimal output**                  | Used `round(total, 2)` for cleaner results                        |
# | **Redundant condition (`elif < 2`)**      | Simplified logic with a clean `else`                              |
# | **No documentation**                      | Added clear docstrings for both functions                         |
# | **No type hints**                         | Added type hints for better readability and IDE support           |
# | **Lacked structure and naming clarity**   | Used PEP8-compliant formatting and descriptive names              |
# | **Mixed error messages and logic**        | Handled string-based errors separately with `isinstance()` check  |
