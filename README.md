# FlowLab

Proyecto académico basado en el **Quiz #4 — Diseño de un Flujo de Automatización en n8n para una Solución de Negocio**.

## Propuesta actual

Se trabajará sobre **Atención al Cliente / Soporte: clasificación y enrutamiento automático de solicitudes**. La solución se adapta a un contexto de pequeñas empresas costarricenses que reciben consultas e incidencias por canales digitales.

## Arquitectura objetivo

**React → API → Webhook n8n → procesamiento y clasificación → condicionales → acción de salida → respuesta**

React es la interfaz de operaciones; la API será la frontera de persistencia y n8n será la capa de automatización. El workflow académico se conserva como evidencia del proceso, no como sustituto de la aplicación.

## Documentación

- [Requerimientos](docs/REQUERIMIENTOS.md)
- [Diseño de producto](docs/DISENO_PRODUCTO.md)
- [Estado de implementación](docs/ESTADO_IMPLEMENTACION.md)
- [Contrato React ↔ n8n](docs/CONTRATO_N8N.md)
- [Validación del workflow en n8n](docs/VALIDACION_N8N.md)

## Estado

**Fase 1 — Prototipo funcional local**

La interfaz ya comunica el producto FlowLab como una herramienta de operaciones de atención al cliente. Incluye dashboard, bandeja de solicitudes, búsqueda, filtros, detalle, creación local de casos, timeline de automatización y avance de estados.

La información actual es de demostración y vive en memoria del navegador. Todavía no existe API, persistencia ni autenticación; la conexión con n8n es opcional y depende de configurar el webhook en `.env`.

La interfaz ya incluye el cliente del webhook. Para activarlo, copia `.env.example` como `.env` y define `VITE_N8N_WEBHOOK_URL` con la URL de prueba o producción del webhook. Sin esa variable, el modo demo local es intencional y se muestra como tal.

El entregable académico unificado es `entregables_quiz4/entregable_unificado_quiz4_flowlab.pdf`; contiene la justificación, el resumen del workflow, la captura real de n8n y el JSON exportado.

## Estructura del frontend

```text
src/
	config/                 Configuración de entorno.
	data/                   Fixtures locales para el modo demo.
	services/               Integraciones externas, incluido n8n.
	features/tickets/       Dominio, hook y componentes de solicitudes.
	App.jsx                 Composición de la aplicación.
```

## Comandos

```bash
npm install
npm run dev
npm run lint
npm run build
```
