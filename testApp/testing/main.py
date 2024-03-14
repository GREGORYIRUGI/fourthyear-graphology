import sys

from json import loads, dumps
from optparse import OptionParser
from .version import VERSION
from .config import HEADERS
from urllib.parse import urlparse

from .inforDisclosure.introspection import introspection
from .inforDisclosure.graphiql import detect_graphiql
from .inforDisclosure.postBasedCsrf import post_based_csrf
from .inforDisclosure.traceMode import trace_mode
from .inforDisclosure.unhandledError import unhandled_error_detection
from .inforDisclosure.getBasedMutation import get_based_mutation
from .inforDisclosure.getMethodSupport import get_method_support
from .DosVuln.alias_overloading import alias_overloading
from .DosVuln.batchRequests import batch_query
from .DosVuln.circularIntrospection import circular_query_introspection
from .DosVuln.directive_overloading import directive_overloading
from .DosVuln.fieldDuplication import field_duplication

from .utils import is_graphql, draw_art
from termcolor import colored


def testDDOs(url,headers=None,format=True,forced_scan=False,debug_mode=False,proxy=None):
    endpoints = ['/graphiql','/playground','/console','/graphql']
    paths = []
    parsed = urlparse(url=url)

    if parsed.path and parsed.path != '/':
        paths.append(url)
    else:
        for endpoint in endpoints:
            paths.append(parsed.scheme + '://' + parsed.netloc + endpoint)
    
    tests = [field_duplication,alias_overloading,
             field_duplication,directive_overloading,circular_query_introspection,
            ]
    
    json_output = []
    if headers:
        try:
            for header in headers:
                extra_headers = loads(header)
                HEADERS.update(extra_headers)
        except:
            print("cannot cast %s into header dictionary. Ensure the format \'{\"key\":\"value\"}\'."%{headers})
    
    if not urlparse(url=url).scheme:
        print("Urls Missing scheme (http:// lor https://). Ensure url contains some scheme.")
        sys.exit(1)
    
    for path in paths:
        if not is_graphql(path,proxy,HEADERS,debug_mode=debug_mode):
            if not forced_scan:
                print(path,'does not seem to be running GraphQL. (Consider using -f to force the scan if GraphQL does not exist on the endploint)')
                continue
            else:
                print('Running a forced scan against the endpoint')
        for test in tests:
            json_output.append(test(path,proxy,HEADERS,debug_mode))
    json_output = sorted(json_output,key=lambda d: d['title'])

    if format == 'json':
        return dumps(json_output)
    else:
        output = []
        for i in json_output:
            if i['result']:
                 output.append('[{}] {} - {} ({})'.format(
    'severity',i['severity'], 
  i['title'], 
    i['description'],
    i['impact']
))

    return '\n'.join(output)


def testCSRF(url,headers=None,format=True,forced_scan=False,debug_mode=False,proxy=None):
    endpoints = ['/graphiql','/playground','/console','/graphql']
    paths = []
    parsed = urlparse(url=url)

    if parsed.path and parsed.path != '/':
        paths.append(url)
    else:
        for endpoint in endpoints:
            paths.append(parsed.scheme + '://' + parsed.netloc + endpoint)
    
    tests = [detect_graphiql,get_based_mutation,
             post_based_csrf]
    
    json_output = []
    if headers:
        try:
            for header in headers:
                extra_headers = loads(header)
                HEADERS.update(extra_headers)
        except:
            print("cannot cast %s into header dictionary. Ensure the format \'{\"key\":\"value\"}\'."%{headers})
    
    if not urlparse(url=url).scheme:
        print("Urls Missing scheme (http:// lor https://). Ensure url contains some scheme.")
        sys.exit(1)
    
    for path in paths:
        if not is_graphql(path,proxy,HEADERS,debug_mode=debug_mode):
            if not forced_scan:
                print(path,'does not seem to be running GraphQL. (Consider using -f to force the scan if GraphQL does not exist on the endploint)')
                continue
            else:
                print('Running a forced scan against the endpoint')
        for test in tests:
            json_output.append(test(path,proxy,HEADERS,debug_mode))
    json_output = sorted(json_output,key=lambda d: d['title'])

    if format == 'json':
        return dumps(json_output)
    else:
        output = []
        for i in json_output:
            if i['result']:
                output.append('[{}] {} - {} ({})'.format(
    'severity',i['severity'], 
  i['title'], 
    i['description'],
    i['impact']
))

    return '\n'.join(output)


