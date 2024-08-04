import React, { useState } from 'react';
import { TextField, Button, Grid } from '@mui/material';
import axios from 'axios';

const PersonaForm = ({ onPersonaCreated }) => {
  const [nombre, setNombre] = useState('');
  const [correo, setCorreo] = useState('');

  // Función para manejar el envío del formulario
  const handleSubmit = async (e) => {
    e.preventDefault();
    //alert('Click realizado 3'); // <-- Muestra un mensaje de alerta en el navegador
    console.log('Formulario enviado'); // <-- Verifica si la función se está ejecutando
    console.log('Nombre:', nombre); // <-- Verifica el valor de nombre
    console.log('Correo:', correo); // <-- Verifica el valor de correo

    try {
      const response = await axios.post('http://localhost:8000/personas/', {
        nombre,
        correo_electronico: correo,
      });
      console.log('Persona creada:', response.data); // <-- Verifica la respuesta de la API

      if (onPersonaCreated) {
        onPersonaCreated(response.data);
      }

      setNombre('');
      setCorreo('');
    } catch (error) {
      console.error('Error creando persona:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <TextField
            label="Nombre"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            required
            fullWidth
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            label="Correo Electrónico"
            value={correo}
            onChange={(e) => setCorreo(e.target.value)}
            required
            fullWidth
          />
        </Grid>
        <Grid item xs={12}>
          <Button type="submit" variant="contained" color="primary" fullWidth>
            Crear Persona
          </Button>
        </Grid>
      </Grid>
    </form>
  );
};

export default PersonaForm;
