from dataclasses import dataclass, replace
#from time import sleep

@dataclass 
class TruckPosition: 
    x: float 
    y: float

@dataclass 
class TruckPositionDelta: 
    truck_id: int 
    delta_x: float 
    delta_y: float 
    
class Subscriber: 
    def __init__(self, server): 
        self.server = server 
        self.subscriptions = {}
        self.updates = {}
        
    def subscribe_to_truck(self, truck_id, client_id): 
        # self.subscriptions[client_id] = truck_id
        if client_id not in self.subscriptions: 
            self.subscriptions[client_id] = [truck_id]
        else:
            self.subscriptions[client_id].append(truck_id)
            # print("debug:", self.subscriptions, client_id, truck_id) 
        
        pos = self.server.subscribe_to_truck(truck_id) 
        return replace(pos) 
    
    def process_update(self, delta): 
        client_ids = []
        for cid, tid in self.subscriptions.items(): 
            if delta.truck_id in tid: 
                client_ids.append(cid) 
        for client_id in client_ids: 
            if client_id not in self.updates: 
                self.updates[client_id] = [] 
            self.updates[client_id].append(delta) 
            
    def get_updates(self, client_id): 
        updates = self.updates.get(client_id, []) 
        self.updates[client_id] = []
        return updates 
    
class Server: 
    def __init__(self): 
        self.registered_trucks = set() 
        self.current_pos = {}
        
    def subscribe_to_truck(self, truck_id): 
        self.registered_trucks.add(truck_id) 
        return replace(self.current_pos[truck_id]) 
    
    def add_position(self, truck_id, pos): 
        self.current_pos[truck_id] = pos 
        
    def on_update(self, subscriber, delta): 
        if delta.truck_id in self.registered_trucks: 
            subscriber.process_update(delta) 
        pos = self.current_pos[delta.truck_id] 
        pos.x += delta.delta_x 
        pos.y += delta.delta_y 
        
class Client: 
    def __init__(self, client_id, subscriber): 
        self.client_id = client_id 
        self.subscriber = subscriber 
        
    def subscribe(self, truck_id): 
        pos = self.subscriber.subscribe_to_truck(truck_id, self.client_id) 
        print(f"S {self.client_id} {truck_id} {pos.x:g} {pos.y:g}") 
        
    def request_update(self): 
        updates = self.subscriber.get_updates(self.client_id) 
        for delta in updates: 
            print(f"U {self.client_id} {delta.truck_id} {delta.delta_x:g} {delta.delta_y:g}") 
            
if __name__ == "__main__": 
    import sys 
    read_line = lambda: sys.stdin.readline().split() 
    server = Server() 
    subscriber = Subscriber(server) 
    clients = [] 
    num_trucks = int(read_line()[0]) 
    
    for i in range(num_trucks): 
        line = read_line() 
        x = float(line[0]) 
        y = float(line[1]) 
        server.add_position(i, TruckPosition(x, y))
        
    while True: 
        line = read_line()
        # sleep(0.1) 
        if len(line) == 0: 
            break 
        elif line[0] == "S": 
            client_id = int(line[1]) 
            truck_id = int(line[2]) 
            
            if client_id >= len(clients): 
                clients.append(Client(client_id, subscriber)) 
            clients[client_id].subscribe(truck_id) 
            
        elif line[0] == "U": 
            truck_id = int(line[1]) 
            dx = float(line[2]) 
            dy = float(line[3]) 
            
            server.on_update(subscriber, TruckPositionDelta(truck_id, dx, dy)) 
            
        elif line[0] == "R": 
            client_id = int(line[1]) 
            clients[client_id].request_update()
        
        else:
            raise Exception("Invalid input")
