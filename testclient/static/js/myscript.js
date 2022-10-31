"use strict"
let n = 1
let next = document.getElementById("next");
let prev = document.getElementById("prev");
let send = document.getElementById("send");
let frm = document.querySelector("form");
let current = document.querySelector("#current");
let start = document.getElementById("start");
let end = document.getElementById("end");

let c = parseInt(current.getAttribute('value'));
let s = parseInt(start.getAttribute('value'));
let e = parseInt(end.getAttribute('value'));
// console.log(c);




if (c == s) { prev.hidden = true }
else {prev.hidden = false }

if (c == e) { next.hidden = true }
else {next.hidden = false }
let radio = document.querySelectorAll('#p input')

function choice(e) {
	let ch = document.querySelector('#choice')
	var choi = e.target.id;
	ch.setAttribute('value', choi);
}

for (var i = 0; i < radio.length; i++) {
    radio[i].addEventListener("click", choice);
}

next.addEventListener('click', () => {
	c = c + 1
	current.setAttribute('value', String(c));
	fetchf();
});

prev.addEventListener('click', () => {
	c = c - 1
	current.setAttribute('value', String(c));
	fetchf();
});
// let ev = new Event('click');
// send.dispatchEvent(ev);

// fetchf(0);

function fetchf() {
	let promise = fetch('/testclient/fetch/', {
        method: 'POST',
        body: new FormData(frm),
	
    })
    .then(
		response => {
			return response.json();
		})
    .then(
		data => {
			// let json = JSON.parse(data);
			console.log(data);

		}
	)
	.catch((error) => {
		console.error('Error:', error);
	  }
	);
	e.preventDefault()
}

send.addEventListener('click', (e) => {
	let promise = fetch('/testclient/end/', {
        method: 'POST',
        body: new FormData(frm),
	
    })
    .then(
		response => {
			return response.json();
		})
	.catch((error) => {
		console.error('Error:', error);
	  }
	);
	e.preventDefault()
});


