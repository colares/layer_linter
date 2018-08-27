from typing import Any

from ..module import Module


class ImportPath:
    """
    A direct dependency path between two modules. For example,
    if foo imports bar.baz, then the ImportPath is:
        ImportPath(
            importer='foo',
            imported='bar.baz'
        )
    """
    def __init__(self, importer: Module, imported: Module) -> None:
        """
        Args:
            importer (str): Absolute name of importing module.
            imported (str): Absolute name of module imported by importer.
        """
        self.importer = importer
        self.imported = imported

    def __str__(self) -> str:
        return "{} <- {}".format(self.importer, self.imported)

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self)

    def __eq__(self, other: Any) -> bool:
        return str(self) == str(other)

    def __hash__(self) -> int:
        return hash(str(self))
