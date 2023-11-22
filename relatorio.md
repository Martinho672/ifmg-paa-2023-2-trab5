# Relatório de Desenvolvimento - Função de Maior Prêmio

**Fernando Martinho Nascimento & Lucas Guimarães Bernardes**

Este relatório descreve a implementação do trabalho 5 `Apagando e Ganhando` e destaca as características da solução, juntamente com as dificuldades enfrentadas durante o desenvolvimento.

## Função `maior_premio`

A função `maior_premio` tem como objetivo encontrar o maior número possível removendo dígitos de um número original. A abordagem utilizada é baseada em uma pilha, onde os dígitos são inseridos mantendo a propriedade de formar o número máximo possível.

### Implementação

- Uma pilha é utilizada para armazenar os dígitos do número resultante.
- Iteração sobre cada dígito do número original.
- Durante a iteração, verifica-se se há dígitos a serem removidos (`d > 0`), se a pilha não está vazia, e se o dígito atual é maior que o topo da pilha. Nesse caso, remove-se o topo da pilha.
- O dígito atual é então inserido na pilha.
- Após a iteração, se ainda restam dígitos a serem removidos (`d > 0`), remove-se dígitos da pilha.
- O resultado é obtido convertendo a pilha em um número inteiro.

### Dificuldades de Implementação

1. **Compreensão do Algoritmo:**
   - A lógica de utilizar uma pilha para manter os dígitos e decidir quais dígitos remover foi um conceito fundamental durante a implementação, bem como compreender e aplicar corretamente essa lógica.

2. **Controle de Dígitos Removidos:**
   - Garantir que a função remova o número correto de dígitos (`d`) e no momento apropriado exigiu uma atenção especial para evitar resultados incorretos.

3. **Manipulação de Números e Strings:**
   - A manipulação de números e strings, especialmente ao converter a pilha de dígitos de volta em um número inteiro, exigiu um cuidado extra para evitar erros de tipo.

## Testes

A função `maior_premio` foi testada com diferentes casos, incluindo números com diferentes quantidades de dígitos e diferentes quantidades de dígitos a serem removidos. Os resultados foram comparados manualmente para verificar a precisão da função.

## Execução do Programa

O programa principal utiliza um loop infinito para receber entradas do usuário. Solicita a quantidade de dígitos do número seguido pela quantidade de dígitos a serem removidos. O usuário é então solicitado a inserir o número original. O programa calcula e exibe o maior número possível após a remoção dos dígitos especificados. O loop continua até que o usuário insira 0 para ambas as quantidades, encerrando o programa.

##### Conclusão 

Apesar dos desafios enfrentados durante o desenvolvimento, o trabalho `Apagando e Ganhando` foi implementado com sucesso, proporcionando uma solução eficaz para encontrar o maior número possível após a remoção de dígitos. Este trabalho contribuiu para a compreensão do paradigma de `programação Gulosa`.
