def date_to_iso8601(date):
    """Returns an ISO8601 string from a date"""
    datetimestr = date.strftime('%Y-%m-%dT%H:%M:%S')
    timezone_sign = date.strftime('%z')[0:1]
    timezone_str = '%s:%s' % (
        date.strftime('%z')[1:3],
        date.strftime('%z')[3:5],
    )

    return f'{datetimestr}{timezone_sign}{timezone_str}'.replace(
        ':', '%3A'
    ).replace(
        '+', '%2B'
    )


def exception_handler(result, name=""):
    """Exception router. Determines which error to raise for bad results

    Arguments:
        result {requests.results} -- requests response

    Keyword Arguments:
        name {str} -- [description] (default: {""})
    """
    try:
        response_conent = result.json()
    # pylint: disable=broad-except
    except Exception:
        response_conent = result.text

    exc_map = {
        300: SalesforceMoreThanOneRecord,
        400: SalesforceMalformedRequest,
        401: SalesforceExpiredSession,
        403: SalesforceRefusedRequest,
        404: SalesforceResourceNotFound,
    }

    exc_cls = exc_map.get(result.status_code, SalesforceGeneralError)
    raise exc_cls(result.url, result.status_code, name, response_content)


def call_salesforce(url, method, session, headers, **kwargs):
    """Utility method for performing HTTP call to Salesforce.
    Returns a `requests.result` object.
    """

    additional_headers = kwargs.pop('additional_headers', dict())
    headers.update(additional_headers or dict())
    result = session.request(method, url, headers=headers, **kwargs)

    if result.status_code >= 300:
        exception_handler(result)

    return result
