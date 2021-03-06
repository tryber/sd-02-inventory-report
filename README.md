# Relatório de Estoque!

Bora gay, boraaaa!!

# Commands

Ambiente Virutal: `python3 -m venv .venv && source .venv/bin/activate`

Nota: após terminar o trabalho, para desativar o ambiente virtual digite `deactivate`

Dependências: `python3 -m pip install -r requirements.txt`

export PYTHONPATH="\${PYTHONPATH}:/home/anderson.bolivar/Documents/projects/sd-02-inventory-report"

## Entregáveis

Para entregar o seu projeto você deverá criar um _Pull Request_ neste repositório. Este _Pull Request_ deverá conter, para aprovação em todos os requisitos, os arquivos `main.py`, `inventory.py`, `inventory_iterator.py`, `importer.py`, `csv_importer.py`, `json_importer.py`, `xml_importer.py`, `simple_report.py`, `complete_report.py`, que conterão seu código `Python` e testes. Atente que os requisitos te orientarão a povoar estes arquivos aos poucos.

### ⚠️ É importante que seus arquivos tenham exatamente estes nomes! ⚠️

Você pode adicionar outros arquivos se julgar necessário. Qualquer dúvida, procure a gente no Slack!.

Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://course.betrybe.com/intro/git/) sempre que precisar!

---

## O que deverá ser desenvolvido

No projeto passado você implementou algumas funções que faziam leitura e escrita de arquivos JSON e CSV, correto? Neste projeto nós vamos fazer algo parecido, mas orientados pela Programação Orientada a Objeto! Você implementará um gerador de relatórios que recebe arquivos com dados de um estoque e gera, de saída, um relatório acerca destes dados.

Esses dados de estoque poderão ser obtidos de diversas formas, sendo elas:

- Através da importação de um arquivo `CSV`;

- Através da importação de um arquivo `JSON`;

- Através da importação de um arquivo `XML`;

Além disso, o relatório final deverá ser gerável em duas versões: simples e completa.

### Como o projeto deve ser executável

Seu programa deverá ser executável **via linha de comando** com o comando `python3 main.py argumento1 argumento2`:

- O **argumento 1** deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um `csv`, `json` ou `xml`.

- O **argumento 2** pode receber duas strings: `simples` ou `completo`, cada uma gerando o respectivo relatório.

---

## Desenvolvimento e testes

Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

```
.
├── README.md
├── setup.cfg
├── requirements.txt
├── main.py
├── data
│   ├── inventory_20200823.csv
│   ├── inventory_20200823.json
│   └── inventory_20200823.xml
├── inventory
│   ├── inventory.py
│   └── inventory_iterator.py
├── importer
│   ├── importer.py
│   ├── csv_importer.py
│   ├── json_importer.py
│   └── xml_importer.py
├── reports
│   ├── simple_report.py
│   └── complete_report.py
├── tests
│   ├── test_main.py
│   ├── test_inventory.py
│   ├── test_inventory_iterator.py
│   ├── test_importer.py
│   ├── test_csv_importer.py
│   ├── test_json_importer.py
│   ├── test_xml_importer.py
│   ├── test_simple_report.py
│   └── test_complete_report.py
```

Apesar do projeto já possuir uma estrutura base, você quem deve implementar tanto as classes quanto os testes. Novos arquivos podem ser criados conforme a necessidade.

Para executar os testes, lembre-se de primeiro **criar e ativar o ambiente virtual**, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém todos as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Com as dependências já instaladas, para executar os testes basta usar o comando:

```bash
$ python3 -m pytest
```

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse artigo: https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1

Para verificar se você está seguindo o guia de estilo do Python corretamente, você pode executá-lo com o seguinte comando:

```bash
$ python3 -m flake8
```

---

## Dados

Arquivos de exemplo nos três formatos de importação estão disponíveis no diretório `data` deste repositório.

### Importação de arquivos CSV

Os arquivos **CSV** são separados por vírgula, como no exemplo abaixo:

```csv
id,nome_do_produto,nome_da_empresa,data_de_fabricacao,data_de_validade,numero_de_serie,instrucoes_de_armazenamento
1,Nicotine Polacrilex,Target Corporation,2020-02-18,2022-09-17,CR25 1551 4467 2549 4402 1,morbi ut odio cras mi pede malesuada in imperdiet et commodo vulputate justo in blandit
2,fentanyl citrate,"Galena Biopharma, Inc.",2019-12-06,2022-12-25,FR29 5951 7573 74OY XKGX 6CSG D20,bibendum morbi non quam nec dui luctus rutrum nulla tellus in
3,NITROUS OXIDE,Keen Compressed Gas Co. Inc.,2019-12-22,2023-11-07,CZ09 8588 0858 8435 9140 2695,ipsum dolor sit amet consectetuer adipiscing elit proin risus praesent
```

### Importação de arquivos JSON

Os arquivos JSON seguem o seguinte modelo:

```json
[
  {
    "id": 1,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2020-07-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus"
  }
]
```

### Importação de arquivos XML

Os arquivos **XML** seguem o seguinte modelo:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<dataset>
  <record>
    <id>1</id>
    <nome_do_produto>valsartan and hydrochlorothiazide</nome_do_produto>
    <nome_da_empresa>Lake Erie Medical &amp; Surgical Supply DBA Quality Care Products LLC</nome_da_empresa>
    <data_de_fabricacao>2019-10-27</data_de_fabricacao>
    <data_de_validade>2022-08-31</data_de_validade>
    <numero_de_serie>MT08 VVDN 2131 9NFL C1JG KTDV RS1L LOZ</numero_de_serie>
    <instrucoes_de_armazenamento>at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat</instrucoes_de_armazenamento>
  </record>
