"""This module provides constants for locale-dependent providers."""
from mimesis.enums import Locale
from mimesis.exceptions import LocaleError
__all__ = ['Locale', 'validate_locale']

def validate_locale(locale=None) -> Locale:
    """Validate the locale and return the corresponding Locale enum member.

    Args:
        locale: The locale to validate. Can be a string or Locale enum member.

    Returns:
        Locale: The validated Locale enum member.

    Raises:
        TypeError: If locale parameter is missing.
        LocaleError: If locale is invalid or not supported.
    """
    if locale is None:
        raise TypeError("The locale parameter is required.")

    if isinstance(locale, Locale):
        return locale

    if not isinstance(locale, str):
        raise LocaleError("Locale must be a string or Locale enum member.")

    try:
        return Locale[locale.upper()]
    except KeyError:
        raise LocaleError(f"Locale '{locale}' is not supported.")