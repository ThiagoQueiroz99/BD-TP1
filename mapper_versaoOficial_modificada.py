import sys

caracteres_especiais = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
numeros = '''0123456789'''

class mapper:
  def __init__ (self):
    self.H = {}

  def Map(self):
    for linha in sys.stdin:
      linha = linha.strip()
      for x in linha:
        if x in caracteres_especiais or x in numeros:
          linha = linha.replace(x, " ") 
      palavras = linha.split()
      for palavra in palavras:
        if palavra in self.H:
          self.H[palavra] += 1
        else:
          self.H[palavra] = 1

  def Close(self):
    for palavra in self.H:
      print("%s\t%s" % (palavra, self.H[palavra]))

if __name__ == "__main__":
  doc = mapper()
  doc.Map()
  doc.Close()