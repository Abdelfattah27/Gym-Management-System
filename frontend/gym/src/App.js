
import './App.css';
import { Route, Routes } from 'react-router';
import HomeScreen from './screens/HomeScreen';

function App() {
  return (
    <div className="App">
     
      <main className='container my-3'>
        <Routes>
          <Route path='/' element={<HomeScreen />}></Route>
         
        </Routes>
      </main>
      
    </div>
  );
}

export default App;
