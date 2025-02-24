import {useContext} from "solid-js";
import {MainContext} from "../../context/MainContext.jsx";
import {WebsocketContext} from "../../backend/WebsocketContext.jsx";
import {BackendContext} from "../../backend/BackendContext.jsx";


export default function Websocket() {
    const mainCtx = useContext(MainContext)
    const backendCtx = useContext(BackendContext)
    const websocketCtx = useContext(WebsocketContext)

    return (
        <>
            <section className={'max-w-1/2 mx-auto text-center my-10'}>
                <h1>StandardSPA - Websocket</h1>
            </section>

            <section className={'max-w-1/2 mx-auto my-10'}>
                <div className={"flex flex-col gap-2 max-w-1/3 mx-auto"}>
                    <button type="button"
                            className="btn-good"
                            onClick={() => websocketCtx.ws().send("Hello from frontend!")}>
                        Send Data
                    </button>
                </div>


            </section>

            <section className={'max-w-1/2 mx-auto text-center my-10'}>
                <a href="http://127.0.0.1:5001">Go to backend app (http://127.0.0.1:5001)</a>
            </section>
        </>
    );
}