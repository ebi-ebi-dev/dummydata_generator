document.getElementById("go_createData").addEventListener("click", () => {
    window.location.href = 'http://localhost:8000/create/';
});

document.getElementById("go_prodAndRand").addEventListener("click", () => {
    console.log("clicked");
    window.location.href = 'http://localhost:8000/product_and_random/';
});