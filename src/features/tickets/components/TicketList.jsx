import { TICKET_FILTERS } from '../ticket.constants'

export function TicketList({ tickets, selectedId, onSelect, activeFilter, onFilterChange, search, onSearchChange }) {
  return (
    <section className="inbox-panel section-card">
      <div className="panel-heading">
        <div><h2>Cola de trabajo</h2><span>{tickets.length} casos que requieren seguimiento</span></div>
        <button className="icon-button" type="button" aria-label="Más opciones">•••</button>
      </div>
      <label className="search-box"><span>⌕</span><input value={search} onChange={(event) => onSearchChange(event.target.value)} placeholder="Buscar cliente, caso o mensaje" /></label>
      <div className="filter-row" role="tablist" aria-label="Filtrar solicitudes">
        {TICKET_FILTERS.map((filter) => <button key={filter.label} className={activeFilter === filter.label ? 'filter active' : 'filter'} type="button" onClick={() => onFilterChange(filter.label)}>{filter.label}</button>)}
      </div>
      <div className="request-list">
        {tickets.map((ticket) => <button key={ticket.id} type="button" className={ticket.id === selectedId ? 'request-row selected' : 'request-row'} onClick={() => onSelect(ticket.id)}><div className="request-row-top"><strong>{ticket.customerName}</strong><span>{ticket.createdAt}</span></div><p>{ticket.message}</p><div className="request-meta"><span className={`priority ${ticket.priority.toLowerCase()}`}>{ticket.priority}</span><span>{ticket.category}</span><span>{ticket.id}</span></div></button>)}
        {tickets.length === 0 && <div className="empty-state">No hay solicitudes con estos filtros.</div>}
      </div>
    </section>
  )
}
