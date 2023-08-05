#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
This module provides drivers with CkipClassic backend.
"""

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = '2018-2020 CKIP Lab'
__license__ = 'CC BY-NC-SA 4.0'

from ckipnlp.container import (
    TextParagraph as _TextParagraph,
    SegParagraph as _SegParagraph,
    WsPosParagraph as _WsPosParagraph,
    ParsedParagraph as _ParsedParagraph,
)

from .base import (
    BaseDriver as _BaseDriver,
    DriverType as _DriverType,
    DriverKind as _DriverKind,
)

################################################################################################################################

class CkipClassicWordSegmenter(_BaseDriver):
    """The CKIP word segmentation driver with CkipClassic backend."""

    driver_type = _DriverType.WORD_SEGMENTER
    driver_kind = _DriverKind.CLASSIC

    _count = 0

    def __init__(self, *, do_pos=False, lazy=False):
        super().__init__(lazy=lazy)
        self._do_pos = do_pos

    def _init(self):
        self.__class__._count += 1  # pylint: disable=protected-access
        if self.__class__._count > 1:  # pylint: disable=protected-access
            raise RuntimeError(f'Never instance more than one {self.__class__.__name__}!')

        import ckip_classic.ws
        self._core = ckip_classic.ws.CkipWs()

    def _call(self, *, text):
        assert isinstance(text, _TextParagraph)

        wspos_text = self._core.apply_list(text.to_text())
        ws, pos = _WsPosParagraph.from_text(wspos_text)

        return (ws, pos,) if self._do_pos else ws

class CkipClassicSentenceParser(_BaseDriver):
    """The CKIP sentence parsing driver with CkipClassic backend."""

    driver_type = _DriverType.SENTENCE_PARSER
    driver_kind = _DriverKind.CLASSIC

    _count = 0

    def _init(self):
        self.__class__._count += 1  # pylint: disable=protected-access
        if self.__class__._count > 1:  # pylint: disable=protected-access
            raise RuntimeError(f'Never instance more than one {self.__class__.__name__}!')

        import ckip_classic.parser
        self._core = ckip_classic.parser.CkipParser(do_ws=False)

    def _call(self, *, ws, pos):
        assert isinstance(ws, _SegParagraph)
        assert isinstance(pos, _SegParagraph)

        wspos_text = _WsPosParagraph.to_text(ws, pos)
        parsed_text = self._core.apply_list(wspos_text)
        parsed = _ParsedParagraph.from_text(parsed_text)

        return parsed

    @staticmethod
    def _half2full(text):
        return text \
           .replace('(', '（') \
           .replace(')', '）') \
           .replace('+', '＋') \
           .replace('-', '－') \
           .replace(':', '：') \
           .replace('|', '｜') \
           .replace('&', '＆') \
           .replace('#', '＃')
