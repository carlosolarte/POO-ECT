## Encapsulamento
---

### Revisão 

#### Classe
Abstração para agrupar objetos comuns

Descreve de maneira _abstrata_ o comportamento dos

#### Objetos 
*Instâncias* de uma classe

Encapsulam um _estado_

---

### Revisão 

- _Atributos_: Características da entidade sendo modelada
- _Métodos_: Definem o *comportamento*
- _Construtor_: Inicializa os atributos
- `self`: auto-referência ao próprio objeto

---

### Objetivos

Nesta aula aprenderemos:
  - _Encapsulamento_: __Segundo pilar__ da POO
  - Implementar diagramas __UML__ simples
  - Setters/getters e `@property` (nosso primeiro decorador)  em Python

---
### Encapsulamento

> Capacidade de esconder informações (dados) nos objetos

- __Proteger__ o acesso direto aos atributos de um objeto
- Os membros que não devem ser usados fora da classe devem estar *escondidos*
- As classes devem __expôr o mínimo necessário__ para serem utilizadas
-  Similar a funções: os dados mínimos que elas precisam são os parâmetros
---

### Encapsulamento

- POO é comumente utilizada no desenvolvimento de bibliotecas
- Os usuários da classe só podem acessar os membros e métodos  *públicos* da classe.
- O usuário da classe é quem utiliza uma biblioteca POO
- Ao chamar um método, podemos ignorar como ele foi implementado
- Facilita a manutenção e reaproveitamento do código

---

### Modificadores de Acesso

Os __modificadores de acesso__ valem para atributos e métodos:

- __Público__:  o membro/método pode ser acessado/chamado de qualquer lugar
- __Privado__: o membro/método só pode ser acessado/chamado  dentro da definição da classe
- __Protegido__: o membro/método pode ser utilizado pelas subclasses. 

> A implementação dos modificadores é um mecanismo dependente da linguagem. Em C++ e
Java, por exemplo, as palavras chaves `public` e `private` devem ser usadas
para esta função

---

### Modificadores de Acesso
#### Exemplo em Java

```java
public class Pessoa{
    // Atributos
    private String nome;
    private int idade;
    // Método público
    public String cumprimentar(Pessoa outro)
    {...
    }
}
```

Em Python... é um pouco diferente. 

---

### Exemplo: Estacionamento
Um estacionamento tem capacidade para um número $n>0$ de vagas. 

Devemos controlar quantos carros estão dentro do estacionamento. 

Os carros podem entrar só se há vagas disponíveis.

Nesse  sistema podemos identificar:
- _Classes_: Carros e o Estacionamento (por enquanto, vamos ignorar os carros)
- _Atributos_: número de vagas, capacidade máxima
- _Métodos_: Os carros podem _entrar_ e _sair_. Além disso, podemos consultar o número de vagas disponíveis.
--- 

### Exemplo: Estacionamento
#### Notação UML: Diagrama de Classes

<img src="img/uml.png" width=250 />

 - `-` denota um membro de classe _privado_.
 - `+` denota um membro _público_
 - `#` denote um membro  _protegido_

<https://www.draw.io/>

--- 
### Exemplo: Estacionamento
Os usuários da classe `Estacionamento` deveriam __modificar diretamente__  o atributo `vagas`? 

*Não!*   O valor do atributo _vagas_ não pode ser modificado direitamente (só utilizando os método `entrar`/`sair`).
<!-- .element: class="fragment" -->

---

### Encapsulamento
- *Esconder* os membros de uma classe.
- *Esconder* como funcionam as rotinas (métodos) da classe.
- O encapsulamento facilita o *reaproveitamento* de código.
- Alterar código resulta mais simples.
- Os usuários da classe só podem acessar os atributos/métodos *públicos* da classe.
- Busca garantir a *consistência* (do estado) dos objetos

> As classes devem expor o mínimo necessário para serem utilizadas.

---

### Encapsulamento em Python
[04-Encapsulamento](04-Encapsulamento.ipynb)
