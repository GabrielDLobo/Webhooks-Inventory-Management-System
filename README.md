# 💻 Webhooks Inventory Management System

Este projeto demonstra a implementação de webhooks para integração entre sistemas, utilizando Django e Python. Ele permite que eventos do sistema de estoque sejam recepcionados e enviados automaticamente para serviços externos, facilitando a comunicação em tempo real entre aplicações.


## 🚀 Objetivo
Criar uma API capaz de:
- Detectar eventos como criação, atualização ou exclusão de produtos
- Criação de serviços desacoplados para envio, recebimento e armazenamento de dados
- Enviar notificações via webhooks para URLs externas
- Simular integrações com sistemas terceiros (ERP, CRM, etc.)
- Boas práticas de arquitetura RESTful


## ⛏️ Instalação

Execute o projeto com Python

```bash
  py manage.py runserver
```

## 💎 Stacks utilizadas

**Back-end:** Python, Django, Django REST Framework, Requests, UUID

 **Database:** SQLite

## 📋 Documentação da API - Webhooks - Endpoint para Recepção dos eventos

```http
  POST api/V1/webhooks/order/
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `PK` | **Obrigatório e Automático** |
| `event type` | `string` |  |
| `event` | `string` |  |
| `created_at` | `datetime` | **Obrigatório e Automático** |
| `updated_at` | `datetime` | **Obrigatório e Automático** |


## 📡 Testando os Webhooks fora do localhost
- Configure uma URL externa (ex: Webhook.site) para receber os eventos.
- Crie um produto no sistema Inventory Management System.
- Verifique se os dados foram enviados corretamente para o endpoint configurado.
