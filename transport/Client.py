from transport import func

class Client:#класс клиента
    
    def __init__(self, name:str, cargo_weight: int, is_vip: bool = False): 
        self.name = name#имя
        self.cargo_weight = cargo_weight#вес груза
        self.is_vip = is_vip#вип-статус
        info={'name':self.name, 'cargo_weight':self.cargo_weight, 'is_vip':self.is_vip}
        func.add_to_client_list(info)

    