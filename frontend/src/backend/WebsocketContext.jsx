import {createContext, createEffect, createSignal, For} from "solid-js";


export class WebsocketMessageHandler {
    constructor(event) {
        this.event = event;

        try {
            this.payload = JSON.parse(event.data);
        } catch (error) {
            console.error("Failed to parse WebSocket event data:", error);
            this.payload = null;
        }

        if (this.payload) {
            this.key = this.payload.key;
            this.action = this.payload.action;
            this.data = this.payload.data;
        } else {
            this.key = null;
            this.action = null;
            this.data = null;
        }
    }
}

function ToastMessage(props) {
    return (
        <div id="toast-simple"
             className="flex items-center w-full max-w-xs p-4 space-x-4 rtl:space-x-reverse text-gray-500 bg-white divide-x rtl:divide-x-reverse divide-gray-200 rounded-lg shadow-sm dark:text-gray-400 dark:divide-gray-700 dark:bg-gray-800"
             role="alert">
            <svg className="w-5 h-5 text-blue-600 dark:text-blue-500 rotate-45" aria-hidden="true"
                 xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 20">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="m9 17 8 2L9 1 1 19l8-2Zm0 0V9"/>
            </svg>
            <div className="ps-4 text-sm font-normal">{props.key} - {props.message}</div>
        </div>
    )
}

export const WebsocketContext = createContext();

export function WebsocketContextProvider(props) {
    const ws_base = __WS_BASE__
    const socket = new WebSocket(ws_base);

    const [toasts, setToasts] = createSignal({})
    const [toastCounter, setToastCounter] = createSignal(0)

    socket.addEventListener("open", (event) => {
        console.log("Connected to server", event);
    });

    socket.addEventListener("message", (event) => {
        const message = new WebsocketMessageHandler(event)

        if (message.action === 'toast' || message.action === 'toast-broadcast') {
            setToastCounter(toastCounter() + 1)

            const copy = toasts()
            const counterAt = toastCounter()

            copy[counterAt] = message.data.message
            setToasts({...copy});

            if (Object.keys(copy).length > 8) {
                console.log('pop', Object.keys(copy)[0])
                toastFirstInFirstOut(Object.keys(copy)[0])
            }

            setTimeout(() => {
                toastTimeout(counterAt)
            }, 10000)

        }

    });

    createEffect(() => {
        console.log(toasts())
    })

    function toastFirstInFirstOut(index) {
        const copy = toasts()
        delete copy[index]
        setToasts({...copy})
    }

    function toastTimeout(index) {
        const copy = toasts()
        if (copy[index]) {
            console.log('index exists')
            delete copy[index]
            setToasts({...copy})
        } else {
            console.log('index does not exist', index)
        }
    }

    function send({key, action, data}) {
        if (typeof data === 'object') {
            socket.send(
                JSON.stringify({
                    key: key,
                    action: action,
                    data: data,
                })
            )
        } else {
            console.error('Data must be a valid object to send.');
        }
    }

    const pushCtx = {
        socket: socket,
        send: send,
    };

    return (
        <WebsocketContext.Provider value={pushCtx}>
            <div className={'fixed top-0 right-0 z-50'}>
                <For each={Object.entries(toasts())}>
                    {([key, toast]) => <ToastMessage key={key} message={toast}/>}
                </For>
            </div>
            {props.children}
        </WebsocketContext.Provider>
    );
}
