import { useConnectContext } from '../state/connectionState';
import { io } from "socket.io-client";

function Connect(){
    const { state, setState } = useConnectContext();

    function connect(){
        const connection = io("localhost:5001/", {
            transports: ["websocket"],
            })
        setState({
            ...state,
            
        })

        connection.on('connected', () => setState({
            ...state,
            'connection': connection,
            'connected': true
            })
        )
    }
    
    return (
        <div className='flex flex-col'>
            <button onClick={connect}>Connect to Na0</button>
            <div>Status: {state.connected ? 'connected' : 'Not Connected'}</div>
        </div>
    )
}

export default Connect