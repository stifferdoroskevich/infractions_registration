import React, { useState } from 'react';
import { Button, List, ListItem, ListItemText } from '@mui/material';
import axios from 'axios';

const PersonaList = () => {
  const [personas, setPersonas] = useState([]);

  const fetchPersonas = async () => {
    try {
      const response = await axios.get('http://localhost:8000/personas/');
      setPersonas(response.data);
    } catch (error) {
      console.error('Error fetching personas:', error);
      alert(`Error fetching personas: ${error.message}`); // Muestra el error en una alerta
    }
  };

  return (
    <div>
      <Button variant="contained" color="primary" onClick={fetchPersonas}>
        Ver Personas
      </Button>
      <List>
        {personas.map((persona) => (
          <ListItem key={persona.id}>
            <ListItemText primary={persona.nombre} secondary={persona.correo_electronico} />
          </ListItem>
        ))}
      </List>
    </div>
  );
};

export default PersonaList;
