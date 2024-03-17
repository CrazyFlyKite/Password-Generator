import logging
from os import PathLike
from secrets import choice
from subprocess import Popen, PIPE
from typing import Optional, Any, Final, TypeAlias, List

from GlobalKit import english, digits
from customtkinter import CTkEntry

from setup_logging import setup_logging

# Setup logging
setup_logging(level=logging.DEBUG, logging_format='[%(levelname)s] - %(message)s')

# Custom types
PathLikeString: TypeAlias = str | bytes | PathLike

# Window
WINDOW_TITLE: Final[str] = 'Password Generator'
WINDOW_WIDTH: Final[int] = 470
WINDOW_HEIGHT: Final[int] = 380
WINDOW_RESIZABLE: Final[bool] = False
WINDOW_ICON: Final[PathLikeString] = '../assets/images/icon.png'

# Fonts
PASSWORD_FONT: Final[str] = 'JetBrains Mono'

# Other
DEFAULT_LENGTH: Final[int] = 12
MAX_PASSWORD_LENGTH: Final[int] = 30
INCLUDE_CATEGORIES: Final[List[str]] = ['lowercase', 'uppercase', 'numbers', 'symbols']
INVALID_INPUT_MESSAGE: str = 'Invalid input!'


# Functions
def generate_password(length: int,
                      lowercase: Optional[bool] = True,
                      uppercase: Optional[bool] = True,
                      numbers: Optional[bool] = True,
                      special: Optional[bool] = True) -> Optional[str]:
	"""
    Generate a random password of specified length with optional character types.

    :parameter length: The length of the generated password.
    :parameter lowercase: Whether to include lowercase letters (default is `True`).
    :parameter uppercase: Whether to include uppercase letters (default is `True`).
    :parameter numbers: Whether to include numeric digits (default is `True`).
    :parameter special: Whether to include special characters (default is `True`).

    :returns: The generated password as a string.
    """

	characters: str = ''
	characters += english.full_lowercase if lowercase else ''
	characters += english.full_lowercase if lowercase else ''
	characters += english.full_uppercase if uppercase else ''
	characters += digits if numbers else ''
	characters += '*%$&@:;/,._+!?' if special else ''

	return None if not characters else ''.join(choice(characters) for _ in range(length))


def copy_to_clipboard(text: str) -> None:
	"""
	Works only on MacOSX
	"""

	process: Popen[bytes] = Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=PIPE)
	process.communicate(text.encode('utf-8'))


# Classes
class CTkNumberEntry(CTkEntry):
	def __init__(self, master: Any, **kwargs) -> None:
		super().__init__(master, **kwargs)
		self.configure(validate='key', validatecommand=(self.register(self.on_validate), '%P'))

	@staticmethod
	def on_validate(new_value: str) -> bool:
		return not new_value.strip() or new_value.isdigit()
