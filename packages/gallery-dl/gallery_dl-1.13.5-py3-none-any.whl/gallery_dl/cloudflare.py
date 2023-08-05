# -*- coding: utf-8 -*-

# Copyright 2015-2020 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Methods to access sites behind Cloudflare protection"""

import re
import time
import operator
import collections
import urllib.parse
from . import text
from .cache import memcache


def is_challenge(response):
    return (response.status_code == 503 and
            response.headers.get("Server", "").startswith("cloudflare") and
            b"jschl-answer" in response.content)


def is_captcha(response):
    return (response.status_code == 403 and
            b'name="captcha-bypass"' in response.content)


def solve_challenge(session, response, kwargs):
    """Solve Cloudflare challenge and get cfclearance cookie"""
    parsed = urllib.parse.urlsplit(response.url)
    root = parsed.scheme + "://" + parsed.netloc

    cf_kwargs = {}
    headers = cf_kwargs["headers"] = collections.OrderedDict()
    params = cf_kwargs["data"] = collections.OrderedDict()

    page = response.text
    url = root + text.unescape(text.extract(page, 'action="', '"')[0])
    headers["Referer"] = response.url

    for inpt in text.extract_iter(page, "<input ", ">"):
        name = text.extract(inpt, 'name="', '"')[0]
        if name == "jschl_answer":
            value = solve_js_challenge(page, parsed.netloc)
        else:
            value = text.unescape(text.extract(inpt, 'value="', '"')[0])
        params[name] = value

    time.sleep(4)

    cf_kwargs["allow_redirects"] = False
    cf_response = session.request("POST", url, **cf_kwargs)

    cookies = {
        cookie.name: cookie.value
        for cookie in cf_response.cookies
    }

    if not cookies:
        import logging
        log = logging.getLogger("cloudflare")
        log.debug("Headers:\n%s", cf_response.headers)
        log.debug("Content:\n%s", cf_response.text)
        return cf_response, None, None

    domain = next(iter(cf_response.cookies)).domain
    cookies["__cfduid"] = response.cookies.get("__cfduid", "")
    return cf_response, domain, cookies


def solve_js_challenge(page, netloc):
    """Evaluate JS challenge in 'page' to get 'jschl_answer' value"""

    # build variable name
    # e.g. '...f, wqnVscP={"DERKbJk":+(...' --> wqnVscP.DERKbJk
    data, pos = text.extract_all(page, (
        ('var' , ',f, ', '='),
        ('key' , '"'   , '"'),
        ('expr', ':'   , '}'),
    ))
    variable = "{}.{}".format(data["var"], data["key"])
    vlength = len(variable)

    # evaluate the initial expression
    solution = evaluate_expression(data["expr"], page, netloc)

    # iterator over all remaining expressions
    # and combine their values in 'solution'
    expressions = text.extract(
        page, "'challenge-form');", "f.submit();", pos)[0]
    for expr in expressions.split(";")[1:]:

        if expr.startswith(variable):
            # select arithmetc function based on operator (+/-/*)
            func = OPERATORS[expr[vlength]]
            # evaluate the rest of the expression
            value = evaluate_expression(expr[vlength+2:], page, netloc)
            # combine expression value with our current solution
            solution = func(solution, value)

        elif expr.startswith("a.value"):
            if "t.length)" in expr:
                # add length of hostname
                solution += len(netloc)
            if ".toFixed(" in expr:
                # trim solution to 10 decimal places
                solution = "{:.10f}".format(solution)
            return solution


def evaluate_expression(expr, page, netloc, *,
                        split_re=re.compile(r"[(+]+([^)]*)\)")):
    """Evaluate a single Javascript expression for the challenge"""

    if expr.startswith("function(p)"):
        # get HTML element with ID k and evaluate the expression inside
        # 'eval(eval("document.getElementById(k).innerHTML"))'
        k, pos = text.extract(page, "k = '", "'")
        e, pos = text.extract(page, 'id="'+k+'"', '<')
        return evaluate_expression(e.partition(">")[2], page, netloc)

    if "/" in expr:
        # split the expression in numerator and denominator subexpressions,
        # evaluate them separately,
        # and return their fraction-result
        num, _, denom = expr.partition("/")
        num = evaluate_expression(num, page, netloc)
        denom = evaluate_expression(denom, page, netloc)
        return num / denom

    if "function(p)" in expr:
        # split initial expression and function code
        initial, _, func = expr.partition("function(p)")
        # evaluate said expression
        initial = evaluate_expression(initial, page, netloc)
        # get function argument and use it as index into 'netloc'
        index = evaluate_expression(func[func.index("}")+1:], page, netloc)
        return initial + ord(netloc[int(index)])

    # iterate over all subexpressions,
    # evaluate them,
    # and accumulate their values in 'result'
    result = ""
    for subexpr in split_re.findall(expr) or (expr,):
        result += str(sum(
            VALUES[part]
            for part in subexpr.split("[]")
        ))
    return int(result)


OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}

VALUES = {
    "": 0,
    "+": 0,
    "!+": 1,
    "!!": 1,
    "+!!": 1,
}


@memcache(keyarg=0)
def cookies(category):
    return None
