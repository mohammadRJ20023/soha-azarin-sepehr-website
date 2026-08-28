from django.db.models import Q


def apply_search(queryset, query, fields):
    query = (query or "").strip()

    if not query:
        return queryset

    search_condition = Q()

    for field in fields:
        lookup = {f"{field}__icontains": query}
        search_condition = search_condition | Q(**lookup)

    return queryset.filter(search_condition)