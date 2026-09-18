# FlowLab — Estado de implementación

Este documento es la fuente de verdad operativa del proyecto. Una capacidad solo se considera existente cuando aparece aquí como implementada y puede verificarse en el código.

## Implementado

- Identidad visual FlowLab orientada a operaciones de atención al cliente.
- Dashboard con métricas de solicitudes abiertas, atención requerida, tiempo de respuesta y procesamiento.
- Bandeja de solicitudes con búsqueda por nombre, ID y mensaje.
- Filtros por todas, nuevas, urgentes, en atención y resueltas.
- Selección de una solicitud y vista de detalle.
- Visualización de cliente, canal, mensaje, categoría, prioridad, equipo y responsable.
- Timeline visual de automatización: `Received → Validated → Classified → Prioritized → Routed → Completed`.
- Creación local de solicitudes mediante formulario.
- Avance local del estado de una solicitud.
- Estado vacío para filtros sin resultados.
- Responsive para escritorio, tablet y móvil.
- Estados de foco visibles para teclado.
- Narrativa operativa visible: recibir mensajes, aplicar reglas y entregar cada caso al equipo correcto.
- Arquitectura frontend separada por configuración, datos, servicios y feature de tickets.
- Cliente n8n aislado en `src/services/n8nClient.js`.
- Modo conectado mediante `VITE_N8N_WEBHOOK_URL` y modo demo explícito cuando la variable está vacía.
- Entregable académico unificado generado en `entregables_quiz4/entregable_unificado_quiz4_flowlab.pdf`.
- El PDF incorpora `captura_n8n.png`, tomada directamente en la instancia n8n, además de la justificación y el JSON exportado.
- La guía de prueba de n8n está en [VALIDACION_N8N.md](VALIDACION_N8N.md); la ejecución real aún requiere importar, activar y probar el workflow en una instancia n8n.

## Simulado

- Las solicitudes iniciales son datos de demostración.
- La creación y el cambio de estado solo modifican el estado React en memoria.
- Las métricas se calculan sobre los datos locales.
- El estado de automatización mostrado no proviene de una ejecución real.

## No implementado

- API REST.
- Persistencia en base de datos.
- Lectura de tickets existentes desde API o n8n.
- Historial persistente de eventos.
- Verificación de una ejecución real en una instancia n8n.
- Autenticación y usuarios reales.
- Pruebas automatizadas de interfaz.

## Siguiente incremento aprobado

1. Añadir una API mínima para crear y consultar solicitudes.
2. Persistir tickets y eventos de automatización.
3. Mapear respuesta y errores del webhook a estados de UI más completos.
4. Incorporar pruebas automatizadas de contrato y flujo principal.

La creación de solicitudes ya puede llamar a n8n cuando se configura `VITE_N8N_WEBHOOK_URL`; sin esa variable, la interfaz permanece en modo demo local y lo informa visualmente.