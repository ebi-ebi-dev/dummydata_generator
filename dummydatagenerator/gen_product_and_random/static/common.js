function displayFormData(){
    const formElm = document.getElementById("json_upload_form");
    const displayElm = document.getElementById("display");
    displayElm.innerHTML = formElm.test_data.value;
    window.console.log("aaaa")
}