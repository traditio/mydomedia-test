import inspect

from annoying.decorators import render_to
from functools import wraps
from coffin.shortcuts import render_to_response
from django.template.context import RequestContext

exec inspect.getsource(render_to)
