import re

_missing = type('_missing', (), {'__bool__': lambda self: False})()


def de_camel(s: str, separator: str = "_", _lowercase: bool = True) -> str:
    """ Returns the string with CamelCase converted to underscores, e.g.,
        de_camel("TomDeSmedt", "-") => "tom-de-smedt"
        de_camel("getHTTPResponse2) => "get_http_response2"
    """
    s = re.sub(r"([a-z0-9])([A-Z])", "\\1%s\\2" % separator, s)
    s = re.sub(r"([A-Z])([A-Z][a-z])", "\\1%s\\2" % separator, s)
    return s.lower() if _lowercase else s


def snake_case(string: str) -> str:
    """
    Converts a string to snake case. For example::

        snake_case('OneTwoThree') -> 'one_two_three'
    """
    if not string:
        return string
    string = string.replace('-', '_').replace(' ', '_')
    return de_camel(string)


def title_case(string: str) -> str:
    """
    Converts a string to title case. For example::

        title_case('one_two_three') -> 'One Two Three'
    """
    if not string:
        return string
    string = string.replace('_', ' ').replace('-', ' ')
    parts = de_camel(string, ' ', _lowercase=False).strip().split(' ')
    return ' '.join([part if part.isupper() else part.title()
                     for part in parts])


__all__ = [
    'de_camel',
    'snake_case',
    'title_case',
]
