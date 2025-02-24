import {createContext, createSignal, onMount} from "solid-js";

export const WebsocketContext = createContext();

export function WebsocketContextProvider(props) {

    const ws_base = __WS_BASE__

    const [ws, setWs] = createSignal(null)

    function createWs() {
        const ws = new WebSocket(ws_base);

        console.log("Server created");

        ws.addEventListener("open", (event) => {
        });

        ws.addEventListener("message", (event) => {
            console.log(event.data);
        });

        setWs(ws)
    }

    function sendWs({action, key, data}) {
        if (typeof data === 'object') {
            ws().send(
                JSON.stringify({
                    _action: action,
                    _key: key,
                    data: data,
                })
            )
        } else {
            console.error('Data must be a valid object to send.');
        }
    }

    onMount(() => {
        createWs()
    })

    const pushCtx = {
        ws: ws,
        sendWs: sendWs,
    };

    return (
        <WebsocketContext.Provider value={pushCtx}>
            {props.children}
        </WebsocketContext.Provider>
    );
}
