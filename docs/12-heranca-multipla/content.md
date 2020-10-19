## Herança Múltipla
---
## Objetivo da aula:

- Apresentar o mecanismo de herança múltipla
    - O que é herança múltipla
    - Como utilizá-lo na linguagem Python
---
## Herança:

- Permite que classes derivadas herdem o comportamento
  (atributos e métodos) de uma classe base
- Introduz a relação "ser um"
- Código na classe base pode ser __reutilizado__ nas classes derivadas
- Classe derivada pode _reimplementar_ um método com funcionalidades específicas

---
## Herança Múltipla
Ocorre quando a classe derivada _possui mais de uma classe base_

Linguagens de programação implementam esse mecanismo de diferentes formas: 
- Java possui suporte utilizando o conceito de Interfaces
- C++ possui suporte
- Python possui suporte

---
## Herança Múltipla
Ocorre quando a classe derivada _possui mais de uma classe base_

A forma de implementação de cada linguagem resolve os problemas
  encontrados com herança múltipla:
- _Ambiguidade de atributos_: as classes base possuem atributos com mesmo nome
- _Ambiguidade de métodos_: as classes bases possuem métodos com mesmo nome

---
## Herança Múltipla

Em Python, as classes base são indicadas por uma tupla:

```python
class Subclasse(Superclasse1, Superclasse2):
...
```

- ```Subclasse``` é a classe derivada
- Todos os atributos e métodos de ```Superclasse1```
  e ```Superclasse2``` estão na subclasse

--- 
## Herança Múltipla

Exemplo

```python
class Superclasse1:
   def metodo_super1(self): ...

class Superclasse2:
   def metodo_super2(self): ...

class Subclasse(Superclasse1, Superclasse2):
   def metodo_sub(self): ...

obj = Subclasse(50)
obj.metodo_super1()
obj.metodo_super2()
obj.metodo_sub()
```
---
## Herança Múltipla

Os métodos __init__ de cada superclasse precisam ser explicitamente chamados

```python
class Subclasse(Superclasse1, Superclasse2): 
  def __init__(self, valor):
        Superclasse1.__init__(self, 0) # atribui 0 a atrib_super1
        Superclasse2.__init__(self, 1) # atribui 1 a atrib_super2

```
---
### Herança Múltipla

As superclasses também podem ser classes abstratas

Todos os métodos abstratos de _todas as superclasses_
abstratas têm que ser implementados para que a subclasse
seja __concreta__

 Caso contrário, a subclasse se torna uma classe abstrata

---
### Herança Múltipla: Problemas

#### Atributos com o mesmo nome
```python
class Superclasse1:
   def __init__(self, valor):
        self.atrib_super = valor

class Superclasse2:
   def __init__(self, valor):
        self.atrib_super = valor

class Subclasse(Superclasse2, Superclasse1):
   def __init__(self, valor):
        Superclasse2.__init__(self, 1)
        Superclasse1.__init__(self, 0)

obj = Subclasse(50)
print(obj.atrib_super) # qual atrib_super e utilizado?
```
--- 
### Atributos com o mesmo nome

Como o `__init__` de cada superclasse foi chamado, o atributo considerado é o último encontrado (e não o primeiro)

Cada chamada de `__init__` _sobrescreve_ a declaração anterior

Portanto, o que vale __é o último que sobrescreve__

---

### Herança Múltipla: Problemas
#### Métodos com o Mesmo Nome

```python
class Superclasse1:
   def metodo_super(self):

class Superclasse2:
   def metodo_super(self):

class Subclasse(Superclasse2, Superclasse1):
  ...

obj = Subclasse(50)
obj.metodo_super() # qual metodo_super e chamado?

```
--- 
### Herança Múltipla: Problemas
#### Métodos com o Mesmo Nome

O método implementado em ```Subclasse``` depende da ordem indicada
  na tupla de classes base.

A linguagem Python considera a primeira superclasse da __esquerda para a direita__

A implementação do método que _for achada primeiro é utilizada_

---
### O problema do Diamante

Considere a seguinte hieraquia de classes

<img src=diamante.png >

---
### O problema do Diamante

Assuma que todas as classes `A`, `B`, `C` e `D` implementam 

```python
def metodo(self): ...
```
Qual método seria chamado?
```python
a = A()
b = B()
c = C()
d = D()
a.metodo()
b.metodo()
c.metodo()
d.metodo()
```

---
### O problema do Diamante
Se `A`, `B` e `C` implementam o método mas `D` não:

```python
class D(B,C):
    pass
```

Qual método seria chamado?

```python
d = D()
d.metodo()
```
---
Mais exemplos no [Notebook](Heranca-multipla.ipynb)
