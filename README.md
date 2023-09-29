# Programação Orientada a Objetos (POO) e Programação Funcional em Python

Neste repositório, você encontrará uma série de exercícios que exploram os conceitos da Programação Orientada a Objetos (POO) e da Programação Funcional em Python. A POO e a Programação Funcional são dois paradigmas de programação importantes que permitem organizar e estruturar o código de maneiras diferentes.

## Conteúdo

1. [Programação Orientada a Objetos (POO)](#programação-orientada-a-objetos-poo)
   - [Conceitos Principais](#conceitos-principais)
   - [Exercícios de POO](#exercícios-de-poo)

2. [Programação Funcional](#programação-funcional)
   - [Conceitos Principais](#conceitos-principais-1)
   - [Exercícios de Programação Funcional](#exercícios-de-programação-funcional)

## Programação Orientada a Objetos (POO)

### Conceitos Principais

A Programação Orientada a Objetos (POO) é um paradigma de programação que se baseia em conceitos de "objetos". Os objetos são instâncias de classes que têm atributos (dados) e métodos (funções) que podem operar nesses dados. Alguns conceitos chave incluem:

- **Classe**: Uma classe é um modelo para criar objetos. Ela define os atributos e métodos que os objetos da classe terão.

- **Objeto**: Um objeto é uma instância de uma classe. Ele contém dados (atributos) e pode realizar ações (métodos).

- **Atributo**: Um atributo é uma variável associada a um objeto que armazena dados sobre o objeto.

- **Método**: Um método é uma função associada a um objeto que pode ser usada para realizar ações relacionadas a esse objeto.

- **Herança**: A herança permite que uma classe herde atributos e métodos de outra classe. Isso facilita a reutilização de código.

### Exercícios de POO

Aqui estão alguns exemplos de exercícios que exploram os conceitos de POO:

#### Exercício 1: Classe `Carro`

Crie uma classe `Carro` com os atributos `marca`, `modelo` e `ano`. Adicione um método para imprimir as informações do carro.

```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def imprimir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

carro1 = Carro("Ford", "Focus", 2020)
carro1.imprimir_info()
```

Neste exercício, você aprenderá a criar uma classe simples e instanciar objetos dela.

#### Exercício 2: Classe `ContaBancaria`

Crie uma classe `ContaBancaria` com os atributos `titular` e `saldo`. Adicione métodos para depositar, sacar e exibir o saldo.

```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Saldo de {self.titular}: {self.saldo} reais")

conta1 = ContaBancaria("João")
conta1.depositar(1000)
conta1.sacar(500)
conta1.exibir_saldo()
```

Este exercício demonstra como criar classes com métodos que manipulam atributos.

## Programação Funcional

### Conceitos Principais

A Programação Funcional é um paradigma de programação que trata as funções como cidadãs de primeira classe. Isso significa que as funções podem ser atribuídas a variáveis, passadas como argumentos e retornadas como valores. Alguns conceitos chave incluem:

- **Funções de Ordem Superior**: Funções que podem receber outras funções como argumentos ou retorná-las.

- **Imutabilidade**: Os dados não mudam após serem criados. As operações criam novos dados em vez de modificar os existentes.

- **Pureza**: Funções puras não têm efeitos colaterais e produzem o mesmo resultado para as mesmas entradas.

- **Recursão**: A recursão é comumente usada em Programação Funcional para resolver problemas.

### Exercícios de Programação Funcional

Aqui estão alguns exemplos de exercícios que exploram os conceitos de Programação Funcional:

#### Exercício 1: Função Lambda para Elevar ao Quadrado

Crie uma função lambda que eleve todos os elementos de uma lista ao quadrado.

```python
quadrado = lambda x: x ** 2
lista = [1, 2, 3, 4, 5]
resultado = list(map(quadrado, lista))
print(resultado)
```

Neste exercício, você aprenderá a usar funções lambda e a função `map` para aplicar uma operação a todos os elementos de uma lista.

#### Exercício 2: Função `filtrar_pares`

Escreva uma função `filtrar_pares` que receba uma lista de números e retorne apenas os números pares.

```python
filtrar_pares = lambda lista: list(filter(lambda x: x % 2 == 0, lista))
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = filtrar_pares(numeros)
print(resultado)
```

Neste exercício, você usará funções lambda e `filter` para filtrar elementos de uma lista com base em uma condição.

### Como Usar Este Repositório

1. Clone este repositório em seu ambiente de desenvolvimento local.

2. Navegue para a pasta do exercício que deseja explorar.

3. Leia o enunciado do exercício e tente resolvê-lo por conta própria.

4. Consulte a solução e a explicação detalhada no arquivo correspondente `ex3.py`.

5. Experimente modificar o código ou criar variações dos exercícios para aprofundar sua compreensão.

## Conclusão

Este repositório fornece uma introdução prática à Programação Orientada a Objetos (POO) e à Programação Funcional em Python. Explore os exercícios e experimente diferentes abordagens para consolidar seus conhecimentos em ambos os paradigmas.

**Divirta-se programando!**
