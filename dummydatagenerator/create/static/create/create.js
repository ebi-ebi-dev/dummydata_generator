console.log("create.!!js")

let content_area = document.getElementById('content_area');
let id_arr = [];


function delChild() {
    content_area.lastElementChild.remove();
}

function addChild() {
    const template = document.getElementById('input_form');
    const clone = template.content.cloneNode(true);

    clone.querySelectorAll("*").forEach((data, idx) =>{
        if(data.id !== "" &&  data.id !== "add_box" && data.id !== "del_box"){
            if (id_arr.length > 0){
                data.id = data.id + parseInt(Math.max(...id_arr) + 1);
            } else {
                data.id = data.id + 1;
            }
        }
        if(data.name === "column_type"){
            data.name = data.name + parseInt(content_area.children.length + 1);
            if (id_arr.length > 1){
                data.name = data.name + parseInt(Math.max(...id_arr) + 1);
            } else {
                data.name = data.name + 1;
            }
        }
    });

    content_area.appendChild(clone);
    initChild();

    box_forms = document.querySelectorAll(`.box`);
    id_arr = [];
    box_forms.forEach((d,i) =>{
        id_arr.push(parseInt(d.id.match(/[0-9]+/)[0]));
    });

}

function initChild() {

    delete_button = document.getElementsByClassName("delete_button");
    delete_button[content_area.children.length-1].addEventListener('click',(e)=>{
        if (content_area.children.length > 1){
            let remove_id = parseInt(e.target.id.match(/[0-9]+/)[0]);
            let remove_idx = id_arr.indexOf(remove_id);
            id_arr.splice(remove_idx, 1); 
            content_area.children[remove_idx].remove();
        } else {
            window.alert("項目は必ず1つ以上必要です。");
        }
    });

    initForm(content_area.children.length)
}

function clearForm(obj){
    initForm(obj.id.match(/[0-9]+/)[0]);
}

function initForm(init_id){
    
    let init_idx = id_arr.indexOf(init_id);

    // カラム名の初期化
    document.getElementById('column_name_text' + init_id).value = "";

    // カラムタイプの初期化、表示項目の初期化
    document.getElementById('normal_column_radio' + init_id).checked = true;
    document.getElementById('product' + init_id).selected = true;
    document.getElementById('link_column_form' + init_id).value = "";

    document.getElementById('generate_type' + init_id).style.display = "";
    document.getElementById('link_column_form' + init_id).style.display = "none";

    // データ・タイプの初期化、詳細フォームの初期化、表示項目の初期化
    document.getElementById('generate_text_area' + init_id).value = "";
    document.getElementById('generate_link_text_area' + init_id).value = "";

    document.getElementById('number_min' + init_id).value = "";
    document.getElementById('number_max' + init_id).value = "";
    document.getElementById('number_step' + init_id).value = "";

    document.getElementById('date_min' + init_id).value = "";
    document.getElementById('date_max' + init_id).value = "";
    document.getElementById('date_step' + init_id).value = "";
    document.getElementById('date_link_min' + init_id).value = "";
    document.getElementById('date_link_max' + init_id).value = "";

    document.getElementById('datetime_min' + init_id).value = "";
    document.getElementById('datetime_max' + init_id).value = "";
    document.getElementById('datetime_step' + init_id).value = "";
    document.getElementById('datetime_link_min' + init_id).value = "";
    document.getElementById('datetime_link_max' + init_id).value = "";

    document.getElementById("generate_text" + init_id).style.display = "none";
    document.getElementById("generate_link_text" + init_id).style.display = "none";
    document.getElementById("generate_number" + init_id).style.display = "none";
    document.getElementById("generate_link_number" + init_id).style.display = "none";
    document.getElementById("generate_date" + init_id).style.display = "";
    document.getElementById("generate_link_date" + init_id).style.display = "none";
    document.getElementById("generate_datetime" + init_id).style.display = "none";
    document.getElementById("generate_link_datetime" + init_id).style.display = "none";
}

