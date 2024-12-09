from questao_2 import PilhaArray

# Validador de expressões matemáticas

def valida_expressao(expressao):
    '''Verifica se a expressão matemática é válida'''
    pilha = PilhaArray()
    for caractere in expressao:
        if caractere in '({[':
            pilha.push(caractere)
        elif caractere in ')}]':
            if pilha.is_empty():
                return False
            topo = pilha.pop()
            if (topo == '(' and caractere != ')') or \
                (topo == '[' and caractere != ']') or \
                (topo == '{' and caractere != '}'):
                return False
