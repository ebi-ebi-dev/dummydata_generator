let input_property =  {
  
}

function set_inputtype(form_id) {
  input_property.input_type = document.getElementById(form_id).value;
  console.log("input_property: ", input_property);
  enable_JSONupload(form_id);
}

function enable_JSONupload(form_id) {
    $.ajax({
      'url': '/product_and_random/',
      'type': 'POST',
      'data': {
        'input_type': input_property.input_type,
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
      $('#JSON_upload_form').empty();
      console.log(response);
      const obj = JSON.parse(response)
      $('#JSON_upload_form').append(obj.input_type_form);
      console.log($('#JSON_upload_form'));
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