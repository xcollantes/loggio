"""Logger initialization module.

This module provides easy access to the enhanced logging utilities.
"""

from .enhanced_logger import (
    ColoredFormatter,
    Colors,
    EnhancedLogger,
    get_logger,
)

__version__ = "0.1.0"
__all__ = ["Colors", "ColoredFormatter", "EnhancedLogger", "get_logger"]
