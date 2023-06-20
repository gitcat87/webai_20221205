class MyC{
    static doA() {
        console.log('doA');
    }
    doB() {
        console.log('doB');
    }
}

const myc = new MyC(); // 힙 영역역에 올렸기 때문에 doB 함수가 메모리 상에 올라가 있다

module.exports = { MyC , myc };