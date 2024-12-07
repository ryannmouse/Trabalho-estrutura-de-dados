## Questão 4 
from questão_2 import PilhaArray
import time
## Questão 4
# p, i = PilhaArray().pares_e_impares(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print('Pares:')
# p.imprimir()
# print('Ímpares:')
# i.imprimir()
pilha = PilhaArray()



start_time = time.time()

# Código para testar
for i in range(10_000_000):
    pilha.push(i)
    
pilha.elimina(456977)

end_time = time.time()

print(f"Tempo de execução: {end_time - start_time} segundos")