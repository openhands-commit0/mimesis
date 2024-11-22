"""Provides pseudo-scientific data."""
from mimesis.datasets import SI_PREFIXES, SI_PREFIXES_SYM
from mimesis.enums import MeasureUnit, MetricPrefixSign
from mimesis.providers.base import BaseProvider
__all__ = ['Science']

class Science(BaseProvider):
    """Class for generating pseudo-scientific data."""

    class Meta:
        name = 'science'

    def rna_sequence(self, length: int=10) -> str:
        """Generates a random RNA sequence.

        :param length: Length of block.
        :return: RNA sequence.

        :Example:
            AGUGACACAA
        """
        rna_nucleotides = ['A', 'G', 'U', 'C']
        return ''.join(self.random.choices(rna_nucleotides, k=length))

    def dna_sequence(self, length: int=10) -> str:
        """Generates a random DNA sequence.

        :param length: Length of block.
        :return: DNA sequence.

        :Example:
            GCTTTAGACC
        """
        dna_nucleotides = ['A', 'G', 'T', 'C']
        return ''.join(self.random.choices(dna_nucleotides, k=length))

    def measure_unit(self, name: MeasureUnit | None=None, symbol: bool=False) -> str:
        """Returns unit name from the International System of Units.

        :param name: Enum object UnitName.
        :param symbol: Return only symbol
        :return: Unit.
        """
        if name is None:
            name = self.random.choice(list(MeasureUnit))

        unit_name, unit_symbol = name.value
        return unit_symbol if symbol else unit_name

    def metric_prefix(self, sign: MetricPrefixSign | None=None, symbol: bool=False) -> str:
        """Generates a random prefix for the International System of Units.

        :param sign: Sing of prefix (positive/negative).
        :param symbol: Return the symbol of the prefix.
        :return: Metric prefix for SI measure units.
        :raises NonEnumerableError: if sign is not supported.

        :Example:
            mega
        """
        if sign is None:
            sign = self.random.choice(list(MetricPrefixSign))

        prefixes = SI_PREFIXES_SYM if symbol else SI_PREFIXES
        return self.random.choice(prefixes[sign.value])