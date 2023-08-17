import sys

class reducer:
  def __init__(self):
    self.H = {}  
    self.classe = [0] * 10                                  #10 classes para o histograma

  def Reduce(self):
    for linha in sys.stdin:
        linha, cont = linha.split('\t', 1)
        cont = int(cont)
        self.H[linha] = cont
    for word in self.H:
      if self.H[word] >= 1 and self.H[word] <= 39:        #classe 1
        self.classe[0] += 1
      elif self.H[word] >= 40 and self.H[word] <= 59:     #classe 2
        self.classe[1] += 1
      elif self.H[word] >= 60 and self.H[word] <= 79:     #classe 3
        self.classe[2] += 1
      elif self.H[word] >= 80 and self.H[word] <= 99:     #classe 4
        self.classe[3] += 1
      elif self.H[word] >= 100 and self.H[word] <= 199:   #classe 5
        self.classe[4] += 1
      elif self.H[word] >= 200 and self.H[word] <= 299:   #classe 6
        self.classe[5] += 1
      elif self.H[word] >= 300 and self.H[word] <= 399:   #classe 7
        self.classe[6] += 1
      elif self.H[word] >= 400 and self.H[word] <= 499:   #classe 8
        self.classe[7] += 1
      elif self.H[word] >= 500 and self.H[word] <= 599:   #classe 9
        self.classe[8] += 1
      elif self.H[word] > 600:                            #classe 10
        self.classe[9] += 1

  def Impressao(self):        
    print("Palavras dentro do invervalo de ocorrencia 1 - 39: ", self.classe[0])
    print("Palavras dentro do invervalo de ocorrencia 40 - 59: ", self.classe[1])
    print("Palavras dentro do invervalo de ocorrencia 60 - 79: ", self.classe[2])
    print("Palavras dentro do invervalo de ocorrencia 80 - 99: ", self.classe[3])
    print("Palavras dentro do invervalo de ocorrencia 100 - 199: ", self.classe[4])
    print("Palavras dentro do invervalo de ocorrencia 200 - 299: ", self.classe[5])
    print("Palavras dentro do invervalo de ocorrencia 300 - 399: ", self.classe[6])
    print("Palavras dentro do invervalo de ocorrencia 400 - 499: ", self.classe[7])
    print("Palavras dentro do invervalo de ocorrencia 500 - 599: ", self.classe[8])
    print("Palavras dentro do invervalo de ocorrencia >= 600: ", self.classe[9])
    
if __name__ == "__main__":
  doc = reducer()
  doc.Reduce()
  doc.Impressao()