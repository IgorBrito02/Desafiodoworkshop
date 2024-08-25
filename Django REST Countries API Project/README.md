# Django REST Countries API Project

Este projeto Django é uma API REST para gerenciar dados de países, consumindo a API externa REST Countries e armazenando as informações em um banco de dados. O projeto inclui funcionalidades para criar, listar, atualizar e excluir países, além de traduzir capitais e fornecer uma interface administrativa.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos e pastas:

- `admin.py`: Configurações do painel administrativo do Django.
- `apps.py`: Configuração do aplicativo Django.
- `forms.py`: Formulários utilizados para criar e atualizar países.
- `models.py`: Definição dos modelos `Region`, `Subregion`, e `Country`.
- `views.py`: Definição das visualizações para manipulação dos dados dos países e renderização das páginas.
- `settings.py`: Configurações principais do Django.
- `urls.py`: Definições de URLs para o projeto.
- `templates/`: Contém os templates HTML utilizados pelo projeto.
- `static/`: Contém arquivos estáticos como CSS e imagens.

## Instalação e Configuração

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. **Crie um ambiente virtual e ative-o:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure as variáveis de ambiente:**

    Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

    ```env
    DJANGO_SECRET_KEY=your-secret-key
    DJANGO_DEBUG=True
    ```

5. **Execute as migrações do banco de dados:**

    ```bash
    python manage.py migrate
    ```

6. **Crie um superusuário para acessar o painel administrativo:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

## Estrutura dos Arquivos

### `admin.py`

Configuração do painel administrativo para o modelo `Country`.

```python
from django.contrib import admin
from .models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital', 'population', 'region', 'subregion', 'alpha2Code', 'alpha3Code', 'additional_info')
