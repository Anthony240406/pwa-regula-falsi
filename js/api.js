// frontend/js/api.js
export async function calcula(N, eps) {
  const resp = await fetch('https://pwa-regula-falsi.onrender.com/api/regula', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ N, exp: eps })
  });
  return await resp.json();
}
