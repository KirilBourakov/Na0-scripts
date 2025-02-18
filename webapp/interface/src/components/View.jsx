import { useConnectContext } from '../state/connectionState';

export default function View(){
    const {state, setState} = useConnectContext();


    if (state.connected){
        return (
            <iframe src="http://127.0.0.1:5001/sight" className="w-full h-screen" scrolling="no">
            </iframe>
        )
    }
    else{ 
        return( 
            <div className='w-full h-screen bg-gray-800 text-white flex flex-col items-center justify-center'>
                <p className='text-3xl'>Not connected</p>
                <p>Connect to the Nao to see what it does</p>
            </div>
        )
    }
}