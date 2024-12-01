menu = [
    {'nav_title': 'Книги', 'url': 'books'},
    {'nav_title': 'Авторы', 'url': 'authors'},
    {'nav_title': 'Добавить автора', 'url': 'add_author'},
    {'nav_title': 'Добавить книгу', 'url': 'add_book'},
]


class CommonDataMixin:
    paginate_by = 5

    def get_common_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        if 'site_title' not in context:
            context['site_title'] = 'Сайт о книгах'
        return context
