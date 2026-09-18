# Validación del workflow en n8n

El JSON exportado es la base del entregable, pero la funcionalidad obligatoria se demuestra ejecutándolo en una instancia n8n.

## Preparación

1. Abre n8n.
2. Importa `entregables_quiz4/workflow_flowlab_tickets.json`.
3. Guarda el workflow.
4. Para una prueba local, usa la URL de prueba que n8n muestra al abrir el Webhook con `Listen for test event`; para producción, activa el workflow y usa la URL de producción.
5. Copia esa URL en `.env` como `VITE_N8N_WEBHOOK_URL` y reinicia Vite.

## Caso válido

Envía un `POST` con este cuerpo:

```json
{
  "customerName": "Sofía Vargas",
  "customerEmail": "sofia@example.com",
  "channel": "Web",
  "message": "Necesito cambiar la dirección de entrega de mi pedido."
}
```

La respuesta esperada es HTTP `200`, con `valid: true`, categoría `Pedido`, prioridad `Alta`, estado `Asignado`, equipo `Servicio al cliente` y `automationStatus: "Routed"`.

## Caso inválido

Envía un `POST` sin `customerEmail` o sin `message`. La respuesta esperada es HTTP `400`, con `valid: false` y `status: "Rechazado"`.

## Evidencia para el quiz

La captura del canvas debe mostrar todos los nodos y conexiones. La ejecución debe mostrar al menos un caso válido y un caso inválido en la pestaña **Executions**. El PDF de justificación explica el problema, las entradas, el procesamiento, las condiciones, las salidas y el valor de negocio.
