import {createContext, createEffect, createSignal, onMount} from "solid-js";

export const WebsocketContext = createContext();

export function WebsocketContextProvider(props) {

    const ws_base = __WS_BASE__

    const [ws, setWs] = createSignal(null)

    function createWs() {
        setWs(new WebSocket(ws_base))

        if (ws().readyState === 1) {
            ws().addEventListener("open", (event) => {
                ws().send("Hello Server!");
            });

            ws().addEventListener("message", (event) => {
                console.log("Message from server ", event.data);
            });
        }
    }

    onMount(() => {
        createWs()
    })

    const pushCtx = {
        ws: ws,
    };

    return (
        <WebsocketContext.Provider value={pushCtx}>
            {props.children}
        </WebsocketContext.Provider>
    );
}
