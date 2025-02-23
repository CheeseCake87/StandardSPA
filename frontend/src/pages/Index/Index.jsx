import {createEffect, createSignal, useContext} from "solid-js";
import {MainContext} from "../../context/MainContext.jsx";
import {BackendContext} from "../../backend/BackendContext.jsx";


export default function Index() {
    const mainCtx = useContext(MainContext)
    const backendCtx = useContext(BackendContext)

    const [apiResponse, setApiResponse] = createSignal(null)

    createEffect(() => {
        console.log(mainCtx.loaded())
    })

    return (
        <>
            <section className={'max-w-1/2 mx-auto text-center my-10'}>
                <h1>StandardSPA</h1>
            </section>

            <section className={'max-w-1/2 mx-auto text-center my-10'}>
                <h2>Main Context Output</h2>
                <p>Message: {mainCtx.message()}, Loaded: {mainCtx.loaded() ? 'loaded' : 'loading...'}</p>
            </section>

            <section className={'max-w-1/2 mx-auto text-center my-10'}>
                <h2>API Output</h2>
                <p>{apiResponse()}</p>
            </section>

            <section className={'max-w-1/2 mx-auto my-10'}>
                <div className={"flex flex-col gap-2 max-w-1/3 mx-auto"}>
                    <button type="button"
                            className="btn-primary"
                            onClick={() => backendCtx.visitApi().then(r => setApiResponse(r.route))}>
                        Visit API
                    </button>
                    <button type="button"
                            className="btn-good"
                            onClick={() => backendCtx.visitSecured().then(r => setApiResponse(r.route))}>
                        Visit Secured
                    </button>
                    <button type="button"
                            className="btn-warning"
                            onClick={() => backendCtx.visitLogin().then(r => setApiResponse(r.route))}>
                        Login
                    </button>
                    <button type="button"
                            className="btn-danger"
                            onClick={() => backendCtx.visitLogout().then(r => setApiResponse(r.route))}>
                        Logout
                    </button>
                </div>


            </section>

            <section className={'max-w-1/2 mx-auto text-center my-10'}>
                <a href="http://127.0.0.1:5001">Go to backend app (http://127.0.0.1:5001)</a>
            </section>
        </>
    );
}