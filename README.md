[![Status Badge](https://img.shields.io/badge/status-development-3066be)](https://github.com/arthur-bryan/projeto-poo)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/arthur-bryan/projeto-poo)](https://github.com/arthur-bryan/projeto-poo/tags)
[![Python Badge](https://img.shields.io/badge/-Python%203.7-3066be?logo=Python&logoColor=white&link=https://www.python.org/)](https://www.python.org/)
![GitHub repo size](https://img.shields.io/github/repo-size/arthur-bryan/projeto-poo)

# Projeto POO

Projeto da disciplina de Estrutura de Dados e Programação Orientada a Objetos, no período 2020.1 do curso superior
de Tecnologias em Redes de Computadores do Instituto Federal de Educação, Ciência e Tecnologia da Paraíba.
A aplicação simula um sistema de reservas de salas de uma empresa de coworking e tem as seguintes funções:

  - Realizar cadastros de sócios e funcionários da empresa
  - Realizar reserva das salas de reuniões para cargos específicos ou auditórios
  - Consultar reservas de um sócio ou funcionário em um dia específico
  - Alterar nomes dos donos de reservas existentes
  - Alterar horário de reservas existentes
  - Exibir sócios e funcionários registrados
  - Exibir reservas realizadas
  - Remover reservas

## Nova feature

  - Persistência de dados: as reservas agora são gerenciadas (CRUD) com SQLite3 e armazenadas num banco local.

## Uso

  Clonar o repositório do projeto, criar o banco de dados (caso não exista) e iniciar o programa

  ```sh
  $ git clone https://github.com/arthur-bryan/projeto-poo
  $ cd projeto-poo/app/models
  $ python3.7 criar_banco.py
  $ cd ../..
  $ python3.7 main.py
  ```
  ou baixar via wget, criar o banco de dados e iniciar
  ```sh
  $ wget https://github.com/arthur-bryan/projeto-poo/archive/main.zip
  $ unzip main.zip
  $ cd projeto-poo-main/app/models
  $ python3.7 criar_banco.py
  $ cd ../..
  $ python3.7 main.py
  ```

## Qualidade do código: 9.73/10

  ### Verifique você mesmo
  Fora do diretório do projeto :
  ```sh
  $ python3.7 -m pip install -r projeto-poo/requirements.txt
  $ pylint projeto-poo
  Your code has been rated at 9.73/10 (previous run: 9.73/10, +0.00)
   ```
  https://pypi.org/project/pylint/

## Licença

  MIT License
  Copyright (c) 2020 Arthur Bryan
