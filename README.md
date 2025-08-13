# 🌐 Webhooks Inventory Management System

Este projeto demonstra a implementação de webhooks para integração entre sistemas, utilizando Django e Python. Ele permite que eventos do sistema de estoque sejam enviados automaticamente para serviços externos, facilitando a comunicação em tempo real entre aplicações.

## 🚀 Objetivo
Criar uma API capaz de:
- Detectar eventos como criação, atualização ou exclusão de produtos
- Enviar notificações via webhooks para URLs externas
- Simular integrações com sistemas terceiros (ERP, CRM, etc.)

## 🧰 Tecnologias utilizadas
- Python 3.7+
- Django
- Django REST Framework
- Requests
- SQLite

## 📦 Estrutura do projeto

- ├── app/
- │   └── models, views, urls
- ├── services/
- │   └── lógica de envio de webhooks
- ├── webhooks/
- │   └── endpoints para receber notificações
- ├── manage.py
- ├── requirements.txt


## 🔧 Como executar

<strong>1. 	Clone o repositório:</strong>
- git clone https://github.com/GabrielDLobo/Webhooks-Inventory-Management-System.git

<strong>2. 	Crie o ambiente virtual e instale as dependências:</strong>
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt

<strong>3. 	Execute as migrations, crie o super usuário e inicie o servidor:</strong>
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver 8001
- Acesse o sistema em: http://localhost:8001/login


## 📡 Testando os Webhooks fora do localhost
- Configure uma URL externa (ex: Webhook.site) para receber os eventos.
- Crie um produto no sistema.
- Verifique se os dados foram enviados corretamente para o endpoint configurado.

## 📚 Aprendizados
- Implementação de webhooks com Django
- Criação de serviços desacoplados para envio, recebimento e armazenamento de dados
- Simulação de integrações com sistemas externos
- Boas práticas de arquitetura RESTful
