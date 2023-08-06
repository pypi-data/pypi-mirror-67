import pkg_resources

__version__ = '1.0.0'

FONTAWESOME_MIN = 'all.min.js'
FONTAWESOME = 'all.js'
DEST_PATH = '/static/fontawesome/js/'

def load_package(site):
    f = site.config.getbool('/', 'fontawesome_compressed')
    fontawesome = FONTAWESOME_MIN if f else FONTAWESOME
    src_path = 'externals/js/'+fontawesome
    
    content = pkg_resources.resource_string(__name__, src_path)
    site.files.add_bytes("binary", DEST_PATH + fontawesome , content )
    site.config.add('/', {'fontawesome_path': DEST_PATH+fontawesome})

    site.add_template_module('fontawesome', 'miyadaiku_theme_fontawesome!macros.html')

