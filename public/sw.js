const CACHE='sakura-v2';
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(['/','/icon.svg','/manifest.webmanifest'])));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('sakura-')&&k!==CACHE).map(k=>caches.delete(k)))));});
self.addEventListener('fetch',e=>{if(e.request.method!=='GET'||new URL(e.request.url).origin!==self.location.origin)return;e.respondWith(fetch(e.request).then(r=>{if(r.status===200&&!e.request.headers.has('range')){const copy=r.clone();caches.open(CACHE).then(c=>c.put(e.request,copy)).catch(()=>{});}return r;}).catch(()=>caches.match(e.request).then(r=>r||(e.request.mode==='navigate'?caches.match('/'):Response.error()))));});
