import json
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib import colors

BASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'entregables_quiz4')
os.makedirs(BASE, exist_ok=True)

NORMALIZE_CODE = """const input = $json.body ?? $json;
const customerName = String(input.customerName ?? '').trim();
const customerEmail = String(input.customerEmail ?? '').trim().toLowerCase();
const channel = String(input.channel ?? 'Web').trim();
const message = String(input.message ?? '').trim();
const valid = Boolean(customerName && customerEmail && message && customerEmail.includes('@'));
const lowerMessage = message.toLowerCase();
const category = lowerMessage.includes('pedido') || lowerMessage.includes('entrega') ? 'Pedido' : lowerMessage.includes('precio') || lowerMessage.includes('costo') ? 'Ventas' : lowerMessage.includes('error') || lowerMessage.includes('no funciona') ? 'Soporte' : lowerMessage.includes('reclamo') || lowerMessage.includes('incompleto') ? 'Reclamo' : 'Información';
const priority = lowerMessage.includes('urgente') || lowerMessage.includes('no puedo') || lowerMessage.includes('incompleto') ? 'Alta' : 'Normal';
return [{ json: { customerName, customerEmail, channel, message, category, priority, valid, status: valid ? 'Procesando' : 'Rechazado', automationStatus: 'Classified' } }];"""

workflow = {
    'name': 'FlowLab - Clasificacion y enrutamiento de tickets',
    'nodes': [
        {'id': 'webhook-ticket', 'name': 'Webhook - Nueva solicitud', 'type': 'n8n-nodes-base.webhook', 'typeVersion': 2, 'position': [-640, 0], 'parameters': {'httpMethod': 'POST', 'path': 'flowlab/tickets', 'responseMode': 'responseNode', 'options': {}}},
        {'id': 'normalize-ticket', 'name': 'Code - Validar y clasificar', 'type': 'n8n-nodes-base.code', 'typeVersion': 2, 'position': [-380, 0], 'parameters': {'jsCode': NORMALIZE_CODE}},
        {'id': 'valid-ticket', 'name': 'IF - Solicitud válida', 'type': 'n8n-nodes-base.if', 'typeVersion': 2, 'position': [-120, 0], 'parameters': {'conditions': {'boolean': [{'value1': '={{ $json.valid }}', 'operation': 'true'}]}}},
        {'id': 'priority-ticket', 'name': 'IF - Prioridad alta', 'type': 'n8n-nodes-base.if', 'typeVersion': 2, 'position': [120, 0], 'parameters': {'conditions': {'string': [{'value1': '={{ $json.priority }}', 'operation': 'equals', 'value2': 'Alta'}]}}},
        {'id': 'urgent-ticket', 'name': 'Code - Enrutar prioridad alta', 'type': 'n8n-nodes-base.code', 'typeVersion': 2, 'position': [140, -160], 'parameters': {'jsCode': "return [{ json: { ...$json, assignedTeam: $json.category === 'Ventas' ? 'Ventas' : 'Servicio al cliente', assignedAgent: 'Guardia de prioridad', priority: 'Alta', status: 'Asignado', automationStatus: 'Routed' } }];"}},
        {'id': 'normal-ticket', 'name': 'Code - Enrutar prioridad normal', 'type': 'n8n-nodes-base.code', 'typeVersion': 2, 'position': [140, 160], 'parameters': {'jsCode': "return [{ json: { ...$json, assignedTeam: $json.category === 'Ventas' ? 'Ventas' : 'Servicio al cliente', assignedAgent: 'Cola general', status: 'Asignado', automationStatus: 'Routed' } }];"}},
        {'id': 'respond-valid', 'name': 'Respond - Ticket procesado', 'type': 'n8n-nodes-base.respondToWebhook', 'typeVersion': 1, 'position': [420, 0], 'parameters': {'respondWith': 'json', 'responseBody': '={{ $json }}', 'options': {}}},
        {'id': 'respond-invalid', 'name': 'Respond - Datos inválidos', 'type': 'n8n-nodes-base.respondToWebhook', 'typeVersion': 1, 'position': [140, 420], 'parameters': {'respondWith': 'json', 'responseCode': 400, 'responseBody': '={{ { valid: false, status: "Rechazado", message: "customerName, customerEmail y message son obligatorios" } }}', 'options': {}}},
    ],
    'connections': {
        'Webhook - Nueva solicitud': {'main': [[{'node': 'Code - Validar y clasificar', 'type': 'main', 'index': 0}]]},
        'Code - Validar y clasificar': {'main': [[{'node': 'IF - Solicitud válida', 'type': 'main', 'index': 0}]]},
        'IF - Solicitud válida': {'main': [[{'node': 'IF - Prioridad alta', 'type': 'main', 'index': 0}], [{'node': 'Respond - Datos inválidos', 'type': 'main', 'index': 0}]]},
        'IF - Prioridad alta': {'main': [[{'node': 'Code - Enrutar prioridad alta', 'type': 'main', 'index': 0}], [{'node': 'Code - Enrutar prioridad normal', 'type': 'main', 'index': 0}]]},
        'Code - Enrutar prioridad alta': {'main': [[{'node': 'Respond - Ticket procesado', 'type': 'main', 'index': 0}]]},
        'Code - Enrutar prioridad normal': {'main': [[{'node': 'Respond - Ticket procesado', 'type': 'main', 'index': 0}]]},
    },
    'settings': {'executionOrder': 'v1'}, 'pinData': {}, 'meta': {'templateCredsSetupCompleted': True},
}
json_path = os.path.join(BASE, 'workflow_flowlab_tickets.json')
with open(json_path, 'w', encoding='utf-8') as handle:
    json.dump(workflow, handle, ensure_ascii=False, indent=2)

