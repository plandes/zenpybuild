import logging
import unittest
from zensols.pybuild import TagUtil

logger = logging.getLogger('zensols.pybuild.test.tag')


class TestTagUtil(unittest.TestCase):
    def test_tagutil(self):
        tu = TagUtil()
        self.assertTrue(tu.get_last_tag().startswith('0.0'))
