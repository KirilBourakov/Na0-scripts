import { useConnectContext } from '../state/connectionState';
import { io } from "socket.io-client";

function Connect(){
    const {state, setState} = useConnectContext();

    function connect(){
        const connection = io("localhost:5001/", {
            transports: ["websocket"],
            })

        connection.on('connected', () => setState({
            ...state,
            'connection': connection,
            'connected': true
            })
        )
        connection.on("disconnect", () => setState({
            ...state,
            'connection': null,
            'connected': false
        }));
    }

    function disconnect(){
        if (state.connection != null){
            state.connection.disconnect()
        }
    }

    function runner(){
        if (state.connected){
            disconnect()
        } else {
            connect()
        }
    }
    
    return (
        <div className='flex flex-col'>
            <h1 className='font-bold text-xl text-center'>Connect to the Nao</h1>
            <hr className='py-2 mx-2'/>
            <button 
                onClick={runner} 
                className={`mx-2 text-white font-bold py-2 px-4 rounded w-fit ${state.connected ? 'bg-red-700 hover:bg-red-900' : 'bg-green-700 hover:bg-green-900'}`}
            >
                {state.connected ? 'Disconnect' : 'Connect'}
            </button>
            
            <p className={`mx-2 ${state.connected ? 'text-green-600' : 'text-red-600'}`}>
                Status: {state.connected ? 'Connected' : 'Not Connected'}
            </p>
        </div>
    )
}

export default Connect