#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu


""" zimwriterfs abstraction via ZimInfo """

import os
import subprocess

from . import logger
from .constants import SCRAPER
from .logging import nicer_args_join


class ZimInfo(object):
    zimwriterfs_path = os.getenv("ZIMWRITERFS_BINARY", "/usr/bin/zimwriterfs")

    def __init__(
        self,
        homepage="home.html",
        favicon="favicon.png",
        language="eng",
        title="my title",
        description="my zim description",
        creator="unknown",
        publisher="kiwix",
        source=None,
        flavour=None,
        tags=[],
        name="test-zim",
        scraper=SCRAPER,
    ):

        self.homepage = homepage
        self.favicon = favicon
        self.language = language
        self.title = title
        self.description = description
        self.creator = creator
        self.publisher = publisher
        self.source = source
        self.flavour = flavour
        self.tags = tags
        self.name = name
        self.scraper = scraper

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_zimwriterfs_args(
        self,
        verbose=True,
        inflateHtml=False,
        uniqueNamespace=False,
        withoutFTIndex=False,
        minChunkSize=None,
        redirects=None,
    ):
        arg_list = [
            "--welcome",
            self.homepage,
            "--favicon",
            self.favicon,
            "--language",
            self.language,
            "--title",
            self.title,
            "--description",
            self.description,
            "--creator",
            self.creator,
            "--publisher",
            self.publisher,
        ]

        if self.source is not None:
            arg_list.extend(["--source", self.source])
        if self.flavour is not None:
            arg_list.extend(["--flavour", self.flavour])
        if self.tags:
            arg_list.extend(["--tags", ";".join(self.tags)])

        arg_list.extend(["--name", self.name, "--scraper", self.scraper])

        if verbose:
            arg_list.append("--verbose")
        if inflateHtml:
            arg_list.append("--inflateHtml")
        if uniqueNamespace:
            arg_list.append("--uniqueNamespace")
        if withoutFTIndex:
            arg_list.append("--withoutFTIndex")
        if minChunkSize is not None:
            arg_list.extend(["--minChunkSize", str(minChunkSize)])
        if redirects is not None:
            arg_list.extend(["--redirects", redirects])

        return arg_list


def make_zim_file(build_dir, output_dir, zim_fname, zim_info):
    """ runs zimwriterfs """
    args = (
        [ZimInfo.zimwriterfs_path]
        + zim_info.to_zimwriterfs_args()
        + [str(build_dir), str(output_dir.joinpath(zim_fname))]
    )

    logger.debug(nicer_args_join(args))
    zimwriterfs = subprocess.run(args)
    zimwriterfs.check_returncode()