</dataset>
```

---

## Requisitos obrigatórios:

#### 1 - Deve haver um método `generate` numa classe `SimpleReport` do módulo `simple-report`. Esse método deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá gerar uma saída para a linha de comando.

##### As seguintes verificações serão feitas:

- O método deve receber de parâmetro uma lista de dicionários no seguinte formato:

  ```json
  [
    {
      "id": 1,
      "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
      "nome_da_empresa": "Forces of Nature",
      "data_de_fabricacao": "2020-07-04",
      "data_de_validade": "2023-02-09",
      "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
      "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
    }
  ]
  ```

- O método deverá gerar, na linha de comando, uma saída com o seguinte formato:

  ```bash
  Data de fabricação mais antiga: YYYY-MM-DD
  Data de validade mais próxima: YYYY-MM-DD
  Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA
  ```

**Dica**: O módulo [datetime](https://docs.python.org/3/library/datetime.html) vai te ajudar.

#### 2 - Deve haver um método `generate` numa classe `CompleteReport` do módulo `complete-report`. Esse método deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá gerar uma saída para a linha de comando.

##### As seguintes verificações serão feitas:

- A classe `CompleteReport` deve herdar o método (`generate`) da classe `SimpleReport`, de modo a especializar seu comportamento.

- O método deve receber de parâmetro uma lista de dicionários no seguinte formato:

  ```json
  [
    {
      "id": 1,
      "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
      "nome_da_empresa": "Forces of Nature",
      "data_de_fabricacao": "2020-07-04",
      "data_de_validade": "2023-02-09",
      "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
      "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
    }
  ]
  ```

- O método deverá gerar, na linha de comando, uma saída com o seguinte formato:

  ```bash
  Data de fabricação mais antiga: YYYY-MM-DD
  Data de validade mais próxima: YYYY-MM-DD
  Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA
  Produtos estocados por empresa:
  - Physicians Total Care, Inc.: QUANTIDADE
  - Newton Laboratories, Inc.: QUANTIDADE
  - Forces of Nature: QUANTIDADE
  ```

#### 3 - Deve haver um método `import_data` dentro de uma classe `Inventory` do módulo `inventory`, capaz de ler um arquivo CSV passado como parâmetro de linha de comando

##### As seguintes verificações serão feitas:

- O método, quando receber um arquivo CSV, deve chamar o método de gerar relatório correspondente à entrada passada, `simples` ou `completo`. Ou seja, o método da classe `Inventory` deve chamar o método da classe que vai gerar o relatório.

#### 4 - Deve haver um método `import_data` dentro de uma classe `Inventory` do módulo `inventory`, capaz de ler um arquivo JSON passado como parâmetro de linha de comando

##### As seguintes verificações serão feitas:

- O método, quando receber um arquivo JSON, deve chamar o método de gerar relatório correspondente à entrada passada, `simples` ou `completo`. Ou seja, o método da classe `Inventory` deve chamar o método da classe que vai gerar o relatório.

#### 5 - Deve haver um método `import_data` dentro de uma classe `Inventory` do módulo `inventory`, capaz de ler um arquivo XML passado como parâmetro de linha de comando

##### As seguintes verificações serão feitas:

- O método, quando receber um arquivo XML, deve chamar o método de gerar relatório correspondente à entrada passada, `simples` ou `completo`. Ou seja, o método da classe `Inventory` deve chamar o método da classe que vai gerar o relatório.

#### 6 - Deve haver uma classe abstrata `Importer` no módulo import. Deve haver três classes herdeiras desta: `CsvImporter`, `JsonImporter` e `XmlImporter`, cada uma definida em seu respectivo módulo.

##### As seguintes verificações serão feitas:

- A classe abstrata deve definir a assinatura do método `import_data` a ser implementado por cada classe herdeira. Ela deve receber como parâmetro o nome do arquivo a ser importado.

- O método `import_data` definida por cada classe herdeira deve lançar uma exceção caso a extensão do arquivo passado por parâmetro seja inválida. Por exemplo, quando se passa um CSV para o `JsonImporter`.

- O método deverá ler os dados do arquivo passado e retorná-los estruturados em uma lista de dicionários conforme exemplo abaixo:

  ```json
  [
    {
      "id": 1,
      "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
      "nome_da_empresa": "Forces of Nature",
      "data_de_fabricacao": "2020-07-04",
      "data_de_validade": "2023-02-09",
      "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
      "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
    }
  ]
  ```

- A classe `Inventory` deve utilizar as classes definidas neste requisito para lidar com a lógica de importação, via **composição**.

#### 7 - Deve haver uma classe `InventoryIterator` no módulo `inventory-iterator`, que implementa a interface de um iterator. A classe `Inventory` deve implementar o método `__iter__` associado a essa classe.

##### As seguintes verificações serão feitas:

- As classes `InventoryIterator` e `Inventory` devem implementar corretamente a interface de um iterator, de modo que o código abaixo nos dê o primeiro item da lista de dicionários com os dados importados:

  ```python
  # ... Acima, um código que instancia e importa um arquivo para a variável `inventory` e importações do módulo Iterator e Iterable

  iterator = iter(inventory)
  first_item = next(iterator)
  ```

## Requisitos bônus:

#### 8 - A cobertura de testes do projeto deve ser de no mínimo 90%.

##### As seguintes verificações serão feitas:

- Todos os testes que envolvem mensagens na saída padrão ou de erro, devem ter sua saída redirecionada para Fakes com `StringIO`;

- Todos os testes que envolvem manipulação de arquivos criam Fakes com `StringIO`;

- A cobertura de testes é de no mínimo 90%.

---
