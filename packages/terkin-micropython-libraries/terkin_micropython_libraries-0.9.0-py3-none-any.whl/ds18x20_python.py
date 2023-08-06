# DS18x20 temperature sensor driver for MicroPython.
# MIT license; Copyright (c) 2016 Damien P. George

from micropython import const
from machine import Pin

CMD_CONVERT = const(0x44)
CMD_RDSCRATCH = const(0xbe)
CMD_WRSCRATCH = const(0x4e)
CMD_RDPOWER = const(0xb4)

class DS18X20:
    def __init__(self, onewire):
        self.ow = onewire
        self.buf = bytearray(9)
        self.power = 1 # strong power supply by default
        self.powerpin = None

    def powermode(self, powerpin=None):
        if self.powerpin is not None: # deassert strong pull-up
            self.powerpin(0)
        self.ow.writebyte(self.ow.CMD_SKIPROM)
        self.ow.writebyte(CMD_RDPOWER)
        self.power = self.ow.readbit()
        if powerpin is not None:
            assert type(powerpin) is Pin, "Parameter must be a Pin object"
            self.powerpin = powerpin
            self.powerpin.init(mode=Pin.OUT, value=0)
        return self.power

    def scan(self):
        return [rom for rom in self.ow.scan() if rom[0] in (0x10, 0x22, 0x28)]

    def convert_temp(self, rom=None):
        self.ow.reset()
        if rom is None:
            self.ow.writebyte(self.ow.CMD_SKIPROM)
        else:
            self.ow.select_rom(rom)
        self.ow.writebyte(CMD_CONVERT, self.powerpin)

    def read_scratch(self, rom):
        if self.powerpin is not None: # deassert strong pull-up
            self.powerpin(0)
        self.ow.reset()
        self.ow.select_rom(rom)
        self.ow.writebyte(CMD_RDSCRATCH)
        self.ow.readinto(self.buf)
        assert self.ow.crc8(self.buf) == 0, 'CRC error'
        return self.buf

    def write_scratch(self, rom, buf):
        if self.powerpin is not None: # deassert strong pull-up
            self.powerpin(0)
        self.ow.reset()
        self.ow.select_rom(rom)
        self.ow.writebyte(CMD_WRSCRATCH)
        self.ow.write(buf)

    def read_temp(self, rom):
        try:
            buf = self.read_scratch(rom)
            if rom[0] == 0x10:
                if buf[1]:
                    t = buf[0] >> 1 | 0x80
                    t = -((~t + 1) & 0xff)
                else:
                    t = buf[0] >> 1
                return t - 0.25 + (buf[7] - buf[6]) / buf[7]
            elif rom[0] in (0x22, 0x28):
                t = buf[1] << 8 | buf[0]
                if t & 0x8000: # sign bit set
                    t = -((t ^ 0xffff) + 1)
                return t / 16
            else:
                return None
        except AssertionError:
            return None
