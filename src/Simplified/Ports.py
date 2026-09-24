from pybricks.iodevices import PUPDevice
from uerrno import ENODEV
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Port
from pybricks.tools import wait

hub = PrimeHub()

# Dictionary of device identifiers along with their name.
device_names = {
    48: "SPIKE Medium Angular Motor",
    49: "SPIKE Large Angular Motor",
    61: "SPIKE Color Sensor",
    62: "SPIKE Ultrasonic Sensor",
    63: "SPIKE Force Sensor"
}

# Make a list of known ports.
ports = [Port.A, Port.B, Port.C, Port.D, Port.E, Port.F]

Color1 : ColorSensor | None = None
Distance1 : UltrasonicSensor | None = None

print("Available ports", ports)

# Go through all available ports.
for port in ports:
    print("Searching on port", port)

    # Try to get the device, if it is attached.
    try:
        device = PUPDevice(port)
        print("Device found on port", port)
    except OSError as ex:
        if ex.args[0] == ENODEV:
            # No device found on this port.
            print(port, ": ---")
            continue
        else:
            raise

    # Get the device id
    id = int(device.info()["id"])

    # Look up the name.
    try:
        print(port, ":", device_names[int(id)])
    except KeyError:
        print(port, ":", "Unknown device with ID", id)

    if (id == 61):
        Color1 = ColorSensor(port)
        print("Color is: " + str(Color1.hsv().h) + ", " + str(Color1.hsv().s) + ", " + str(Color1.hsv().v))
    elif (id == 49 or id == 48):
        print("Starting motor...")
        Motor(port).run(100)
        print("Motor started")
    elif (id == 62):
        Distance1 = UltrasonicSensor(port)
        print("Distance is:", Distance1.distance())

if Color1 != None:
    Color1.lights.off()

LightsOn = False
MotorsOn = False
while (True):
    pressed = hub.buttons.pressed()
    if (Button.LEFT in pressed):
        if LightsOn:
            if (Color1 != None):
                Color1.lights.off()
            if (Distance1 != None):
                Distance1.lights.off()
        else:
            if (Color1 != None):
                Color1.lights.on(100)
            if (Distance1 != None):
                Distance1.lights.on(100)
        LightsOn = not LightsOn
        while Button.LEFT in hub.buttons.pressed():
            wait(10)
    if (Button.RIGHT in pressed):
        if MotorsOn:
            pass
        else:
            pass
        MotorsOn = not MotorsOn
        while Button.RIGHT in hub.buttons.pressed():
            wait(10)
    if (Color1 != None and Distance1 != None):
        hub.light.on(Color1.hsv())
        if not LightsOn:
            Color1.lights.off()
            Distance1.lights.off()
        else:
            Color1.lights.on(100)
            Distance1.lights.on(100)
        hub.display.number((Distance1.distance() / 4) - 110)
    wait(10)