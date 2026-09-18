import { TicketWorkspace } from './features/tickets/TicketWorkspace'
import './App.css'

function App() {
  return <div className="app-shell"><header className="topbar"><div className="brand-wrap"><span className="brand-mark">F</span><div><span className="brand-name">FlowLab</span><small>Customer operations</small></div></div><div className="topbar-actions"><span className="system-status"><i /> Operaciones de soporte</span><button className="avatar" type="button" aria-label="Abrir perfil">AS</button></div></header><main><TicketWorkspace /></main></div>
}

export default App
