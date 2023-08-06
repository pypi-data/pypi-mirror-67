#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Copyright (C) 2019 Christoph Fink, University of Helsinki
#
#   This program is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation; either version 3
#   of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, see <http://www.gnu.org/licenses/>.

""" A base class for downloading video metadata from the
    Youtube Data API v3 """


__all__ = [
    "YoutubeVideoMetadataDownloader"
]


import datetime
import dateutil

from .cache import (
    Cache
)
from .youtubecommentthreaddownloader import (
    YoutubeCommentThreadDownloader
)
from .youtubemetadatadownloader import (
    YoutubeMetadataDownloader
)
from .youtubevideo import (
    YoutubeVideo
)


class YoutubeVideoMetadataDownloader(YoutubeMetadataDownloader):
    """ TODO
    """
    ENDPOINT = "search"
    DATE_FORMAT = "{:%Y-%m-%dT%H:%M:%S.000Z}"

    def __init__(
            self,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        try:
            self.search_terms = self._config["search_terms"]
        except (KeyError, AttributeError):
            self.search_terms = None
        self._published = None

    @property
    def _published(self):
        if self.__published is None:
            try:
                with Cache() as cache:
                    published = cache[self.search_terms]["publishedBefore"]
                    if isinstance(published, datetime.datetime):
                        published = \
                            self.DATE_FORMAT.format(published)
                    self.__published = published
            except KeyError:
                pass
        return self.__published

    @_published.setter
    def _published(self, published):
        self.__published = published

        if published is not None:
            try:
                published = dateutil.parser.isoparse(published)
                published += datetime.timedelta(seconds=1)

                with Cache() as cache:
                    if self.search_terms not in cache:
                        cache[self.search_terms] = {}

                    cache[self.search_terms]["publishedBefore"] = \
                        self.DATE_FORMAT.format(published)
            except ValueError:  # dateutil parser
                pass

    @property
    def _params(self):
        params = {
            "key": self._config["youtube_api_key"],
            "part": "snippet",
            "maxResults": 50,
            "order": "date",
            "type": "video",
            "q": self.search_terms
        }
        if self._published is not None:
            params["publishedBefore"] = self._published
        return params

    def download(self, search_terms=None):
        """ TODO """
        if search_terms is not None:
            self.search_terms = search_terms

        if self.search_terms is None:
            raise AttributeError(
                f"{self.__class__.__name__}.search_terms is undefined"
            )

        for item in self.items:
            video = YoutubeVideo(item)
            YoutubeCommentThreadDownloader(video.orig_id).download()
            del video

            self._published = item["snippet"]["publishedAt"]
