document.addEventListener("DOMContentLoaded", function () {

    const slider = document.querySelector(".team-carousel");

    if (!slider) {
        return;
    }

    const wrapper = slider.querySelector(".team-carousel-track");
    const slides = Array.from(
        slider.querySelectorAll(".team-carousel-slide")
    );

    const nextButton = slider.querySelector(".team-carousel-next");
    const prevButton = slider.querySelector(".team-carousel-prev");
    const pagination = slider.querySelector(".team-carousel-dots");


    if (!wrapper || slides.length === 0) {
        return;
    }


    let currentIndex = 0;
    let autoplayTimer = null;


    /*
    ============================================
    تعداد کارت‌های قابل نمایش
    ============================================
    */

    function getVisibleSlides() {

        const width = window.innerWidth;

        if (width <= 575) {
            return 1;
        }

        if (width <= 991) {
            return 2;
        }

        if (width <= 1199) {
            return 3;
        }

        return 4;
    }


    /*
    ============================================
    بیشترین حرکت ممکن
    ============================================
    */

    function getMaxIndex() {

        return Math.max(
            0,
            slides.length - getVisibleSlides()
        );

    }


    /*
    ============================================
    فاصله هر کارت
    ============================================
    */

    function getStep() {

        if (slides.length === 0) {
            return 0;
        }

        const slide = slides[0];

        const style = window.getComputedStyle(wrapper);

        const gap = parseFloat(style.columnGap || style.gap) || 0;

        return slide.getBoundingClientRect().width + gap;

    }


    /*
    ============================================
    حرکت اسلایدر
    ============================================
    */

    function updateSlider() {

        const step = getStep();

        /*
        چون سایت RTL است،
        برای نشان دادن نفر بعدی track را
        به سمت چپ می‌بریم.
        */

        const distance = currentIndex * step;

        wrapper.style.transform =
            `translateX(-${distance}px)`;

        updateButtons();

        updatePagination();

    }


    /*
    ============================================
    دکمه‌ها
    ============================================
    */

    function updateButtons() {

        const maxIndex = getMaxIndex();

        /*
        اگر همه نفرات جا می‌شوند
        دکمه‌ها غیرفعال باشند
        */

        const disabled =
            slides.length <= getVisibleSlides();


        if (nextButton) {

            nextButton.disabled = disabled;

        }


        if (prevButton) {

            prevButton.disabled = disabled;

        }

    }


    /*
    ============================================
    Next
    ============================================
    */

    function nextSlide() {

        const maxIndex = getMaxIndex();


        if (maxIndex === 0) {
            return;
        }


        if (currentIndex < maxIndex) {

            currentIndex++;

        } else {

            /*
            وقتی به آخر رسیدیم
            دوباره برگرد اول
            */

            currentIndex = 0;

        }


        updateSlider();

    }


    /*
    ============================================
    Previous
    ============================================
    */

    function previousSlide() {

        const maxIndex = getMaxIndex();


        if (maxIndex === 0) {
            return;
        }


        if (currentIndex > 0) {

            currentIndex--;

        } else {

            /*
            اگر اول بودیم
            برو آخر
            */

            currentIndex = maxIndex;

        }


        updateSlider();

    }


    /*
    ============================================
    Pagination
    ============================================
    */

    function createPagination() {

        if (!pagination) {
            return;
        }


        pagination.innerHTML = "";


        const maxIndex = getMaxIndex();


        if (maxIndex === 0) {
            return;
        }


        for (
            let i = 0;
            i <= maxIndex;
            i++
        ) {

            const button =
                document.createElement("button");


            button.type = "button";


            button.className =
                "team-carousel-dot";


            button.setAttribute(
                "aria-label",
                `نمایش اسلاید ${i + 1}`
            );


            button.addEventListener(
                "click",
                function () {

                    currentIndex = i;

                    updateSlider();

                    restartAutoplay();

                }
            );


            pagination.appendChild(button);

        }


        updatePagination();

    }


    /*
    ============================================
    فعال کردن pagination
    ============================================
    */

    function updatePagination() {

        if (!pagination) {
            return;
        }


        const bullets =
            pagination.querySelectorAll(
                ".team-carousel-dot"
            );


        bullets.forEach(
            function (bullet, index) {

                bullet.classList.toggle(
                    "active",
                    index === currentIndex
                );

            }
        );

    }


    /*
    ============================================
    Autoplay
    ============================================
    */

    function stopAutoplay() {

        if (autoplayTimer) {

            clearInterval(
                autoplayTimer
            );

            autoplayTimer = null;

        }

    }


    function startAutoplay() {

        stopAutoplay();


        if (
            slides.length <=
            getVisibleSlides()
        ) {

            return;

        }


        autoplayTimer =
            setInterval(
                function () {

                    nextSlide();

                },
                5000
            );

    }


    function restartAutoplay() {

        startAutoplay();

    }


    /*
    ============================================
    کلیک دکمه راست
    ============================================
    */

    if (nextButton) {

        nextButton.addEventListener(
            "click",
            function (event) {

                event.preventDefault();

                nextSlide();

                restartAutoplay();

            }
        );

    }


    /*
    ============================================
    کلیک دکمه چپ
    ============================================
    */

    if (prevButton) {

        prevButton.addEventListener(
            "click",
            function (event) {

                event.preventDefault();

                previousSlide();

                restartAutoplay();

            }
        );

    }


    /*
    ============================================
    توقف هنگام رفتن موس روی اسلایدر
    ============================================
    */

    slider.addEventListener(
        "mouseenter",
        stopAutoplay
    );


    slider.addEventListener(
        "mouseleave",
        startAutoplay
    );


    /*
    ============================================
    Resize
    ============================================
    */

    window.addEventListener(
        "resize",
        function () {

            const maxIndex =
                getMaxIndex();


            if (currentIndex > maxIndex) {

                currentIndex =
                    maxIndex;

            }


            createPagination();

            updateSlider();

        }
    );


    /*
    ============================================
    شروع
    ============================================
    */

    createPagination();

    updateSlider();

    startAutoplay();

});