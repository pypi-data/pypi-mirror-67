from .device import Device


class Thermometer(Device):
    """
    1 wire thermometer base class

    This class extends Device and is designed to be subclassed by all the 1wire
    thermometer devices.

    Parameters
    ----------
    owserver : pyownet.protocol._Proxy :
        The proxy object used to access the owserver

    path : str :
        The owfs path for the Thermometer

    uncached : bool:
        (Default value = False)
        If True forces owserver to query the 1wire bus on each property access.
    """
    @property
    def temperature(self) -> float:
        """
        Read-only. Measured temperature at the default resolution.
        """
        return float(self._read('temperature'))
