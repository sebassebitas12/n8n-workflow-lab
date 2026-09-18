const webhookUrl = import.meta.env.VITE_N8N_WEBHOOK_URL?.trim() ?? ''

export const appConfig = {
  n8nWebhookUrl: webhookUrl,
  isN8nConfigured: Boolean(webhookUrl),
}
