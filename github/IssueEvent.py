# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import github.GithubObject

import github.Issue
import github.NamedUser


class IssueEvent(github.GithubObject.CompletableGithubObject):
    """
    This class represents IssueEvents as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def actor(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._actor)
        return self._NoneIfNotSet(self._actor)

    @property
    def commit_id(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._commit_id)
        return self._NoneIfNotSet(self._commit_id)

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def event(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._event)
        return self._NoneIfNotSet(self._event)

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def issue(self):
        """
        :type: :class:`github.Issue.Issue`
        """
        self._completeIfNotSet(self._issue)
        return self._NoneIfNotSet(self._issue)

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def _initAttributes(self):
        self._actor = github.GithubObject.NotSet
        self._commit_id = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._event = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._issue = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "actor" in attributes:  # pragma no branch
            assert attributes["actor"] is None or isinstance(attributes["actor"], dict), attributes["actor"]
            self._actor = None if attributes["actor"] is None else github.NamedUser.NamedUser(self._requester, attributes["actor"], completed=False)
        if "commit_id" in attributes:  # pragma no branch
            assert attributes["commit_id"] is None or isinstance(attributes["commit_id"], (str, unicode)), attributes["commit_id"]
            self._commit_id = attributes["commit_id"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "event" in attributes:  # pragma no branch
            assert attributes["event"] is None or isinstance(attributes["event"], (str, unicode)), attributes["event"]
            self._event = attributes["event"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "issue" in attributes:  # pragma no branch
            assert attributes["issue"] is None or isinstance(attributes["issue"], dict), attributes["issue"]
            self._issue = None if attributes["issue"] is None else github.Issue.Issue(self._requester, attributes["issue"], completed=False)
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
