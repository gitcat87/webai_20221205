import './App.css';
import { Container } from 'react-bootstrap'
import { BrowserRouter, Link, Route, Routes } from "react-router-dom";
import ImReady from './components/ImReady';
import "bootstrap/dist/css/bootstrap.min.css";



function App() {
  return (
    <BrowserRouter>
      <Container>
        <div className="App">
          <h1>준비 됐어요</h1>
          <ImReady></ImReady>
        </div>
      </Container>
    </BrowserRouter>
  );
}

export default App;
