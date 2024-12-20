from uuid import uuid4 #библиотека для id
from transport import Client
from transport import func

class Vehicle:
    def __init__(self, capacity:int): #функция добавляющая аргументы при создании экземпляра класса
        self.vehicle_id = str(uuid4()).split('-')[0]#id транспорта
        self.capacity = capacity#грузоподъёмность
        self.current_load = 0#загруженность
        self.clients_list = list()#список клиентов чьи грузы загружены
        self.add_to_transport_list()
        
    def add_to_transport_list(self):  # метод для добавления информации о транспортном средстве
        info = {
            'id': self.vehicle_id,
            'capacity': self.capacity,
            'current_load': self.current_load,
            'client_list': self.clients_list
        }
        func.add_to_transport_list(info)

    def load_cargo(self, client:Client.Client):#функция загружающая груз на транспортное средство
        self.current_load += client.cargo_weight 

    def __str__(self):#магический метод
        data = "ID: " + self.vehicle_id + "\nГрузоподъемность: " + str(self.capacity) + "\nТекущая загрузка: " + str(self.current_load)
        return data