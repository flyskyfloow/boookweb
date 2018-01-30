from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, Http404, HttpResponse, render_to_response, render

from searchbookapp.models import Ssrnpaper
from django.core.paginator import Paginator
# # 获取论文全部信息
# papers = Ssrnpaper.objects.all()
# # 每5个对象分为一页
# paper = Paginator(papers, 5)
# # 分页器相关的方法和属性
# # 得到里面总共有多少个模型对象
# print(paper.count)
# # 总页数
# print(paper.num_pages)
# # 页面列表 遍历可以得到全部页码
# print(paper.page_range)
# # 得到第1页包含的模型对象，该对象集合可以用于遍历得到里面的模型对象
# papers_page = paper.page(1)
# # 得到该对象集合当前是哪一页
# print(papers_page.number)
# # 判断是否有前一页
# print(papers_page.has_previous())
# # 判断是否有后一页
# print(papers_page.has_next())


def home1(request):
    string = u"中华人民共和国"
    return render(request, 'home.html', {'string': string})


def home2(request):
    Tutorisalist = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'Tutorisalist': Tutorisalist})
# Create your views here.


def home(request):
    info_dict = {'ip-1': u'192.168.1.1', 'ip-2': u'192.168.1.2'}
    return render(request, 'home.html', {'info_dict': info_dict})


def getpaper(request):
    data = {}
    # page 是get请求时候的变量
    current_page = request.GET.get("page", 1)
    papers = Ssrnpaper.objects.all()
    paper_pages = Paginator(papers, 10)
    papers = paper_pages.page(current_page)
    data["papers"] = papers
    data["paper_pages"] = paper_pages
    # listpaper = Ssrnpaper.objects.all()
    return render_to_response("Ssrnindex.html", data)


def search(request):
    data = {}
    q = request.GET.get("q")
    title1 = Ssrnpaper.objects.get(gid=q)
    data['title'] = title1.title
    data["link"] = title1.link
    data['download'] = title1.downloads
    data['author'] = title1.author

    return render_to_response('results.html', data)
