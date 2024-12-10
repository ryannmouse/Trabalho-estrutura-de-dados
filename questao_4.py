from questao_2 import PilhaArray

# Validador de expressões matemáticas

def valida_expressao(expressao):
    '''Verifica se a expressão matemática é válida'''
    pilha = PilhaArray()
    for caractere in expressao:
        if caractere in '({[':
            pilha.push(caractere)
        elif caractere in ')}]':
            if pilha.esta_vazia():
                return False
            topo = pilha.pop()
            if (topo == '(' and caractere != ')') or \
                (topo == '[' and caractere != ']') or \
                (topo == '{' and caractere != '}'):
                return False
            
    return pilha.esta_vazia() # Se a pilha terminar vazia, a expressão é válida

def main():
    expressao = input('Digite uma expressão matemática: ')
    if valida_expressao(expressao):
        print('Expressão válida!')
    else:
        print('Expressão inválida!')

if __name__ == '__main__':
    main()