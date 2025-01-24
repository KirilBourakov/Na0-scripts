import { useConnectContext } from '../state/connectionState';

function Connect(){
    const { state, setState } = useConnectContext();

    return (
        <div>
            <button>Connect to Na0</button>
            <div>Status: {state ? 'not connected' : 'connected'}</div>
        </div>
    )
}

export default Connect