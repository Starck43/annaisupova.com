document.addEventListener("DOMContentLoaded", function() {
	const sidebar = document.querySelector('.nav-block');
	const searchForm = document.querySelector('.search-form');
	const homePage = document.querySelector('.home');

	if ( ! homePage && window.innerWidth >= 992 ) {
		sidebar.classList.add('active');
	}

	const burger = document.querySelector('#burger-menu');
	burger.addEventListener("click", (e) => {
		sidebar.classList.toggle('active');
	}, true);

	const search = document.querySelector('.search-link');
	search.addEventListener("click", (e) => {
		searchForm.classList.toggle('active');
	}, true);



});
