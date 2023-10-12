let sendData = document.getElementById("sendData");
sendData.addEventListener('click', handler)

let getData = document.getElementById("getData");
getData.addEventListener('click', manager)

function handler() {
    console.log("Running HAndler...")
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/data')
    xhr.onprogress = function () {
        console.log("Onprogress");
    }
    xhr.onreadystatechange = function () {
        console.log("Ready state is ", this.readyState)
    }
    xhr.onload = function () {
        if (this.status === 200)
            document.getElementById('card1').innerText = this.responseText;
        else
            console.log("Some error occured")
    }
    xhr.send();
    console.log("Completed!")
}

function manager() {
    console.log("Running MAnager...")
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/info');
    // xhr.getResponseHeader('Content-type');
    xhr.onprogress = function () {
        console.log("Onprogress");
    }
    // xhr.onreadystatechange = function () {
    //     console.log("Ready state is ", this.readyState);
    // }
    // xhr.onload = function () {
    //     if (this.status === 200){
    //         document.getElementById('card1').innerText = this.responseText;
    //         console.log(this.responseType)
    //     }
    //     else
    //         console.log("Some error occured")
    // }
    params = {"name":"text", "salary":"123", "age":"19", "list":["a", "b", "c"]}
    xhr.send(params);
    console.log("Completed!")
}