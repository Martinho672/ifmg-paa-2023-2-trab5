def maior_premio(numero, d):
    pilha = []

    for digito in numero:
        """
        Enquanto houver dígitos a serem removidos e a pilha não estiver vazia
        e o dígito atual for maior que o topo da pilha vai removendo o topo da pilha
        */
        """
        while d > 0 and pilha and pilha[-1] < digito:
            pilha.pop()
            d -= 1
        
        # joga o digito atual na pilha
        pilha.append(digito)

    while d > 0:
        pilha.pop()
        d -= 1

    resultado = int(''.join(pilha))
    return resultado

while True:
    print("Digite a quantidade de digitos do número seguido por um espaço com a quantidade de digitos a serem removidos:")
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    print("Digite o número a ser verificado:")
    numero_original = input().strip()
    resultado = maior_premio(numero_original, d)
    print(resultado)
