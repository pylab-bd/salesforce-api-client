from .util import date_to_iso8601, exception_handler
from .login import SalesforceLogin
"""Core Classes and exceptions for Salesforce Client
"""

# Has to be defined prior to login import
DEFAULT_API_VERSION = '1.0'


try:
    from urlparse import urlparse, urljoin
except ImportError:
    # Python 3+
    from urllib.parse import urlparse, urljoin
