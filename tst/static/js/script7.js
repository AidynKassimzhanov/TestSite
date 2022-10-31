"use strict"

let send = document.getElementById("send");
let prev = document.getElementById("prev");
let next = document.getElementById("next");

// let next = document.getElementById("next");

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

      // div.innerHTML = data;
		}
	)
	.catch((error) => {
		console.error('Error:', error);
	  }
	);
	
	e.preventDefault();
})


