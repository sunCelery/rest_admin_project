class CityNotFoundOrNotGiven(Exception):
    """
    Raised when there is no such city in the Earth
    or no "city" not given in payload
    """
    pass


class DateNotGiven(Exception):
    """
    Raised when date given in wrong form
    or "date" not given in payload
    """
    pass
