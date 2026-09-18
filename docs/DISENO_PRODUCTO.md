# FlowLab — Dirección de producto y diseño

## Concepto

FlowLab será una plataforma moderna de **operaciones de atención al cliente** para pequeñas empresas. El producto convierte solicitudes dispersas en una bandeja organizada donde cada caso es validado, clasificado, priorizado y encaminado automáticamente.

## Identidad

**Nombre:** FlowLab  
**Descriptor:** Customer Operations Automation  
**Personalidad:** tecnológica, rápida, clara, operativa y confiable.

La marca no debe parecer un proyecto académico ni un CRUD genérico. Debe sentirse como un SaaS real de operaciones.

## Dirección visual

Referencia conceptual: dashboards modernos de helpdesk/SaaS con bandeja de tickets, métricas, estados, timeline y vistas de operación. Se tomaron como referencia patrones observados en galerías actuales de diseño de dashboards de soporte, incluyendo inbox unificado, ticket detail, métricas y Kanban. citeturn0search1turn0search3turn0search6

### Estilo

- Dark-first, con posibilidad de light mode posteriormente.
- Fondo carbón/negro suave.
- Superficies ligeramente elevadas.
- Tipografía sans moderna y compacta.
- Verde/teal como color principal de acción y automatización.
- Estados mediante colores semánticos, no decoración.
- Bordes sutiles, radios moderados y sombras contenidas.
- Microanimaciones para cambios de estado y procesamiento.
- Mucha jerarquía visual; evitar tarjetas innecesarias.

## Experiencia principal

### Dashboard

Debe responder rápidamente:

- ¿Cuántas solicitudes están pendientes?
- ¿Cuántas son urgentes?
- ¿Qué está procesando n8n?
- ¿Cuáles requieren intervención humana?
- ¿Cómo está funcionando el sistema?

### Inbox / Solicitudes

Vista principal tipo operations inbox:

- búsqueda
- filtros
- prioridad
- categoría
- estado
- responsable
- canal
- fecha

Cada solicitud tendrá un estado visible y una lectura rápida antes de abrir el detalle.

### Detalle

El detalle combinará:

- información del cliente
- mensaje original
- categoría detectada
- prioridad
- responsable
- estado
- timeline de eventos
- resultado de automatización
- acciones manuales

### Automatización

No será una pantalla decorativa. Mostrará el estado real del procesamiento:

**Received → Validated → Classified → Prioritized → Routed → Completed**

Esto permitirá demostrar visualmente el trabajo de n8n.

## Modelo inicial

### Ticket

- id
- customerName
- customerEmail
- channel
- message
- category
- priority
- status
- assignedTeam
- assignedAgent
- createdAt
- updatedAt
- automationStatus

### Categorías

- ventas
- pedido
- reclamo
- soporte
- información

### Prioridades

- baja
- normal
- alta
- urgente

### Estados

- nuevo
- procesando
- asignado
- en atención
- resuelto
- cerrado

## Principio de producto

La automatización debe ahorrar trabajo real. Si n8n puede determinar una categoría, prioridad o responsable de forma confiable, lo hará; si el caso necesita criterio humano, la aplicación debe hacerlo evidente.

## Arquitectura conceptual

**React UI → API REST → n8n Webhook → procesamiento → API/registro → React**

La aplicación no dependerá directamente de n8n para toda su persistencia. La automatización será una capa de proceso, no el sustituto de la arquitectura del producto.

## MVP

1. Dashboard.
2. Inbox de solicitudes.
3. Crear solicitud.
4. Detalle de solicitud.
5. Clasificación y prioridad.
6. Estados y asignación.
7. Workflow n8n.
8. Historial/timeline.
9. Métricas básicas.
10. Estados de loading/error/empty/success.

## Fuera del MVP

- WhatsApp real.
- CRM comercial real.
- IA generativa obligatoria.
- Multiempresa.
- Facturación.
- Autenticación empresarial avanzada.
- Integraciones de producción no necesarias para demostrar el flujo.

Estas funciones pueden investigarse posteriormente, pero no se incorporarán únicamente para aumentar el tamaño del proyecto.
