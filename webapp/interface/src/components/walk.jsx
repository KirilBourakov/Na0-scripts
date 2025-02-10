import { io } from "socket.io-client";
import { useEffect, useState } from "react";
import { Joystick } from 'react-joystick-component';
import { FaCircleArrowDown, FaCircleArrowLeft, FaCircleArrowRight, FaCircleArrowUp } from "react-icons/fa6";

function Walk() {
    const [direction, setDirection] = useState([0,0])

    // let socket;
    // useEffect(() => {
    //     socket = io("localhost:5001/", {
    //     transports: ["websocket"],
    //     })

    //     window.addEventListener('keydown', (e) => {
    //         let force = [0, 0, 0]
    //         if (e.key == 'w'){
    //         force[0] += 1
    //         }
    //         if (e.key == 's'){
    //         force[0] -= 1
    //         }
    //         if (e.key == 'd'){
    //         force[1] += 1
    //         }
    //         if (e.key == 'a'){
    //         force[1] -= 1
    //         }
    //         socket.emit("walk", {direction: 'down', force: force})
    //     })
    //     window.addEventListener('keyup', (e) => {
    //         socket.emit("walk", {direction: 'up', force: [1,0,0]})
    //     })

    // }, [])

    // function flip(target){
    //     if (target == 'right') return 'left'
    //     if (target == 'left') return 'right'
    //     if (target == 'up') return 'down'
    //     return 'up'
    // }

    // function handleClicks(event){
    //     const clickedElementId = event.target.id;
    //     const opp = flip(clickedElementId)
    //     const val = move[clickedElementId]

    //     setMove({
    //         ...move,
    //         [clickedElementId]: true,
    //         [opp]: false,
    //     })

    //     let force = [0, 0, 0]
    //         if (move['up']){
    //         force[0] += 1
    //         }
    //         if (move['down']){
    //         force[0] -= 1
    //         }
    //         if (move['right']){
    //         force[1] += 1
    //         }
    //         if (move['left']){
    //         force[1] -= 1
    //         }
    //         socket.emit("walk", {direction: 'down', force: force})
    //     }

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
        console.log('send now.')
    }

    return (

        <div className="flex flex-col items-center justify-center">
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