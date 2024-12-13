from transport import Vehicle
from transport import func

class Train(Vehicle.Vehicle):
    def __init__(self, capacity:int, number_of_cars:int, info):
        self.number_of_cars = number_of_cars
        super().__init__(capacity)
        super().__init__(info) = {'id':self.vehicle_id,'capacity':self.capacity, 'current_load': 0, 'client_list':self.clients_list, 'number_of_cars':self.number_of_cars}
        func.add_to_transport_list(info)
        
    def __str__(self):
        return super().__str__()+"\nКоличество вагонов: "+str(self.number_of_cars)