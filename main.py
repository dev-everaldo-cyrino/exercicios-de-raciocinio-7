n = 1
pessoa = []
altura = []
idade = []
for x in range(5):
    pessoa.append(input('nome da {}° pessoa: '.format(n)))
    idade.append(float(input('idade da {}° pessoa: '.format(n))))
    altura.append(float(input('altura da {}° pessoa: '.format(n))))
    print('..........................')
    n +=1
n = 1
for x in range(5):
    print('''
          altura: {}
          idade: {}
          pessoa: {}'''.format(altura[n * -1],idade[n * -1],pessoa[n * -1]))
    n +=1