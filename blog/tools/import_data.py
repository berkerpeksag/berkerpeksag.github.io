#!/usr/bin/env python
# coding: utf-8

import codecs
from datetime import datetime
import logging
import MySQLdb

logging.root.setLevel(logging.INFO)


class ImportData(object):
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

    def create_sql(self, table=None):
        if table is None:
            raise Exception('You should write a table name.')

        rows = self.query('SELECT * FROM %s ORDER BY fldTarih DESC' % table)

        if rows:
            today = datetime.today().strftime('%Y-%m-%d')
            filename = '{0:>s}-{1:>s}.sql'.format(table, today)

            f = codecs.open(filename, 'w', 'utf-8')
            for row in rows:
                olddate = str(row['fldTarih']) + ' ' + str(row['fldSaat'])
                f.write('''INSERT INTO blog_post VALUES(%d, %d, %d, %d, '%s',
                        '%s', "%s", '%s', '%s');''' % (
                            row['fldID'], 1, row['fldAktif'], 1,
                            row['fldBaslik'], row['fldBaslikEncode'],
                            row['fldYazi'], olddate, olddate))

            logging.info('File: %s', filename)


config = {'host': 'www.berkerpeksag.com', 'db': 'dbberkerpeksag',
          'user': 'root', 'passwd': 'berker88',
          'use_unicode': True, 'charset': 'utf8'}

importer = ImportData(**config)

importer.create_sql('tblbloglar')
