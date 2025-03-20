import { useConnectContext } from '../state/connectionState';
import { useEffect, useState } from "react";
import { Joystick } from 'react-joystick-component';
import { FaCircleArrowDown, FaCircleArrowLeft, FaCircleArrowRight, FaCircleArrowUp } from "react-icons/fa6";

function Walk() {
    const connectionState = useConnectContext();
    const [direction, setDirection] = useState([0,0])

    function handleMove(data){  
        let newDirection = [0, 0]
        if (data.x > 0.5){
            newDirection[0] = 1
        } else if (data.x < -0.5){
            newDirection[0] = -1
        }

        if (data.y > 0.5){
            newDirection[1] = 1
        } else if (data.y < -0.5){
            newDirection[1] = -1
        }
        setDirection(newDirection)
    }
    function handleStop(){
        if (!connectionState.state.connected || connectionState.state.connection === null){   
            setDirection([0,0])
        } 
        else {
            connectionState.state.connection.emit("moveUpdate", {x: direction[0], y: direction[1]})
        }
    }

    return (

        <div className="flex flex-col items-center justify-center">
            <h1 className='font-bold text-xl text-center'>Move</h1>
            <hr className='py-2 mx-2 w-full'/>

            <div className="m-2">
                <FaCircleArrowUp 
                    size={35} 
                    className={`${direction[1] == 1 ? "text-green-700" : "text-red-700"}`}
                />
            </div>
            <div className="flex items-center justify-center">
                <div className="m-2">
                    <FaCircleArrowLeft 
                        size={35}
                        className={`${direction[0] == -1 ? "text-green-700" : "text-red-700"}`}
                    />
                </div>

                <Joystick size={100} sticky={true} baseColor="#808080" stickColor="#D3D3D3" move={handleMove} stop={handleStop}></Joystick>
                
                <div className="m-2">
                    <FaCircleArrowRight 
                        size={35} 
                        className={`${direction[0] == 1 ? "text-green-700" : "text-red-700"}`}
                    />
                </div>
            </div>
            <div className="m-2">
                <FaCircleArrowDown 
                    size={35} 
                    className={`${direction[1] == -1 ? "text-green-700" : "text-red-700"}`}
                />
            </div>
        </div>
    )
}

export default Walk