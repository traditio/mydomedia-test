from annoying.decorators import render_to


@render_to('base.html')
def test(request):
    return {}