function control_visible_Ctype(obj){

    let change_id = parseInt(obj.id.match(/[0-9]+/)[0]);
    let change_idx = id_arr.indexOf(change_id);

    gt = document.getElementById("generate_type" + change_id);
    lct = document.getElementById("link_column_form" + change_id);

    g_text = document.getElementById("generate_text" + change_id);
    g_link_text = document.getElementById("generate_link_text" + change_id);
    g_number = document.getElementById("generate_number" + change_id);
    g_link_number = document.getElementById("generate_link_number" + change_id);
    g_date = document.getElementById("generate_date" + change_id);
    g_link_date = document.getElementById("generate_link_date" + change_id);
    g_datetime = document.getElementById("generate_datetime" + change_id);
    g_link_datetime = document.getElementById("generate_link_datetime" + change_id);

    console.log(change_id, change_idx, id_arr, gt);
    if (obj.checked){
        if (obj.id === "normal_column_radio" + change_id) {
            gt.style.display = "";
            lct.style.display = "none";

            document.getElementById("data_type_date" + change_id).selected = true;
            console.log(document.getElementById("data_type_text" + change_id).selected);
            g_text.style.display = "none";
            g_link_text.style.display = "none";
            g_number.style.display = "none";
            g_link_number.style.display = "none";
            g_date.style.display = "";
            g_link_date.style.display = "none";
            g_datetime.style.display = "none";
            g_link_datetime.style.display = "none";
        } else if (obj.id === "link_column_radio" + change_id) {
            gt.style.display = "none";
            lct.style.display = "";

            document.getElementById("data_type_date" + change_id).selected = true;
            console.log(document.getElementById("data_type_text" + change_id).selected);
            g_text.style.display = "none";
            g_link_text.style.display = "none";
            g_number.style.display = "none";
            g_link_number.style.display = "none";
            g_date.style.display = "none";
            g_link_date.style.display = "";
            g_datetime.style.display = "none";
            g_link_datetime.style.display = "none";
        } else {
            console.log("hazure", obj.id , change_id);
            window.alert("エラー。要確認！");
        }
    }

    
}

