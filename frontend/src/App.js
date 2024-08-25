import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Register } from './pages'; 
import './App.css'; 

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000/api';

function App() {
  return (
    <Router>
      <div className='App'>
        <Routes>
          <Route path='/register' element={<Register />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
