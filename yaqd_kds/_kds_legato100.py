__all__ = ["KdsLegato100"]

import asyncio
from typing import Dict, Any, List
import serial

from yaqd_core import IsDaemon, HasPosition, HasLimits, UsesSerial, UsesUart, aserial


class KdsLegato100(UsesUart, UsesSerial, HasLimits, HasPosition, IsDaemon):
    _kind = "kds-legato100"

    def __init__(self, name, config, config_filepath):
        super().__init__(name, config, config_filepath)
        # Perform any unique initialization
        self._ser = aserial.ASerial(
            port=self._config["serial_port"],
            baudrate=self._config["baud_rate"],
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
        )
        # self._ser.stopbits=1

    def run(self):
        # self._ser(f"{self._config['address']} run\r".encode())
        print("start the currently loaded program")
        self._ser.write("run\r\n".encode())
        print("run\r\n".encode())

    def _set_position(self, position: float) -> None:
        print("set position\r\n")
        raise NotImplementedError

    def direct_serial_write(self, message: bytes):
        print("write me some serial")
        self._ser.write(message)
        print(message)

    def purge(self):
        print("empty the syringe")
        raise NotImplementedError

    def prime(self):
        print("retract for new syringe")
        raise NotImplementedError

    def stop(self):
        print("stop the pump!")
        self._ser.write("stop\r\n".encode())
        # print("stop\r\n".encode())

    def get_rate(self):
        print("get the current rate")
        self._ser.write("crate\r\n".encode())
        # read_val = self._ser.read(size=8)
        # print(read_val)

    def set_infuse_rate(self, infuse_rate):
        self._ser.write(f"irate {infuse_rate}\r\n".encode())
        # read_val = self._ser.read(size=8)
        # print(read_val)

    def get_force(self):
        print("get the current rate")
        raise NotImplementedError
        self._ser.write("force\r\n".encode())
        # read_val = self._ser.read(size=8)
        # print(read_val)

    def set_force(self, force):
        self._ser.write(f"force {force}\r\n".encode())
        # read_val = self._ser.read(size=8)
        # print(read_val)

    def get_diameter(self):
        print("get the current rate")
        raise NotImplementedError
        self._ser.write("diameter\r\n".encode())
        # read_val = self._ser.read(size=8)
        # print(read_val)

    def set_diameter(self, diameter):
        print("setting diameter to {diameter} mm")
        self._ser.write(f"diameter {diameter}\r\n".encode())
        # read_val = self._ser.read(size=8)
        # print(read_val)

    def set_brightness(self, brightness):
        print("setting diameter to {diameter} mm")
        self._ser.write(f"dim {brightness}\r\n".encode())
        # read_val = self._ser.read(size=8)
        # print(read_val)

    async def update_state(self):
        """Continually monitor and update the current daemon state."""
        # If there is no state to monitor continuously, delete this function
        while True:
            # Perform any updates to internal state
            self._busy = False
            # There must be at least one `await` in this loop
            # This one waits for something to trigger the "busy" state
            # (Setting `self._busy = True)
            # Otherwise, you can simply `await asyncio.sleep(0.01)`
            await self._busy_sig.wait()
