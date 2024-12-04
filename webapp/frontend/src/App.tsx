import { io } from "socket.io-client";
import { useEffect, useState } from "react";

function App() {
  const [count, setCount] = useState(0)

  useEffect(() => {
    
    const socket = io("localhost:5001/", {
      transports: ["websocket"],
      cors: {
        origin: "http://localhost:3000/",
      },
    })

  }, [])

  return (
    <>
      W,A,S,D to move
    </>
  )
}

export default App
