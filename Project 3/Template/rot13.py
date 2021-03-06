import os
import webapp2
import jinja2
import codecs

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        user_text = ""
        self.render("rot13.html", user_text = user_text)

    def post(self):
        user_input = self.request.get('text')
        rot13_output = rot13(user_input)
        self.render("rot13.html", user_text = rot13_output)

def rot13(s):
    return codecs.encode(s, 'rot13')

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
