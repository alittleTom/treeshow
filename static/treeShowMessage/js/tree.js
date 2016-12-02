/**
 * Created by Administrator on 2016/11/7.
 */

$(function () {
    getdata();

    $("#loading").ajaxStart(function () {
        $(this).html("加载中");
    });
    $("#loading").ajaxSuccess(function () {
        $(this).html("");
        // $(this).empty(); // 或者直接清除
    });

});
function getdata() {
    $.ajax({
        type: 'get',
        url: "gettreedata/",
        dataType: 'json',
        success: function (result) {

            $('#tree').treeview({
                color: "#428bca",
                showBorder: false,
                data: result,
                borderColor: 'red',
                showTags: true,
                enableLinks: false,
                levels: 1,
                onhoverColor: '#B7FF4A',
                onNodeSelected: function (event, data) {
                    // 事件代码...
                    if (data.nodes == undefined) {
                        //叶子节点添加事件

                        $.ajax({
                            type: "get",
                            data: {'q': data.text},
                            url: '/showInfo/',
                            success: function (data) {
                                ajaxobj = eval("(" + data + ")")
                                show(ajaxobj);
                            }
                        });
                    }
                },
            });
        }
    });

}
function show(data) {
    $("#kemu").html(ifnull(data.kemu))
    $("#huizong2").html(ifnull(data.huizong2))
    $("#huizong1").html(ifnull(data.huizong1))
    $("#mingxi").html(ifnull(data.mingxi))
    $("#leixing").html(ifnull(data.leixing))
    $("#shujuyuan").html(ifnull(data.shujuyuan))
    $("#choujinmingcheng").html(ifnull(data.酬金名称))
    $("#choujinjieguobiao").html(ifnull(data.酬金结果表))
    $("#cunchuguocheng").html(ifnull(data.存储过程))

}
function ifnull(data) {
    if (data == "") {
        return '无'
    }
    else {
        return data
    }
}

function getTabMessage() {
    var date = $("#date").val()
    var mxname = $("#mingxi").html()
    if (date == "") {
        alert("月份不能为空")
    } else if (mxname == "") {
        alert("请先选择要查询的酬金")
    } else {
        inittable()
    }
}

function inittable() {
    $('#kf_table').bootstrapTable('destroy');
    $('#cs_table').bootstrapTable('destroy');
    $("#kf_table").bootstrapTable({
        url: 'getkftable',  //请求后台的URL（*）
        dataType: 'json',
        method: 'get',  //请求方式（*）
        toolbar: '#toolbar',  //工具按钮用哪个容器
        stripted: true,  //是否显示行间隔色
        cache: false,  //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
        pagination: true,   //是否显示分页（*）
        sortable: false,  //是否启用排序
        sortOrder: "asc",  //排序方式
        queryParams: function () {
            return {
                //limit: params.limit,//页面大小
                //offset: params.offset,//页码
                date: $("#date").val(),
                mxname: $("#mingxi").html(),
            }
        },  //传递参数（*）
        sidePagination: "server",   //分页方式：client客户端分页，server服务端分页（*）
        pageNumber: 1,   //初始化加载第一页，默认第一页
        pageSize: 5,  //每页的记录行数（*）
        pageList: [10, 25, 50, 100],  //可供选择的每页的行数（*）
        search: true,  //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
        strictSearch: false,//设置为 true启用 全匹配搜索，否则为模糊搜索
        showColumns: true,   //是否显示所有的列
        showRefresh: true,   //是否显示刷新按钮
        minimumCountColumns: 2,   //最少允许的列数
        clickToSelect: true,  //是否启用点击选中行
        height: 500,    //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
        uniqueId: '主键1',  //每一行的唯一标识，一般为主键列
        showToggle: true,   //是否显示详细视图和列表视图的切换按钮
        cardView: false,   //是否显示详细视图
        detailView: false,   //是否显示父子表
        columns: [{
            field: '主键1',
            title: '主键1'
        }, {
            field: '主键2',
            title: '主键2'
        }, {
            field: '酬金',
            title: '酬金'
        }, {
            field: '渠道编码',
            title: '渠道编码'
        },
        ],
        formatLoadingMessage: function () {
            return "请稍等，正在加载中...";
        },
        formatNoMatches: function () {  //没有匹配的结果
            return '无符合条件的记录';
        },
    });
    $("#cs_table").bootstrapTable({
        url: 'getcstable',  //请求后台的URL（*）
        dataType: 'json',
        method: 'get',  //请求方式（*）
        toolbar: '#toolbar',  //工具按钮用哪个容器
        stripted: true,  //是否显示行间隔色
        cache: false,  //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
        pagination: true,   //是否显示分页（*）
        sortable: false,  //是否启用排序
        sortOrder: "asc",  //排序方式
        queryParams: function () {
            return {
                //limit: params.limit,//页面大小
                //offset: params.offset,//页码
                date: $("#date").val(),
                mxname: $("#mingxi").html(),
            }
        },  //传递参数（*）
        sidePagination: "server",   //分页方式：client客户端分页，server服务端分页（*）
        pageNumber: 1,   //初始化加载第一页，默认第一页
        pageSize: 5,  //每页的记录行数（*）
        pageList: [10, 25, 50, 100],  //可供选择的每页的行数（*）
        search: true,  //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
        strictSearch: false,//设置为 true启用 全匹配搜索，否则为模糊搜索
        showColumns: true,   //是否显示所有的列
        showRefresh: true,   //是否显示刷新按钮
        minimumCountColumns: 2,   //最少允许的列数
        clickToSelect: true,  //是否启用点击选中行
        height: 500,    //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
        uniqueId: '主键1',  //每一行的唯一标识，一般为主键列
        showToggle: true,   //是否显示详细视图和列表视图的切换按钮
        cardView: false,   //是否显示详细视图
        detailView: false,   //是否显示父子表
        columns: [{
            field: '主键1',
            title: '主键1'
        }, {
            field: '主键2',
            title: '主键2'
        }, {
            field: '酬金',
            title: '酬金'
        }, {
            field: '渠道编码',
            title: '渠道编码'
        },
        ],
        formatLoadingMessage: function () {
            return "请稍等，正在加载中...";
        },
        formatNoMatches: function () {  //没有匹配的结果
            return '无符合条件的记录';
        },
    });
}


