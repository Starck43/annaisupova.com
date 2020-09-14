document.addEventListener("DOMContentLoaded", function() {
	const logo = document.querySelector('#logo');
	const contact_name = document.querySelector('#id_name');
	const contact_email = document.querySelector('#id_email');
	const contact_message = document.querySelector('#id_message');
	const contact_btn = document.querySelector('#send-message-btn');
	console.log(location.href);
	var img = new Image();
	if (logo) img.src = logo.currentSrc;
	img.onload = function() {
		contactsElementsAdjust(logo.height);
	}

	//var secondContainer  = document.querySelector('.second-container');
	contactsElementsAdjust = function(obj_height){
		contact_name.style.height = contact_email.style.height = (obj_height*0.93) + 'px';
/*		var heightDiff = secondContainer.clientHeight-secondContainer.scrollHeight;
		contact_message.style.height = contact_message.clientHeight + heightDiff + 'px';*/
	}

/*	const inputItems = document.querySelectorAll('.dropdown-item');
	inputItems.forEach( (item) => {
		item.addEventListener('click', (e) => {
		}, {passive: true});
	});
*/
	const contact_form = document.querySelector('form'),
		contacts = document.querySelector('.contacts-block');
	contact_form.addEventListener("focus", (e) => {
			contacts.style.top = -contact_btn.clientHeight + 'px';
			contact_btn.classList.add('active');
			contact_message.style.minHeight = '80px';
	}, true);

	contact_form.addEventListener("blur", (e) => {
			contacts.style.top = '0';
			contact_btn.classList.remove('active');
			contact_message.style.minHeight = 'auto';

	}, true);

	window.addEventListener("resize", function(){
		contactsElementsAdjust(logo.height);

		if ( window.matchMedia("(orientation: landscape)").matches ) {
			document.getElementsByTagName("html")[0].style.height = "100vh";

			setTimeout(function(){
				document.getElementsByTagName("html")[0].style.height = "100%";
			}, 500);
		}
	}, true);

	const container  = document.querySelector('.container');
	container.addEventListener("click", (e) => {
		var section = e.target.parentElement.getAttribute('section');
		if ( section ) {
			container.classList.toggle(section+'__selected');
			if ( ! container.classList.contains(section+'__selected')) section = '';
			setLocation(section);
		}
	});

	// Выполнение кода при отображении страницы при возврате назад в браузере
	window.addEventListener( "pageshow", (e) => {
		var historyTraversal = e.persisted || ( typeof window.performance != "undefined" && window.performance.navigation.type === 2 );
		var section = location.pathname.replace(/\//g, '');
		if ( historyTraversal && (section == 'design'|| section == 'styling') ) {
			container.classList.add(section+'__selected');
		}
	});
/*	window.onpopstate = function(event) {
		alert(`location: ${document.location}, state: ${JSON.stringify(event.state)}`)
	}*/

});

function setLocation(curLoc){
	if (curLoc == '') {
		history.replaceState(null, null, '/');
	}
	else
	{
		curLoc = '/'+curLoc.replace(/\//g, '') + '/';
		if ( curLoc == location.pathname ) return;
		//location.pathname = curLoc;
		try {
			history.pushState(null, null, curLoc);
			return;
		} catch(e) {}
	}
}