import { io } from "socket.io-client";
import { useEffect, useState } from "react";

function Walk() {
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

  return (
    <div>
      W,A,S,D to move
    </div>
  )
}

export default Walk