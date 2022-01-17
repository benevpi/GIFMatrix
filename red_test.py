import sacn
import time

ip_address = "192.168.1.81"

num_leds = 256

#connect to matrix
sender = sacn.sACNsender(fps=40) 
sender.start()  # start the sending thread
sender.activate_output(1)  
sender[1].destination = ip_address
sender.activate_output(2)
sender[2].destination = ip_address


data = []
for i in range(num_leds):
	data.append(10)
	data.append(0)
	data.append(0)

def send_two_universes(data, sender):
    sender[1].dmx_data = data[:510]
    sender[2].dmx_data = data[510:]
	
send_two_universes(data, sender)
	
time.sleep(5)
sender.stop()