from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Recived status code is not equal to expected'
    WRONG_ELEMENT_CODE = 'Number of items is not equal to expected'