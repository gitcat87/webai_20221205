import { useState } from "react";

const EvenOdd = () => {
  const [inputnumber, setNum] = useState([]);
  const [warningMessage, setWarningMessage] = useState("");
  const [isAscending, setIsAscending] = useState(true);

  const handleInput = e => {
    const num = e.target.value.split(/\r?\n/).map(str => str.trim());
    const sortNum = num.sort((a, b) => a - b);

    if (sortNum.length <= 10) {
      setNum(sortNum);
      setWarningMessage("");
    } else {
      setWarningMessage("10개 이하의 숫자만 입력해주세요.");
    }
  };

  const handleReset = () => {
    setNum([]);
    setWarningMessage("");
  };

  const handleSort = () => {
    setIsAscending(!isAscending);
  };

  const sortedNumbers = isAscending
    ? inputnumber.sort((a, b) => a - b)
    : inputnumber.sort((a, b) => b - a);

  return (
    <>
      <div>
        <h1>{sortedNumbers.join(", ")}</h1>
        <textarea id="inputbox" type="text" onChange={handleInput}></textarea>
        {warningMessage && <p>{warningMessage}</p>}
        <button onClick={handleSort}>
          {isAscending ? "내림차순" : "오름차순"}
        </button>
        <button onClick={handleReset}>리셋</button>
      </div>
    </>
  );
};

export default EvenOdd;
