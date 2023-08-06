# Pylint doesn't play well with fixtures and dependency injection from pytest
# pylint: disable=redefined-outer-name

import subprocess
import pytest

from buildstream.testing import Repo
from buildstream import utils, ProgramNotFoundError

try:
    OSTREE_CLI = utils.get_host_tool("ostree")
    HAVE_OSTREE_CLI = True
except ProgramNotFoundError:
    HAVE_OSTREE_CLI = False

try:
    from bst_plugins_experimental.sources import (  # pylint: disable=unused-import
        _ostree,
    )

    HAVE_OSTREE = True
except (ImportError, ValueError):
    HAVE_OSTREE = False


class OSTree(Repo):
    def __init__(self, directory, subdir):
        if not HAVE_OSTREE_CLI or not HAVE_OSTREE:
            pytest.skip("ostree cli is not available")

        super(OSTree, self).__init__(directory, subdir)
        self.ostree = OSTREE_CLI

    def create(self, directory):
        subprocess.call(
            [self.ostree, "init", "--repo", self.repo, "--mode", "archive-z2"]
        )
        subprocess.call(
            [
                self.ostree,
                "commit",
                "--repo",
                self.repo,
                "--branch",
                "master",
                "--subject",
                "Initial commit",
                directory,
            ]
        )

        latest = self.latest_commit()

        return latest

    def source_config(self, ref=None):
        config = {
            "kind": "ostree",
            "url": "file://" + self.repo,
            "track": "master",
        }
        if ref is not None:
            config["ref"] = ref

        return config

    def latest_commit(self):
        return subprocess.check_output(
            [self.ostree, "rev-parse", "--repo", self.repo, "master"],
            universal_newlines=True,
        ).strip()
