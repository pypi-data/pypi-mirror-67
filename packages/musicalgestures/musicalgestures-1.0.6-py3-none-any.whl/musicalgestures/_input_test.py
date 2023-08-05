class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes
    ----------
    - message : str

        Explanation of the error.
    """

    def __init__(self, message):
        self.message = message


def mg_input_test(filename, filtertype, thresh, starttime, endtime, blur, skip):
    """
    Gives feedback to user if initialization from input went wrong.

    Parameters
    ----------
    - filename : str

        Path to the input video file.
    - filtertype : {'Regular', 'Binary', 'Blob'}

        `Regular` turns all values below `thresh` to 0.
        `Binary` turns all values below `thresh` to 0, above `thresh` to 1.
        `Blob` removes individual pixels with erosion method.
    - thresh : float

        A number in the range of 0 to 1. Default is 0.05.
        Eliminates pixel values less than given threshold.
    - starttime : int or float

        Trims the video from this start time (s).

    - endtime : int or float

        Trims the video until this end time (s).
    - blur : {'None', 'Average'}

        `Average` to apply a 10px * 10px blurring filter, `None` otherwise.
    - skip : int

        Every n frames to discard. `skip=0` keeps all frames, `skip=1` skips every other frame.
    """

    filenametest = type(filename) == str

    if filenametest:
        if filtertype.lower() not in ['regular', 'binary', 'blob']:
            msg = 'Please specify a filter type as str: "Regular", "Binary" or "Blob"'
            raise InputError(msg)

        if blur.lower() not in ['average', 'none']:
            msg = 'Please specify a blur type as str: "Average" or "None"'
            raise InputError(msg)

        if not isinstance(thresh, (float, int)):
            msg = 'Please specify a threshold as a float between 0 and 1.'
            raise InputError(msg)

        if not isinstance(starttime, (float, int)):
            msg = 'Please specify a starttime as a float.'
            raise InputError(msg)

        if not isinstance(endtime, (float, int)):
            msg = 'Please specify a endtime as a float.'
            raise InputError(msg)

        if not isinstance(skip, int):
            msg = 'Please specify a skip as an integer of frames you wish to skip (Max = N frames).'
            raise InputError(msg)

    else:
        msg = 'Minimum input for this function: filename as a str.'
        raise InputError(msg)
