## Módulos em Python
---
### Objetivos
- Apresentar o conceito e a utilidade de _Módulos_ em Python
- Solucionar o exercício de cursos/disciplinas/alunos

---
### Módulos em Python:

Conjunto de variáveis, funções e classes contidos em um ou mais arquivos `.py`

Módulos podem ser importados por um programa (similar ao `#include` de C++)

Em Python, um módulo pode ser considerado sinônimo de biblioteca

---
### Importação de Módulos

Considere o código a seguir: 
```
import math # modulo da biblioteca padrão
print(math.e) # constante de Euler
print(math.sqrt(16)) # raiz quadrada de 16
```

- Note o uso de `math.sqrt`
- O nome do módulo deve ser utilizado

---
### Importação de Módulos
Podemos importar também __todas__ as definições de um módulo:

```
from math import *
print(e) # contante de Euler
print(sqrt(16)) # raiz quadrada de 16
```

- Note o uso da função `sqrt` (sem o nome do módulo)

---
### Importação de Módulos
Também podemos importar algumas das definições do módulo:

```python
from math import e, sqrt
print(e)
print(sqrt(16))
```

- Note que `math.sin` não existe porque apenas foram importadas as
  definições `e` e `sqrt`

---
### Biblioteca Padrão

A biblioteca padrão Python possui vários módulos importantes (alguns já formam
explorados nas últimas aulas) :

- Módulo math: contém funções matemáticas
- Módulo random: contém funções para números aleatórios de diferentes distribuições de probabilidade
- Módulo os: contém funcionalidades para o Sistema Operacional (ex.: Windows, Mac, Linux, etc.)
- E muitos outros serão explorados ao longo do semestre

---
### Biblioteca Padrão

```python
import math
dir(math)
help(math)
```

- `dir`: usada para descobrir os nomes definidos por um módulo

---
### Definir Módulos

Todo arquivo `.py` é um módulo
```
#arquivo alo.py
```

```
def dois():
 '''Função que retorna 2'''
 return 2

class Alo:
 '''Classe ainda não implementada'''
 pass
```

Como utilizar esse arquivo?
- Como script/programa
- Como módulo (para ser importado)

---

### Definir Módulos

No console de Python

```
import alo
dir(alo)
help(alo)
print(alo.dois())
x = alo.Alo()
```

---

### Definir Módulos

Mas também podemos importar `alo` em outro módulo

Arquivo `test.py`:

```
import alo

def printDois():
    '''Imprimir o resultados de alo.dois()'''
    print(alo.dois())

def main():
    '''Função principal'''
    printDois()

if __name__ == "__main__":
    main()
```

---

### Definir Módulos

O que significa esse `__name__ == "__main__"`?

- Execute `python test.py`
- Agora, entre no console e execute `import test`
- Note que a função `main` não é executada. 
- Mas podemos executar `test.main()`
- Execute `dir()` e depois `print(__name__)`
- O atributo especial de um módulo `__name__` contém a string `"__main__"` quando
  ele não está sendo importado

---

### Pacotes

Um diretório que contem arquivos Python e, em especial o arquivo `__init__.py`,
é considerado como um __pacote__. 

Um pacote pode conter vários módulos (conhecidos também como submódulos).

Os pacotes permitem:

- Organizar o código fonte
- Oferecem a possibilidade de importar os módulos de forma mais flexível.
- Evitam a colisão de nomes iguais entre diferentes módulos

--- 

### Pacotes

```
sigaa
    __init__.py #Sempre executado quando um módulo é chamado
    aluno.py
    professor.py
    curso.py
    ...
```

ver código em `sigaa`
