import Walk from "./components/walk";
import View from "./components/View"
import './static/main.css'
import Connect from "./components/Connect";

function App() {
  return (
    <>
      <Connect />
      <div className="flex">
        <div className="w-5/12">
          <Walk/>
        </div>
        
        <div className="w-7/12 m-5">
          <View />
        </div>
        
      </div>
    </>
  )
}

export default App
