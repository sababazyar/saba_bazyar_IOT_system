
'''

APM : 
lotfan print() ro bartaye tamame function ha tamame command ha ezafe konid
moafagh bashid


bale chashm
ezafe kardam


APM:
besiar awli ahsant
hala mesle create_devcie , create_sensor ham besazid dakhemele khode AminPanel

'''


import numpy as np

class Sensor:
    def init(self, name, group, unit, pin):
        self.name = name
        self.group = group
        self.pin = pin 
        self.unit = unit 
        self.current_value = None
        print(f'Sensor {self.name} is ready in group {self.group} with unit {self.unit} on pin {self.pin}')

 def read_sensor(self):
        self.current_value = np.random.uniform(20, 25)
        print(f'sensor {self.name} read value: {self.current_value} {self.unit}')
        return self.current_value

class Device:
    def init(self, topic):
        self.topic = topic
        self.topic_list = topic.split('/')
        self.location = self.topic_list[0]
        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.name = self.topic_list[3]
        self.status = 'off'  
        print(f'device {self.name} is ready in {self.group} as {self.device_type}')

    def turn_off(self):
        self.status = 'off'
        print(f'device {self.name} turned off')

    def turn_on(self):
        self.status = 'on'
        print(f'device {self.name} turned on')

    def get_status(self):
        print(f'device {self.name} status is: {self.status}')
        return self.status

device = Device('home/living_room/light/ceiling')
device.turn_on()
print(f'Device {device.name} status: {device.get_status()}')

class AdminPanel:
    def init(self):
        self.groups = {}
        print('admin panel is ready')

    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'group {group_name} is created')
        else:
            print('your group already exists')

    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f'device {device.name} added to group {group_name}')
        else:
            print('your group is not created')

    def create_device(self, group_name, device_type, name):
        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_device = Device(topic)
            self.add_device_to_group(group_name, new_device)
            print(f'device {new_device.name} is created')
        else:
            print('your group is not created')

    def create_multiple_devices(self, group_name, device_type, number_of_devices):
        if group_name in self.groups:
            for i in range(1, number_of_devices + 1):  
                device_name = f'{device_type}{i}'
                topic = f'home/{group_name}/{device_type}/{device_name}'
                new_device = Device(topic)
                self.add_device_to_group(group_name, new_device)
                print(f'device {new_device.name} is created')
        else:
            print('your group is not created')

    def get_devices_in_group(self, group_name):
        if group_name in self.groups:
            devices = self.groups[group_name]
            print(f'devices in group {group_name} are : {[device.name for device in devices]}')
            return devices 
        else:
            print('your group is not created')
            return []

    def turn_on_all_in_group(self, group_name):
        devices = self.get_devices_in_group(group_name)
        for device in devices:
            device.turn_on()
        else:
            print('no devices found in group')

    def turn_off_all_in_group(self, group_name):
        devices = self.get_devices_in_group(group_name)
        if devices:
            for device in devices:
                device.turn_off()
        else:
            print('no devices found in the group')
            
    def turn_on_all_devices(self):
       print('turning on all devices')
       for group in self.groups.values():
            for device in group:
                device.turn_on()
                print(f'device {device.name} has been turned on') 
    def turn_off_all_devices(self):
        print('turning off all devices')
        for group in self.groups.values():
            for device in group:
                device.turn_off()
                print(f'device {device.name} has been turned off')

    def get_status_in_group(self, group_name):
        print(f'getting status for all devices in group: {group_name}')
        if group_name in self.groups:
            devices = self.get_devices_in_group(group_name)
            for device in devices:
             print(f'device {device.name} is : {device.get_status()}')
        else:
         print('your group is not created')

    def get_status_in_device_type(self, device_type):
        print(f'getting status for all devices of type : {device_type}')
        found = False 
        for group_name, devices in self.groups.items():
             for device in devices:
                 if device.device_type == device_type:
                      print(f'{device.name} in {group_name} is {device.get_status()}')
                      found = True
        if not found:
            print(f'No devices of type {device_type} found')



#def create_sensor...
