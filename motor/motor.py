import RPi.GPIO as GPIO

# motor_EN_A: Pin7
# motor_A: Pin8, Pin10

MOTOR_A_EN = 7
MOTOR_A_PIN1 = 8
MOTOR_A_PIN2 = 10

pwm_a = 0


def motorStop():
    GPIO.output(MOTOR_A_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_A_PIN2, GPIO.LOW)
    GPIO.output(MOTOR_A_EN, GPIO.LOW)


def setup():
    global pwm_a
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MOTOR_A_EN, GPIO.OUT)
    GPIO.setup(MOTOR_A_PIN1, GPIO.OUT)
    GPIO.setup(MOTOR_A_PIN2, GPIO.OUT)

    motorStop()
    pwm_a = GPIO.PWM(MOTOR_A_EN, 1000)


def turn_right():
    global pwm_a
    GPIO.output(MOTOR_A_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR_A_PIN2, GPIO.LOW)
    pwm_a.start(100)
    pwm_a.ChangeDutyCycle(100)  # chose speed as 100


def turn_left():
    global pwm_a
    GPIO.output(MOTOR_A_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_A_PIN2, GPIO.HIGH)
    pwm_a.start(100)
    pwm_a.ChangeDutyCycle(100)  # chose speed as 100


def destroy():
    motorStop()
    GPIO.cleanup()
