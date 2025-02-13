import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { ConnectionProvider } from "./state/connectionState";
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ConnectionProvider>
      <App />
    </ConnectionProvider>
  </StrictMode>,
)
