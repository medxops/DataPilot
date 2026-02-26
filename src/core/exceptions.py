"""
DataPilot Custom Exceptions
"""


class DataPilotError(Exception):
    """Base exception for all DataPilot errors"""

    pass


class DatabaseError(DataPilotError):
    """Database-related errors"""

    pass


class ETLError(DataPilotError):
    """ETL processing errors"""

    pass


class ValidationError(DataPilotError):
    """Data validation errors"""

    pass


class DataFileNotFoundError(DataPilotError):
    """File not found errors"""

    pass


class ConfigurationError(DataPilotError):
    """Configuration errors"""

    pass


class LoadJobError(DataPilotError):
    """Data loading job errors"""

    pass
