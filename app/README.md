# 🗳️ VOTING_BBB_API

This project simulates the **voting flow of a reality TV elimination system**, inspired by _Big Brother Brasil (BBB)_. It implements an **event-driven architecture** using **FastAPI**, **Kafka**, and **PostgreSQL**, all containerized with **Docker** and routed through **NGINX**.

---

## 1. 🎯 Objective

The main goal is to emulate the voting pipeline for an elimination round of the BBB reality show. This includes:

- Submitting votes via an API
- Streaming them through Kafka
- Consuming the messages
- Persisting them into a PostgreSQL database

---

## 2. 🧱 Architecture Overview

The architecture follows a **Producer-Consumer** model:

- **FastAPI** acts as the **vote producer**.
- **Kafka** handles **streaming** of vote messages.
- A **consumer service** reads messages and stores them in **PostgreSQL**.
- **NGINX** is configured as a **reverse proxy**, managing traffic between clients and the API.

---

## 3. 🗂️ Project Structure

```bash
VOTING_BBB/
├── app/
│   ├── app_utils/
│   │   └── utils.py           # Utility functions
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── voting.py          # Routes for vote submission
│   │   └── factory.py         # Factory for router setup
│   ├── schemas/
│   │   └── voting_schema.py   # Pydantic models
│
├── src/
│   └── core/
│       └── queues/
│           ├── __init__.py
│           ├── base.py        # Base classes for queues
│           ├── factory.py     # Queue factory
│           └── kafka.py       # Kafka producer/consumer logic
│
├── tests/                     # Test cases
├── venv/                      # Python virtual environment
│
├── .dockerignore              # Docker ignore file
├── .gitignore                 # Git ignore file
├── docker-compose.yml         # Service orchestration (planned)
├── Dockerfile                 # Build instructions (planned)
├── main.py                    # FastAPI application entry point
├── README.md
└── requirements.txt           # Python dependencies
