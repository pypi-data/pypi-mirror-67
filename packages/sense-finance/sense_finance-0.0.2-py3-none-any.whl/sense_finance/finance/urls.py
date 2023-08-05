from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^finance_params$', views.finance_select_params),  # 公司财务分析筛选参数
    url(r'^industry_params$', views.industry_select_params),  # 行业财务分析筛选参数
    url(r'^finance_statistics$', views.finance_statistics),  # 公司财务分析
    url(r'^finance_industry_analysis$', views.finance_industry_analysis),  # 行业财务分析
]
