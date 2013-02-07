from collections import defaultdict

from webassets import Bundle


LANGUAGES = ('en', 'ru')

DEFAULT_PAGE = 'one'
DEFAULT_LANGUAGE = 'en'

LAYOUTS = defaultdict(lambda: 'page.html', {
    'one': 'one.html',
    'two': 'two.html',
})

BUNDLES = {
    'css': Bundle('./css/bootstrap.css', 
                  Bundle('./less/styles.less', filters='less'),
                  output='./gen/styles.css'),
}

PAGINATION = {
    'two/*': 3,
}

ORDERING = {
    '*': ['one', 'two', 'three', 'four'],
    'two/*': 'alphabetically',
}
