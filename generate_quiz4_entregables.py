import os
import json
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

base = os.path.join(os.getcwd(), 'entregables_quiz4')
os.makedirs(base, exist_ok=True)

workflow = {
    "name": "Lead Marketing - Captura y seguimiento automático",
    "nodes": [
        {
            "id": "webhook-1",
            "name": "Webhook - Landing Page",
            "type": "n8n-nodes-base.webhook",
            "typeVersion": 1,
            "position": [-200, 0],
            "parameters": {
                "httpMethod": "POST",
                "path": "lead-nuevo",
                "responseMode": "onReceived",
                "options": {}
            }
        },
        {
            "id": "set-1",
            "name": "Code - Validar y limpiar datos",
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [0, 0],
            "parameters": {
                "jsCode": "const lead = $json;\nconst email = (lead.email || '').trim().toLowerCase();\nconst nombre = (lead.nombre || '').trim();\nconst telefono = (lead.telefono || '').trim();\nconst fuente = (lead.fuente || 'web');\nconst score = Number(lead.score || 0);\nreturn [{ json: { nombre, email, telefono, fuente, score, valid: !!(nombre && email && score >= 0) } }];"
            }
        },
        {
            "id": "if-1",
            "name": "IF - Lead calificado",
            "type": "n8n-nodes-base.if",
            "typeVersion": 1,
            "position": [220, 0],
            "parameters": {
                "conditions": {
                    "number": [
                        { "value1": "={{ $json.score }}", "operation": "largerEqual", "value2": 70 }
                    ]
                }
            }
        },
        {
            "id": "sheet-1",
            "name": "Google Sheets - Crear contacto",
            "type": "n8n-nodes-base.googleSheets",
            "typeVersion": 4,
            "position": [440, -180],
            "parameters": {
                "sheetId": "CRM_Leads",
                "operation": "appendOrUpdate",
                "documentId": "crm-leads"
            }
        },
        {
            "id": "slack-1",
            "name": "Slack - Notificar vendedor",
            "type": "n8n-nodes-base.slack",
            "typeVersion": 2,
            "position": [660, -180],
            "parameters": {
                "channel": "#ventas",
                "text": "Nuevo lead calificado: {{ $json.nombre }}"
            }
        },
        {
            "id": "gmail-1",
            "name": "Gmail - Bienvenida + oferta",
            "type": "n8n-nodes-base.gmail",
            "typeVersion": 2,
            "position": [440, 180],
            "parameters": {
                "subject": "Bienvenido/a a nuestra comunidad",
                "message": "Hola {{ $json.nombre }}, gracias por contactarnos."
            }
        },
        {
            "id": "email-1",
            "name": "Gmail - Nutrición por correo",
            "type": "n8n-nodes-base.gmail",
            "typeVersion": 2,
            "position": [660, 180],
            "parameters": {
                "subject": "Recibe información sobre nuestros servicios",
                "message": "Hola {{ $json.nombre }}, te dejamos más detalle."
            }
        }
    ],
    "connections": {
        "webhook-1": {
            "main": [[{ "node": "set-1", "type": "main", "index": 0 }]]
        },
        "set-1": {
            "main": [[{ "node": "if-1", "type": "main", "index": 0 }]]
        },
        "if-1": {
            "main": [
                [{ "node": "sheet-1", "type": "main", "index": 0 }, { "node": "slack-1", "type": "main", "index": 0 }],
                [{ "node": "gmail-1", "type": "main", "index": 0 }, { "node": "email-1", "type": "main", "index": 0 }]
            ]
        }
    },
    "settings": { "executionOrder": "v1" },
    "staticData": None,
    "meta": { "instanceId": "quiz4-n8n-flowlab" },
    "pinData": {}
}

json_path = os.path.join(base, 'flujo_leads_marketing.json')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(workflow, f, ensure_ascii=False, indent=2)

img = Image.new('RGB', (1600, 900), '#F7F8FB')
draw = ImageDraw.Draw(img)

try:
    title_font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 30)
    node_font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 20)
    small_font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 16)
except Exception:
    title_font = ImageFont.load_default()
    node_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

