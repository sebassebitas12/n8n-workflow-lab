import { useMemo, useState } from 'react'
import { demoTickets } from '../../data/tickets'
import { createN8nClient } from '../../services/n8nClient'
import { TICKET_FILTERS } from './ticket.constants'

function createLocalTicket(input, index) {
  return {
    id: `FL-${1049 + index}`,
    customerName: input.customerName,
    customerEmail: input.customerEmail,
    channel: 'Web',
    message: input.message,
    category: 'Información',
    priority: 'Normal',
    status: 'Nuevo',
    assignedTeam: 'Sin asignar',
    assignedAgent: 'Sin asignar',
    createdAt: 'Ahora',
    automationStatus: 'Received',
  }
}

export function useTickets({ webhookUrl }) {
  const [tickets, setTickets] = useState(demoTickets)
  const [activeFilter, setActiveFilter] = useState('Todas')
  const [selectedId, setSelectedId] = useState(demoTickets[0].id)
  const [search, setSearch] = useState('')
  const [isCreating, setIsCreating] = useState(false)
  const [error, setError] = useState('')
  const client = useMemo(() => createN8nClient(webhookUrl), [webhookUrl])

  const selectedTicket = tickets.find((ticket) => ticket.id === selectedId) ?? tickets[0]
  const visibleTickets = useMemo(() => {
    const filter = TICKET_FILTERS.find((item) => item.label === activeFilter) ?? TICKET_FILTERS[0]
    const normalizedSearch = search.toLowerCase().trim()
    return tickets.filter((ticket) => {
      const matchesSearch = !normalizedSearch || `${ticket.customerName} ${ticket.id} ${ticket.message}`.toLowerCase().includes(normalizedSearch)
      return filter.matches(ticket) && matchesSearch
    })
  }, [activeFilter, search, tickets])

  async function createTicket(input) {
    setError('')
    setIsCreating(true)
    try {
      const localTicket = createLocalTicket(input, tickets.length - demoTickets.length)
      const result = client.isConfigured ? await client.createTicket(input) : null
      const ticket = result?.ticket ?? result?.data ?? result ?? localTicket
      const normalizedTicket = { ...localTicket, ...ticket, id: ticket.id ?? localTicket.id, createdAt: ticket.createdAt ?? 'Ahora' }
      setTickets((current) => [normalizedTicket, ...current])
      setSelectedId(normalizedTicket.id)
      return { mode: client.isConfigured ? 'n8n' : 'demo', ticket: normalizedTicket }
    } catch (requestError) {
      setError(requestError.message)
      throw requestError
    } finally {
      setIsCreating(false)
    }
  }

  function advanceTicket() {
    if (!selectedTicket || selectedTicket.status === 'Resuelto') return
    const nextStatus = selectedTicket.status === 'Nuevo' ? 'Procesando' : selectedTicket.status === 'Procesando' ? 'En atención' : 'Resuelto'
    setTickets((current) => current.map((ticket) => ticket.id === selectedTicket.id ? { ...ticket, status: nextStatus } : ticket))
  }

  return { tickets, visibleTickets, selectedTicket, activeFilter, setActiveFilter, selectedId, setSelectedId, search, setSearch, isCreating, error, createTicket, advanceTicket, isN8nConfigured: client.isConfigured }
}
