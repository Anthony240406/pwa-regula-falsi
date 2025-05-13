// frontend/js/api.js
export async function calcula(N, eps) {
  const resp = await fetch('https://TU-SERVICIO.onrender.com/api/regula', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ N, error: eps })
  });
  return await resp.json();
}
