# -*- coding: utf-8 -*-

import asyncio
import aiosqlite
import os
import re

from .base import (AsyncDataDriver, FileConnMixin)
# Should provice async methods .fetch, .execute

import logging
log = logging.getLogger(__name__)

class SqLite(AsyncDataDriver, FileConnMixin):
    
    default_conn_str = ":memory:"
    autoclose = True

    def is_connected(self):
        return self.engine is not None

    async def _connect(self):
        db_filename = self.conn_str
        engine = await aiosqlite.connect(db_filename)
        engine.row_factory = dict_factory
        engine.isolation_level = "IMMEDIATE"
        self.engine = engine

    async def fetch(self, sql):
        cursor = None
        try:
            await self._ensure_connection()
            cursor = await self.engine.execute(sql)
            return await cursor.fetchall()
        except Exception as e:
            log.error("DB operation error: {} at {}".format(e, self.db_name))
            raise
        finally:
            if cursor:
                await cursor.close()
            if self.autoclose:
                await self.close()
    
    async def change(self, sql):
        try:
            await self._ensure_connection()
            await self.engine.execute(sql)
            await self.engine.commit()
        except Exception as e:
            log.error("DB operation error: {} at {}".format(e, self.db_name))
            raise
        finally:
            if self.autoclose:
                await self.close()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
