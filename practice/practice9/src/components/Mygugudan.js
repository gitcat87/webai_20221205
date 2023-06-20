import React, { useState } from 'react';


const Mygugudan = () => {
    let [guguMotherNum,setNum] = useState("")
    const guguChildNum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    const res = []

    for (let i = 0; i < 9; i++){        
        res.push(guguMotherNum*guguChildNum[i])          
    }
    const test = res.join(",")

   
    
    console.log(res)
    
    const handleInput = (e) => {
        const num = e.target.value
        
        setNum(num)
    }


    return (
      <>
        <div>
          <h1>{test}</h1>
          입력하세요&nbsp;&nbsp;&nbsp;<input onChange={handleInput}></input>
        </div>
      </>
    );
}
 
export default Mygugudan;