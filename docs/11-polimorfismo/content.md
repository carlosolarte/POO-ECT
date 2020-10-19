## Polimorfismo
---

### Objetivo da aula

Nesta aula veremos: 

- O que é polimorfismo
- Como utilizá-lo na linguagem Python
- *Duck typing*

---

### Os pilares da POO

- Abstração
- Encapsulamento
- Herança
- __Polimorfismo__

---

### Polimorfismo

 Mecanismo presente em linguagens OO que permitem a um objeto se comportar de
 formas diferentes 

*Poli*: muitos, *morfismo*: formas

Mais um recurso utilizado para promover a reutilização de código

Uma mesma mensagem pode executar _diferentes_ métodos/código.

---

### Polimorfismo em ling. tipadas (Java)

1. Instanciando objetos da classe base utilizando construtores da classe derivada.

```java
// Gato é uma subclasse de Mamifero
Mamifero M = new Gato(); 
// Funcionario é uma subclasse de Pessoa
Pessoa P = new Funcionario(...); 

// Utilizando casting explicito
Gato G = new Gato();
Animal A2 = (Animal) G ;

// Erro!! Não toda pessoa é um funcionário
Funcionario F = new Pessoa(...); 
```
Podemos atribuir em variáveis da superclasse, objetos da subclasse. 

---
### Polimorfismo em ling. tipadas (Java)

2. Considere um método que recebe como parâmetro
   objetos da classe base. 

```java
void imprimirDados(Pessoa P){
 ...
}

Funcionario F = new Funcionario(...);
// Como todo funcionário é uma pessoa
// podemos utilizar o método imprimirDados com parâmetro F
imprimirDados(F); 
```

Podemos _"substituir"_ o parâmetro do tipo `Pessoa` por um `Funcionario`
(porque todo `Funcionario` __é uma__ `Pessoa`).

---
### Polimorfismo em ling. tipadas (Java)

3. _Sobrecarga_ de operadores (um mesmo operador se comporta de diversas
   formas)
```
int f(int x);
float f(float x);
char f(char x);
```

A função `f` possui diferentes __assinaturas__. 

---
### Em Python a história é diferente

1. sem tipos explícitos, isso aqui não faz sentido
```java
Pessoa P = new Funcionario(...); 
```

Note que em Python, uma variável pode ser atribuída a objetos de tipos
diferentes (que não necessariamente pertencem __à mesma hierarquia__) 

```python 
x = 4 
x = [1,2,3] 
x = "alo" 
x = Pessoa(...) 
x = Carro(...) 
```

---
### Em Python a história é diferente
2. Chamar funções/métodos com instâncias de alguma subclasse. 

Como não temos tipos, podemos chamar uma função/método com objetos
de tipos diferentes (não necessariamente objetos de uma subclasse):

```python
str(3)
str(3.2)
P = Pessoa(...)
str(P)
####
len("alo") #3
len([1,2,3]) #3
```

---
### Em Python a história é diferente
3. Sobrecarga de operadores. Em Python não podemos criar 2 funções com 
diferentes assinaturas: 

```
def f(x):
 ...

def f(x,y):  # a definição anterior de f já não existe mais
 ...

f(4) # Erro! 2 parâmetros são esperados
```

---
### Em Python a história é diferente

Parece que só temos como alternativa (2) 
(de forma mais genérica com _Duck Typing_)

```python
class Pessoa:
    def __init__(self, nome, idade): ...

    def compara_idades(self, p2):
        return p1.idade <= p2.idade

class Aluno(Pessoa): ...
class Professor(Pessoa): ...

p = Pessoa('joão', 25)
a = Aluno('maria', 20, 111) 
print(p.compara_idades(a))
```

---

### Polimorfismo

Neste código:
```python
p = Pessoa('joão', 25)
a = Aluno('maria', 20, 111)
prof = Professor('santos', 40, 'ECT')

for pess in [p, a, prof]:
   print(pess) 
```
Python converte `pess` para string utilizando o método `__str__` (ou `__repr__`)

Mas... __o método__ `__str__` __de qual classe?__

---
### Polimorfismo

Mas um exemplo:

