const timeH = document.querySelector("h1");
const timeleft = document.querySelector("h2");
let timeSecond = 6;
let trigger = true;



    

const countDown = setInterval(() => {
    let change
    timeSecond--;
    displayTime(timeSecond);
    if (timeSecond < 0 || timeSecond == 0) {
      endTime();
      clearInterval(countDown);
    }
    if (timeSecond < 10) {
      timeleft.innerHTML = `열차 출발까지 ${timeSecond}초 남았습니다.`;
      if (trigger == true) {
        console.log(trigger+"바뀌는 중")
        change = setInterval(() => {
          timeleft.style.color = "red";
        }, 100);

        trigger = false;
      }
      if (timeSecond == 0) {
        timeleft.innerHTML = "다음 열차를 이용해주세요"
        if (trigger == false) {
          console.log(trigger)
          console.log('마지막까지 옴')
          timeleft.style.color = "green"
          clearInterval(change)
        }
          
      }
  }
 

  }, 1000);



function displayTime(second) {
  const min = Math.floor(second / 60);
  const sec = Math.floor(second % 60);
  timeH.innerHTML = `${min < 10 ? "0" : ""}${min}:${sec < 10 ? "0" : ""}${sec}`;
}
function endTime() {
  timeH.innerHTML = "TIME OUT";
}
