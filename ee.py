
from opcua import Server
from random import randint
import time


server = Server()
url = "opc.tcp://192.168.0.155:4840"
server.set_endpoint(url)
name = "Rocket_Systems_OPCUA_Simulation_Server"
add_space = server.register_namespace(name)

node = server.get_objects_node()
param = node.add_object(add_space, "Parameters")

temp = param.add_variable(add_space, "Temperature", 0)
press = param.add_variable(add_space, "Pressure", 0)
temp.set_writable()
press.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
    temperature = randint(10, 50)
    pressure = randint(200, 999)
    print(temperature, pressure)

    temp.set_value(temperature)
    press.set_value(pressure)

    time.sleep(3)