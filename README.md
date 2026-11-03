# coffe and creps

Aplicacion de ejemplo con frontend en Vue 3 + TypeScript y API en FastAPI.

## Requisitos

- Node.js 20.19+ o 22.12+
- Python 3.10+

## Iniciar el backend

Desde la raiz del repositorio:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

La API queda disponible en `http://127.0.0.1:8000`. La documentacion interactiva
esta en `http://127.0.0.1:8000/docs`.

## Iniciar el frontend

En otra terminal, desde la raiz del repositorio:

```powershell
cd frontend
npm install
npm run dev
```

Abre la URL que muestra Vite (normalmente `http://localhost:5173`). El frontend
consulta `/api/health` y Vite reenvia esa ruta al backend.
