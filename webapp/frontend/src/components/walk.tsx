import { io } from "socket.io-client";
import { useEffect, useState } from "react";
import { Socket } from "socket.io";

function Walk() {
    const [move, setMove] = useState({
        'right': false,
        'left': false,
        'down': false,
        'up': false
    })

    useEffect(() => {
        const socket = io("localhost:5001/", {
        transports: ["websocket"],
        })

        window.addEventListener('keydown', (e) => {
            let force = [0, 0, 0]
            if (e.key == 'w'){
            force[0] += 1
            }
            if (e.key == 's'){
            force[0] -= 1
            }
            if (e.key == 'd'){
            force[1] += 1
            }
            if (e.key == 'a'){
            force[1] -= 1
            }
            socket.emit("walk", {direction: 'down', force: force})
        })
        window.addEventListener('keyup', (e) => {
            socket.emit("walk", {direction: 'up', force: [1,0,0]})
        })

    }, [])

    function flip(target: string): string{
        if (target == 'right') return 'left'
        if (target == 'left') return 'right'
        if (target == 'up') return 'down'
        return 'up'
    }

    function handleClicks(event: any){
        const clickedElementId: string = event.target.id;
        const opp = flip(clickedElementId)
        const val = move[clickedElementId]

        setMove({
            ...move,
            [clickedElementId]: !val,
            [opp]: false,
        })

        let force = [0, 0, 0]
            if (move['up']){
            force[0] += 1
            }
            if (move['down']){
            force[0] -= 1
            }
            if (move['right']){
            force[1] += 1
            }
            if (move['left']){
            force[1] -= 1
            }
            socket.emit("walk", {direction: 'down', force: force})
        }

    return (
        <div>
        W,A,S,D to move


        <div className="flex flex-col justify-center items-center">
            <button className={`p-2 m-1 ${move['up'] ? 'bg-red-800' : 'bg-gray-500'} rounded-md`} id="up" onClick={handleClicks}>U</button>
            <div>
                <button className={`p-2 m-1 ${move['left'] ? 'bg-red-800' : 'bg-gray-500'} rounded-md`} id="left" onClick={handleClicks}>L</button>
                <button className={`p-2 m-1 ${move['right'] ? 'bg-red-800' : 'bg-gray-500'} rounded-md`} id="right" onClick={handleClicks}>R</button>
            </div>
            <button className={`p-2 m-1 ${move['down'] ? 'bg-red-800' : 'bg-gray-500'} rounded-md`} id="down" onClick={handleClicks}>D</button>
        </div>

        </div>
    )
}

export default Walk