```python
class Animal(ABC):
 ...
 @abstractmethod
    def emite_som(self):
        pass

class Gato(Mamifero):
    def emite_som(self):
        print('miau')

g = Gato()
c = Cachorro()
o = Ornitorrinco()
p = Pinguim()
a = Aguia()
animais = [g,c,o,a]
for a in animais:
  a.emite_som()
```
__Qual método `emite_som` deve ser executado?__

--- 

### Qual método executar?
```python
animais = [g,c,o,a]
for a in animais:
  a.emite_som()
```

Regras:

 - A variável ```a``` (no laço ```for```) é acessada e o objeto armazenado é encontrado.
 - A classe de ```a``` é encontrada
 - A implementação do método é encontrada e executada.
 - Se a classe de  ```a``` __não tiver uma implementação do método__, o método é buscado na superclasse.

---

### Polimorfismo

 Capacidade de um objeto para ser referenciado de várias formas.

 A chamada dos métodos é polimórfica: a mesma chamada pode, em momentos
 diferentes, invocar diferentes métodos (depende do tipo do objeto).

---
### O princípio da substituição de Liskov
  <img src="Barbara.jpg" ></img> 

Barbara Liskov, cientista da computação estadunidense conhecida por criar o
_Princípio de Substituição de Liskov_, por ser uma das primeiras mulheres a
obter um PhD em Ciência da Computação nos Estados Unidos e por inventar o Tipo
Abstrato de Dado (TAD)(tomada da
[Wikipedia](https://pt.wikipedia.org/wiki/Barbara_Liskov)) 

</td>
 </tr>
</table>
---
### O princípio da substituição de  Liskov
  <img src="Barbara.jpg" ></img> 

Barbara recebeu em 2008 o Prêmio Turing da ACM por seu trabalho na concepção
de linguagens de programação e de metodologia de software que levaram ao
desenvolvimento da _programação orientada para objetos_.

---
### O princípio da substituição de  Liskov
- *Uma classe base deve poder ser substituída pela sua classe derivada*
- Considere o método ```q(x)```. Se ```q``` pode ser utilizado com objetos da
  superclasse T, então ```q``` deve poder também ser invocado com um objeto de
  uma subclasse ```S``` derivada de ```T```.

---
### O princípio da substituição de  Liskov

```python
# A função cumprimentar foi escrita para cumprimentar uma pessoa
def cumprimentar(P):
    '''P : Pessoa'''
    print(f'Olá {P.nome}, tudo bem ?')

# Mas podemos utilizar cumprimentar com subclasses de P
p = Pessoa('joão', 25)
a = Aluno('maria', 20, 111)
cumprimentar(p)
cumprimentar(a)
```

--- 
### Duck Typing
Sendo uma linguagem de tipagem dinâmica, em Python, um método/função pode ser
utilizada por _qualquer objeto que implemente certo comportamento_ (sem ser parte
de uma hierarquia de herança).

>Quando eu vejo um pássaro que anda como pato, nada como um pato
e grasna como pato, então pra mim este pássaro é um pato.

---
### Duck Typing

```python
class A:
    def doIt(self):
        return 'Trabalhando em A'

class B:
    def doIt(self):
        return 'Trabalhando em B'

def trabalhar(x):
    '''x deve ser um objeto que implementa o método doIt'''
    print(x.doIt())

a = A()
b = B()
trabalhar(a)
trabalhar(b)
```

---
### Duck Typing

Forma de tipagem que está mais interessada no que o objeto possui como
atributos/métodos do que se ele é de uma determinada classe

*Duck typing* já foi utilizado diversas vezes:

- Quando usamos ```a + b```: não interessa os tipos de ```a``` e ```b```,
  desde que as classes de ```a``` e ```b``` implementem o operador de soma (método ```def __add__(self, outro):```)
- Quando usamos ```print(a)```: não interessa o tipo de ```a```,
  o objeto vai ser impresso (e o método ```__str__``` é chamado). 
- Quando usamos ```a.liga()```: não interessa o tipo de ```a```, desde que
  este objeto possua o método ```liga```. 

---

Ver [Notebook](Polimorfismo.ipynb)
