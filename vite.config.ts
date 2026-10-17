import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
export default defineConfig(({mode})=>({plugins:mode==='test'?[react()]:[react(),tailwindcss()],test:{environment:'jsdom',setupFiles:['./src/test-setup.ts'],pool:'threads',maxWorkers:1,fileParallelism:false}}));
