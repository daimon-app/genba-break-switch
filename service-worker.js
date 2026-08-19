// DAIMON Service Worker
// オフラインでも開けるようにキャッシュする

const CACHE_NAME = 'kirikae-v10';
const ASSETS = [
  './',
  './index.html',
  './start.html',
  './faq.html',
  './install.html',
  './terms.html',
  './privacy.html',
  './commerce.html',
  './support.html',
  './site.css',
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
  if (event.request.method !== 'GET') return;

  const url = new URL(event.request.url);
  const isHtml = event.request.mode === 'navigate' ||
    url.pathname.endsWith('/') ||
    url.pathname.endsWith('.html');

  // Public pages must refresh from the network first so existing PWA users
  // receive changed safety guidance, policy pages, and product naming.
  if (isHtml) {
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          const copy = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy));
          return response;
        })
        .catch(() => caches.match(event.request))
    );
    return;
  }

  event.respondWith(
    caches.match(event.request).then((cached) => {
      if (cached) return cached;
      return fetch(event.request);
    })
  );
});
