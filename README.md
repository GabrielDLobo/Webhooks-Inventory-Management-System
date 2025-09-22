# 🔗📦 Webhooks Inventory Management System

---

### English Version

A Django-based inventory management system enhanced with **webhook integration** to enable real-time communication between services. This project builds upon traditional inventory control by allowing external systems to receive updates when products are created, updated, or deleted.

### PT/BR

Um sistema de gestão de estoque baseado em Django com integração via **webhooks**, permitindo comunicação em tempo real entre serviços. O projeto expande o controle tradicional de estoque ao permitir que sistemas externos recebam notificações quando produtos são criados, atualizados ou excluídos.


### English Version
Note: these webhooks are a continuation of the inventory management system, follow the link of the project: https://github.com/GabrielDLobo/02-Inventory-Management-System


### PT/BR
Observação: estes webhooks são uma continuação do projeto inventory management system, segue o link do projeto principal: https://github.com/GabrielDLobo/02-Inventory-Management-System

---

## 🚀 Features | Funcionalidades

- 📦 Product CRUD with webhook triggers  
- 🔐 JWT-based authentication  
- 📤 Webhook delivery with retry logic  
- 🧾 Supplier, Category, Brand modules  
- 📊 RESTful API with modular structure  
- 🧠 Optional AI integration (OpenAI)

### PT/BR 

- 📦 CRUD de produtos com disparo de webhooks  
- 🔐 Autenticação baseada em JWT  
- 📤 Entrega de webhooks com lógica de re-tentativas  
- 🧾 Módulos de Fornecedores, Categorias e Marcas  
- 📊 API RESTful com estrutura modular  
- 🧠 Integração opcional com IA (OpenAI)

---

## 🚀 Objective / Objetivo

Build an API capable of:
- Detecting events such as product creation, update, or deletion  
- Creating decoupled services for sending, receiving, and storing data  
- Sending real-time notifications via webhooks to external URLs  
- Simulating integrations with third-party systems (ERP, CRM, etc.)  
- Following best practices in RESTful architecture

### PT/BR

Criar uma API capaz de:
- Detectar eventos como criação, atualização ou exclusão de produtos
- Criação de serviços desacoplados para envio, recebimento e armazenamento de dados
- Enviar notificações via webhooks para URLs externas
- Simular integrações com sistemas terceiros (ERP, CRM, etc.)
- Boas práticas de arquitetura RESTful

---

## ⛏️ Installation / Instalação

Execute the Python project

```bash
  py manage.py runserver
```

---

## 🧪 Tech Stack | Stacks Utilizadas

| Layer         | Technologies                                 |
|---------------|----------------------------------------------|
| Back-end      | Python, Django, Django Rest Framework        |
| Auth          | Simple JWT                                   |
| Webhooks      | Custom Django signals + HTTP requests + UUID |
| Database      | Sqlite                                       |
| AI (optional) | OpenAI                                       |

---

# 📋 API Reference | Documentação Geral da API

## 🔔 Webhooks Module | Módulo de Webhooks

### POST /api/v1/webhooks/order/ — Receive Webhook Event  
Receives external webhook events sent by third-party systems.  
Recebe eventos de webhook enviados por sistemas terceiros.

#### Request Body | Corpo da Requisição

| Parameter      | Type     | Required | Description / Descrição                     |
|----------------|----------|----------|---------------------------------------------|
| `id`           | PK       | ✅       | Auto-generated ID / ID gerado automaticamente |
| `event_type`   | string   | ✅       | Type of event (e.g. product.created) / Tipo do evento |
| `event`        | string   | ✅       | Event payload or description / Conteúdo ou descrição do evento |
| `created_at`   | datetime | ✅       | Timestamp of creation / Data de criação     |
| `updated_at`   | datetime | ✅       | Timestamp of update / Data de atualização   |

#### Example Payload | Exemplo de Payload

```json
{
  "event_type": "product.updated",
  "event": "Product ID 12 updated with new quantity",
  "created_at": "2025-09-22T12:00:00Z",
  "updated_at": "2025-09-22T12:00:00Z"
}
```

## 📡  Testing Webhooks Outside Localhost / Testando os Webhooks fora do localhost

- Set up an external URL (e.g., Webhook.site) to receive incoming events  
- Create a product in the Inventory Management System  
- Verify that the data was successfully sent to the configured endpoint

### PT/BR
- Configure uma URL externa (ex: Webhook.site) para receber os eventos.
- Crie um produto no sistema Inventory Management System.
- Verifique se os dados foram enviados corretamente para o endpoint configurado.