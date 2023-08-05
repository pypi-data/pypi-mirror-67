#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
This module provides co-reference detection pipeline.
"""

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = '2018-2020 CKIP Lab'
__license__ = 'CC BY-NC-SA 4.0'

from collections.abc import (
    Mapping as _Mapping,
)

from ckipnlp.driver.base import (
    DriverType as _DriverType,
    DriverKind as _DriverKind,
    DriverRegister as _DriverRegister,
)

from .core import (
    CkipPipeline as _CkipPipeline,
)

################################################################################################################################

class CkipCorefDocument(_Mapping):
    """The co-reference document.

    Attributes
    ----------
        ws : :class:`SegParagraph <ckipnlp.container.seg.SegParagraph>`
            The word-segmented sentences.
        pos : :class:`SegParagraph <ckipnlp.container.seg.SegParagraph>`
            The part-of-speech sentences.
        parsed : :class:`ParsedParagraph <ckipnlp.container.parsed.ParsedParagraph>`
            The parsed sentences.
        coref : :class:`CorefParagraph <ckipnlp.container.coref.CorefParagraph>`
            The co-reference sentences.
    """

    __keys = ('ws', 'pos', 'parsed', 'coref',)

    def __init__(self, *, ws=None, pos=None, parsed=None, coref=None):
        self.ws = ws
        self.pos = pos
        self.parsed = parsed
        self.coref = coref

    def __len__(self):
        return len(self.__keys)

    def __iter__(self):
        yield from self.__keys

    def __getitem__(self, key):
        return getattr(self, key)

################################################################################################################################

class CkipCorefPipeline(_CkipPipeline):
    """The co-reference detection pipeline.

    Arguments
    ---------
        sentence_segmenter_kind : :class:`DriverKind <ckipnlp.driver.base.DriverKind>`
            The type of sentence segmenter.

        word_segmenter_kind : :class:`DriverKind <ckipnlp.driver.base.DriverKind>`
            The type of word segmenter.

        pos_tagger_kind : :class:`DriverKind <ckipnlp.driver.base.DriverKind>`
            The type of part-of-speech tagger.

        ner_chunker_kind : :class:`DriverKind <ckipnlp.driver.base.DriverKind>`
            The type of named-entity recognition chunker.

        sentence_parser_kind : :class:`DriverKind <ckipnlp.driver.base.DriverKind>`
            The type of sentence parser.

        coref_chunker_kind : :class:`DriverKind <ckipnlp.driver.base.DriverKind>`
            The type of co-reference detection chunker.

    Other Parameters
    ----------------
        lazy : bool
            Lazy initialize the drivers.
    """

    def __init__(self, *,
        coref_chunker_kind=_DriverKind.BUILTIN,
        lazy=True,
        **kwargs,
    ):
        super().__init__(lazy=lazy, **kwargs)

        # CoRef
        if coref_chunker_kind:
            assert self._wspos_driver.is_dummy, 'Co-reference pipeline is not compatible with CkipClassic word segmenter!'

        self._coref_chunker = _DriverRegister.get(_DriverType.COREF_CHUNKER, coref_chunker_kind)(lazy=lazy)

    def __call__(self, doc):
        corefdoc = CkipCorefDocument()
        self.get_coref(doc, corefdoc)
        return corefdoc

    def get_coref(self, doc, corefdoc):
        """Apply co-reference delectation.

        Arguments
        ---------
            doc : :class:`CkipDocument <.core.CkipDocument>`
                The input document.
            corefdoc : :class:`CkipCorefDocument`
                The input document for co-reference.

        Returns
        -------
            corefdoc.coref : :class:`CorefParagraph <ckipnlp.container.coref.CorefParagraph>`
                The co-reference results.

        .. note::

            This routine modify **corefdoc** inplace.
        """
        self.get_text(doc)
        self.get_ws(doc)
        self.get_pos(doc)
        self.get_ner(doc)

        # Update word segmentation
        if corefdoc.ws is None:
            corefdoc.ws = self._coref_chunker.transform_ws(
                text=doc.text,
                ws=doc.ws,
                ner=doc.ner,
            )

        # Update POS-tagging
        if corefdoc.pos is None:
            corefdoc.pos = self.get_pos(corefdoc)
            self._coref_chunker.transform_pos(
                ws=corefdoc.ws,
                pos=corefdoc.pos,
                ner=doc.ner,
            )

        # Do parsing
        if corefdoc.parsed is None:
            corefdoc.parsed = self.get_parsed(corefdoc)

        # Do co-reference detection
        corefdoc.coref = self._coref_chunker(parsed=corefdoc.parsed)

        return corefdoc.coref
