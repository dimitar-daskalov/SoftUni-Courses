paths = {'GET': [],
         'POST': [], }

command = input()
while not command == "END":
    path = command[:command.rindex('/')]
    method = command[command.rindex('/') + 1:]
    paths[method.upper()].append(path)
    command = input()


def read_request():
    method, path, *_ = input().split(' ')
    return {
        'method': method,
        'path': path,
    }


def make_request(paths, request):
    valid_paths_for_method = paths[request['method']]

    if request['path'] in valid_paths_for_method:
        return '''HTTP/1.1 200 OK
Content-Length: 2
Content-Type: text/plain


OK'''
    else:
        return '''HTTP/1.1 404 Not Found
Content-Length: 9
Content-Type: text/plain


Not Found'''


print(make_request(paths, read_request()))
