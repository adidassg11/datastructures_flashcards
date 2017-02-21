import datetime
import web

db = web.database(dbn='mysql', db='blog', user='sal')

def get_posts():
    return db.select('entries', order='id DESC')

def get_post(id):
    try:
        return db.select('entries', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_post(title, text):
    db.insert('entries', title=title, content=text, posted_on=datetime.datetime.utcnow())

def del_post(id):
    pass

def update_post(id, title, text):
    pass
