#!/usr/bin/env python
# coding: utf-8

import codecs
import logging
import sqlite3

logging.root.setLevel(logging.DEBUG)


chars = {'&uuml;': 'ü', '&ouml;': 'ö', '&ccedil;': 'ç',
         '&Uuml;': 'Ü', '&Ouml;': 'Ö', '&Ccedil;': 'Ç'}


def replace_all(text, dict):
    for i, j in dict.iteritems():
        text = text.replace(i, j)
    return text

conn = sqlite3.connect('blog.db')
conn.row_factory = sqlite3.Row

c = conn.cursor()
c.execute('SELECT id, body FROM blog_post WHERE id != 84')
cc = conn.cursor()

for row in c:
    sql = """UPDATE blog_post SET body = "%s" WHERE id = %d""" % (
        replace_all(codecs.encode(row['body'], 'utf-8'), chars),
        row['id'])
    logging.debug('%d %s' % (row['id'], sql))
    cc.execute(sql)
    conn.commit()

cc.close()
c.close()
