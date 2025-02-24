import {defineConfig} from 'vite'
import solid from 'vite-plugin-solid'
import devtools from 'solid-devtools/vite';
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
    plugins: [
        /*
        Uncomment the following line to enable solid-devtools.
        For more info see https://github.com/thetarnav/solid-devtools/tree/main/packages/extension#readme
        */
        devtools({
            /* features options - all disabled by default */
            autoname: true, // e.g. enable autoname
        }),
        solid(),
        tailwindcss(),
    ],
    root: 'src',
    server: {
        host: '127.0.0.1',
        port: 5002
    },
    build: {
        outDir: '../dist',
        emptyOutDir: true,
    },
    define: {
        __API_BASE__: JSON.stringify('http://127.0.0.1:5001'),
        __WS_BASE__: JSON.stringify('ws://127.0.0.1:5003'),
    }
})
