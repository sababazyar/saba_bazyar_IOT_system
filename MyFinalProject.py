
'''

APM : 
lotfan print() ro bartaye tamame function ha tamame command ha ezafe konid
moafagh bashid 

bale chashm
ezafe kardam


APM:
besiar awli ahsant
hala mesle create_devcie , create_sensor ham besazid dakhemele khode AminPanel


chash hatman
as tabe create_sensor ta tabe get_data_from_sensor_in_group ro neveshtam llotfa molaheze befarmaeed
fekr konam hame tabe hayi ke farmode bodin ro ezafe kardam faghat task3 monde


APM:
salam
tabeh haye  turn_on_all_in_group and  turn_off_all_in_group print nadare ke bayad print ezafe beshe
besiar awli faghat tabeye akahretono mamnoon misham tozih bedid


salam, vaght bekheir
chash, ezafe kardam
bale hatman, in tebe gharar shod ke biad data haro az hame sensor hayi ke toye ye group moshakhasi hastan peyda kone o barresi kone.
avalesh ke miad va vorody ke esm ye group hast ro migire bad ba if baresi mikone ke vojod dare ya na 
agar vojod dasht tamam dastgah hye mojodi ke as no sensor ha hastan ba isinstance peyda mikone
yani yejorayi engar list device haye mojod toye ye group ro barresi mikone ta faghat sensor haro joda kone chon ma faghat donbal data haye sensor ha hastim
badesh vaghti ke sensor haro peyda kard ye halghe roye har sensor ejra mishe va data ha khonde mishan va ba esm sensor va group khodeshon print mishan
hala agar group kolan vojod nadashte bashe payam 'group dosnt exist' print mishe va agar faghat sensor haye on group peyda nashe payam 'no sensors found...' print mishe


APM:
besiar awli ahsant 
shoam kamelan motvajeye mozoye class va object shodid

kheyli mamnonam
task 3 ro ham anjam dadam, do tabe hazf device va hazf sesor az ye group ro neveshtam.
lotfan molaheze befarmaid ke agar iradi nadasht baraton toye telegram link ro ersal konam


APM:
salam arz shdo besiar awli
fght ghabl az hazf bayad check kone esme sensor -- aya sensore ya na age sensor bod hazf kone ag devcie bod beeg device (error)
hamchenin baraye device

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
        print(f' turning on all devices in group {group_name}')
        devices = self.get_devices_in_group(group_name)
        if devices:
            for device in devices:
                device.turn_on()
                print(f'device {device.name} turned on')
        else:
            print(f'no devices found in group {group_name}')

    def turn_off_all_in_group(self, group_name):
        print(f'turning off all devices in group {group_name}')
        devices = self.get_devices_in_group(group_name)
        if devices:
            for device in devices:
                device.turn_off()
                print(f'device {device.name} turned off')
        else:
            print(f'no devices found in group {group_name}')

            
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
            print(f'no devices of type {device_type} found')
    def create_sensor(self, group_name, sensor_name):
        print(f'trying to create a sensor with name: {sensor_name} in group: {group_name}')
        if group_name in self.groups:
             topic = f'home/{group_name}/sensor/{sensor_name}'
             print(f'creating sensor topic: {topic}')
             new_sensor = Sensor(sensor_name)
             self.groups[group_name].append(new_sensor)
             print(f'sensor {new_sensor.name} is created in {group_name}')
        else:
             print('group doesnt exist')
            
    def add_sensor_in_group(self, group_name, sensor):
        print(f'trying to add sensor: {sensor.name} to group: {group_name}')
        if group_name in self.groups:
            self.groups[group_name].append(sensor) 
            print(f'sensor {sensor.name} added to group {group_name}')
       else:
           print('group doesnt exist')

    def add_device_in_group(self, group_name, device):
        print(f'trying to add device: {device.name} to group: {group_name}')
        if group_name in self.groups:
            self.groups[group_name].append(device)   
            print(f'device {device.name} added to group {group_name}')
       else:
           print('group does not exist')
          
   def get_data_from_sensor_in_group(self, group_name):
       print(f'trying to get data from sensors in group: {group_name}')
       if group_name in self.groups:
           sensors = [device for device in self.groups[group_name] if isinstance(device, Sensor)]
           if sensors:
               for sensor in sensors:
                   data = sensor.read_sensor()
                   print(f'data from {sensor.name} in {group_name}: {data}')
           else:
               print(f'no sensors found in group {group_name}')
       else:
           print('group doesnt exist')

#---Task3---


#1.tabe hazf ye sensor az ye group-------
    def remove_sensor_from_group(groups, group_name, sensor_name):
        print(f'trying to remove sensor {sensor_name} from {group_name} group')
        if group_name in groups:
            if isinstance (sensor,sensor):
                if sensor_name in groups[group_name]:
                    groups[group_name].remove(sensor_name)
                    print(f'sensor {sensor_name} removed from group {group_name}')
                else:
                    print(f'sensor {sensor_name} is not found in group {group_name}')
            else:
                print(f'{sensor_name} is not a sensor instance')
        else:
           print('group doesnt exist')


#2.tabe hazf yek dastgah (device)--------
    def remove_device(devices, device_name):
        print(f'trying to remove {device_name}')
        if device_name in devices:
            devices.remove(device_name)
            print(f'device {device_name} is removed')
    else:
        print(f'device {device_name} is not found')


