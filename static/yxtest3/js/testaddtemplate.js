/**
 * Created by Administrator on 2016/11/17.
 */
$(function () {
     $("#submit_btn1").click(function () {
         var data = check()
         console.log(data)
         if (data != null) {
             $("#testname").ajaxSubmit({
                 type: 'post',
                 url: 'submit/',
                 data: data,
                 dataType: "json",
                 success: function (data) {
                     console.log(data)
                     alert('添加成功')
                 }

             });
         }
         /*if (data != null) {
             console.log("hello")
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
         }*/
         $("#back_btn1").click(function () {
             window.history.back(-1);

         });
     });
         });


function check() {
    name=$("#name").val();
    doc=$("#doc").val()
    creator=$("#creator").val()
    status=$("#status").val()
    time=$("#time").val()
    requirement_id=$("#requirement_id").val()
    requirement_name=$("#requirement_name").val()
    if(name==''||checktext(name)){
        alert('测试案例名称为空或者含有%&\' , ; = ? $ \"这些非法字符串')
        return false;
    }
    if(doc==''||checktext(doc)){
        alert('文档名称为空或者含有%&\' , ; = ? $ \"这些非法字符串')
        return false;
    }
    if(creator==''||checktext(creator)){
        alert('负责人为空或者含有%&\' , ; = ? $ \"这些非法字符串')
        return false;
    }
    if(status==''||checktext(status)){
        alert('状态为空或者含有%&\' , ; = ? $ \"这些非法字符串')
        return false;
    }
    if(time==''){
        alert('日期时间填完整')
        return false;
    }
    if( requirement_id==''||checktext(requirement_id)){
        return false;
    }
     if( requirement_name==''||checktext(requirement_name)){
        return false;
    }
    return {'name':name,'doc':doc,'creator':creator,'status':status,'time':time,'requirement_id':requirement_id,'requirement_name':requirement_name};
}

function checktext(text) {
   /* 如果返回ture说明包含非法字符，返回false说明不包含*/
    reg = /\w*[%&',;=?$\x22]+/;
    if (reg.test(text))
        return true;
    else
        return false;

}
