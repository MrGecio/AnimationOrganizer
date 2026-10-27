import './App.css';
import { Routes, Route } from 'react-router-dom';
import Login from './pages/Login/Login.jsx';
//import { Route } from 'react-router-dom';

function App() {
  return (

    //Vamos a agregar las rutas Para el uso de los routers desde APP
    <div className="App">


      <Routes>
        <Route path="/" element={<Login />} />

      </Routes>

    </div>

  );
}
export default App;
