import React, { useState } from 'react';
import { Container, AppBar, Toolbar, Typography } from '@mui/material';
import PersonaForm from './components/PersonaForm';
import PersonaList from './components/PersonaList';

function App() {
  const [personas, setPersonas] = useState([]);

  // Función para manejar la creación de una nueva persona
  const handlePersonaCreated = (newPersona) => {
    setPersonas((prevPersonas) => [...prevPersonas, newPersona]);
  };

  return (
    <Container>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">Sistema de Registro de Infracciones de Tránsito</Typography>
        </Toolbar>
      </AppBar>
      <PersonaForm onPersonaCreated={handlePersonaCreated} />
      <PersonaList personas={personas} setPersonas={setPersonas} />
    </Container>
  );
}

export default App;
