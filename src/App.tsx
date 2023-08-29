import { useState } from "react";
import Persona from "./components/Persona";

import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <div className="flex-grid">
        <Persona></Persona>
      </div>
    </>
  );
}

export default App;
