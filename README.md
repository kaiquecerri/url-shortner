# 🔗 URL Shortener (Encurtador de URLs)

Um encurtador de links desenvolvido em **Python** com **Django**, permitindo que usuários criem, editem, excluam e redirecionem URLs encurtadas de forma personalizada. A interface conta com suporte a estilização moderna utilizando **Tailwind CSS** e componentes **DaisyUI**.

---

## 📌 Para Que Serve?

O projeto permite transformar URLs longas em links curtos e personalizados. Cada usuário cadastrado possui sua própria área para gerenciar seus links.

### ✨ Principais Funcionalidades:
- **Autenticação de Usuários:**
  - Cadastro de nova conta (`/user/register`)
  - Login de usuários (`/user/login`)
  - Logout (`/user/logout`)
- **Gerenciamento de URLs:**
  - Listagem de URLs criadas exclusivamente pelo usuário autenticado.
  - Criação de links encurtados customizados (definindo nome, URL original e slug encurtado).
  - Edição de URLs já criadas.
  - Exclusão de URLs.
- **Redirecionamento Rápido:**
  - Acesso ao link encurtado via `/acess_url/<slug>` com redirecionamento automático para a URL original.
- **Painel Administrativo:**
  - Interface administrativa completa do Django (`/admin`).

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** [Python](https://www.python.org/) (3.10+) & [Django](https://www.djangoproject.com/)
- **Banco de Dados:** SQLite (padrão de desenvolvimento do Django)
- **Frontend & Estilização:**
  - Django Templates (HTML5)
  - [Tailwind CSS](https://tailwindcss.com/) (v4)
  - [DaisyUI](https://daisyui.com/) (v5)
  - [Node.js](https://nodejs.org/) & npm (para compilação dos assets CSS)

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:
- **[Python](https://www.python.org/downloads/)** (versão 3.10 ou superior)
- **[Node.js](https://nodejs.org/)** (versão 18 ou superior) e **npm**
- **Git** (opcional, para controle de versão)

---

## 🚀 Como Rodar Localmente

Siga o passo a passo abaixo para configurar e executar o projeto no seu computador:

### 1. Configurar o Ambiente Virtual (Python)

Crie e ative um ambiente virtual para isolar as dependências:

**No Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
*(Caso já exista a pasta `shorner-env`, basta ativá-la com `.\shorner-env\Scripts\Activate.ps1`)*

**No Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2. Instalar as Dependências do Python

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

---

### 4. Executar as Migrações do Banco de Dados

Crie as tabelas no banco de dados SQLite:

```bash
python manage.py migrate
```

---

### 5. (Opcional) Criar um Superusuário Administrador

Para acessar o Django Admin (`/admin`), crie um superusuário:

```bash
python manage.py createsuperuser
```
*Preencha o nome de usuário, e-mail e senha conforme solicitado.*

---

### 6. Instalar as Dependências do Frontend (Node.js)

Instale os pacotes necessários para o Tailwind CSS e DaisyUI:

```bash
npm install
```

---

### 7. Compilar o CSS

Gere o arquivo `output.css` a partir do `theme/input.css`:

- **Modo de desenvolvimento (observando alterações):**
  ```bash
  npm run dev:css
  ```
- **Ou build único de produção (minificado):**
  ```bash
  npm run build:css
  ```

---

### 8. Iniciar o Servidor Django

Em um terminal com a venv ativada, inicie a aplicação:

```bash
python manage.py runserver
```
*(Ou utilize o atalho configurado no `package.json`: `npm run dev`)*

---

### 9. Acessar a Aplicação

Abra o seu navegador web e acesse:
- **Página Inicial / Gerenciamento:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Cadastro:** [http://127.0.0.1:8000/user/register](http://127.0.0.1:8000/user/register)
- **Login:** [http://127.0.0.1:8000/user/login](http://127.0.0.1:8000/user/login)
- **Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📂 Estrutura do Projeto

```text
url-shortner/
│
├── shortner/               # App de gerenciamento e redirecionamento de URLs
│   ├── models.py           # Modelo da entidade Url
│   ├── views.py            # Regras de negócio (CRUD e redirecionamento)
│   ├── forms.py            # Formulário de criação/edição da URL
│   ├── urls.py             # Rotas do encurtador
│   └── templates/          # Templates HTML do app shortner
│
├── users/                  # App de autenticação e contas de usuário
│   ├── views.py            # Registro e logout
│   ├── urls.py             # Rotas de login, logout e registro
│   └── templates/          # Templates HTML do app users
│
├── url_shortner/           # Configuração principal do Django
│   ├── settings.py         # Configurações do projeto
│   ├── urls.py             # Roteador central de URLs
│   └── wsgi.py / asgi.py   # Pontos de entrada para servidores
│
├── theme/
│   └── input.css           # Arquivo base com Tailwind e DaisyUI
├── static/
│   └── css/output.css      # CSS compilado e servido estaticamente
│
├── db.sqlite3              # Banco de dados local SQLite
├── manage.py               # Utilitário de linha de comando do Django
├── package.json            # Configurações e scripts npm (Tailwind)
├── requirements.txt        # Dependências do Python
└── README.md               # Documentação do projeto
```

---

## 📜 Scripts Disponíveis (`package.json`)

| Comando | Descrição |
| --- | --- |
| `npm run dev` | Inicia o servidor Django (`python ./manage.py runserver`) |
| `npm run dev:css` | Compila o Tailwind CSS em modo de monitoramento contínuo (`--watch`) |
| `npm run build:css` | Compila e minifica o CSS para produção |
