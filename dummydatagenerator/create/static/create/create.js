console.log("create.js")

let formIndex = 1;

function addForm() {
    let input_data = document.createElement('div');
    let content_area = document.getElementById("input_form");
    let clone_element = content_area.cloneNode(true);
    input_data = content_area;
    input_data.id = 'inputform_' + formIndex;
    console.log(input_data);
    // input_data.placeholder = 'フォーム-' + formIndex;
    var parent = document.getElementById('input_form');
    parent.appendChild(input_data);
    formIndex++ ;
}

document.getElementById("add_box").addEventListener("click", () => {
    addForm();
});

// document.getElementById("go_prodAndRand").addEventListener("click", () => {
//     console.log("clicked");
//     window.location.href = 'http://localhost:8000/product_and_random/';
// });