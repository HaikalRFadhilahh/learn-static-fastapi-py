# Universitas & Program Studi API

A **FastAPI**-based RESTful API for managing Indonesian universities (**Universitas**) and their study programs (**Program Studi**). This project provides full CRUD operations with in-memory data storage and Pydantic v2 validation.

---

## Features

- CRUD operations for universities and study programs
- Partial update (PATCH) support for universities
- Bulk insert support for study programs
- Search/filter by keyword across multiple fields
- Input validation using Pydantic v2
- Structured JSON responses (success & error)
- No external database required (in-memory storage)

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **FastAPI** | Web framework |
| **Python 3.10+** | Runtime |
| **Pydantic v2** | Data validation & serialization |
| **Uvicorn** | ASGI server (recommended) |

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Install dependencies
pip install fastapi uvicorn pydantic
```

### Running the Server

```bash
# Using FastAPI CLI
fastapi dev main.py

# Or using Uvicorn directly
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`.

### Interactive Documentation

Once the server is running, visit:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## API Endpoints

### Universities (`/universitas`)

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/universitas` | List all universities (`?q=` for search) |
| `GET` | `/universitas/{kodeUniversitas}/detail` | Get university details by code |
| `POST` | `/universitas` | Create a new university |
| `PATCH` | `/universitas/{kodeUniversitas}` | Partially update a university |
| `DELETE` | `/universitas/{kodeUniversitas}` | Delete a university |

### Study Programs (`/prodi`)

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/prodi` | List all study programs across universities (`?q=` for search) |
| `GET` | `/prodi/{kodeUniversitas}` | List study programs of a specific university (`?q=` for search) |
| `POST` | `/prodi/{kodeUniversitas}` | Add study program(s) to a university (single or array) |
| `DELETE` | `/prodi/{kodeUniversitas}/{kodeProgramStudi}` | Delete a study program from a university |

---

## Request / Response Examples

### Create a University

**Request:**

```http
POST /universitas
Content-Type: application/json

{
  "kodeUniversitas": "ITB",
  "namaUniversitas": "Institut Teknologi Bandung",
  "akreditasi": "Unggul",
  "alamat": "Bandung, Jawa Barat",
  "programStudi": [
    {
      "kodeProgramStudi": "STI",
      "namaProgramStudi": "Sarjana Teknik Informatika",
      "akreditasi": "Unggul"
    }
  ]
}
```

**Response:**

```json
{
  "status": "success",
  "message": "Data Universitas berhasil ditambahkan",
  "data": {
    "kodeUniversitas": "ITB",
    "namaUniversitas": "Institut Teknologi Bandung",
    "akreditasi": "Unggul",
    "alamat": "Bandung, Jawa Barat",
    "programStudi": [
      {
        "kodeProgramStudi": "STI",
        "namaProgramStudi": "Sarjana Teknik Informatika",
        "akreditasi": "Unggul"
      }
    ]
  }
}
```

### Update a University (Partial)

**Request:**

```http
PATCH /universitas/AMIKOM
Content-Type: application/json

{
  "akreditasi": "A"
}
```

### Add Study Programs to a University (Bulk)

**Request:**

```http
POST /prodi/UGM
Content-Type: application/json

[
  {
    "kodeProgramStudi": "KEDOKTERAN",
    "namaProgramStudi": "Sarjana Kedokteran",
    "akreditasi": "Unggul"
  },
  {
    "kodeProgramStudi": "HUKUM",
    "namaProgramStudi": "Sarjana Hukum",
    "akreditasi": "A"
  }
]
```

### Search Universities

```http
GET /universitas?q=amikom
```

---

## Data Models

### Universitas

| Field | Type | Constraints |
|---|---|---|
| `kodeUniversitas` | `string` | 3–10 characters, required |
| `namaUniversitas` | `string` | min 3 characters, required |
| `akreditasi` | `enum` | One of: `Unggul`, `A`, `Baik Sekali`, `Baik`, `Cukup`, `Belum Akreditasi` |
| `alamat` | `string` | min 3 characters, required |
| `programStudi` | `array` | List of `ProgramStudi`, optional |

### ProgramStudi

| Field | Type | Constraints |
|---|---|---|
| `kodeProgramStudi` | `string` | 2–10 characters, required |
| `namaProgramStudi` | `string` | 3–100 characters, required |
| `akreditasi` | `enum` | One of: `Unggul`, `A`, `Baik Sekali`, `Baik`, `Cukup`, `Belum Akreditasi` |

---

## Error Handling

All errors return a consistent JSON structure:

```json
{
  "status": "error",
  "message": "Error description",
  "error": [
    {
      "field": "field_name",
      "err": "Validation error message"
    }
  ]
}
```

Common HTTP status codes:

| Status | Description |
|---|---|
| `200` | Success |
| `400` | Validation error |
| `404` | Resource not found |
| `409` | Duplicate resource |

---

## Project Structure

```
├── main.py                  # FastAPI entry point
├── pyproject.toml           # Project configuration
├── README.md                # Documentation
├── data/
│   └── data.py              # In-memory seed data
├── dto/
│   ├── error.py             # Error response schema
│   └── universitas.py       # Insert/Update DTOs
├── error/
│   └── validationError.py   # Validation error handler
├── handler/
│   ├── programStudi.py      # Study program business logic
│   └── universitas.py       # University business logic
├── helper/
│   └── checkKode.py         # Duplicate code checker
├── model/
│   ├── programStudi.py      # ProgramStudi Pydantic model
│   └── universitas.py       # Universitas Pydantic model
└── routes/
    ├── programStudi.py      # Study program route definitions
    └── universitas.py       # University route definitions
```

---

## Seed Data

The API comes pre-loaded with sample data:

| University | Code | Study Programs |
|---|---|---|
| **Universitas Amikom Yogyakarta** | `AMIKOM` | IF, SI, AR, MTI |
| **Universitas Gadjah Mada** | `UGM` | DIKE, FAPERTA |

---

## Running with FastAPI CLI

```bash
fastapi dev main.py
```

This project is configured with `pyproject.toml` for the FastAPI CLI:

```toml
[tool.fastapi]
entrypoint = "main:app"
```

---

## License

This project is for educational/demonstration purposes.
