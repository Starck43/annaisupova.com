document.addEventListener("DOMContentLoaded", function() {

	var slider = Peppermint( document.querySelector('#slider'), {
		dots: true,
		slideshow: false,
		speed: 600,
		slideshowInterval: 5000,
		stopSlideshowAfterInteraction: true,
		disableIfOneSlide: true,
		onSetup: function(n) {
			console.log('Slides count: ' + n);
		}
	});
	//сохранить ссылки на HTML-ноды
	const rightArrow = document.querySelector('#arrow-right');
	const leftArrow = document.querySelector('#arrow-left');

	//клик по `#right-arr` переключит на следующий слайд
	rightArrow.addEventListener('click', slider.next, false);

	//клик по `#left-arr` переключит на предыдущий слайд
	leftArrow.addEventListener('click', slider.prev, false);

	var lazyLoadInstance = new LazyLoad();
	window.onresize = function() {
		lazyLoadInstance = new LazyLoad();
	}

});
