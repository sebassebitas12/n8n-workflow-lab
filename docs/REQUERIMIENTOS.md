# FlowLab — Requerimientos del proyecto

## 1. Contexto

FlowLab nace a partir del Quiz #4: **Diseño de un Flujo de Automatización en n8n para una Solución de Negocio**. El entregable académico obligatorio es un workflow funcional en n8n que automatice un proceso real de negocio mediante trigger, procesamiento, condicionales, transformación de datos e integración/salida.

## 2. Solución seleccionada

**Atención al Cliente / Soporte — Clasificación y enrutamiento automático de solicitudes.**

El escenario conserva la lógica propuesta por el quiz, pero se adapta a un contexto de pequeñas empresas costarricenses que reciben atención y solicitudes por canales digitales.

## 3. Problema de negocio

Una pequeña empresa recibe consultas, solicitudes e incidencias de clientes mediante canales digitales. Los mensajes pueden pertenecer a categorías distintas y tener diferentes niveles de urgencia, por lo que el personal debe leerlos, clasificarlos y dirigirlos manualmente a la persona responsable. Esto dificulta el seguimiento y consume tiempo operativo.

## 4. Evidencia de contexto costarricense

La elección se apoya en datos recientes del INEC: 93,9% de las microempresas tiene acceso a Internet y el uso de Internet para atender clientes es reportado por una proporción muy alta de las microempresas. El proyecto usa estos datos como contexto general; no afirma que una empresa específica tenga el problema descrito.

## 5. Objetivo

Diseñar una solución web que permita registrar solicitudes de clientes y utilizar n8n como capa de automatización para validar, transformar, clasificar, priorizar y enrutar cada solicitud hacia el área responsable.

## 6. Flujo conceptual

**Cliente → React → API → Webhook n8n → Validación/normalización → Clasificación → Priorización → Condicional → Asignación → Registro/notificación → API/React**

## 7. Responsabilidades

### React
- Interfaz para registrar y consultar solicitudes.
- Visualización de estados, prioridad, categoría y responsable.
- Estados de carga, error, vacío y éxito.

### API
- Recibir y exponer solicitudes.
- Persistir datos del dominio.
- Servir como frontera entre la aplicación y las automatizaciones.

### n8n
- Recibir solicitudes mediante Webhook.
- Validar y normalizar datos.
- Clasificar la solicitud.
- Determinar prioridad.
- Enrutar mediante condiciones.
- Ejecutar la acción de salida y devolver una respuesta consistente.

## 8. Ejemplos de clasificación

- "Mi pedido llegó incompleto" → Reclamo/Pedido → prioridad alta → Servicio al cliente.
- "¿Cuánto cuesta entregar en Curridabat?" → Consulta/Ventas → prioridad normal → Ventas.
- "Necesito cambiar la dirección de mi pedido" → Cambio de pedido → prioridad alta → Operaciones.

## 9. Requisitos del Quiz #4

1. Elegir una de las cinco soluciones propuestas.
2. Identificar trigger, procesamiento, condicionales y salida.
3. Construir el workflow con nodos reales de n8n; se permiten Webhook, Set y NoOp como simulación cuando un servicio externo no esté disponible.
4. Exportar el workflow como archivo JSON.
5. Capturar el canvas completo.
6. Redactar una justificación de negocio de 5–8 líneas.

### Entregables académicos

- Workflow JSON exportado.
- Captura(s) del workflow completo.
- Documento breve de justificación.

## 10. Criterios de validación

- Trigger adecuado al caso.
- Lógica correcta de transformación, condiciones y manejo de datos.
- Integración coherente entre nodos.
- Ejecución sin errores o simulación consistente.
- Justificación clara del valor de negocio.

## 11. Alcance inicial

El proyecto se desarrollará incrementalmente. Primero se documentará y validará el dominio; después se definirá la arquitectura React/API/n8n, el contrato de datos, el workflow y finalmente la interfaz y pruebas.

No se agregan funciones únicamente para hacer el proyecto más grande: cada función deberá justificar su relación con el problema de negocio.

## 12. Decisión de diseño

La identidad visual y el diseño de la interfaz se definirán desde el inicio, pero sin permitir que el diseño sustituya la lógica del producto. La aplicación deberá comunicar claramente que es una herramienta de operaciones y gestión de solicitudes, no simplemente un formulario conectado a n8n.

## 13. Pendientes antes de implementar

- Definir el tipo de empresa/caso de uso representativo.
- Definir entidades y estados del dominio.
- Definir contrato React/API/n8n.
- Elegir persistencia para el MVP.
- Diseñar el workflow definitivo.
- Definir estrategia de pruebas.
- Crear identidad visual y mockups.

## 14. Estado verificado

La interfaz cuenta actualmente con un prototipo local de dashboard, bandeja, detalle, creación de solicitudes y avance de estados. Estas funciones trabajan con datos en memoria y no representan todavía una integración con API o n8n. El estado detallado y las capacidades que no existen se mantienen en [ESTADO_IMPLEMENTACION.md](ESTADO_IMPLEMENTACION.md).
