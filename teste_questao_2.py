## Questão 4 
from pilha_estatica import PilhaArray
import time
## Questão 4
# p, i = PilhaArray().pares_e_impares(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print('Pares:')
# p.imprimir()
# print('Ímpares:')
# i.imprimir()

pilha = PilhaArray()

# Código para testar
for i in range(1_000_000):
    pilha.push(i)
    
	
start_time = time.time()

# Configurar cada teste com time
print("Testando liberar()")
tempo_liberar = time.time()
print(f"Tempo de execução da liberar(): {tempo_liberar - start_time}")

print("\nTestando palindromo()")
pilha.palindromo()
tempo_palindromo = time.time()
print(f"Tempo de execução da palindromo(): { tempo_palindromo - tempo_liberar }")

print("\nTestando elimina()")
tempo_elimina = time.time()
print(f"Tempo de execução da elimina(): { tempo_elimina -tempo_palindromo }")

print("\nTestando imprimir_reversa()")
pilha.imprimir_reversa()
tempo_imprimir_reversa = time.time()
print(f"Tempo de execução da imprimir_reversa(): {tempo_imprimir_reversa - tempo_elimina}")


