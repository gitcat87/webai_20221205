
import './App.css';
import SignInSide from './components/Member';
import Main from './components/Main';
import Vaform from './components/VaForm'
import Valist from './components/Valist'
import Board from './components/Board'
import Member from  './components/Member'
import { Routes,Route } from 'react-router-dom';


function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<SignInSide />} />
        <Route path="/main" element={<Main />} />
        <Route path="/vaform" element={<Vaform />} />
        <Route path="/valist" element={<Valist />} />
        <Route path="/board" element={<Board />} />
        <Route path="/member" element={<Member />} />
      </Routes>
    </div>
  );
}

export default App;
