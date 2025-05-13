// frontend/js/app.js
import { calcula } from './api.js';

const form = document.getElementById('calc-form');
const resultadoDiv = document.getElementById('resultado');
const tablaEl = document.getElementById('tabla');
const tbody = tablaEl.querySelector('tbody');

form.addEventListener('submit', async e => {
  e.preventDefault();

  const N = parseFloat(document.getElementById('inputN').value);
  const eps = parseFloat(document.getElementById('inputEps').value);
  const { raiz, tabla, error } = await calcula(N, eps);

  if (error) {
    resultadoDiv.textContent = `Error: ${error}`;
    tablaEl.hidden = true;
    return;
  }

  resultadoDiv.textContent = raiz !== null
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
  tablaEl.hidden = !tabla.length;
});
