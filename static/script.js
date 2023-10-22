let sendData = document.getElementById("sendData");
sendData.addEventListener('click', handler)

let getData = document.getElementById("getData");
getData.addEventListener('click', manager)

function handler() {
    console.log("Running HAndler...")
    fetch('http://127.0.0.1:5000/data')
    .then(res => res.text())
    .then(data => console.log(data))
    console.log("Completed!")
}

function manager() {
    console.log("Running MAnager...")
    params = {"name":"text", "salary":"123", "age":"19", "list":["a", "b", "c"]}
    // xhr.send(JSON.stringify(params));
    fetch('http://127.0.0.1:5000/info', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(params)
    })
    console.log("Completed!")
}