#
# autor: Michel
# data: 15/07/2025

def IMC(peso: float, altura: float):
  """
Calcula IMC
  Args:
      peso (float): o peso da pessoa
      altura (float): a altura da pessoa
  Returns:
      float: o valor calculado do IMC
  """
  valor = peso / (altura ** 2) # altura * altura
  return valor

# testes:
pessoa = IMC(80, 1.72)
print(f"IMC: {pessoa:.2f}")
# ajuda: https://docs.python.org/3/library/functions.html#help
help(IMC)