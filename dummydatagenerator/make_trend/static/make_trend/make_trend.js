const scrollToTrendForm = function () {
    console.log("scrollToTrendForm ")
    const TrendFormLeft = document.getElementById("trendform").getBoundingClientRect().left;
    const TrendFormBottom = document.getElementById("trendform").getBoundingClientRect().bottom;
    window.scrollTo({
        left: TrendFormLeft,
        top: TrendFormBottom,
        behavior: 'smooth'
    });
};
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})