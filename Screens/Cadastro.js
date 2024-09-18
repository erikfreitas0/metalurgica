// src/Cadastro.js
import React, { useState } from 'react';
import { Container, TextField, Button, Typography, Box, Grid, Paper } from '@mui/material';
import { makeStyles } from '@mui/styles';

// Estilos personalizados
const useStyles = makeStyles({
  root: {
    height: '100vh',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f5f5f5',
  },
  formContainer: {
    padding: '40px',
    maxWidth: '500px',
    width: '100%',
    borderRadius: '15px',
    boxShadow: '0px 4px 20px rgba(0, 0, 0, 0.1)',
    backgroundColor: '#fff',
  },
  title: {
    marginBottom: '30px',
    fontWeight: 'bold',
    color: '#004d40',
  },
  button: {
    marginTop: '20px',
    backgroundColor: '#004d40',
    color: '#fff',
    '&:hover': {
      backgroundColor: '#00332f',
    },
  },
});

const Cadastro = () => {
  const classes = useStyles();

  // State para armazenar os dados do formulário
  const [formData, setFormData] = useState({
    nome: '',
    cpf: '',
    email: '',
    telefone: '',
    username: '',
    senha: '',
  });

  // Função para atualizar os dados do formulário
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  // Função de envio do formulário
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData); // Aqui você pode enviar os dados para um backend ou realizar outra ação
  };

  return (
    <div className={classes.root}>
      <Container component="main" maxWidth="xs">
        <Paper elevation={3} className={classes.formContainer}>
          <Typography variant="h5" className={classes.title} align="center">
            Cadastro Metalúrgica
          </Typography>
          <form onSubmit={handleSubmit}>
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  fullWidth
                  label="Nome Completo"
                  name="nome"
                  value={formData.nome}
                  onChange={handleChange}
                  required
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  fullWidth
                  label="CPF"
                  name="cpf"
                  value={formData.cpf}
                  onChange={handleChange}
                  required
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  fullWidth
                  label="Email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  required
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  fullWidth
                  label="Telefone"
                  name="telefone"
                  value={formData.telefone}
                  onChange={handleChange}
                  required
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  fullWidth
                  label="Username"
                  name="username"
                  value={formData.username}
                  onChange={handleChange}
                  required
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  fullWidth
                  type="password"
                  label="Senha"
                  name="senha"
                  value={formData.senha}
                  onChange={handleChange}
                  required
                />
              </Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              className={classes.button}
            >
              Cadastrar
            </Button>
          </form>
        </Paper>
      </Container>
    </div>
  );
};

export default Cadastro;
