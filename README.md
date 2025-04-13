# 📘 Legal Document Verification System - README

This is a **demo project** for a Legal Document Verification System using **Hyperledger Fabric**, **Solidity (Ethereum)**, **FastAPI**, and **PostgreSQL**.

The backend exposes the following API endpoints:

### 📁 `/documents` endpoints:
- `POST /documents/upload` – Upload a document with metadata
- `GET /documents/{doc_id}` – Retrieve document metadata by ID
- `GET /documents/download/{doc_id}` – Download the original document

### 🔍 `/verification` endpoint:
- `POST /verification/verify` – Verify a document's authenticity

## 🛠 Prerequisites

- [Python 3.12+](https://www.python.org)
- [Node.js + npm](https://nodejs.org/) 
- [Docker Desktop](https://www.docker.com/products/docker-desktop) with WSL 2 integration enabled
- [Ganache CLI](https://trufflesuite.com/ganache/):
  ```bash
  sudo npm install -g ganache
  ```

## 🐘 PostgreSQL Setup

```bash
sudo -u postgres psql
CREATE USER docadmin WITH PASSWORD 'your_password';
CREATE DATABASE legaldocdb OWNER docadmin;
\q
```

Make sure your `.env` matches:
```env
DB_USER=docadmin
DB_PASSWORD='your_password'
DB_HOST=localhost
DB_PORT=5432
DB_NAME=legaldocdb
```

## ⛓️ Ethereum (Ganache) Setup

```bash
ganache
```

In another terminal:
```bash
cd blockchain/ethereum
python3
>>> from solcx import install_solc
>>> install_solc("0.8.0")
>>> exit()

python3 deploy_contract.py
```

Output will include:
```
Contract deployed at: 0xABC...
```

## 🌐 Hyperledger Fabric

Ensure Docker Desktop is installed with WSL integration enabled.

Then run:
```bash
docker compose -f blockchain/hyperledger/network/docker-compose.yaml up -d
```
## ⚙️ Backend Setup (FastAPI)

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install requirements:
```bash
pip install -r backend/requirements.txt
```

3. Run the backend:
```bash
cd backend
uvicorn app.main:app --reload
```
## 📂 Example API Usage

### ➕ Upload a Document
```bash
curl -X POST "http://localhost:8000/documents/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/document.pdf" \
  -F 'metadata={"title":"Contract","docType":"Legal","caseNumber":"123","parties":["Alice","Bob"],"tags":["contract"]}'
```

### ✅ Verify a Document
```bash
curl -X POST "http://localhost:8000/verification/verify" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/document.pdf"
```

## 🧩 Environment Variables (`.env`)
```env
DB_USER=docadmin
DB_PASSWORD='your_password'
DB_HOST=localhost
DB_PORT=5432
DB_NAME=legaldocdb

ENCRYPTION_KEY=Fernet key
ETHEREUM_NODE_URL=http://localhost:8545
CONTRACT_ADDRESS=0x... # Fill after deploy
HYPERLEDGER_CONFIG_PATH=blockchain/hyperledger/network/config
```

A valid Fernet key is a base64-encoded 32-byte value, resulting in a 44-character string like:
```bash
u6KD1s7YZKkZkzvRM7oJ4BlEwTqgI7LTyRMUOJ_gG9w=
```
---

Need help? Just ask! 🚀

