# Olympics Medals Project

Este projeto Django realiza a extração de dados de medalhas olímpicas da página oficial das Olimpíadas de Paris 2024. A partir dos dados extraídos, é possível consultar as informações das medalhas dos 20 primeiros países, filtrando por esporte e país, por meio de uma API.

## Estrutura do Projeto

- **Django Framework**: O backend foi desenvolvido utilizando Django.
- **Django REST Framework**: Para construção da API.
- **BeautifulSoup e Requests**: Utilizadas para realizar o web scraping.
- **Banco de Dados**: SQLite (pode ser alterado conforme necessidade).
  
### Funcionalidades:

1. Web Scraping para capturar dados de medalhas (ouro, prata e bronze) e por esporte.
2. Armazenamento dos dados em um banco de dados relacional.
3. API para consulta das medalhas dos países e esportes.
4. Endpoints para listar os 20 primeiros países no quadro de medalhas.

## Requisitos

- Python 3.x
- Django 4.x
- Django REST Framework
- BeautifulSoup4
- Requests

## Instalação

Siga os passos abaixo para configurar o projeto em seu ambiente local:

### 1. Clone este repositório

```bash
git clone https://github.com/USERNAME/olympics-medals.git
cd olympics-medals

2. Crie um ambiente virtual
É recomendado usar um ambiente virtual para isolar as dependências do projeto. Crie e ative um ambiente virtual com:

```bash
python -m venv env
source env/bin/activate # No Windows: env\Scripts\activate
```

3. Instale as dependências
Instale todas as bibliotecas necessárias usando o pip:

```bash
pip install -r requirements.txt
```

4. Configure o banco de dados
O banco de dados padrão é o SQLite, que já está configurado no arquivo settings.py. Se preferir usar outro banco de dados (PostgreSQL, MySQL, etc.), ajuste as configurações no arquivo olympics/settings.py.

5. Rode as migrações
Execute o comando abaixo para criar as tabelas do banco de dados conforme os modelos definidos:

```bash
python manage.py migrate
```

6. Execute o Web Scraper
Para popular o banco de dados com os dados de medalhas olímpicas, execute o web scraper:

```bash
python manage.py scrape_medals
```

Isso irá capturar os dados da página das Olimpíadas de Paris 2024 e armazená-los no banco de dados.

7. Inicie o servidor
Com o banco de dados populado, você pode iniciar o servidor Django para testar a aplicação:

```bash
python manage.py runserver
```

Acesse a aplicação no navegador através do endereço http://127.0.0.1:8000/.

Endpoints da API
A API está configurada para fornecer os dados das medalhas de acordo com os seguintes endpoints:

1. Consultar o total de medalhas de um país específico
Método: GET
Rota: /api/medals/{country}/
Exemplo: /api/medals/Brazil/
Descrição: Retorna o total de medalhas (ouro, prata, bronze) para o país especificado.
Exemplo de Resposta:
```json
{
"name": "Brazil",
"gold_medals": 8,
"silver_medals": 6,
"bronze_medals": 4
}
```

2. Exibir detalhes dos esportes nos quais um país específico ganhou medalhas
Método: GET
Rota: /api/medals/{country}/sports/
Exemplo: /api/medals/Brazil/sports/
Descrição: Lista os esportes nos quais o país ganhou medalhas, juntamente com a contagem de medalhas para cada esporte.
Exemplo de Resposta:
```json
[
{
"sport": "Football",
"gold_medals": 2,
"silver_medals": 1,
"bronze_medals": 0
},
{
"sport": "Judo",
"gold_medals": 1,
"silver_medals": 2,
"bronze_medals": 1
}
]
```

3. Listar os 20 primeiros países no quadro de medalhas, com suas respectivas medalhas por esporte
Método: GET
Rota: /api/medals/top-20/
Descrição: Retorna os 20 primeiros países no quadro de medalhas, incluindo o número de medalhas (ouro, prata, bronze) conquistadas em cada esporte.
Exemplo de Resposta:
```json
[
{
"name": "USA",
"gold_medals": 25,
"silver_medals": 18,
"bronze_medals": 10
},
{
"name": "China",
"gold_medals": 22,
"silver_medals": 20,
"bronze_medals": 12
}
]
```
```
