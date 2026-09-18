import './App.css'

const workflowNodes = [
  { name: 'Webhook', type: 'Trigger', detail: 'Landing page / formulario web' },
  { name: 'Validación', type: 'Procesamiento', detail: 'Limpieza y scoring del lead' },
  { name: 'IF', type: 'Condición', detail: 'Lead calificado vs. nutrición' },
  { name: 'Google Sheets', type: 'Salida', detail: 'Registro en CRM' },
  { name: 'Slack', type: 'Salida', detail: 'Notificación a ventas' },
  { name: 'Correo', type: 'Salida', detail: 'Email de bienvenida' },
]

const benefits = [
  'Reduce el tiempo de respuesta a leads nuevos.',
  'Evita perder oportunidades por registro manual.',
  'Clasifica la demanda según prioridad y calidad.',
  'Mejora la coordinación entre marketing y ventas.',
]

function App() {
  return (
    <div className="app-shell">
      <header className="topbar">
        <div className="brand-wrap">
          <span className="brand-mark">n8n</span>
          <span className="brand-name">FlowLab</span>
        </div>
        <nav className="nav">
          <a href="#solucion">Solución</a>
          <a href="#flujo">Flujo</a>
          <a href="#entregables">Entregables</a>
        </nav>
      </header>

      <main>
        <section className="hero section-card">
          <div className="hero-content">
            <span className="eyebrow">Quiz #4 · Automatización de negocio</span>
            <h1>Captura y seguimiento automático de leads para ventas.</h1>
            <p className="lead">
              Automatizamos la recepción de leads desde un formulario web, validamos su
a calidad, los clasificamos y los enviamos a los canales correctos para responder
              más rápido y evitar pérdidas de negocio.
            </p>

            <div className="cta-row">
              <a className="primary-btn" href="/entregables_quiz4/documentacion_quiz4.pdf" target="_blank" rel="noreferrer">
                Ver PDF
              </a>
              <a className="secondary-btn" href="/entregables_quiz4/flujo_leads_marketing.json" target="_blank" rel="noreferrer">
                Descargar JSON
              </a>
            </div>
          </div>

          <div className="hero-panel">
            <div className="mini-stat">
              <span>Trigger</span>
              <strong>Webhook</strong>
            </div>
            <div className="mini-stat">
              <span>Condición</span>
              <strong>Lead calificado</strong>
            </div>
            <div className="mini-stat">
              <span>Salidas</span>
              <strong>CRM + Slack + Email</strong>
            </div>
          </div>
        </section>

        <section id="solucion" className="info-grid">
          <article className="section-card">
            <span className="section-tag">Problema</span>
            <h2>Los leads llegan tarde y se pierden</h2>
            <p>
              Cuando un potencial cliente completa el formulario de la landing page, la
              información suele quedar dispersa en correos, hojas de cálculo o mensajes
              manuales. Eso retrasa la atención y reduce la posibilidad de cierre.
            </p>
          </article>

          <article className="section-card">
            <span className="section-tag">Solución</span>
            <h2>Workflow inteligente en n8n</h2>
            <p>
              El flujo recibe el formulario, limpia y valida los datos, determina si el lead
              es calificado y luego lo envía al canal correcto según su prioridad.
            </p>
          </article>
        </section>

        <section id="flujo" className="workflow-section">
          <div className="section-heading">
            <span className="section-tag">Flujo</span>
            <h2>Arquitectura del workflow</h2>
          </div>

          <div className="workflow-diagram" aria-label="Diagrama del flujo n8n">
            {workflowNodes.map((node, index) => (
              <div key={node.name} className={index === 0 ? 'node node-start' : 'node'}>
                <span className="node-name">{node.name}</span>
                <span className="node-type">{node.type}</span>
                <small>{node.detail}</small>
              </div>
            ))}
          </div>
        </section>

        <section className="benefits section-card">
          <div className="section-heading left">
            <span className="section-tag">Valor de negocio</span>
            <h2>Qué genera este flujo</h2>
          </div>
          <ul>
            {benefits.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </section>

        <section id="entregables" className="deliverables section-card">
          <div className="section-heading left">
            <span className="section-tag">Entregables</span>
            <h2>Proyecto completo</h2>
          </div>

          <div className="file-grid">
            <a href="/entregables_quiz4/documentacion_quiz4.pdf" target="_blank" rel="noreferrer">
              <span>PDF</span>
              <strong>Documentación del quiz</strong>
            </a>
            <a href="/entregables_quiz4/flujo_leads_marketing.json" target="_blank" rel="noreferrer">
              <span>JSON</span>
              <strong>Workflow exportado de n8n</strong>
            </a>
            <a href="/entregables_quiz4/canvas_flujo_leads.png" target="_blank" rel="noreferrer">
              <span>PNG</span>
              <strong>Captura del canvas del flujo</strong>
            </a>
          </div>
        </section>
      </main>
    </div>
  )
}

export default App
