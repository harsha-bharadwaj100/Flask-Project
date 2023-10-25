const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay))
var socket = io();
socket.connect('http://127.0.0.1:5000/')
socket.on('connect', function() {
socket.emit('my event', {data: 'I\'m connected!'});
});
function foo(){
console.log("foo was called!");
}
function emitter(){
socket.emit('ready', "Come on!")
}
socket.on('called', async function(funcName){
// for(let i=0; i<25000; i++){
//         console.log('Run!');
//     }
eval(funcName + "();")
})