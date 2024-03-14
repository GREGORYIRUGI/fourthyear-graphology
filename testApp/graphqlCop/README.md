# GraphQL Cop - Security Audit Utility for GraphQL

<p align="center">
  <img src="https://github.com/dolevf/graphql-cop/blob/main/static/images/logo.png?raw=true" width="500px" alt="GraphQL Cop"/>
</p>


## About
GraphQL Cop is a small Python utility to run common security tests against GraphQL APIs. GraphQL Cop is perfect for running CI/CD checks in GraphQL. It is lightweight, and covers interesting security issues in GraphQL.

GraphQL Cop allows you to reproduce the findings by providing cURL commands upon any identified vulnerabilities. 

## Requirements
- Python3
- Requests Library

## Detections
- Alias Overloading (DoS)
- Batch Queries (DoS)
- GET based Queries (CSRF)
- POST based Queries using urlencoded payloads (CSRF)
- GraphQL Tracing / Debug Modes (Info Leak)
- Field Duplication (DoS)
- Field Suggestions (Info Leak)
- GraphiQL (Info Leak)
- Introspection (Info Leak)
- Directives Overloading (DoS)
- Circular Query using Introspection (DoS)
- Mutation support over GET methods (CSRF)

## Usage

```
$ python graphql-cop.py -h

Usage: graphql-cop.py -t http://example.com -o json

Options:
  -h, --help            show this help message and exit
  -t URL, --target=URL  target url with the path - if a GraphQL path is not
                        provided, GraphQL Cop will iterate through a series of
                        common GraphQL paths
  -H HEADER, --header=HEADER
                        Append Header(s) to the request '{"Authorization":
                        "Bearer eyjt"}' - Use multiple -H for additional
                        Headers
  -o FORMAT, --output=FORMAT
                        json
  -f, --force           Forces a scan when GraphQL cannot be detected
  -d, --debug           Append a header with the test name for debugging
  -x PROXY, --proxy=PROXY
                        HTTP(S) proxy URL in the form
                        http://user:pass@host:port
  -v, --version         Print out the current version and exit.
```

Test a website

```
$ python3 graphql-cop.py -t https://mywebsite.com/graphql

                GraphQL Cop 1.1
           Security Auditor for GraphQL
            Dolev Farhi & Nick Aleks

Starting...
[HIGH] Introspection Query Enabled (Information Leakage)
[LOW] GraphQL Playground UI (Information Leakage)
[HIGH] Alias Overloading with 100+ aliases is allowed (Denial of Service)
[HIGH] Queries are allowed with 1000+ of the same repeated field (Denial of Service)
```

Test a website, dump to a parse-able JSON output, cURL reproduction command
```
python3 graphql-cop.py -t https://mywebsite.com/graphql -o json

 {'curl_verify': 'curl -X POST -H "User-Agent: graphql-cop/1.2" -H '
                 '"Accept-Encoding: gzip, deflate" -H "Accept: */*" -H '
                 '"Connection: keep-alive" -H "Content-Length: 33" -H '
                 '"Content-Type: application/json" -d \'{"query": "query { '
                 '__typename }"}\' \'http://localhost:5013/graphql\'',
  'description': 'Tracing is Enabled',
  'impact': 'Information Leakage',
  'result': False,
  'severity': 'INFO',
  'color': 'green',
  'title': 'Trace Mode'},
 {'curl_verify': 'curl -X POST -H "User-Agent: graphql-cop/1.2" -H '
                 '"Accept-Encoding: gzip, deflate" -H "Accept: */*" -H '
                 '"Connection: keep-alive" -H "Content-Length: 64" -H '
                 '"Content-Type: application/json" -d \'{"query": "query { '
                 '__typename @aa@aa@aa@aa@aa@aa@aa@aa@aa@aa }"}\' '
                 "'http://localhost:5013/graphql'",
  'description': 'Multiple duplicated directives allowed in a query',
  'impact': 'Denial of Service',
  'result': True,
  'severity': 'HIGH',
  'color': 'red',
  'title': 'Directive Overloading'}]
```

