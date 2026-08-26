document.addEventListener("DOMContentLoaded", function () {
    const filterBox = document.querySelector(".event_filter");
    const cards = document.querySelectorAll("#services-grid .event_outer");

    if (!filterBox || cards.length === 0) return;

    filterBox.addEventListener("click", function (e) {
        const link = e.target.closest("a");
        if (!link) return;

        e.preventDefault();
        const unitId = link.getAttribute("data-unit");

        cards.forEach(function (card) {
            const match = !unitId || card.getAttribute("data-unit") === unitId;
            card.style.display = match ? "" : "none";
        });

        filterBox.querySelector(".active")?.classList.remove("active");
        link.classList.add("active");
    });
});