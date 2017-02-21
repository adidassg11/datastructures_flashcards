#!/usr/bin/python

import web
import model

urls = (
    '/', 'Index',
    '/view/(\d+)', 'View',
    '/new', 'New',
    #TODO: more
)

### TEMPLATES
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates', base='base', globals=t_globals)

class Index:
    def GET(self):
        posts = model.get_posts()
        return render.index(posts)

class View:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.view(post)

class New:
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull, size=30, description="post title:"),
        web.form.Textarea('content', web.form.notnull, rows=30, cols=80, description="Post content:"),
        web.form.Button('Post entry'),
    )

    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.title, form.d.content)
        raise web.seeother('/')

#TODO: other classes
#

app = web.application(urls, globals())
app.run()

