import {createContext, createSignal, onMount} from "solid-js";

export const MainContext = createContext();

export function MainContextProvider(props) {
    const [message, setMessage] = createSignal("Hello, SPA!");
    const [loaded, setLoaded] = createSignal(false);

    const pushCtx = {
        message: message,
        setMessage: setMessage,
        loaded: loaded,
        setLoaded: setLoaded,
    };

    onMount(() => {
        setLoaded(true);
    })

    return (
        <MainContext.Provider value={pushCtx}>
            {props.children}
        </MainContext.Provider>
    );
}
