
class CSVLimit(Exception):
    """
    Raised when a CSV upload exceeds the supported row limit.
    """
    
    def __init__(self):
        super().__init__(
            "Please upload less than or equal to 20 records",
        )
