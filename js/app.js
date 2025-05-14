// frontend/js/app.js

import { calcula } from './api.js';

window.addEventListener('DOMContentLoaded', () => {
  const form      = document.getElementById('calc-form');
  const resultado = document.getElementById('resultado');
  const tablaEl   = document.getElementById('tabla');
  const tbody     = tablaEl.querySelector('tbody');

  console.log('DOM cargado, inicializando form…');

  form.addEventListener('submit', async e => {
    e.preventDefault();

    const N   = parseFloat(document.getElementById('inputN').value);
    const exp = parseInt  (document.getElementById('inputExp').value, 10);
    resultado.textContent = 'Calculando…';

    try {
      const { raiz, tabla, error } = await calcula(N, exp);
      if (error) {
        resultado.textContent = `Error: ${error}`;
        tablaEl.hidden = true;
        return;
      }

      resultado.textContent = raiz !== null
        ? `≈ ${raiz.toFixed(6)}`
        : 'Intervalo inválido';

      tbody.innerHTML = '';
      tabla.forEach(fila => {
        const tr = document.createElement('tr');
        fila.forEach(c => {
          const td = document.createElement('td');
          td.textContent = c;
          tr.appendChild(td);
        });
        tbody.appendChild(tr);
      });
      tablaEl.hidden = false;
    } catch (err) {
      resultado.textContent = 'Error de red o servidor';
      console.error(err);
    }
  });
});