def testInfodisclosure(url,headers=None,format=True,forced_scan=False,debug_mode=False,proxy=None):
    endpoints = ['/graphiql','/playground','/console','/graphql']
    paths = []
    parsed = urlparse(url=url)

    if parsed.path and parsed.path != '/':
        paths.append(url)
    else:
        for endpoint in endpoints:
            paths.append(parsed.scheme + '://' + parsed.netloc + endpoint)
    
    tests = [introspection,detect_graphiql,trace_mode,unhandled_error_detection]
    
    json_output = []
    if headers:
        try:
            for header in headers:
                extra_headers = loads(header)
                HEADERS.update(extra_headers)
        except:
            print("cannot cast %s into header dictionary. Ensure the format \'{\"key\":\"value\"}\'."%{headers})
    
    if not urlparse(url=url).scheme:
        print("Urls Missing scheme (http:// lor https://). Ensure url contains some scheme.")
        sys.exit(1)
    
    for path in paths:
        if not is_graphql(path,proxy,HEADERS,debug_mode=debug_mode):
            if not forced_scan:
                print(path,'does not seem to be running GraphQL. (Consider using -f to force the scan if GraphQL does not exist on the endploint)')
                continue
            else:
                print('Running a forced scan against the endpoint')
        for test in tests:
            json_output.append(test(path,proxy,HEADERS,debug_mode))
    json_output = sorted(json_output,key=lambda d: d['title'])

    if format == 'json':
        return dumps(json_output)
    else:
        output = []
        for i in json_output:
            if i['result']:
                output.append('[{}] {} - {} ({})'.format(
    'severity',i['severity'], 
  i['title'], 
    i['description'],
    i['impact']
))

    return '\n'.join(output)


def run_queries(url,headers=None,format=True,forced_scan=False,debug_mode=False,proxy=None):
    endpoints = ['/graphiql','/playground','/console','/graphql']
    paths = []
    parsed = urlparse(url=url)

    if parsed.path and parsed.path != '/':
        paths.append(url)
    else:
        for endpoint in endpoints:
            paths.append(parsed.scheme + '://' + parsed.netloc + endpoint)
    
    tests = [field_duplication,introspection,detect_graphiql,get_based_mutation,
             get_method_support,alias_overloading,
             trace_mode,directive_overloading,circular_query_introspection,
             post_based_csrf,unhandled_error_detection]
    
    json_output = []

    if headers:
        try:
            for header in headers:
                extra_headers = loads(header)
                HEADERS.update(extra_headers)
        except:
            print("cannot cast %s into header dictionary. Ensure the format \'{\"key\":\"value\"}\'."%{headers})
    
    if not urlparse(url=url).scheme:
        print("Urls Missing scheme (http:// lor https://). Ensure url contains some scheme.")
        sys.exit(1)
    
    for path in paths:
        if not is_graphql(path,proxy,HEADERS,debug_mode=debug_mode):
            if not forced_scan:
                print(path,'does not seem to be running GraphQL. (Consider using -f to force the scan if GraphQL does not exist on the endploint)')
                continue
            else:
                print('Running a forced scan against the endpoint')
        for test in tests:
            json_output.append(test(path,proxy,HEADERS,debug_mode))
    json_output = sorted(json_output,key=lambda d: d['title'])

    if format == 'json':
        return dumps(json_output)
    else:
        output = []
        for i in json_output:
            if i['result']:
                output.append('[{}] {} - {} ({})'.format(
    # colored(i['severity'], i['color'], attrs=['bold']),
    # colored(i['title'], 'white', attrs=['bold']),
                    "severity",i['severity'], i['title'],
    i['description'],
    i['impact']
))

        return '\n'.join(output)
    
