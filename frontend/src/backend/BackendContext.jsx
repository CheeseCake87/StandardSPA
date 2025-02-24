import {createContext} from "solid-js";

export const BackendContext = createContext();

export function BackendContextProvider(props) {

    const api_base = __API_BASE__
    const api = api_base + '/api'

    async function visitApi() {
        return await fetch(
            api + '/', {
                method: 'GET',
                credentials: 'include'
            }).then(res => res.json())
    }

    async function visitSecured() {
        return await fetch(
            api + '/secured', {
                method: 'GET',
                credentials: 'include'
            }).then(res => res.json())
    }

    async function visitLogin() {
        return await fetch(
            api + '/login', {
                method: 'GET',
                credentials: 'include'
            }).then(res => res.json())
    }

    async function visitLogout() {
        return await fetch(
            api + '/logout', {
                method: 'GET',
                credentials: 'include'
            }).then(res => res.json())
    }

    const pushCtx = {
        visitApi: visitApi,
        visitSecured: visitSecured,
        visitLogin: visitLogin,
        visitLogout: visitLogout
    };

    return (
        <BackendContext.Provider value={pushCtx}>
            {props.children}
        </BackendContext.Provider>
    );
}
