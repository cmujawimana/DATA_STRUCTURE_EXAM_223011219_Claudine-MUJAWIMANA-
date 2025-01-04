from datetime import datetime

class MaintenanceRequest:
    def __init__(self, request_id, description, priority, location, requester):
        self.request_id = request_id
        self.description = description
        self.priority = self._validate_priority(priority)
        self.location = location
        self.requester = requester
        self.timestamp = None
        self.status = "Pending"

    def _validate_priority(self, priority):
        valid_priorities = {"High": 3, "Medium": 2, "Low": 1}
        if priority not in valid_priorities:
            raise ValueError("Priority must be High, Medium, or Low")
        return priority

    def __str__(self):
        return f"[ID: {self.request_id}, Priority: {self.priority}, Location: {self.location}, Requester: {self.requester}, Status: {self.status}]"

class MaintenanceStack:
    def __init__(self):
        self.high_priority = []
        self.medium_priority = []
        self.low_priority = []
        self.size = 0
        self.max_size = 1000

    def push(self, request):
        if self.size >= self.max_size:
            raise Exception("Stack overflow: Maximum capacity reached")
        request.timestamp = datetime.now()
        if request.priority == "High":
            self.high_priority.append(request)
        elif request.priority == "Medium":
            self.medium_priority.append(request)
        else:
            self.low_priority.append(request)
        self.size += 1
        print(f"PUSH: Added request {request.request_id} with priority {request.priority}")

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow: No maintenance requests available")
        self.size -= 1
        if self.high_priority:
            request = self.high_priority.pop()
        elif self.medium_priority:
            request = self.medium_priority.pop()
        else:
            request = self.low_priority.pop()
        print(f"POP: Removed request {request.request_id} with priority {request.priority}")
        return request

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        if self.high_priority:
            request = self.high_priority[-1]
        elif self.medium_priority:
            request = self.medium_priority[-1]
        else:
            request = self.low_priority[-1]
        print(f"PEEK: Viewing request {request.request_id} with priority {request.priority}")
        return request

    def is_empty(self):
        empty = self.size == 0
        print(f"IS_EMPTY: Stack is {'empty' if empty else 'not empty'}")
        return empty

    def get_priority_requests(self, priority):
        if priority == "High":
            requests = self.high_priority.copy()
        elif priority == "Medium":
            requests = self.medium_priority.copy()
        elif priority == "Low":
            requests = self.low_priority.copy()
        else:
            raise ValueError("Priority must be High, Medium, or Low")
        print(f"GET_PRIORITY_REQUESTS: Retrieved {len(requests)} requests with priority {priority}")
        return requests

    def get_all_requests(self):
        all_requests = self.high_priority + self.medium_priority + self.low_priority
        print(f"GET_ALL_REQUESTS: Retrieved {len(all_requests)} total requests")
        return all_requests
def test_maintenance_stack():
    stack = MaintenanceStack()
    requests = [
        MaintenanceRequest("MR001", "Fix broken elevator", "High", "Building A", "John"),
        MaintenanceRequest("MR002", "Clean air vents", "Medium", "Building B", "Jane"),
        MaintenanceRequest("MR003", "Paint walls", "Low", "Building C", "Bob"),
        MaintenanceRequest("MR004", "Repair water leak", "High", "Building D", "Alice")
    ]
    for request in requests:
        stack.push(request)
    stack.peek()
    while not stack.is_empty():
        processed_request = stack.pop()
        processed_request.status = "Completed"
        print("Processed request:", processed_request)

if __name__ == "__main__":
    test_maintenance_stack()
