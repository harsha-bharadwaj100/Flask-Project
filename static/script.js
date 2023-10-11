let sendData = document.getElementById("sendData");
sendData.addEventListener('click', handler)

function handler() {
    console.log("Running HAndler...")
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/data', true)
    xhr.onprogress = function () {
        console.log("Onprogress");
    }
    xhr.onload = function () {
        document.getElementById('card1').innerText = this.responseText;
    }
    xhr.send();
}