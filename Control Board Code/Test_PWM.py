import machine
import time

CENTER_NS = 1500000
FORWARD_NS = 2000000
REVERSE_NS = 1000000

PWM_FREQ = 50 #20ms Period
PWM_CENTER_NS = 500000

pLed = machine.Pin('D13', machine.Pin.OUT)
pMotorLeft = machine.Pin('D29', machine.Pin.OUT)
pInputLeft = machine.Pin('D33', machine.Pin.IN)

class PWMInputRead:
    def __init__(self, pin: machine.Pin) -> None:
        self.tick_start = 0
        self.tick_end = 0
        self.pin = pin
        self.delta_us = 0
        self.pin.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=self.callback)
        return
    
    def callback(self, p) -> None:
        if p.value():
            self.tick_start = time.ticks_us()
            return
        self.tick_end = time.ticks_us()
        self.delta_us = time.ticks_diff(self.tick_end, self.tick_start)
        return

class PWMPairs:
    def __init__(self, input: machine.Pin, output: machine.Pin) -> None:
        self.input = input
        self.output = output
        self.pwm_out = machine.PWM(self.output, freq=PWM_FREQ, duty_ns=CENTER_NS)
        self.pwm_in = PWMInputRead(self.input)
        self.read_error_us = 0
        return
    
    def calibrate_input(self) -> None:
        self.pwm_out.duty_ns(CENTER_NS)
        time.sleep(0.1)
        self.read_error_us = CENTER_NS/1000 - self.pwm_in.delta_us
        return
    
    def in_percent(self) -> float:
        return float(((((self.pwm_in.delta_us + self.read_error_us) * 1000) - CENTER_NS)/ PWM_CENTER_NS) * 100.0)
    
    def out_percent(self, percent: float) -> None:
        self.pwm_out.duty_ns(int(percent / 100.0 * PWM_CENTER_NS) + CENTER_NS)
        return

pair = PWMPairs(pInputLeft, pMotorLeft)
pair.calibrate_input()
print(pair.read_error_us)
print(pair.in_percent())