function control_visible_Dtype(obj){

    let change_id = parseInt(obj.id.match(/[0-9]+/)[0]);
    let change_idx = id_arr.indexOf(change_id);

    // データタイプの表示非表示制御

    // generate_typeの選択状況取得
    is_normal_checked = document.getElementById("normal_column_radio" + change_id).checked;

    // deta_typeの選択状況取得
    dt_selected = {
        "text" : document.getElementById("data_type_text" + change_id).selected,
        "number" : document.getElementById("data_type_number" + change_id).selected,
        "date" : document.getElementById("data_type_date" + change_id).selected,
        "datetime" : document.getElementById("data_type_datetime" + change_id).selected,
    }

    // 表示非表示制御
    g_text = document.getElementsByClassName("generate_text");
    g_link_text = document.getElementsByClassName("generate_link_text");
    g_number = document.getElementsByClassName("generate_number");
    g_link_number = document.getElementsByClassName("generate_link_number");
    g_date = document.getElementsByClassName("generate_date");
    g_link_date = document.getElementsByClassName("generate_link_date");
    g_datetime = document.getElementsByClassName("generate_datetime");
    g_link_datetime = document.getElementsByClassName("generate_link_datetime");

    if (is_normal_checked){
        Object.keys(dt_selected).forEach( (key, i) => {
            switch (true) {
                case key === "text" && dt_selected[key]: 
                    console.log(is_normal_checked, key, dt_selected[key]);
                    g_text[change_idx].style.display = "";
                    g_link_text[change_idx].style.display = "none";
                    g_number[change_idx].style.display = "none";
                    g_link_number[change_idx].style.display = "none";
                    g_date[change_idx].style.display = "none";
                    g_link_date[change_idx].style.display = "none";
                    g_datetime[change_idx].style.display = "none";
                    g_link_datetime[change_idx].style.display = "none";
                    break;
                
                case key === "number" && dt_selected[key]: 
                    console.log(is_normal_checked, key, dt_selected[key]);
                    g_text[change_idx].style.display = "none";
                    g_link_text[change_idx].style.display = "none";
                    g_number[change_idx].style.display = "";
                    g_link_number[change_idx].style.display = "none";
                    g_date[change_idx].style.display = "none";
                    g_link_date[change_idx].style.display = "none";
                    g_datetime[change_idx].style.display = "none";
                    g_link_datetime[change_idx].style.display = "none";
                    break;
                
                case key === "date" && dt_selected[key]: 
                    console.log(is_normal_checked, key, dt_selected[key]);
                    g_text[change_idx].style.display = "none";
                    g_link_text[change_idx].style.display = "none";
                    g_number[change_idx].style.display = "none";
                    g_link_number[change_idx].style.display = "none";
                    g_date[change_idx].style.display = "";
                    g_link_date[change_idx].style.display = "none";
                    g_datetime[change_idx].style.display = "none";
                    g_link_datetime[change_idx].style.display = "none";
                    break;
                
                case key === "datetime" && dt_selected[key]: 
                    console.log(is_normal_checked, key, dt_selected[key]);
                    g_text[change_idx].style.display = "none";
                    g_link_text[change_idx].style.display = "none";
                    g_number[change_idx].style.display = "none";
                    g_link_number[change_idx].style.display = "none";
                    g_date[change_idx].style.display = "none";
                    g_link_date[change_idx].style.display = "none";
                    g_datetime[change_idx].style.display = "";
                    g_link_datetime[change_idx].style.display = "none";
                    break;
            }
        })
    } else {
        Object.keys(dt_selected).forEach( (key, i) => {
            switch (true) {
                case key === "text" && dt_selected[key]: 
                    console.log(is_normal_checked, key, dt_selected[key]);
                    g_text[change_idx].style.display = "none";
                    g_link_text[change_idx].style.display = "";
                    g_number[change_idx].style.display = "none";
                    g_link_number[change_idx].style.display = "none";
                    g_date[change_idx].style.display = "none";
                    g_link_date[change_idx].style.display = "none";
                    g_datetime[change_idx].style.display = "none";
                    g_link_datetime[change_idx].style.display = "none";
                    break;
                
                case key === "number" && dt_selected[key]: 
                    console.log(is_normal_checked, key, dt_selected[key]);
                    g_text[change_idx].style.display = "none";
                    g_link_text[change_idx].style.display = "none";
                    g_number[change_idx].style.display = "none";
                    g_link_number[change_idx].style.display = "";
                    g_date[change_idx].style.display = "none";
                    g_link_date[change_idx].style.display = "none";
                    g_datetime[change_idx].style.display = "none";
                    g_link_datetime[change_idx].style.display = "none";
                    break;
                
                case key === "date" && dt_selected[key]: 
                    console.log(is_normal_checked, key, dt_selected[key]);
                    g_text[change_idx].style.display = "none";
                    g_link_text[change_idx].style.display = "none";
                    g_number[change_idx].style.display = "none";
                    g_link_number[change_idx].style.display = "none";
                    g_date[change_idx].style.display = "none";
                    g_link_date[change_idx].style.display = "";
                    g_datetime[change_idx].style.display = "none";
                    g_link_datetime[change_idx].style.display = "none";
                    break;
                
                case key === "datetime" && dt_selected[key]: 
                    console.log(is_normal_checked, key, dt_selected[key]);
                    g_text[change_idx].style.display = "none";
                    g_link_text[change_idx].style.display = "none";
                    g_number[change_idx].style.display = "none";
                    g_link_number[change_idx].style.display = "none";
                    g_date[change_idx].style.display = "none";
                    g_link_date[change_idx].style.display = "none";
                    g_datetime[change_idx].style.display = "none";
                    g_link_datetime[change_idx].style.display = "";
                    break;
            }
        })
    }
}

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