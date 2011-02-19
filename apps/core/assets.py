from django_assets import Bundle, register

js = Bundle('js/jquery.min.js',
            Bundle('js/base.coffee',
                filters='coffeescript', output='gen/coffee.js'),
            output='gen/all.js')

register('js_all', js)

css = Bundle('css/screen.scss', 'css/print.scss', 'css/ie.scss',
             filters='compass', output='gen/all.css')
register('css_all', css)

