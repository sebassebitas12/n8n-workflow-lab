export const AUTOMATION_STEPS = ['Received', 'Validated', 'Classified', 'Prioritized', 'Routed', 'Completed']

export const TICKET_FILTERS = [
  { label: 'Todas', matches: () => true },
  { label: 'Nuevas', matches: (ticket) => ticket.status === 'Nuevo' },
  { label: 'Urgentes', matches: (ticket) => ticket.priority === 'Urgente' },
  { label: 'En atención', matches: (ticket) => ticket.status === 'En atención' },
  { label: 'Resueltas', matches: (ticket) => ticket.status === 'Resuelto' },
]

export const TICKET_STATUSES = ['Nuevo', 'Procesando', 'Asignado', 'En atención', 'Resuelto', 'Cerrado']
