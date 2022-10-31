"use strict"

let send = document.getElementById("send");
let prev = document.getElementById("prev");
let next = document.getElementById("next");


let pans = document.getElementsByClassName("panswers");
let p = pans[0].cloneNode(true);
let frm = document.querySelector("form");


send.addEventListener('click', (e) => {

    fetch('/test/getquestionfetch/', {
        method: 'POST',
        body: new FormData(frm),
		// headers : { 
		// 	'Content-Type': 'application/json',
		// 	'Accept': 'application/json'
		//    }
    })
    .then(
		response => {
			return response.json();
		})
    .then(
		data => {
			// let json = JSON.parse(data);
			console.log(data);
			for(var i=0; i<pans.length; i++) {
				frm.removeChild(pans[i]);
			}

			
      // div.innerHTML = data;
		}
	)
	.catch((error) => {
		console.error('Error:', error);
	  }
	);
	
	e.preventDefault();
})


