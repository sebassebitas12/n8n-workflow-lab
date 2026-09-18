import { useState } from 'react'

const initialForm = { customerName: '', customerEmail: '', message: '' }

export function CreateTicketDialog({ isOpen, isSubmitting, error, onClose, onSubmit }) {
  const [form, setForm] = useState(initialForm)
  if (!isOpen) return null

  function updateField(event) {
    setForm((current) => ({ ...current, [event.target.name]: event.target.value }))
  }

  async function submit(event) {
    event.preventDefault()
    await onSubmit(form)
    setForm(initialForm)
  }

  return <div className="modal-backdrop" role="presentation"><form className="modal" onSubmit={submit}><div className="panel-heading"><div><span className="eyebrow">Nueva entrada</span><h2>Crear solicitud</h2></div><button className="icon-button" type="button" aria-label="Cerrar formulario" onClick={onClose}>×</button></div><label>Nombre del cliente<input name="customerName" value={form.customerName} onChange={updateField} required placeholder="Nombre completo" /></label><label>Correo electrónico<input name="customerEmail" value={form.customerEmail} onChange={updateField} type="email" required placeholder="cliente@correo.com" /></label><label>Descripción<textarea name="message" value={form.message} onChange={updateField} required rows="4" placeholder="¿En qué podemos ayudar?" /></label>{error && <p className="form-error" role="alert">{error}</p>}<div className="modal-actions"><button className="secondary-btn" type="button" onClick={onClose}>Cancelar</button><button className="primary-btn" type="submit" disabled={isSubmitting}>{isSubmitting ? 'Enviando...' : 'Crear solicitud'}</button></div></form></div>
}
