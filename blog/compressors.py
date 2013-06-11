from cssmin import cssmin
from pipeline.compressors import CompressorBase


class CssminCompressor(CompressorBase):

    def compress_css(self, css):
        return cssmin(css)
