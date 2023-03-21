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