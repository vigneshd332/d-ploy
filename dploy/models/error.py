from pydantic import BaseModel


class SuccessResponse(BaseModel):
    """Model for success response"""

    message: str


class GenericError(BaseException):
    """Model for generic error with detail"""

    detail: str
