import math

import urllib.parse


from flask import request, Response

from flask_sqlalchemy_booster.responses import as_json

from io import StringIO

from toolspy import merge, null_safe_type_cast, subdict, write_csv_file

from .utils import (
    convert_sqla_collection_items_to_dicts,
    get_queried_field_labels, sqla_sort)

from .utils.dash_utils import (
    convert_dt_data_to_df,
    convert_dt_to_df)


QUERY_MODIFIERS = [
    'page', 'per_page', 'limit', 'offset', 'order_by', 'sort', 'group_by']


def fetch_query_modifiers_from_request():
    return subdict(
        request.args,
        QUERY_MODIFIERS
    )


def construct_query_modifiers(
        query_modifiers=None, allow_modification_via_requests=True):
    default_query_modifiers = {
        "page": None,
        "per_page": 20,
        "limit": None,
        "offset": None,
        "order_by": None,
        "sort": "asc",
        "group_by": None
    }
    print("received query modifiers as ", query_modifiers)
    if query_modifiers is None:
        query_modifiers = {}
    query_modifiers = subdict(query_modifiers, QUERY_MODIFIERS)
    query_modifiers = merge(
        default_query_modifiers, query_modifiers)
    if allow_modification_via_requests:
        query_modifiers = merge(
            query_modifiers, fetch_query_modifiers_from_request())
    for k in ['page', 'per_page', 'limit', 'offset']:
        if k in query_modifiers:
            query_modifiers[k] = null_safe_type_cast(
                int, query_modifiers.get(k))
    print("final query_modifiers ", query_modifiers)
    return query_modifiers


def apply_modifiers_on_sqla_query(
        q, page=None, per_page=20, limit=None, offset=None,
        group_by=None, order_by=None, sort='asc'):
    if group_by is not None:
        q = q.group_by(group_by)
    if order_by is not None:
        q = q.order_by(sqla_sort(sort)(order_by))
    if page:
        per_page = int(per_page)
        q = q.limit(per_page).offset((int(page) - 1) * per_page)
    elif limit and offset:
        q = q.limit(limit).offset(int(offset) - 1)
    return q


def construct_meta_dict_from_query(q, query_modifiers):
    meta = {
        "total_items": q.count(),
    }
    if query_modifiers.get("page"):
        meta["page"] = query_modifiers["page"]
        meta["per_page"] = query_modifiers.get("per_page")
        meta["total_pages"] = math.ceil(
            meta["total_items"] / meta["per_page"])
        meta["columns"] = get_queried_field_labels(q)
    return meta


def construct_list_of_dicts_from_query(
        q, query_modifiers=None, allow_modification_via_requests=True):
    query_modifiers = construct_query_modifiers(
        query_modifiers,
        allow_modification_via_requests=allow_modification_via_requests)
    q = apply_modifiers_on_sqla_query(q, **query_modifiers)
    return convert_sqla_collection_items_to_dicts(q.all())


def construct_json_response_from_query(
        q, query_modifiers=None, allow_modification_via_requests=True):

    query_modifiers = construct_query_modifiers(
        query_modifiers,
        allow_modification_via_requests=allow_modification_via_requests)
    meta = construct_meta_dict_from_query(q, query_modifiers)

    q = apply_modifiers_on_sqla_query(q, **query_modifiers)

    result = q.all()
    # q.session.remove()

    return as_json(
        convert_sqla_collection_items_to_dicts(
            result
        ),
        meta=meta,
        struct_key="data"
    )


def convert_csv_text_to_csv_response(csvtext):
    return Response(csvtext, mimetype="text/csv")


def construct_csv_response_from_query(
        q, query_modifiers=None, allow_modification_via_requests=True):
    cols = get_queried_field_labels(q)
    rows = construct_list_of_dicts_from_query(
        q, query_modifiers=query_modifiers,
        allow_modification_via_requests=allow_modification_via_requests)
    strfile = StringIO()
    write_csv_file(strfile, rows=rows, cols=cols)
    csv_content = strfile.getvalue().strip("\r\n")
    strfile.close()
    return convert_csv_text_to_csv_response(csv_content)


def convert_df_to_csv_response(df):
    return convert_csv_text_to_csv_response(
        df.to_csv(encoding='utf-8'))


def convert_dt_to_csv_response(dt, index_col=None):
    return convert_df_to_csv_response(
        df=convert_dt_to_df(dt, index_col=index_col),
    )


def convert_dt_data_to_csv_response(dt_data, index_col=None):
    return convert_df_to_csv_response(
        df=convert_dt_data_to_df(dt_data, index_col=index_col)
    )
