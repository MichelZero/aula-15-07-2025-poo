#
# autor: Michel
# data: 15/07/2025

# procedure
def somar_procedure(a, b):
  valor = a + b
  print(f"total = {valor}") # o valor é impresso, o que caracteriza um procedimento

# function
def somar_function(a, b):
  valor = a + b
  return f"total = {valor}" # o valor é retornado, o que caracteriza uma function



# teste procedimento
somar_procedure(2, 3) # (a: Any, b: Any) -> None

# teste function
total = somar_function(2, 3) # (a: Any, b: Any) -> str
print(total)