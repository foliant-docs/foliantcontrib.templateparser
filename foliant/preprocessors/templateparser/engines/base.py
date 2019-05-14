from pathlib import Path, PosixPath


class TemplateEngineBase:
    """Base class for template engines"""

    def __init__(self,
                 content: str,
                 context: dict,
                 params: dict,
                 md_file: PosixPath or str):
        self._content = content
        self._context = context
        self._params = params
        self._md_file = Path(md_file)

    def build(self):
        """Build template with engine and return resulting string"""
        raise NotImplementedError()
