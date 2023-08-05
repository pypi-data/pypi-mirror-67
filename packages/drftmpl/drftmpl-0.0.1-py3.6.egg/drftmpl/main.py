'''
Auto genenel rest_framework members:
viewset serializer router.
Extends app urls
'''

import os
import re
from os import path

from jinja2 import Template

BASE_DIR = path.dirname(path.abspath(__file__))
print(BASE_DIR)
modules = ['serializer', 'viewset', 'router']


def _render(data, *args, **kwds) -> str:
    '''jinja2 render'''
    vars = dict(*args, **kwds)
    tmp = Template(data)
    return tmp.render(vars).strip()


def render(file, models, app=None) -> str:
    # render by file
    with open(file) as f:
        data = f.read()
    return _render(data, models=models, app=app)


def exists_app(app) -> str:
    # app exists?
    if not path.isdir(app):
        print('No this app')
        os._exit(0)
    return app


def write_or_add_to_file(filename, head='', tail='', add=False):
    '''
    @filename are in modules[index] + `s.py`
    condition modules
    '''
    with open(filename, 'w') as f:
        if add is False:
            n = '\n' * 3
        else:
            n = '\n\n'
        if 'viewset' in filename or 'serializer' in filename:
            f.write(head + n + tail)
        elif 'router' in filename:
            f.write(head + '\n' + tail)


def add_model_to_import(data, model):
    '''
    eg: add AuthorViewSet to `from .viewsets import BlogViewset, AuthorViewSet`
    '''
    new_data = ''
    for line in data.splitlines():
        if line.startswith('from .ser'):
            line += ', ' + model.title() + 'Serializer'
        elif line.startswith('from .models'):
            line += ', ' + model.title()
        new_data += line + '\n'
    return new_data


def add_to_tail(tail_filename, models, filename):
    '''
    add viewset serialzer router to tail. eg.
    class BlogViewSet(ModelViewSet):
        pass
    @filename viewsets.py
    @filename are in modules[index] + `s.py`
    '''
    with open(filename) as pyobj:
        pydata = pyobj.read()
        models = [model for model in models if model not in pydata.lower()]

    with open(tail_filename) as f:
        data = f.read()
        print('filename', filename, tail_filename, models)
    if models:
        for model in models:
            tail_data = datas = ''
            if 'viewset' in tail_filename or 'serializer' in tail_filename:
                datas += add_model_to_import(pydata, model)
            elif 'router' in tail_filename:
                datas = pydata
            tail_data += _render(data, models=models)
            if model in datas.lower() is not False:
                print('datas', datas)
                write_or_add_to_file(filename, head=datas, tail=tail_data, add=True)
                print(f'add {model} to {filename}')
        return datas + '\n\n' + tail_data


def get_project_name() -> str:
    """
    from manage.py get project name
    return project_name
    """
    with open('manage.py') as f:
        manage_obj = f.read()
        result = re.search("DJANGO_SETTINGS_MODULE', '(.*?)'\)", manage_obj)
        project_name = path.join(*result.group(1).rsplit('.')[:-1])
        return project_name


def condition_filename(file, app) -> str:
    if 'viewset' in file or 'serializer' in file:
        filename = path.join(app, f'{file}s.py')
    elif 'router' in file:
        filename = path.join(get_project_name(), f'{file}s.py')
    return filename


def run(models, app):
    # write or add modules to app
    for file in modules:
        filename = condition_filename(file, app)
        if path.exists(filename):
            print('\nexists ' + filename)
            add_to_tail(path.join(BASE_DIR, 'templates', f'{file}s.tail.py.tmpl'), models, filename)
        else:
            print('start ' + file)
            head = render(path.join(BASE_DIR, 'templates', f'{file}s.py.tmpl'), models, app)
            tail = render(path.join(BASE_DIR, 'templates', f'{file}s.tail.py.tmpl'), models)
            write_or_add_to_file(filename, head=head, tail=tail)
            print(f'genenel {filename} done.')
