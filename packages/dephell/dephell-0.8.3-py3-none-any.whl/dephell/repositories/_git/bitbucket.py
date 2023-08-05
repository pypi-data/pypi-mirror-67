# built-in
import re

# app
from ...cached_property import cached_property
from ...config import config
from ...networking import requests_session
from .base import BaseRepo


rex_author = re.compile(r'bitbucket\.com[/:]([a-zA-Z_-])')


class BitbucketRepo(BaseRepo):

    @cached_property
    def author(self):
        match = rex_author.search(self.link)
        if match:
            # get from `#hash=...`
            return match.group(1)

    # https://api.bitbucket.org/2.0/repositories/mnpenner/merge-attrs/refs/tags
    # https://bitbucket.org/atlassian/python-bitbucket/src/master/pybitbucket/auth.py
    # https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Busername%7D/%7Brepo_slug%7D/refs/tags
    def _get_tags(self):
        url = config['bitbucket'] + '/repositories/{author}/{name}/refs/tags'.format(
            author=self.author,
            name=self.name,
        )
        with requests_session() as session:
            response = session.get(url)

        tags = []
        for tag in response.json()['values']:
            tags.append(tag['name'])
        return tags
