import machine
import time

CENTER_NS = 1500000
FORWARD_NS = 2000000
REVERSE_NS = 1000000

PWM_FREQ = 50 #20ms Period

pLed = machine.Pin('D13', machine.Pin.OUT)
pAuto = machine.Pin('D4', machine.Pin.OUT)
pMotorLeft = machine.Pin('D2', machine.Pin.OUT)
pMotorRight = machine.Pin('D3', machine.Pin.OUT)
pInputLeft = machine.Pin('D11', machine.Pin.IN)
pInputRight = machine.Pin('D12', machine.Pin.IN)
pMotorFault = machine.Pin('D5', machine.Pin.IN)
pEngineKill = machine.Pin('D41', machine.Pin.OUT)
pEngineStart = machine.Pin('D40', machine.Pin.OUT)
pActuator3Control = machine.Pin('D22', machine.Pin.IN)
pActuator3Motor = machine.Pin('D23', machine.Pin.OUT)
pActuator4Control = machine.Pin('D36', machine.Pin.IN)
pActuator4Motor = machine.Pin('D37', machine.Pin.OUT)

# Flash Led
def read_pwm_inputs(t):
    machine.time_pulse_us(pMotorRight, 1, 1000000)

ioTimer = machine.Timer(-1)
ioTimer.init(period=10, mode=machine.Timer.PERIODIC, callback=read_pwm_inputs)

# Turn on Auto Mode
pAuto.on()

pwmL = machine.PWM(pMotorLeft, freq=PWM_FREQ, duty_ns=CENTER_NS )
pwmR = machine.PWM(pMotorLeft, freq=PWM_FREQ, duty_ns=CENTER_NS )

