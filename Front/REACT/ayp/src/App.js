import React, { useEffect } from 'react';
import axios from 'axios'; 
function App() {
  const MY_SERVER = 'http://localhost:5000'
  
  const loadData = () => {
    axios.get(MY_SERVER).then((response) => console.log(response))
  }
  useEffect(() => {
    loadData()
  },[]);

  return (
    <div>
     <h1> App</h1>
    </div>
  );
}

export default App;
