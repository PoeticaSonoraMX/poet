from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from config.settings import SUBPATH
from app.controllers.work import get_work_context
from app.controllers.search import get_search_context
from app.controllers.entity import get_entity_context
from app.controllers.collection import get_work_collection_context


def paginate_list(request, page_list, number_of_pages=10):
    paginator = Paginator(page_list, number_of_pages)
    page = request.GET.get('page', 1)
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)

    return {
        'page': p,
        'search_terms': parameters,
    }


def home(request):
    return render(request, 'poet/home.html.j2')


def work(request, work_id):
    context = get_work_context(work_id)
    admin_link = f'{SUBPATH}/admin/app/work/{work_id}/change'

    context['admin_link'] = admin_link
    return render(request, 'poet/work.html.j2', context)


def collection(request, collection_id):
    context = get_work_collection_context(collection_id)
    admin_link = f'{SUBPATH}/admin/app/workcollection/{collection_id}/change'

    context['admin_link'] = admin_link
    context['works'] = paginate_list(request, context['works'])

    return render(request, 'poet/collection.html.j2', context)


def entity(request, entity_id):
    context = get_entity_context(entity_id)
    admin_link = f'{SUBPATH}/admin/app/entity/{entity_id}/change'
    context['admin_link'] = admin_link
    context['works'] = paginate_list(request, context['works'])

    return render(request, 'poet/entity.html.j2', context)


def search(request):
    context = get_search_context(dict(request.GET))
    context['works'] = paginate_list(request, context['works'])

    return render(request, 'poet/search.html.j2', context)


def error_404_view(request, exception=None):
    return render(request, 'errors/404.html.j2', status=404)


def error_500_view(request, exception=None):
    return render(request, 'errors/500.html.j2', status=500)


def error_403_view(request, exception=None):
    return render(request, 'errors/403.html.j2', status=403)


def error_400_view(request, exception=None):
    return render(request, 'errors/400.html.j2', status=400)
