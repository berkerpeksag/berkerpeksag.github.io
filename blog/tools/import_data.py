#!/usr/bin/env python
# coding: utf-8

import codecs
from datetime import datetime
import logging
import MySQLdb
import re

logging.root.setLevel(logging.INFO)


class DataImporter(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        self._db = None
        try:
            self._db = MySQLdb.connect(**kwargs)
        except Exception:
            logging.error('Cannot connect to MySQL.')

    def query(self, sql):
        cursor = self._db.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close()
            logging.info('Cursor closed.')

    def create_sql(self, table):
        rows = self.query('SELECT * FROM {} ORDER BY fldTarih DESC'.format(table))

        if rows:
            today = datetime.today().strftime('%Y-%m-%d')
            filename = '{0:>s}-{1:>s}.sql'.format(table, today)

            file = codecs.open(filename, 'w', 'utf-8')
            for row in rows:
                row['old_date'] = unicode(row['fldTarih']) + ' ' + unicode(row['fldSaat'])
                row['user_id'] = 1

                sql = """INSERT INTO blog_post VALUES({fldID:d}, {user_id:d}, {fldAktif:d},
                         {user_id:d}, {fldBaslik:>s}, {fldBaslikEncode:>s}, {fldYazi:>s},
                         {old_date:>s}, {old_date:>s});"""

                file.write(re.escape(sql.format(**row)))

            logging.info('File: {}'.format(filename))


config = {'host': 'www.berkerpeksag.com', 'db': 'dbberkerpeksag',
          'user': 'root', 'passwd': 'berker88',
          'use_unicode': True, 'charset': 'utf8'}

importer = DataImporter(**config)

importer.create_sql('tblbloglar')
