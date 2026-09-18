export function TicketMetrics({ tickets, isN8nConfigured }) {
  const openTickets = tickets.filter((ticket) => !['Resuelto', 'Cerrado'].includes(ticket.status)).length
  const attentionTickets = tickets.filter((ticket) => ['Urgente', 'Alta'].includes(ticket.priority)).length

  return <section className="metrics-grid" aria-label="Resumen de la operación"><article><span>Casos en la cola</span><strong>{openTickets}</strong><small className="positive">Esperan resolución</small></article><article><span>Intervención prioritaria</span><strong>{attentionTickets}</strong><small className="warning">Alta o urgente</small></article><article><span>Primera respuesta</span><strong>18 min</strong><small className="positive">Promedio del turno</small></article><article><span>Canal de entrada</span><strong className="metric-status">{isN8nConfigured ? 'Conectado' : 'Demo'}</strong><small className={isN8nConfigured ? 'positive' : 'muted'}>{isN8nConfigured ? 'n8n está recibiendo casos' : 'Datos locales de ejemplo'}</small></article></section>
}
