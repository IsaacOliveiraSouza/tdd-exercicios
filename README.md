# TDD - Exercícios

Implementação dos três exercícios da atividade de TDD em **Python 3.12** com **pytest** e **pytest-cov**.

| Exercício | Código | Testes |
|---|---|---|
| 1 - Triângulo | `exercicio1/triangulo.py` | `tests/test_triangulo.py` |
| 2 - Validação de Person | `exercicio2/pessoa.py` | `tests/test_pessoa.py` |
| 3 - Calculadora de salário | `exercicio3/salario.py` | `tests/test_salario.py` |

O histórico de commits segue o ciclo do TDD: para cada exercício há um commit com o esqueleto e os testes falhando, seguido do commit com a implementação que faz os testes passarem.

## Build

Requisitos: Python 3.10 ou superior.

```bash
git clone <url-do-repositorio>
cd tdd-exercicios
python -m venv .venv
```

Ativar o ambiente virtual:

```bash
# Linux/macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

Instalar as dependências:

```bash
pip install -r requirements.txt
```

## Execução dos testes

Todos os testes:

```bash
python -m pytest
```

Todos os testes com cobertura:

```bash
python -m pytest --cov=exercicio1 --cov=exercicio2 --cov=exercicio3 --cov-report=term-missing
```

Relatório HTML (gerado em `htmlcov/index.html`):

```bash
python -m pytest --cov=exercicio1 --cov=exercicio2 --cov=exercicio3 --cov-report=html
```

## Exercício 1 - Triângulo

A classe `Triangulo` recebe três lados inteiros e o método `classificar()` retorna `equilatero`, `isosceles`, `escaleno` ou `invalido`. O triângulo é inválido quando algum lado é menor ou igual a zero ou quando a soma de dois lados não é maior que o terceiro.

Casos de teste:

| Situação | Teste | Entradas |
|---|---|---|
| Escaleno válido | `test_escaleno_valido` | (3, 4, 5) |
| Isósceles válido | `test_isosceles_valido` | (5, 5, 3) |
| Equilátero válido | `test_equilatero_valido` | (4, 4, 4) |
| Isósceles com permutações | `test_isosceles_permutacoes` | (5, 5, 3), (5, 3, 5), (3, 5, 5) |
| Um valor zero | `test_um_valor_zero` | (0, 4, 5) |
| Um valor negativo | `test_um_valor_negativo` | (-3, 4, 5) |
| Soma de 2 lados igual ao terceiro | `test_soma_de_dois_lados_igual_ao_terceiro` | (1, 2, 3) |
| Permutações do item acima | `test_soma_igual_permutacoes` | as 6 permutações de (1, 2, 3) |
| Soma de 2 lados menor que o terceiro | `test_soma_de_dois_lados_menor_que_o_terceiro` | (1, 2, 5) |
| Permutações do item acima | `test_soma_menor_permutacoes` | as 6 permutações de (1, 2, 5) |
| Três valores zero | `test_tres_valores_zero` | (0, 0, 0) |

Comando:

```bash
python -m pytest tests/test_triangulo.py --cov=exercicio1 --cov-report=term-missing
```

Evidência de cobertura:

```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
exercicio1\__init__.py        0      0   100%
exercicio1\triangulo.py      18      0   100%
-------------------------------------------------------
TOTAL                        18      0   100%
23 passed
```

## Exercício 2 - Validação de Person

Classes `Person` (nome, idade e lista de `Email`), `Email` (atributo `name`) e `PersonDAO`, com o método `is_valid_to_include(person)` que retorna a lista de erros encontrados (lista vazia quando a pessoa é válida). Regras validadas:

- o nome tem ao menos 2 partes, compostas apenas por letras;
- a idade está no intervalo [1, 200];
- a pessoa tem ao menos um `Email`;
- todo email está no formato `_____@____._____`, com ao menos um caractere em cada parte.

Comando:

```bash
python -m pytest tests/test_pessoa.py --cov=exercicio2 --cov-report=term-missing
```

Evidência de cobertura:

```
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
exercicio2\__init__.py       0      0   100%
exercicio2\pessoa.py        35      0   100%
------------------------------------------------------
TOTAL                       35      0   100%
29 passed
```

## Exercício 3 - Calculadora de salário

`Funcionario` tem nome, email, salário-base e `Cargo`. A `CalculadoraSalario` aplica o desconto de acordo com o cargo:

| Cargo | Limite | Desconto (>= limite) | Desconto (< limite) |
|---|---|---|---|
| DESENVOLVEDOR | 3.000,00 | 20% | 10% |
| DBA | 2.000,00 | 25% | 15% |
| TESTADOR | 2.000,00 | 25% | 15% |
| GERENTE | 5.000,00 | 30% | 20% |

Os testes cobrem, para cada cargo, um valor acima do limite, o próprio limite, um valor logo abaixo do limite e um valor bem abaixo.

Comando:

```bash
python -m pytest tests/test_salario.py --cov=exercicio3 --cov-report=term-missing
```

Evidência de cobertura:

```
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
exercicio3\__init__.py       0      0   100%
exercicio3\salario.py       19      0   100%
------------------------------------------------------
TOTAL                       19      0   100%
17 passed
```
