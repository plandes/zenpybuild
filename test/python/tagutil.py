import logging
import unittest
import copy
from zensols.pybuild import TagUtil, Version

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('zensols.pybuild.test.tag')


class TestTagUtil(unittest.TestCase):
    def test_tagutil(self):
        tu = TagUtil()
        self.assertTrue(tu.get_last_tag().startswith('0.0'))

    def test_ver(self):
        vstr = Version()
        self.assertEqual('v0.0.1', str(vstr))
        ver = Version.from_string('v1.2.3')
        self.assertEqual(1, ver.major)
        self.assertEqual(2, ver.minor)
        self.assertEqual(3, ver.debug)
        ver = Version.from_string('1.2.3')
        self.assertEqual(1, ver.major)
        self.assertEqual(2, ver.minor)
        self.assertEqual(3, ver.debug)
        ver.increment()
        self.assertEqual(1, ver.major)
        self.assertEqual(2, ver.minor)
        self.assertEqual(4, ver.debug)
        ver2 = copy.deepcopy(ver)
        self.assertTrue(ver == ver2)
        ver2.increment('major')
        self.assertTrue(ver != ver2)
        self.assertEqual('v2.2.4', str(ver2))
        self.assertTrue(ver < ver2)
        self.assertTrue(ver2 > ver)

        self.assertTrue(Version.from_string('v1.2.3') < Version.from_string('v2.2.3'))
        self.assertTrue(Version.from_string('v1.2.3') < Version.from_string('v1.3.3'))
        self.assertTrue(Version.from_string('v1.2.3') < Version.from_string('v1.2.4'))

        self.assertTrue(Version.from_string('v1.2.3') <= Version.from_string('v1.2.3'))
        self.assertTrue(Version.from_string('v1.2.3') <= Version.from_string('v2.2.3'))
        self.assertTrue(Version.from_string('v1.2.3') <= Version.from_string('v1.3.3'))
        self.assertTrue(Version.from_string('v1.2.3') <= Version.from_string('v1.2.4'))

        self.assertTrue(Version.from_string('v2.2.3') > Version.from_string('v1.2.3'))
        self.assertTrue(Version.from_string('v1.3.3') > Version.from_string('v1.2.3'))
        self.assertTrue(Version.from_string('v1.2.4') > Version.from_string('v1.2.3'))

        self.assertTrue(Version.from_string('v1.2.3') >= Version.from_string('v1.2.3'))
        self.assertTrue(Version.from_string('v2.2.3') >= Version.from_string('v1.2.3'))
        self.assertTrue(Version.from_string('v1.3.3') >= Version.from_string('v1.2.3'))
        self.assertTrue(Version.from_string('v1.2.4') >= Version.from_string('v1.2.3'))

    def test_tmp(self):
        tu = TagUtil(dry_run=True)
        entries = tu.get_entries()
        first = entries[0]
        last = entries[-1]
        self.assertTrue(first['ver'] < last['ver'])
        tu.create()
