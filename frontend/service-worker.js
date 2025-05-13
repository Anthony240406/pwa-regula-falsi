const CACHE_NAME = 'regula-falsi-cache-v1';
const ASSETS = [
  '.',               // equivale a index.html
  'index.html',
  'css/styles.css',
  'js/app.js',
  'js/api.js',
  'images/icons/icon-192.png',
  'images/icons/icon-512.png'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll(ASSETS)));
});
self.addEventListener('fetch', e => {
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
});
