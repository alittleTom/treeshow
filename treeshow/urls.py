"""treeshow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from treeShowMessage import views as treeShowMessage
from CJComparison import views as CJComparision
from yxtest3 import views as yxtest3

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', treeShowMessage.getdatatest),

                  # 展示多算酬金模块
                  url(r'^gettreedata/$', treeShowMessage.gettreedata),
                  url(r'^showInfo/', treeShowMessage.showInfo),
                  url(r'^getkftable/', CJComparision.getkftable),
                  url(r'^getcstable/', CJComparision.getcstable),
                  # url(r'^cj/',CJComparision.executeSql),
                  url(r'^cj/', CJComparision.kf_more_cj),

                  # 需求测试脚本模块
                  url(r'^yxtest3/table/show/$', yxtest3.requirementtable),
                  url(r'^yxtest3/table/requirement/gettable/$', yxtest3.requirementtable),

                  url(r'^yxtest3/table/requirement/add/$', yxtest3.requirementadd),
                  url(r'^yxtest3/table/requirement/add/submit/$', yxtest3.requirementadd_submit),

                  url(r'^yxtest3/table/requirement/test/add/$', yxtest3.testadd),
                  url(r'^yxtest3/table/requirement/test/add/submit/$', yxtest3.testaddsubmit),

                  url(r'^yxtest3/table/test/script/add/$', yxtest3.scriptadd),
                  url(r'^yxtest3/table/test/script/add/submit/$', yxtest3.scriptadd_submit),

                  # 下面这个网址是展示需求表的
                  url(r'^yxtest3/table/requirement/$', yxtest3.requirementtemplates),
                  url(r'^yxtest3/table/requirement/query/(.+)/$', yxtest3.requirementQuery),
                  url(r'^yxtest3/table/test/gettable/$', yxtest3.testtable),
                  # 下面这个网址是展示测试表的
                  url(r'^yxtest3/table/test/$', yxtest3.testtemplate),
                  url(r'^yxtest3/table/script/gettable/$', yxtest3.scripttable),
                  # 下面这个网址是展示脚本表的
                  url(r'^yxtest3/table/script/$', yxtest3.scripttemplate),
                  url(r'^yxtest3/testmessage/$', yxtest3.messagetest),
                  url(r'^yxtest3/testmessage/gettable/$', yxtest3.gettable),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