pdf_path = os.path.join(BASE, 'entregable_unificado_quiz4_flowlab.pdf')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleFlow', parent=styles['Title'], fontSize=20, leading=24, textColor=colors.HexColor('#183b56'), spaceAfter=16))
styles.add(ParagraphStyle(name='HeadingFlow', parent=styles['Heading2'], fontSize=14, leading=18, textColor=colors.HexColor('#176b87'), spaceBefore=12, spaceAfter=8))
styles.add(ParagraphStyle(name='BodyFlow', parent=styles['BodyText'], fontSize=10, leading=15, spaceAfter=6))
styles.add(ParagraphStyle(name='SmallFlow', parent=styles['BodyText'], fontSize=8, leading=11, textColor=colors.HexColor('#52616b')))

story = [
    Paragraph('Quiz #4 · FlowLab', styles['TitleFlow']),
    Paragraph('Clasificación y enrutamiento automático de solicitudes de soporte', styles['HeadingFlow']),
    Paragraph('<b>Solución elegida:</b> Atención al Cliente / Soporte.', styles['BodyFlow']),
    Paragraph('<b>Problema:</b> las solicitudes llegan por varios canales y el equipo pierde tiempo leyendo, clasificando y asignando cada caso manualmente.', styles['BodyFlow']),
    Paragraph('<b>Entrada:</b> React envía al Webhook el nombre, correo, canal y mensaje del cliente.', styles['BodyFlow']),
    Paragraph('<b>Procesamiento:</b> un nodo Code valida los campos, normaliza el correo, detecta la categoría y determina la prioridad con reglas de negocio.', styles['BodyFlow']),
    Paragraph('<b>Condicionales:</b> un IF rechaza datos inválidos y otro separa los casos de prioridad alta de los casos normales.', styles['BodyFlow']),
    Paragraph('<b>Salida:</b> n8n devuelve el ticket con categoría, prioridad, equipo, responsable, estado y resultado de automatización.', styles['BodyFlow']),
    Paragraph('<b>Valor:</b> la solución reduce trabajo repetitivo, acelera la primera respuesta y hace visible quién debe actuar sobre cada solicitud.', styles['BodyFlow']),
    Spacer(1, 8),
    Paragraph('Estructura del workflow', styles['HeadingFlow']),
    Table([['Etapa', 'Nodos', 'Resultado'], ['Trigger', 'Webhook - Nueva solicitud', 'Recibe el ticket desde React'], ['Procesamiento', 'Code - Validar y clasificar', 'Normaliza y determina categoría/prioridad'], ['Condiciones', 'IF - Solicitud válida / IF - Prioridad alta', 'Acepta, rechaza y enruta'], ['Salida', 'Code de enrutamiento / Respond to Webhook', 'Devuelve el ticket procesado']], colWidths=[3.2*cm, 7*cm, 7*cm], style=TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#183b56')), ('TEXTCOLOR', (0,0), (-1,0), colors.white), ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#b8c7d1')), ('VALIGN', (0,0), (-1,-1), 'TOP'), ('FONTSIZE', (0,0), (-1,-1), 8), ('LEADING', (0,0), (-1,-1), 11), ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#f4f8fa')), ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6)])),
    PageBreak(),
    Paragraph('Canvas del workflow', styles['HeadingFlow']),
]

canvas_path = next((os.path.join(BASE, name) for name in ('captura_n8n.png', 'canvas_workflow_flowlab.png') if os.path.exists(os.path.join(BASE, name))), None)
if canvas_path:
    story.append(Image(canvas_path, width=18*cm, height=10.3*cm))
    story.append(Paragraph('Captura tomada directamente desde la instancia n8n.', styles['SmallFlow']))
else:
    story.append(Paragraph('La captura del canvas debe tomarse directamente desde n8n y guardarse como <b>canvas_workflow_flowlab.png</b> en esta carpeta. Al regenerar este PDF se incorporará automáticamente.', styles['BodyFlow']))

story.extend([PageBreak(), Paragraph('Workflow JSON exportado', styles['HeadingFlow']), Preformatted(json.dumps(workflow, ensure_ascii=False, indent=2), styles['Code'])])
SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.4*cm, bottomMargin=1.4*cm, title='Entregable unificado Quiz 4 - FlowLab').build(story)
print(json_path)
print(pdf_path)