Test a website using `graphql-cop` through a proxy (e.g. Burp Suite listening on 127.0.0.1:8080) with custom headers (e.g. Authorization):

```
$ python3 graphql-cop.py -t https://mywebsite.com/graphql --proxy=http://127.0.0.1:8080 --header '{"Authorization": "Bearer token_here"}'

                GraphQL Cop 1.2
           Security Auditor for GraphQL
            Dolev Farhi & Nick Aleks

Starting...
[HIGH] Introspection Query Enabled (Information Leakage)
[LOW] GraphQL Playground UI (Information Leakage)
[HIGH] Alias Overloading with 100+ aliases is allowed (Denial of Service)
[HIGH] Queries are allowed with 1000+ of the same repeated field (Denial of Service)
```
# parser = OptionParser(usage='%prog -t http://example.com -o json')
# parser.add_option('-t', '--target', dest='url', help='target url with the path - if a GraphQL path is not provided, GraphQL Cop will iterate through a series of common GraphQL paths')
# parser.add_option('-H', '--header', dest='header', action='append', help='Append Header(s) to the request \'{"Authorization": "Bearer eyjt"}\' - Use multiple -H for additional Headers')
# parser.add_option('-o', '--output', dest='format',
#                         help='json', default=False)
# parser.add_option('-f', '--force', dest='forced_scan', action='store_true',
#                         help='Forces a scan when GraphQL cannot be detected', default=False)
# parser.add_option('-d', '--debug', dest='debug_mode', action='store_true',
#                         help='Append a header with the test name for debugging', default=False)
# parser.add_option('-x', '--proxy', dest='proxy', default=None,
#                   help='HTTP(S) proxy URL in the form http://user:pass@host:port')
# parser.add_option('--version', '-v', dest='version', action='store_true', default=False,
#                         help='Print out the current version and exit.')


# options, args = parser.parse_args()
# def main():
#     final_res =''
#     if options.version:
#         print('version:', VERSION)
#         sys.exit(0)

#     if not options.url:
#         print(draw_art())
#         parser.print_help()
#         sys.exit(1)

#     if options.proxy:
#         proxy = {
#             'http': options.proxy,
#             'https': options.proxy
#         }
#     else:
#         proxy = {}

#     if options.header != None:
#         try:
#             for l in options.header:
#                 extra_headers = loads(l)
#                 HEADERS.update(extra_headers)
#         except:
#             print("Cannot cast %s into header dictionary. Ensure the format \'{\"key\": \"value\"}\'."%(options.header))

#     if not urlparse(options.url).scheme:
#         print("URL missing scheme (http:// or https://). Ensure URL contains some scheme.")
#         sys.exit(1)
#     else:
#         url = options.url

#     endpoints = ['/graphiql', '/playground', '/console', '/graphql']
#     paths = []
#     parsed = urlparse(url)

#     if parsed.path and parsed.path != '/':
#         paths.append(url)
#     else:
#         for endpoint in endpoints:
#             paths.append(parsed.scheme + '://' + parsed.netloc + endpoint)

#     tests = [introspection, detect_graphiql,
#             get_method_support, alias_overloading, batch_query,
#             field_duplication, trace_mode, directive_overloading,
#             circular_query_introspection, get_based_mutation, post_based_csrf,
#             unhandled_error_detection]

#     json_output = []

#     for path in paths:
#         if not is_graphql(path, proxy, HEADERS, options.debug_mode):
#             if not options.forced_scan:
#                 print(path, 'does not seem to be running GraphQL. (Consider using -f to force the scan if GraphQL does exist on the endpoint)')
#                 continue
#             else:
#                 print('Running a forced scan against the endpoint')
#         for test in tests:
#             json_output.append(test(path, proxy, HEADERS, options.debug_mode))

#     json_output = sorted(json_output, key=lambda d: d['title']) 

#     if options.format == 'json':
#         print(dumps(json_output))
#     else:
#         for i in json_output:
#             if i['result']:
#                 print('[{}] {} - {} ({})'.format(i['severity'], i['color'], attrs=['bold']), i['title'], 'white', attrs=['bold']), i['description'], i['impact']
#     return final_res