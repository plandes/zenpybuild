import logging
import unittest
from io import StringIO
from pathlib import Path
from zensols.pybuild import SetupUtil

#logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('zensols.pybuild.test.su')


class TestSetupUtil(unittest.TestCase):
    def test_setup_util(self):
        setup_str = """name=zensols.progname
packages=[]
version=0.0.1
description=This project attempts to export a local Zotero library to a usable HTML website.
author=Paul Landes
author_email=landes@mailc.net
url=https://github.com/plandes/progname
download_url=https://github.com/plandes/progname/releases/download/v0.0.1/zensols.progname-0.0.1-py3-none-any.whl
long_description=# Inspect and iterat...
long_description_content_type=text/markdown
install_requires=['zensols.actioncli>=0.6']
keywords=['akeyword']
classifiers=['aclass']
entry_points={'console_scripts': ['progname=zensols.progname:main']}
"""

        setup_path = Path(__file__).parent.parent.parent.joinpath('src/python')
        su = SetupUtil(
            setup_path=setup_path,
            name='zensols.progname',
            package_names=['zensols'],
            user='plandes',
            project='progname',
            description='This project attempts to export a local Zotero library to a usable HTML website.',
            keywords=['akeyword'],
            classifiers=['aclass'],
        )
        sio = StringIO()
        su.write(sio)
        logger.debug(sio.getvalue())
        if False:
            print(setup_str)
            print('-' * 40)
            print(sio.getvalue())
        self.maxDiff = None
        self.assertEqual(setup_str, sio.getvalue())
