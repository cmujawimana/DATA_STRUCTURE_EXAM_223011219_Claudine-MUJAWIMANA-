from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class MaintenanceRequest:
    request_id: str
    priority: int  
    description: str
    building: str
    floor: str
    status: str
    timestamp: datetime
    requester: str

class Node:
    def __init__(self, request: MaintenanceRequest):
        self.request = request
        self.next = None

class MaintenanceLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_request(self, request: MaintenanceRequest) -> None:
        new_node = Node(request)
        self.size += 1
        if self.head is None or request.priority < self.head.request.priority:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while (current.next is not None and 
               current.next.request.priority <= request.priority):
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def remove_request(self, request_id: str) -> Optional[MaintenanceRequest]:
        if self.head is None:
            return None

        if self.head.request.request_id == request_id:
            removed_request = self.head.request
            self.head = self.head.next
            self.size -= 1
            return removed_request

        current = self.head
        while current.next is not None:
            if current.next.request.request_id == request_id:
                removed_request = current.next.request
                current.next = current.next.next
                self.size -= 1
                return removed_request
            current = current.next

        return None

    def update_status(self, request_id: str, new_status: str) -> bool:
        current = self.head
        while current is not None:
            if current.request.request_id == request_id:
                current.request.status = new_status
                return True
            current = current.next
        return False

    def display_all_requests(self) -> None:
        if self.head is None:
            print("Empty List: None")
            return

        print("\nMaintenance Request Linked List Structure:")
        print("HEAD", end="")
        current = self.head
        while current is not None:
            print(" -> [", end="")
            req = current.request
            print(f"ID: {req.request_id} | "
                  f"Priority: {req.priority} | "
                  f"Building: {req.building} | "
                  f"Status: {req.status}]", end="")
            current = current.next
        print(" -> None")
        print("\nDetailed Request Information:")
        current = self.head
        node_num = 1
        while current is not None:
            req = current.request
            print(f"\nNode {node_num}:")
            print(f"  ID: {req.request_id}")
            print(f"  Priority: {req.priority}")
            print(f"  Description: {req.description}")
            print(f"  Location: Building {req.building}, Floor {req.floor}")
            print(f"  Status: {req.status}")
            print(f"  Requester: {req.requester}")
            print(f"  Timestamp: {req.timestamp}")
            print(f"  Next -> {'None' if current.next is None else current.next.request.request_id}")
            print("-" * 50)
            current = current.next
            node_num += 1

def main():
    maintenance_system = MaintenanceLinkedList()
    requests = [
        MaintenanceRequest(
            request_id="REQ001",
            priority=1,
            description="Water leak in ceiling",
            building="A",
            floor="3",
            status="Pending",
            timestamp=datetime.now(),
            requester="John Smith"
        ),
        MaintenanceRequest(
            request_id="REQ002",
            priority=3,
            description="Light bulb replacement",
            building="B",
            floor="2",
            status="Pending",
            timestamp=datetime.now(),
            requester="Jane Doe"
        ),
        MaintenanceRequest(
            request_id="REQ003",
            priority=1,
            description="Broken elevator",
            building="A",
            floor="1",
            status="Pending",
            timestamp=datetime.now(),
            requester="Mike Johnson"
        )
    ]
    print("Adding maintenance requests...")
    for request in requests:
        maintenance_system.add_request(request)
    maintenance_system.display_all_requests()
    print("\nUpdating status of REQ001 to 'In Progress'...")
    maintenance_system.update_status("REQ001", "In Progress")
    maintenance_system.display_all_requests()
    print("\nRemoving request REQ002...")
    maintenance_system.remove_request("REQ002")
    maintenance_system.display_all_requests()

if __name__ == "__main__":
    main()