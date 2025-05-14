// frontend/js/app.js (solo la parte de pintar la tabla)
tbody.innerHTML = '';
// añadimos encabezados: n, x, f(x), Error
tabla.forEach(fila => {
  const tr = document.createElement('tr');
  fila.forEach(c => {
    const td = document.createElement('td');
    td.textContent = c;
    tr.appendChild(td);
  });
  tbody.appendChild(tr);
});
// Asegúrate de que tu <thead> en index.html tenga solo esas 4 cabeceras.
