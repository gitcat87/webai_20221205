import { Container } from "react-bootstrap";
import React, { useState } from 'react';


const ImReady = () => {
    const [ready, setReady] = useState(true)

  return (
    <>
      <Container>
        <div className="DivWrapO">
                  {ready ? <div className="round" onClick={() => setReady(!ready)}></div> : <div className="Notready" onClick={()=>setReady(!ready)}></div>}
        </div>
        
      </Container>
    </>
  );
};

export default ImReady;
