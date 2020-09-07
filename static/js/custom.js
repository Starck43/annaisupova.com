document.addEventListener("DOMContentLoaded", function() {
	var logo = document.querySelector('#logo');
	var contact_name = document.querySelector('#id_name');
	var contact_email = document.querySelector('#id_email');
	var contact_message = document.querySelector('#id_message');
	var contact_btn = document.querySelector('#send-message-btn');
	var secondContainer  = document.querySelector('.second-container');
	var img = new Image();

	img.src = logo.currentSrc;
	img.onload = function() {
		contactsElementsAdjust(logo.height);
	}

	contactsElementsAdjust = function(obj_height){
		contact_name.style.height = contact_email.style.height = (obj_height*0.93) + 'px';
/*		var heightDiff = secondContainer.clientHeight-secondContainer.scrollHeight;
		contact_message.style.height = contact_message.clientHeight + heightDiff + 'px';*/
	}

/*	const inputItems = document.querySelectorAll('.dropdown-item');
	dropdownItems.forEach( (item) => {
		item.addEventListener('click', (e) => {
		}, {passive: true});
	});*/
	const contact_form = document.querySelector('form');
	contact_form.addEventListener("focus", (e) => {

			contact_btn.classList.add('active');
			contact_message.style.minHeight = '80px';

	}, true);

	contact_form.addEventListener("blur", (e) => {

			contact_btn.classList.remove('active');
			contact_message.style.minHeight = 'auto';

	}, true);

	window.addEventListener("resize", function(){
		contactsElementsAdjust(logo.height);

		if ( window.innerWidth < 992 && window.matchMedia("(orientation: portrait)").matches ) {
			document.getElementsByTagName("html")[0].style.height = "100vh";

			setTimeout(function(){
				document.getElementsByTagName("html")[0].style.height = "100%";
			}, 500);
		}
	}, false);

});