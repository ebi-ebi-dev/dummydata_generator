
let input_property =  {
  
}

function set_columnname(form_id) {
  input_property.column_name = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_columntype(form_id) {
  input_property.column_type = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
  enable_generateType(form_id);
}

function set_generatetype(form_id) {
  input_property.generate_type = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_link_columnname(form_id) {
  input_property.link_column_name = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_datatype(form_id) {
  input_property.data_type = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
  enable_dataType(form_id);
}

function set_link_datatype(form_id) {
  input_property.link_data_type = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
  enable_dataType(form_id);
}

function set_text(form_id) {
  input_property.text = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_number_min(form_id) {
  input_property.number_min = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_number_max(form_id) {
  input_property.number_max = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_number_step(form_id) {
  input_property.number_step = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_date_min(form_id) {
  input_property.date_min = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_date_max(form_id) {
  input_property.date_max = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_date_step(form_id) {
  input_property.date_step = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_datetime_min(form_id) {
  input_property.datetime_min = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}
function set_datetime_max(form_id) {
  input_property.datetime_max = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}
function set_datetime_step(form_id) {
  input_property.datetime_step = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_link_text(form_id) {
  input_property.link_text = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_link_number_min(form_id) {
  input_property.link_number_min = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_link_number_max(form_id) {
  input_property.link_number_max = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_link_number_step(form_id) {
  input_property.link_number_step = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_link_date_min(form_id) {
  input_property.link_date_min = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}
function set_link_date_max(form_id) {
  input_property.link_date_max = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}
function set_link_date_step(form_id) {
  input_property.link_date_step = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}
function set_link_date_rand_min(form_id) {
  input_property.link_date_rand_min = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_link_date_rand_max(form_id) {
  input_property.link_date_rand_max = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function set_link_datetime_min(form_id) {
  input_property.link_datetime_min = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}
function set_link_datetime_max(form_id) {
  input_property.link_datetime_max = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}
function set_link_datetime_step(form_id) {
  input_property.link_datetime_step = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}
function set_link_datetime_rand_min(form_id) {
  input_property.link_datetime_rand_min = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}
function set_link_datetime_rand_max(form_id) {
  input_property.link_datetime_rand_max = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
}

function enable_generateType(form_id) {
  $.ajax({
    'url': '/create/',
    'type': 'POST',
    'data': {
      'column_name': input_property.column_name,
      'column_type': input_property.column_type,
    },
    traditional: true,
    contentType: "application/json",
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
            xhr.overrideMimeType("text/html;charset=UTF-8");
        }
        },
        success: function(data) {
          ;
        },
        error: function(xhr, status, error) {
            alert(status + "\n" + 
                    "Status: " + xhr.status + "\n" + error);
        }
  }).done(response => {
    // $('#new_form_1').empty();
    $('#generate_type_form').empty();
    $('#data_detail').empty();
    const obj = JSON.parse(response)
    // $('#new_form_1').append(obj.new_form1);
    $('#generate_type_form').append(obj.generate_type_form);
    console.log($('#generate_type_form'));
  }).fail(response => { // 通信が失敗したときの処理
    console.log("failed");
  });
}

function enable_dataType(form_id) {
  tmp_elm = document.getElementById(form_id);
  let child_nodes_count = tmp_elm.childElementCount;
  for(let i=0; i<child_nodes_count; i++) {
    let children = tmp_elm.children[i]
    let grandchild_nodes_count = children.childElementCount;
    for(let i=0; i<grandchild_nodes_count; i++) {
      console.log(children.children[i]);
    }
  }

  $.ajax({
    'url': '/create/',
    'type': 'POST',
    'data': {
      'column_name': input_property.column_name,
      'column_type': input_property.column_type,
      'generate_type': input_property.generate_type,
      'link_column_name': input_property.link_column_name,
      'data_type': input_property.data_type,
    },
    traditional: true,
    contentType: "application/json",
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
            xhr.overrideMimeType("text/html;charset=UTF-8");
        }
        },
        success: function(data) {
          ;
        },
        error: function(xhr, status, error) {
            alert(status + "\n" + 
                    "Status: " + xhr.status + "\n" + error);
        }
  }).done(response => {
    $('#data_detail').empty();
    $('#gen_button').empty();
    $('#output_json').empty();
    const obj = JSON.parse(response)
    $('#data_detail').append(obj.data_detail);
    $('#gen_button').append(obj.gen_button);
    $('#output_json').append(obj.output_json);
    console.log(obj.gen_button);
  }).fail(response => { // 通信が失敗したときの処理
    console.log("failed");
  });
}

function send_data_detail(form_id) {
  $.ajax({
    'url': '/create/',
    'type': 'POST',
    'data': {
      'column_name': input_property.column_name,
      'column_type': input_property.column_type,
      'generate_type': input_property.generate_type,
      'link_column_name': input_property.link_column_name,
      'data_type': input_property.data_type,

      'text': input_property.text,
      'number_min': input_property.number_min,
      'number_max': input_property.number_max,
      'number_step': input_property.number_step,
      'date_min': input_property.date_min,
      'date_max': input_property.date_max,
      'date_step': input_property.date_step,
      'datetime_min': input_property.datetime_min,
      'datetime_max': input_property.datetime_max,
      'datetime_step': input_property.datetime_step,

      'link_text': input_property.link_text,
      'link_number_min': input_property.link_number_min,
      'link_number_max': input_property.link_number_max,
      'link_number_step': input_property.link_number_step,
      'link_date_min': input_property.link_date_min,
      'link_date_max': input_property.link_date_max,
      'link_date_step': input_property.link_date_step,
      'link_date_rand_min': input_property.link_date_rand_min,
      'link_date_rand_max': input_property.link_date_rand_max,
      
      'link_datetime_min': input_property.link_datetime_min,
      'link_datetime_max': input_property.link_datetime_max,
      'link_datetime_step': input_property.link_datetime_step,
      'link_datetime_rand_min': input_property.link_datetime_rand_min,
      'link_datetime_rand_max': input_property.link_datetime_rand_max,

    },
    traditional: true,
    contentType: "application/json",
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
            xhr.overrideMimeType("text/html;charset=UTF-8");
        }
        },
        success: function(data) {
          ;
        },
        error: function(xhr, status, error) {
            alert(status + "\n" + 
                    "Status: " + xhr.status + "\n" + error);
        }
  }).done(response => {
    $('#output_json').empty();
    const obj = JSON.parse(response)
    $('#output_json').append(obj.output_json);
    console.log(obj);
  }).fail(response => { // 通信が失敗したときの処理
    console.log("failed");
  });
}


//// for CSRF /////

// ①Django側にPOST送信する際に記述する"お決まりのコード"
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function generate(){
  console.log("generate")
}

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}