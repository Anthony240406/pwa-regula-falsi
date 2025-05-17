// frontend/js/app.js

import { calcula } from './api.js';

window.addEventListener('DOMContentLoaded', () => {
  const form      = document.getElementById('calc-form');
  const resultado = document.getElementById('resultado');
  const tablaEl   = document.getElementById('tabla');
  const tbody     = tablaEl.querySelector('tbody');

  form.addEventListener('submit', async e => {
    e.preventDefault();

    // Leer valores del formulario
    const N   = parseFloat(document.getElementById('inputN').value);
    const exp = parseInt  (document.getElementById('inputExp').value, 10);

    resultado.textContent = 'Calculando…';
    tbody.innerHTML = '';  // limpiar tabla

    try {
      // Llamada a la API
      const { raiz, tabla, error } = await calcula(N, exp);
      if (error) {
        resultado.textContent = `Error: ${error}`;
        return;
      }

      // Mostrar resultado
      resultado.textContent = `≈ ${raiz.toFixed(6)}`;

      // Pintar cada fila de la tabla
      tabla.forEach(fila => {
        const tr = document.createElement('tr');
        fila.forEach(c => {
          const td = document.createElement('td');
          td.textContent = c;
          tr.appendChild(td);
        });
        tbody.appendChild(tr);
      });
    } catch (err) {
      console.error(err);
      resultado.textContent = 'Error de red o servidor';
    }
  });
});
