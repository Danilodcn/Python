from PIL import Image

im = Image.open("grafico.jpeg")
pixels = im.load()

largura, altura = im.size
p = (1,2, 3, 4, 5)

def grafico_reta(p1, p2):
       "(ponto, ponto) desenha uma reta na imagem"
       def coeficiente():
              "Calcula o coefiente angular da reta que passa pelos pontos p1 e p2"
              if p1[0] < p2[0]:
                     p1, p2 = (p2, p1)
              x1, y1 = p1
              x2, y2 = p2
              return (y2 - y1) / (x2 - x1)
 
       print(coeficiente())
       
       
       im.show()

p1, p2 = ((200, 70), (300, 120))
grafico_reta(p1, p2)
       
print("Acabou" + "!" * 10)
p = []
for x in range(largura):
       for y in range(altura):
              if pixels[x, y] == (0, 0, 0):
                     p += [x, y]

print(p)
