import { useState } from 'react'
import { appConfig } from '../../config/env'
import { CreateTicketDialog } from './components/CreateTicketDialog'
import { TicketDetail } from './components/TicketDetail'
import { TicketList } from './components/TicketList'
import { TicketMetrics } from './components/TicketMetrics'
import { useTickets } from './useTickets'

export function TicketWorkspace() {
  const [isCreateOpen, setIsCreateOpen] = useState(false)
  const tickets = useTickets({ webhookUrl: appConfig.n8nWebhookUrl })

  async function handleCreate(input) {
    await tickets.createTicket(input)
    setIsCreateOpen(false)
  }

  return <>
    <section className="page-heading"><div><p className="eyebrow">Mesa de soporte · Turno actual</p><h1>Que ningún caso se pierda.</h1><p className="lead">FlowLab reúne los mensajes de tus clientes, aplica las reglas de atención y deja cada caso en manos del equipo correcto.</p></div><button className="primary-btn" type="button" onClick={() => setIsCreateOpen(true)}>+ Registrar caso</button></section>
    <section className="operation-context" aria-label="Cómo funciona FlowLab"><div><span className="context-number">01</span><div><strong>Recibir</strong><p>Un cliente escribe por web, correo o chat.</p></div></div><div><span className="context-number">02</span><div><strong>Decidir</strong><p>Las reglas detectan categoría y urgencia.</p></div></div><div><span className="context-number">03</span><div><strong>Actuar</strong><p>El caso llega al equipo que puede resolverlo.</p></div></div></section>
    {!tickets.isN8nConfigured && <div className="connection-banner" role="status"><strong>Modo demo local</strong><span>Configura <code>VITE_N8N_WEBHOOK_URL</code> para enviar solicitudes a n8n.</span></div>}
    {tickets.error && <div className="connection-banner error" role="alert"><strong>Falló la conexión</strong><span>{tickets.error}</span></div>}
    <TicketMetrics tickets={tickets.tickets} isN8nConfigured={tickets.isN8nConfigured} />
    <section className="workspace-grid"><TicketList tickets={tickets.visibleTickets} selectedId={tickets.selectedId} onSelect={tickets.setSelectedId} activeFilter={tickets.activeFilter} onFilterChange={tickets.setActiveFilter} search={tickets.search} onSearchChange={tickets.setSearch} /><TicketDetail ticket={tickets.selectedTicket} onAdvance={tickets.advanceTicket} /></section>
    <CreateTicketDialog isOpen={isCreateOpen} isSubmitting={tickets.isCreating} error={tickets.error} onClose={() => setIsCreateOpen(false)} onSubmit={handleCreate} />
  </>
}
