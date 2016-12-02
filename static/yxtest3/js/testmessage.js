/**
 * Created by Administrator on 2016/11/14.
 */
$(function () {
    //初始化Table
    var oTable=new TableInit()
    oTable.Init()
});

var TableInit=function () {
    var oTableInit=new Object();
    //初始化Table
    oTableInit.Init=function () {
        $('#table').bootstrapTable({
            url:getRootPath()+'gettable',  //请求后台的URL（*）
            method:'get',  //请求方式（*）
            toobar:'#toolbar',  //工具按钮用哪个容器
            stripted:true,  //是否显示行间隔色
            cache:false,  //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
            pagination:true,   //是否显示分页（*）
            sortable:true,  //是否启用排序
            sortOrder:"desc",  //排序方式
            queryParams:oTableInit.queryParams,  //传递参数（*）
            sidePagination:"server",   //分页方式：client客户端分页，server服务端分页（*）
            pageNumber:1,   //初始化加载第一页，默认第一页
            pageSize:10,  //每页的记录行数（*）
            pageList:[10,25,50,100],  //可供选择的每页的行数（*）
            search:true,  //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
            strictSearch:false,//设置为 true启用 全匹配搜索，否则为模糊搜索
            showColumns:true,   //是否显示所有的列
            showRefresh:true,   //是否显示刷新按钮
            minimumCountColumns:2,   //最少允许的列数
            clickToSelect:true,  //是否启用点击选中行
            height:500,    //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
            uniqueId:'id',  //每一行的唯一标识，一般为主键列
            showToggle:true,   //是否显示详细视图和列表视图的切换按钮
            cardView:false,   //是否显示详细视图
            detailView:false,   //是否显示父子表
           columns:[{
               checkbox:false
           },{
               field:'name',
               title:'需求名称'
           },{
               field:'rootname',
               title:'需求根节点'
           },{
               field:'prename',
               title:'上一需求'
           },{
               field:'status',
               title:'状态'
           },{
               field:'time',
               title:'创建时间'
           }]
        });
    };
    oTableInit.queryParams =function (params) {
        var temp={
            limit:params.limit,//页面大小
            offset:params.offset,//页码
        };
        return temp;
    }
    return oTableInit;
}

function getRootPath() {
//获取当前网址，如： /meun.jsp
    var curWwwPath = window.document.location.href;
//获取主机地址之后的目录，如： proj/meun.jsp
    var pathName = window.document.location.pathname;
    var pos = curWwwPath.indexOf(pathName);
//获取主机地址，如： http://localhost:8083
    var localhostPath = curWwwPath.substring(0, pos);
//获取带"/"的项目名，如：/proj
    var projectName = pathName.substring(0, pathName.substr(1).indexOf(
            '/') + 1);
    return (localhostPath + projectName);
}