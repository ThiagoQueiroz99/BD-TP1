import sys

class reducer:
  def Reduce(self):
    palavras_distintas = 0
    for linha in sys.stdin:
      palavra, cont = linha.split('\t', 1)
      cont = int(cont)
      if cont == 1:
        palavras_distintas += 1
    print("Quantidade de palavras distintas: ", palavras_distintas)

if __name__ == "__main__":
  doc = reducer()
  doc.Reduce()