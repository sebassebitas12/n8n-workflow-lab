# Contrato React ↔ n8n

Este contrato define la única forma soportada de enviar una solicitud desde FlowLab al workflow. El endpoint se configura con `VITE_N8N_WEBHOOK_URL`.

## Solicitud

```json
{
  "customerName": "Sofía Vargas",
  "customerEmail": "sofia@example.com",
  "channel": "Web",
  "message": "Necesito cambiar la dirección de entrega de mi pedido."
}
```

Campos obligatorios: `customerName`, `customerEmail` y `message`. `channel` puede omitirse y el cliente lo completa como `Web`.

## Respuesta exitosa

```json
{
  "customerName": "Sofía Vargas",
  "customerEmail": "sofia@example.com",
  "channel": "Web",
  "message": "Necesito cambiar la dirección de entrega de mi pedido.",
  "category": "Pedido",
  "priority": "Alta",
  "valid": true,
  "status": "Asignado",
  "assignedTeam": "Servicio al cliente",
  "assignedAgent": "Guardia de prioridad",
  "automationStatus": "Routed"
}
```

## Respuesta inválida

El workflow debe responder HTTP `400` con `valid: false`, `status: "Rechazado"` y un mensaje legible. React muestra el error sin insertar el caso en la bandeja.

## Estados permitidos

- `status`: `Nuevo`, `Procesando`, `Asignado`, `En atención`, `Resuelto`, `Cerrado`.
- `priority`: `Baja`, `Normal`, `Alta`, `Urgente`.
- `automationStatus`: `Received`, `Validated`, `Classified`, `Prioritized`, `Routed`, `Completed`.

El workflow exportado en `entregables_quiz4/workflow_flowlab_tickets.json` implementa este contrato sin credenciales externas. La verificación contra una instancia n8n real sigue siendo responsabilidad del laboratorio de integración.
