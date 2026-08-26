(function ($) {

    "use strict";


    /* =====================================================
       ELEMENTS
    ===================================================== */

    const header = document.getElementById("site-header");

    const toggle = document.getElementById(
        "site-header-toggle"
    );

    const navigation = document.getElementById(
        "site-navigation"
    );


    if (!header) {
        return;
    }


    /* =====================================================
       HEADER SCROLL
       
       فقط Home که Hero دارد.
       صفحات داخلی مثل project_list
       از ابتدا Header ثابت دارند.
    ===================================================== */

    function updateHeader() {

        if (
            document.body.classList.contains(
                "inner-page"
            )
        ) {
            return;
        }


        const scrollTop = window.scrollY;

        const hero = document.getElementById("top");


        /*
         * اگر Hero وجود نداشت،
         * Header بعد از مقدار کمی اسکرول
         * شیشه‌ای شود.
         */

        if (!hero) {

            if (scrollTop > 20) {

                header.classList.add(
                    "is-scrolled"
                );

            } else {

                header.classList.remove(
                    "is-scrolled"
                );
            }

            return;
        }


        /*
         * Hero داریم.
         *
         * Header در ابتدا شفاف است.
         * بعد از عبور از Hero شیشه‌ای می‌شود.
         */

        const threshold = Math.max(
            hero.offsetHeight -
            header.offsetHeight -
            40,

            20
        );


        if (scrollTop > threshold) {

            header.classList.add(
                "is-scrolled"
            );

        } else {

            header.classList.remove(
                "is-scrolled"
            );
        }
    }


    /*
     * فقط روی صفحات Home
     */

    if (
        !document.body.classList.contains(
            "inner-page"
        )
    ) {

        window.addEventListener(
            "scroll",
            updateHeader,
            {
                passive: true
            }
        );


        window.addEventListener(
            "resize",
            updateHeader
        );


        updateHeader();
    }


    /* =====================================================
       MOBILE MENU
    ===================================================== */

    if (toggle && navigation) {

        toggle.addEventListener(
            "click",
            function () {

                const isOpen =
                    navigation.classList.toggle(
                        "is-open"
                    );


                toggle.setAttribute(
                    "aria-expanded",
                    isOpen
                        ? "true"
                        : "false"
                );
            }
        );


        /*
         * بعد از کلیک روی لینک،
         * منوی موبایل بسته شود.
         */

        navigation
            .querySelectorAll("a")
            .forEach(function (link) {

                link.addEventListener(
                    "click",
                    function () {

                        navigation.classList.remove(
                            "is-open"
                        );


                        toggle.setAttribute(
                            "aria-expanded",
                            "false"
                        );
                    }
                );
            });
    }


    /* =====================================================
       CLOSE MOBILE MENU
       وقتی بیرون منو کلیک شود
    ===================================================== */

    document.addEventListener(
        "click",
        function (event) {

            if (
                !toggle ||
                !navigation
            ) {
                return;
            }


            const clickedInsideHeader =
                header.contains(event.target);


            if (!clickedInsideHeader) {

                navigation.classList.remove(
                    "is-open"
                );


                toggle.setAttribute(
                    "aria-expanded",
                    "false"
                );
            }
        }
    );


})(window.jQuery);