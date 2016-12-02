/**
 * Created by Administrator on 2016/11/17.
 */
$(function () {
    $("#submit_btn").click(function () {
        var data = getdataAndCheck();
        if (data != null) {
            $.ajax({
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
    $("#back_btn").click(function () {
        window.history.back(-1);
    });
});
function getdataAndCheck() {
    var name = $("#name").val();
    var time = $("#time").val();
    var root = $("#root").val();
    var pre = $("#pre").val();
    var status = $("#status").val();
    if (name == '' || checktext(name)) {
        alert('需求案例名称为空或者含有%&\' , ; = ? $ \"这些非法字符串')
        return null;
    }
    if (time == '') {
        alert('日期时间填完整')
        return null;
    }
    return {name: name, time: time, root: root, pre: pre, status: status}
}
function checktext(text) {
    /**如果返回ture说明包含非法字符，返回false说明不包含**/
    reg = /\w*[%&',;=?$\x22]+/;
    if (reg.test(text))
        return true;
    else
        return false;

}