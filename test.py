from PiRelay8 import Relay
import time

r1 = Relay("RELAY1")
r2 = Relay("RELAY2")
r3 = Relay("RELAY3")
r4 = Relay("RELAY4")
r5 = Relay("RELAY5")
r6 = Relay("RELAY6")
r7 = Relay("RELAY7")
r8 = Relay("RELAY8")


r1.off()
r2.off()
r3.off()
r4.off()
r5.off()
r6.off()
r7.off()
r8.off()

r1.on()
time.sleep(0.5)
r1.off()
time.sleep(0.5)

r2.on()
time.sleep(0.5)
r2.off()
time.sleep(0.5)

r3.on()
time.sleep(0.5)
r3.off()
time.sleep(0.5)

r4.on()
time.sleep(0.5)
r4.off()
time.sleep(0.5)

r5.on()
time.sleep(0.5)
r5.off()
time.sleep(0.5)

r6.on()
time.sleep(0.5)
r6.off()
time.sleep(0.5)

r7.on()
time.sleep(0.5)
r7.off()
time.sleep(0.5)

r8.on()
time.sleep(0.5)
r8.off()
time.sleep(0.5)
