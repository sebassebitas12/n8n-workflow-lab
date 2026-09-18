export class N8nClientError extends Error {
  constructor(message, cause) {
    super(message)
    this.name = 'N8nClientError'
    this.cause = cause
  }
}

export function createN8nClient(webhookUrl) {
  return {
    isConfigured: Boolean(webhookUrl),
    async createTicket(ticket) {
      if (!webhookUrl) {
        throw new N8nClientError('No hay una URL de webhook n8n configurada.')
      }

      try {
        const response = await fetch(webhookUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            customerName: ticket.customerName,
            customerEmail: ticket.customerEmail,
            channel: ticket.channel ?? 'Web',
            message: ticket.message,
          }),
        })

        if (!response.ok) {
          throw new Error(`n8n respondió con HTTP ${response.status}`)
        }

        return await response.json()
      } catch (error) {
        if (error instanceof N8nClientError) throw error
        throw new N8nClientError('No fue posible conectar con el webhook n8n.', error)
      }
    },
  }
}
