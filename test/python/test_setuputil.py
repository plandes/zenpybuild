import logging
import unittest
from io import StringIO
from pathlib import Path
from zensols.pybuild import SetupUtil, VERSION

logger = logging.getLogger(__name__)


class TestSetupUtil(unittest.TestCase):
    def test_setup_util(self):
        setup_str = """name=zensols.progname
packages=[]
version=%(ver)s
description=This project attempts to export a local Zotero library to a usable HTML website.
author=Paul Landes
author_email=landes@mailc.net
url=https://github.com/plandes/progname
download_url=https://github.com/plandes/progname/releases/download/v%(ver)s/zensols.progname-%(ver)s-py3-none-any.whl
long_description=# Inspect and iterat...
long_description_content_type=text/markdown
install_requires=['GitPython~=3.1.29', 'gitdb2~=2.0.3']
keywords=['akeyword']
classifiers=['aclass']
entry_points={'console_scripts': ['progname=zensols.progname:main']}
""" % {'ver': VERSION}

        setup_path = Path(__file__).parent.parent.parent.joinpath('src/python')
        su = SetupUtil(
            setup_path=setup_path,
            name='zensols.progname',
            user='plandes',
            project='progname',
            description='This project attempts to export a local Zotero library to a usable HTML website.',
            keywords=['akeyword'],
            classifiers=['aclass'],
        )
        sio = StringIO()
        su.write(writer=sio)
        logger.debug(sio.getvalue())
        if False:
            print(setup_str)
            print('-' * 40)
            print(sio.getvalue())
        self.maxDiff = None
        self.assertEqual(setup_str, sio.getvalue())

    def test_short_description(self):
        su = SetupUtil.source(rel_setup_path=Path('test-resources/src/setup.py'))
        inf = su.get_info()
        self.assertEqual('Inspect and iterate on git tags and invoke setup utils',
                         inf['short_description'])
