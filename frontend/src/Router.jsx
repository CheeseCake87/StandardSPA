import {render} from 'solid-js/web'
import {Route, Router} from '@solidjs/router'
import Index from './pages/Index/Index.jsx'
import {MainContextProvider} from "./context/MainContext.jsx";
import {BackendContextProvider} from "./backend/BackendContext.jsx";

import 'solid-devtools';

import 'flowbite';
import {WebsocketContextProvider} from "./backend/WebsocketContext.jsx";
import Websocket from "./pages/Websocket/Websocket.jsx";

const root = document.getElementById('root')
if (import.meta.env.DEV && !(root instanceof HTMLElement)) {
    throw new Error('Root element not found. Did you forget ' +
        'to add it to your index.html? Or maybe the id attribute got misspelled?')
}

render(() => (
    <Router>
        <Route path="" component={BackendContextProvider}>
            <Route path="" component={MainContextProvider}>
                <Route path="/" component={Index}/>
                <Route path="" component={WebsocketContextProvider}>
                    <Route path="/websocket" component={Websocket}/>
                </Route>
            </Route>
        </Route>
    </Router>
), root)