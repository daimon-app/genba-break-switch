// DAIMON Service Worker
// オフラインでも開けるようにキャッシュする

const CACHE_NAME = 'daimon-v8';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './assets/sounds/ocean-waves.mp3',
  './assets/sounds/river.mp3',
  './assets/sounds/forest.mp3',
  './assets/sounds/rain.mp3',
  './icons/icon-192.png',
  './icons/icon-512.png',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => {
      if (cached) return cached;
      return fetch(event.request).catch(() => cached);
    })
  );
});
