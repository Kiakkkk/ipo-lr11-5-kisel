from transport import Client, Vehicle 

class TransportCompany:
    def __init__(self, name:str):
        self.name = name
        self.vehicles = list()
        self.clients = list()
        
    def add_vehicle(self, vehicle:Vehicle.Vehicle):
        self.vehicles.append(vehicle)
        self.vehicles.sort(key=lambda vehicle: vehicle.capacity, reverse=True)
        print("Добавлено транспортное средство: ", vehicle.vehicle_id)

    def list_vehicles(self):
        return self.vehicles
    
    def add_client(self,client:Client.Client):
        self.clients.append(client)
        vip_cargo = list()
        cargo = list()
        for client in self.clients:
            if client.is_vip:
                vip_cargo.append([client, client.cargo_weight])
            else:
                cargo.append([client, client.cargo_weight])
        sorted(vip_cargo)
        sorted(cargo)
        self.clients = vip_cargo + cargo
        print("Добавлен клиент")

    def optimize_cargo_distribution(self):
        for client in self.clients:
            for transp in self.vehicles:
                if (transp.current_load + client.cargo_weight <= transp.capacity):
                    transp.load_cargo(client)
                    print(f"Груз клиента {client.name} загружен в транспорт {transp.vehicle_id}")
                    break

            '''for client in vip_cargo:
                transp.load_cargo(client)
                print(f"Груз клиента {client.name} загружен в транспорт {transp.vehicle_id}")
            for client in cargo:
                transp.load_cargo(client)
                print(f"Груз клиента {client.name} загружен в транспорт {transp.vehicle_id}")
'''
        


