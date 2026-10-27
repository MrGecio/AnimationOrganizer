import './App.css';
import { Routes, Route } from 'react-router-dom';
import Login from './pages/Login/Login.jsx';
//import { Route } from 'react-router-dom';

function App() {
  return (

    <div className="App">


      <Routes>
        <Route path="/" element={<Login />} />

      </Routes>

    </div>

  );
}
export default App;
