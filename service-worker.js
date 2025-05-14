// service-worker.js

const CACHE_NAME = 'regula-falsi-v3';  // <-- incrementa el número cuando actualices CSS
const ASSETS = [
  '/',
  '/index.html',
  '/css/styles.css',
  '/js/app.js',
  '/js/api.js',
  '/manifest.json',
  '/images/icons/icon-192.png',
  '/images/icons/icon-512.png',
  // añade aquí cualquier otro archivo estático
];

self.addEventListener('install', event => {
  // Toma el control inmediatamente
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS))
  );
});

self.addEventListener('activate', event => {
  // Controla todas las pestañas sin esperar recarga
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys
          .filter(key => key !== CACHE_NAME)
          .map(old => caches.delete(old))
      )
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  // Network-first: intenta la red, si falla sirve del cache
  event.respondWith(
    fetch(event.request)
      .then(res => {
        // Actualiza el cache con la nueva respuesta
        const clone = res.clone();
        caches.open(CACHE_NAME).then(c => c.put(event.request, clone));
        return res;
      })
      .catch(() => caches.match(event.request))
  );
});
