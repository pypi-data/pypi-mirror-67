import unittest
import unittest.mock

def setUpModule():
    pass

def tearDownModule():
    pass

# Probably you should make some magic with you test oracle db:):
# alter session set "_ORACLE_SCRIPT"=true; 
# create user houston identified by houston;
# grant CREATE SESSION, ALTER SESSION, CREATE DATABASE LINK, CREATE MATERIALIZED VIEW, CREATE PROCEDURE, CREATE PUBLIC SYNONYM, CREATE ROLE, CREATE SEQUENCE, CREATE SYNONYM, CREATE TABLE, CREATE TRIGGER, CREATE TYPE, CREATE VIEW, UNLIMITED TABLESPACE to houston;
# granst select on <testtabsle> to houston;


from test.test_env import SKIP_EXT_DB_SERVERS
@unittest.skipIf(SKIP_EXT_DB_SERVERS, 
    "Skip when test servers are not available in environment")
class OracleDbTestCase(unittest.TestCase):
    CONN_STR = "houston/houston@//localhost:51521/XE"

    @classmethod
    def clean_test_db(cls):
        pass

    @classmethod
    def setUpClass(cls):
        from fairways.ci import helpers
        cls.helpers = helpers

        from fairways.io.syn import oracle

        import time
        import re
        import os
        cls.oracle = oracle
        cls.time = time
        cls.re = re

        cls.clean_test_db()
        root = helpers.getLogger()

    @classmethod
    def tearDownClass(cls):
        cls.clean_test_db()

    def test_select_const(self):
        """
        """
        oracle = self.oracle

        # default=":memory:"
        db_alias = "MY_TEST_ORACLE"

        with unittest.mock.patch.dict('os.environ', {db_alias: self.CONN_STR}, clear=True):
            db = oracle.OracleDb(db_alias)

            sql = "select 99 from dual"
            # sql = "select * from SYSTEM.regions"
            result = db.fetch(sql)

        self.assertEqual(len(result), 1)
        self.assertDictEqual(result[0], {'99': 99})