nodes = [
    {'name': 'Webhook\nLanding Page', 'x': 80, 'y': 350, 'w': 220, 'h': 120, 'color': '#E3F2FD'},
    {'name': 'Code\nValidar y limpiar\ndatos', 'x': 400, 'y': 350, 'w': 260, 'h': 140, 'color': '#E8F5E9'},
    {'name': 'IF\nLead calificado', 'x': 760, 'y': 350, 'w': 220, 'h': 120, 'color': '#FFF3E0'},
    {'name': 'Google Sheets\nCrear contacto', 'x': 1080, 'y': 180, 'w': 260, 'h': 120, 'color': '#F3E5F5'},
    {'name': 'Slack\nNotificar vendedor', 'x': 1080, 'y': 50, 'w': 260, 'h': 110, 'color': '#E0F7FA'},
    {'name': 'Gmail\nBienvenida + oferta', 'x': 1080, 'y': 510, 'w': 260, 'h': 120, 'color': '#FCE4EC'},
    {'name': 'Gmail\nNutrición por correo', 'x': 1080, 'y': 680, 'w': 260, 'h': 120, 'color': '#EDE7F6'}
]

draw.text((60, 30), 'Workflow n8n - Lead Marketing', fill='#1F2937', font=title_font)

for n in nodes:
    x, y, w, h = n['x'], n['y'], n['w'], n['h']
    draw.rounded_rectangle((x, y, x + w, y + h), radius=16, fill=n['color'], outline='#374151', width=2)
    bbox = draw.textbbox((0, 0), n['name'], font=node_font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((x + (w - tw) / 2, y + (h - th) / 2), n['name'], fill='#111827', font=node_font)

for a, b in [(1, 2), (2, 3), (3, 4), (3, 5), (3, 6), (3, 7)]:
    x1, y1, w1, h1 = nodes[a - 1]['x'], nodes[a - 1]['y'], nodes[a - 1]['w'], nodes[a - 1]['h']
    x2, y2, w2, h2 = nodes[b - 1]['x'], nodes[b - 1]['y'], nodes[b - 1]['w'], nodes[b - 1]['h']
    start = (x1 + w1, y1 + h1 / 2)
    end = (x2, y2 + h2 / 2)
    draw.line([start, (start[0] + 60, start[1]), (end[0] - 60, start[1]), end], fill='#4B5563', width=4)
    draw.polygon([(end[0] - 12, end[1] - 8), (end[0], end[1]), (end[0] - 12, end[1] + 8)], fill='#4B5563')

legend = [
    ('Trigger', '#E3F2FD'),
    ('Procesamiento', '#E8F5E9'),
    ('Condición', '#FFF3E0'),
    ('Salida', '#F3E5F5')
]
for i, (label, color) in enumerate(legend):
    x = 60 + i * 260
    draw.rounded_rectangle((x, 820, x + 180, 870), radius=12, fill=color, outline='#374151', width=1)
    draw.text((x + 90, 845), label, fill='#111827', font=small_font, anchor='mm')

img_path = os.path.join(base, 'canvas_flujo_leads.png')
img.save(img_path)

pdf_path = os.path.join(base, 'documentacion_quiz4.pdf')
can = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4
can.setTitle('Quiz 4 - Flujo de Automatización n8n')
can.setFont('Helvetica-Bold', 20)
can.drawString(50, height - 50, 'Quiz #4 - Diseño de flujo de automatización en n8n')
can.setFont('Helvetica', 12)
texto = [
    'Solución elegida: Ventas / Marketing',
    'Problema de negocio: los leads generados en la landing page se registran tarde y pueden perderse si no se atienden a tiempo.',
    'El flujo inicia con un Webhook que recibe la información del formulario de contacto.',
    'Un nodo de validación limpia y valida correo, teléfono, fuente y score para identificar si el lead tiene potencial.',
    'La condición IF decide si el lead es calificado o si debe ser nutrido con información y seguimiento por correo.',
    'Si el lead es valioso, se registra en Google Sheets y se notifica al vendedor en Slack para una respuesta rápida.',
    'Si no es calificado, se envía un correo de bienvenida con contenido adicional para mantener la relación.',
    'Valor generado: reduce la demora en la atención, mejora la conversión y evita que oportunidades importantes queden sin seguimiento.'
]

current_y = height - 110
for line in texto:
    can.drawString(50, current_y, line)
    current_y -= 22

can.drawImage(img_path, 55, 130, width=500, height=300)
can.setFont('Helvetica-Oblique', 10)
can.drawString(55, 110, 'Captura del canvas del workflow implementado en n8n (diagrama representativo del flujo).')
can.save()

print('JSON:', json_path)
print('PNG:', img_path)
print('PDF:', pdf_path)
print('Archivos generados correctamente.')
