import logging
import re
import sys
import json
from pathlib import Path
from datetime import datetime
from git import Repo, TagReference
from zensols.pybuild import Version

logger = logging.getLogger('zensols.gittag.tag')


class TagUtil(object):
    """Git tag helper"""
    def __init__(self, repo_dir='.', message='none'):
        logger.debug('creating witih repo dir: {}'.format(repo_dir))
        if isinstance(repo_dir, Path):
            repo_dir = str(repo_dir.resolve())
        self.repo = Repo(repo_dir)
        assert not self.repo.bare
        self.message = message

    def parse_version(self, name):
        m = re.search('v(\d+)\.(\d+)\.(\d+)$', name)
        if m is not None:
            return {'major': int(m.group(1)),
                    'minor': int(m.group(2)),
                    'debug': int(m.group(3))}

    def format_version(self, ver, prefix='v'):
        return prefix + ('{major}.{minor}.{debug}'.format(**ver))

    def get_entries(self):
        tags = self.repo.tags
        logger.debug('tags: {}'.format(tags))
        tags = filter(lambda x: hasattr(x.object, 'tagged_date'), tags)
        tags = sorted(tags, key=lambda x: x.object.tagged_date)
        tag_entries = []
        for tag in tags:
            name = tag.object.tag
            ver = self.parse_version(tag.object.tag)
            if ver is not None:
                tag_entries.append({'name': name,
                                    'ver': ver,
                                    'date': tag.object.tagged_date,
                                    'tag': tag,
                                    'message': tag.object.message})
        return tag_entries

    def last_tag_entry(self):
        entries = self.get_entries()
        logger.debug('entires: {}'.format(entries))
        if (len(entries) > 0):
            return entries[-1]

    def get_last_tag(self):
        entry = self.last_tag_entry()
        if entry:
            return self.format_version(entry['ver'], prefix='')

    def print_last_tag(self):
        last_tag = self.get_last_tag()
        if last_tag:
            print(last_tag)

    def get_last_commit(self):
        commits = list(self.repo.iter_commits('HEAD'))
        if len(commits) > 0:
            return commits[0]

    def get_info(self):
        last_tag = self.get_last_tag()
        inf = {'tag': last_tag,
               'build_date': datetime.now().isoformat()}
        c = self.get_last_commit()
        if c:
            inf['commit'] = {'author': str(c.author),
                             'date': c.committed_datetime.isoformat(),
                             'sha': str(c),
                             'summary': c.summary}
        return inf

    def dump_info(self, writer=sys.stdout):
        json.dump(self.get_info(), writer, indent=2)

    def increment_version(self, version_part):
        entry = self.last_tag_entry()
        if entry:
            ver = entry['ver']
            ver_key = Version.reverse_mapping[version_part]
            logger.debug('ver_key: {}, entry: <{}>'.format(ver_key, entry))
            ver[ver_key] = ver[ver_key] + 1
        else:
            ver = {'major': 0, 'minor': 0, 'debug': 1}
        logger.debug('new version: {}'.format(ver))
        return self.format_version(ver)

    def delete_last_tag(self):
        entry = self.last_tag_entry()
        tag = entry['tag']
        name = entry['name']
        logger.info('deleting: {}'.format(name))
        TagReference.delete(self.repo, tag)

    def recreate_last_tag(self):
        entry = self.last_tag_entry()
        tag = entry['tag']
        name = entry['name']
        msg = entry['message']
        logger.info('deleting: {}'.format(name))
        TagReference.delete(self.repo, tag)
        logger.info('creating {} with commit <{}>'.format(name, msg))
        TagReference.create(self.repo, name, message=msg)

    def create(self):
        new_tag_name = self.increment_version(Version.debug)
        logger.info('creating {} with commit <{}>'.format(
            new_tag_name, self.message))
        TagReference.create(self.repo, new_tag_name, message=self.message)
