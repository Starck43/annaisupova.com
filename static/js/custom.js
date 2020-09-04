document.addEventListener("DOMContentLoaded", function() {
	var date = new Date(), hours = date.getHours();
	//console.log(hours);
	if (hours > 18 || hours < 7) {
		const html = document.querySelector('html');
		html.style.filter = 'invert(80%)';
	}
	$('textarea').summernote({
		//airMode: true,
		lang: 'ru-RU',
		tabsize: 2,
		height: 150,
	});

	function backToTop(){
		var scrollStep = window.pageYOffset / 20;
		if (window.pageYOffset > 0) {
			window.scrollBy(0, -(scrollStep));
			setTimeout(backToTop, 0);
		}
	}

	const gotoUpLink = document.querySelector('.go-to-up');
	gotoUpLink && gotoUpLink.addEventListener("click", function(e) {
		e.preventDefault();
		backToTop();
		/*
		window.scrollTo({
			top: 0,
			behavior: 'smooth'
		});
		*/
	}, {passive: true});
/*
	const dropdownItems = document.querySelectorAll('.dropdown-item');
	dropdownItems.forEach( (item) => {
		item.addEventListener('click', (e) => {
			for (let sibling of e.target.parentNode.children) {
				sibling.classList.remove('active');
			}
			e.target.classList.add('active')
		}, {passive: true});
	});
*/
});