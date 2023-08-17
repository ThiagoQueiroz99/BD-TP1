import sys
import operator

class reducer:
  def __init__(self):
    self.H = {}

  def Reduce(self):
    for linha in sys.stdin:
      linha, cont = linha.split('\t', 1)
      cont = int(cont)
      self.H[linha] = cont
    H_ordenado = sorted(self.H.items(), key = operator.itemgetter(1), reverse = True)
    i = 0
    print("Listagem das 10 palavras que mais ocorreram:")
    for i in range(10):
      print(H_ordenado[i])
    
if __name__ == "__main__":
  doc = reducer()
  doc.Reduce()