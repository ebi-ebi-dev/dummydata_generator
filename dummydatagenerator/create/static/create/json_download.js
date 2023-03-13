

document.getElementById("json_download").addEventListener( 'click', (e) => {
    json_textarea = document.getElementById('json_form').value;
    let blobedText = new Blob([json_textarea], {type: 'text/plain' });
    let url = URL.createObjectURL(blobedText);

    // ダウンロード用のaタグ生成
    const a = document.createElement('a');
    a.href =  URL.createObjectURL(blobedText);
    a.download = 'sample.json';
    a.click();
    console.log(json_textarea);

});