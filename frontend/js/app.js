// frontend/js/app.js

import { calcula } from './api.js';

window.addEventListener('DOMContentLoaded', () => {
  const form      = document.getElementById('calc-form');
  const resultado = document.getElementById('resultado');
  const tablaEl   = document.getElementById('tabla');
  const tbody     = tablaEl.querySelector('tbody');

  form.addEventListener('submit', async e => {
    e.preventDefault();
    const N   = parseFloat(document.getElementById('inputN').value);
    const exp = parseInt  (document.getElementById('inputExp').value, 10);

    resultado.textContent = 'Calculando…';
    tbody.innerHTML = '';      // limpiamos filas previas

    try {
      const { raiz, tabla, error } = await calcula(N, exp);
      if (error) {
        resultado.textContent = `Error: ${error}`;
        return;
      }
      resultado.textContent = `≈ ${raiz.toFixed(6)}`;

      tabla.forEach(fila => {
        const tr = document.createElement('tr');
        fila.forEach(c => {
          const td = document.createElement('td');
          td.textContent = c;
          tr.appendChild(td);
        });
        tbody.appendChild(tr);
      });
    } catch {
      resultado.textContent = 'Error de red o servidor';
    }
  });
});
