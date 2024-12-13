from transport import Vehicle
from transport import func

class Airplane(Vehicle.Vehicle):
    def __init__(self, capacity:int, max_altitude:int):
        super().__init__(capacity)
        self.max_altitude = max_altitude
        info = {'id':self.vehicle_id,'capacity':self.capacity, 'current_load': 0, 'client_list':self.clients_list, 'max_altitude':self.max_altitude}
        func.add_to_transport_list(info)
    def __str__(self):
        return super().__str__()+"\nМаксимальная высота полёта: "+str(self.max_altitude)