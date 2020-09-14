document.addEventListener("DOMContentLoaded", function() {
	const eventItems = document.querySelectorAll('.event-year-title');
	eventItems.forEach( (item) => {
		item.addEventListener('click', (elem) => {
			const hiddenBlock = elem.target.nextElementSibling;
			hiddenBlock.style.height = elem.target.classList.contains('collapsed') ? 0 : hiddenBlock.scrollHeight + 'px';
			elem.target.classList.toggle('collapsed');
		}, {passive: true});
	});
});