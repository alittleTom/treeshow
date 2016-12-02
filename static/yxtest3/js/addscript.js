$(function () {
    $("#submit_btn1").click(function () {
        var data = getdataAndCheck();
        if (data != null) {
            $("#testname1").ajaxSubmit({
                type: "post",
                url: "submit/",
                data: data,
                dataType: "json",
                success: function (resultJson) {
                    console.log(resultJson)
                    alert('添加成功')
                }
            });
        }
    });

    $("#back_btn1").click(function () {
        window.history.back(-1);
    });
});
function getdataAndCheck(data) {
    var name = $("#name").val();
    var creator = $("#creator").val();
    var time = $("#time").val();
    var doc = $("#id_filePath").val();
    var remarks = $("#remarks").val();
    var test_id = $("#test_id").val();
   /* var doc = document.getElementById('doc');
    /!*doc.select();*!/
   /!* var realpath = document.selection.createRange().text;*!/*/
    console.log(doc)
    if (name == '' || checktext(name)) {
        alert('脚本案例名称为空或者含有%&\' , ; = ? $ \"这些非法字符串')
        return null;
    }
    if(creator==''||checktext(creator)){
        alert('负责人为空或者含有%&\' , ; = ? $ \"这些非法字符串')
        return false;
    }
    if (time == '') {
        alert('日期时间填完整')
        return null;
    }
    if(doc==''||checktext(doc)){
        alert('文档名称为空或者含有%&\' , ; = ? $ \"这些非法字符串')
        return false;
    }
    if(remarks == '' || checktext(remarks)){
         alert('备注为空或者含有%&\' , ; = ? $ \"这些非法字符串')
        return false;
    }
    return {name: name, creator: creator, time:time, doc:doc, remarks: remarks,test_id:test_id, }
}

function checktext(text) {
    /**如果返回ture说明包含非法字符，返回false说明不包含**/
    reg = /\w*[%&',;=?$\x22]+/;
    if (reg.test(text))
        return true;
    else
        return false;

}