console.log("create.!!js")

let content_area = document.getElementById('content_area');


function delChild() {
    content_area.lastElementChild.remove();
}

function addChild() {
    const template = document.getElementById('input_form');
    const clone = template.content.cloneNode(true);

    clone.querySelectorAll("*").forEach((data, idx) =>{
        if(data.id !== "" &&  data.id !== "add_box" && data.id !== "del_box"){
            data.id = data.id + parseInt(content_area.children.length + 1);
        }
        if(data.name === "column_type"){
            data.name = data.name + parseInt(content_area.children.length + 1);
        }
    });

    content_area.appendChild(clone);
    initChild();

}

function initChild() {

    
    delete_button = document.getElementsByClassName("delete_button");
    tmp = 
    console.log()
    delete_button[content_area.children.length-1].addEventListener('click',(e)=>{
        if (content_area.children.length > 1){
            let idx = parseInt(e.target.id.match(/[0-9]+/)[0])-1;
            content_area.children[idx].remove();
        } else {
            window.alert("項目は必ず1つ以上必要です。");
        }
    });

    let idx = content_area.children.length-1;
    gt = document.getElementsByClassName("generate_type");
    lct = document.getElementsByClassName("link_column_form");
    gt[idx].style.display = "";
    lct[idx].style.display = "none";

    g_date = document.getElementsByClassName("generate_date");
    g_datetime = document.getElementsByClassName("generate_datetime");
    g_link_date = document.getElementsByClassName("generate_link_date");
    g_link_datetime = document.getElementsByClassName("generate_link_datetime");
    g_text = document.getElementsByClassName("generate_text");
    g_link_text = document.getElementsByClassName("generate_link_text");
    g_date[idx].style.display = "";
    g_datetime[idx].style.display = "none";
    g_link_date[idx].style.display = "none";
    g_link_datetime[idx].style.display = "none";
    g_text[idx].style.display = "none";
    g_link_text[idx].style.display = "none";
}

function control_visible_Ctype(obj){
    column_type = document.getElementsByName("column_type");

    let form_num = parseInt(obj.id.match(/[0-9]+/)[0]);
    let idx = form_num - 1;

    gt = document.getElementsByClassName("generate_type");
    lct = document.getElementsByClassName("link_column_form");
    if (obj.checked){
        if (obj.id === "normal_column_radio" + form_num) {
            console.log(obj.id);
            gt[idx].style.display = "";
            lct[idx].style.display = "none";
        } else if (obj.id === "link_column_radio" + form_num) {
            console.log(obj.id);
            gt[idx].style.display = "none";
            lct[idx].style.display = "";
        } else {
            console.log("hazure", obj.id , form_num);
            window.alert("エラー。要確認！");
        }
    }
    // generate_type[content_area.children.length-1].addEventListener('click',(e)=>{
    //     let idx = parseInt(e.target.id.match(/[0-9]+/)[0])-1;
    //     if(){
    //         content_area.children[idx].remove();
    //     }
    // });
}

function control_visible_Dtype(obj){
    console.log(obj);

    data_type = document.getElementsByName("data_type");

    let form_num = parseInt(obj.id.match(/[0-9]+/)[0]);
    let idx = form_num - 1;

    dt = document.getElementsByClassName("data_type_menu");
    console.log(dt[idx].value);


}


// console.log(document.getElementsByClassName("column_type"));
// document.getElementsByClassName("column_type").addEventListener("click", () => {
//     console.log(document.getElementsByClassName("column_type"));
// });

window.addEventListener('DOMContentLoaded', function(){
    addChild();
    document.getElementById("add_box").addEventListener("click", () => {
        addChild();
    });
    document.getElementById("del_box").addEventListener("click", () => {
        if (content_area.children.length > 1){
            delChild();
        } else {
            window.alert("項目は必ず1つ以上必要です。");
        }
    });
});