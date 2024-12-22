from pilha_estatica import PilhaArray

# Validador de expressões matemáticas

def valida_expressao(expressao): # O(n)
    '''Verifica se a expressão matemática é válida'''
    pilha = PilhaArray()  # Inicializa uma pilha vazia
    for caractere in expressao:
        if caractere in '({[':
            pilha.push(caractere)   # Empilha os caracteres de abertura     
        elif caractere in ')}]':
            if pilha.esta_vazia():  # Se a pilha estiver vazia, a expressão é inválida
                return False
            topo = pilha.pop()      # Caso contrário, desempilha o último caractere
            if (topo == '(' and caractere != ')') or \
                (topo == '[' and caractere != ']') or \
                (topo == '{' and caractere != '}'):
                return False        # Se os caracteres não forem correspondentes, a expressão é inválida
            
    return pilha.esta_vazia() # Se a pilha terminar vazia, a expressão é válida

def main():
    expressao = input('Digite uma expressão matemática: ')
    if valida_expressao(expressao):
        print('Expressão válida!')
    else:
        print('Expressão inválida!')

if __name__ == '__main__':
    main()