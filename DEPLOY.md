# Despliegue como backend

Este proyecto expone un servicio FastAPI para Chatwoot y pruebas directas.

## Ejecutar localmente

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Prueba de salud:

```text
http://localhost:8000/health
```

Prueba del agente:

```bash
curl -X POST http://localhost:8000/test \
  -H "Content-Type: application/json" \
  -d '{"message":"Hola, que cursos tienen?"}'
```

## Render

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

Variables de entorno requeridas:

```env
OPENAI_API_KEY=
SUPABASE_URL=
SUPABASE_SERVICE_KEY=
TAVILY_API_KEY=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=5432
DB_NAME=postgres
CHATWOOT_BASE_URL=
CHATWOOT_ACCOUNT_ID=
CHATWOOT_API_ACCESS_TOKEN=
CHATWOOT_BOT_LABEL=atiende-ia
AGENT_TIMEZONE=America/Bogota
```

Webhook de Chatwoot:

```text
https://TU-DOMINIO/webhook
```
