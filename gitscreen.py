import web

urls = ('/.*', 'hooks',
        '/', 'index')

app = web.application(urls, globals())

class index:
    def GET(self):
        # redirect to the static file ...
        raise web.seeother('/index.html')

class hooks:
    def POST(self):
        data = web.data()
        print
        print 'DATA RECEIVED:'
        print data
        print
        return 'OK'

if __name__ == '__main__':
    app.run()
