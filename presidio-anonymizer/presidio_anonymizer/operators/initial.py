import re
from typing import Dict
from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Operator that converts names or multi-word phrases to initials."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        # If no text provided, nothing to do
        if not text:
            return text

        # Trim external whitespace
        stripped = text.strip()
        if stripped == "":
            return ""

        # Find prefix of all characters BEFORE the first alphanumeric
        match = re.search(r"[A-Za-z0-9]", stripped)
        if not match:
            # No alphanumeric characters at all
            return stripped

        prefix = stripped[:match.start()]     # Things like @ -- ** etc.
        rest = stripped[match.start():]       # Where words begin

        # Split rest into words
        words = rest.split()

        initials = []
        for word in words:
            m = re.search(r"[A-Za-z0-9]", word)
            if m:
                initials.append(f"{m.group(0).upper()}.")

        return prefix + " ".join(initials)

    def validate(self, params: Dict = None) -> None:
        """This operator takes no parameters."""
        return

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize
