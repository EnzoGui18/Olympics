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
