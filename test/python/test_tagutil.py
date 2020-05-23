import logging
import unittest
import copy
from zensols.pybuild import Tag, Version

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('zensols.pybuild.test.tag')


class TestTag(unittest.TestCase):
    def test_tagutil(self):
        tu = Tag()
        self.assertTrue(tu.last_tag.startswith('0.0'))

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

    def test_ver_sort(self):
        v1 = Version.from_string('v0.0.6')
        v2 = Version.from_string('v1.0.0')
        self.assertEqual('v0.0.6', str(v1))
        self.assertEqual('v1.0.0', str(v2))
        self.assertTrue(v1 < v2)
        self.assertTrue(v2 > v1)
        vers = [v2, v1]
        vers = list(sorted(vers))
        self.assertTrue(vers[0] == v1)
        self.assertTrue(vers[1] == v2)
        vers = [v1, v2]
        vers = list(sorted(vers))
        self.assertTrue(vers[0] == v1)
        self.assertTrue(vers[1] == v2)

    def test_tmp(self):
        tu = Tag(dry_run=True)
        entries = tu.get_entries()
        first = entries[0]
        last = entries[-1]
        self.assertTrue(first['ver'] < last['ver'])
        tu.create()
