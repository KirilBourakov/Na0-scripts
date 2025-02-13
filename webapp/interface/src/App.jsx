import './static/main.css'
import Connect from "./components/Connect";
import Walk from "./components/Walk";
import View from "./components/View"

function App() {
  return (
      <div className="flex">
        <div className="w-5/12">
          <Connect />
          <Walk />
        </div>
        
        <div className="w-7/12 m-5">
          <View />
        </div>
        
      </div>
  )
}

export default App
