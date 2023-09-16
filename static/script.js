function colour() {
     
    setInterval(function() {
        if (colorChanger){
            if (document.getElementById('var').style.color == 'black')
                var col1 = 'orange';
            else
                col1 = 'black';
 
        // setting value of color 1 through var

            document.getElementById('var').style.color = col1;
        }
        
        // console.log("Changed Welcome!")
        // changing color of h1 in html
    }, 10);
 
}

colour();