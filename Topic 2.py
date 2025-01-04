class MaintenanceRequest:
    def __init__(self, request_id, apartment_no, description, priority, status="Pending"):
        self.request_id = request_id
        self.apartment_no = apartment_no
        self.description = description
        self.priority = priority
        self.status = status
        self.creation_date = datetime.now()

    def __str__(self):
        return f"Request #{self.request_id} - Apt {self.apartment_no} - {self.description} - Priority: {self.priority} - Status: {self.status}"
class MaintenanceSystem:
    def __init__(self):
        self.requests = []
        self.current_id = 1000
    def add_request(self, apartment_no, description, priority):  
        request = MaintenanceRequest(self.current_id, apartment_no, description, priority)
        self.requests.append(request)
        self.current_id += 1
        return request.request_id

    def get_request(self, request_id):
        for request in self.requests:
            if request.request_id == request_id:
                return request
        return None

    def update_status(self, request_id, new_status):
        request = self.get_request(request_id)
        if request:
            request.status = new_status
            return True
        return False

    def get_pending_requests(self):
        return [request for request in self.requests if request.status == "Pending"]
    def get_requests_by_priority(self, priority):
        return [request for request in self.requests if request.priority == priority]
    def get_requests_by_apartment(self, apartment_no):
        return [request for request in self.requests if request.apartment_no == apartment_no]

    def remove_request(self, request_id):
        for i, request in enumerate(self.requests):
            if request.request_id == request_id:
                return self.requests.pop(i)
        return None

    def get_all_requests(self):
        return self.requests
    def get_requests_by_status(self, status):
        return [request for request in self.requests if request.status == status]
    def print_all_requests(self):
        if not self.requests:
            print("No maintenance requests in the system.")
            return
        for request in self.requests:
            print(request)

if __name__ == "__main__":
    from datetime import datetime
    system = MaintenanceSystem()
    request1_id = system.add_request("101", "Leaking faucet in bathroom", "Medium")
    request2_id = system.add_request("203", "AC not working", "High")
    request3_id = system.add_request("101", "Light bulb replacement", "Low")
    print("\nAll Maintenance Requests:")
    system.print_all_requests()
    system.update_status(request1_id, "In Progress")
    print("\nHigh Priority Requests:")
    high_priority = system.get_requests_by_priority("High")
    for request in high_priority:
        print(request)
    print("\nRequests for Apartment 101:")
    apt_requests = system.get_requests_by_apartment("101")
    for request in apt_requests:
        print(request)