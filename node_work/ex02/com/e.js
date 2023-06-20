// const doa = () => {
//     return new Promise();
// }

// module.exports = doa;

// //프로미스는 resolver가 선언되어야 한다.
// //promise에는 시간이 걸리는 작업을 담아주면 된다

module.exports = () => {
    return new Promise((res, rej) => {
        setTimeout(() => {
            const data = 'axios를 통해서 받은 데이터'
            if (data) {
                res(data)
            }
            else {
                rej('에러에러')
            }
        }, 2000);
    })
}