import { AUTOMATION_STEPS } from '../ticket.constants'

export function TicketDetail({ ticket, onAdvance }) {
  if (!ticket) return <aside className="detail-panel section-card"><div className="empty-state">Selecciona una solicitud para ver su detalle.</div></aside>
  const automationIndex = AUTOMATION_STEPS.indexOf(ticket.automationStatus)

  return (
    <aside className="detail-panel section-card">
      <div className="detail-heading"><div><span className="detail-id">{ticket.id}</span><h2>{ticket.customerName}</h2></div><button className="icon-button" type="button" aria-label="Cerrar detalle">×</button></div>
      <p className="customer-email">{ticket.customerEmail} · {ticket.channel}</p>
      <div className="detail-tags"><span className={`priority ${ticket.priority.toLowerCase()}`}>{ticket.priority}</span><span className="status-pill">{ticket.status}</span></div>
      <div className="detail-section"><h3>Mensaje original</h3><p className="message">{ticket.message}</p></div>
      <div className="detail-section"><h3>Decisión de operación</h3><dl className="data-list"><div><dt>Categoría detectada</dt><dd>{ticket.category}</dd></div><div><dt>Equipo que atiende</dt><dd>{ticket.assignedTeam}</dd></div><div><dt>Responsable actual</dt><dd>{ticket.assignedAgent}</dd></div></dl></div>
      <div className="detail-section automation"><div className="automation-title"><h3>Recorrido del caso</h3><span>{ticket.automationStatus}</span></div><p className="automation-note">Reglas de FlowLab aplicadas antes de asignar este caso.</p><div className="timeline">{AUTOMATION_STEPS.map((step, index) => <div key={step} className={index <= automationIndex ? 'timeline-step done' : 'timeline-step'}><i />{step}</div>)}</div></div>
      <button className="advance-btn" type="button" onClick={onAdvance} disabled={ticket.status === 'Resuelto'}>{ticket.status === 'Resuelto' ? 'Caso resuelto' : 'Avanzar estado'}</button>
    </aside>
  )
}
