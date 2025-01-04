import time
from dataclasses import dataclass
from typing import List

@dataclass
class MaintenanceRequest:
    id: str
    priority: int  
    description: str
    building: str
    floor: str
    timestamp: float

class MaintenanceHeap:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.heap: List[MaintenanceRequest] = []
        
    def size(self) -> int:
        return len(self.heap)
    
    def is_empty(self) -> bool:
        return len(self.heap) == 0
    
    def is_full(self) -> bool:
        return len(self.heap) >= self.max_size
    
    def parent_index(self, index: int) -> int:
        return (index - 1) // 2
    
    def left_child_index(self, index: int) -> int:
        return 2 * index + 1
    
    def right_child_index(self, index: int) -> int:
        return 2 * index + 2
        
    def swap(self, index1: int, index2: int):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
    def insert(self, request: MaintenanceRequest) -> bool:
        if self.is_full():
            return False
            
        self.heap.append(request)
        self._bubble_up(len(self.heap) - 1)
        return True
        
    def _bubble_up(self, index: int):
        while index > 0:
            parent_idx = self.parent_index(index)
            if self.heap[index].priority < self.heap[parent_idx].priority:
                self.swap(index, parent_idx)
                index = parent_idx
            else:
                break
                
    def get_highest_priority(self) -> MaintenanceRequest:
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]
        
    def extract_highest_priority(self) -> MaintenanceRequest:
        if self.is_empty():
            raise IndexError("Heap is empty")
            
        if len(self.heap) == 1:
            return self.heap.pop()
            
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
            
        return root
        
    def _bubble_down(self, index: int):
        while True:
            min_index = index
            left = self.left_child_index(index)
            right = self.right_child_index(index)
            if left < len(self.heap) and self.heap[left].priority < self.heap[min_index].priority:
                min_index = left
            if right < len(self.heap) and self.heap[right].priority < self.heap[min_index].priority:
                min_index = right
            if min_index == index:
                break
                
            self.swap(index, min_index)
            index = min_index
            
    def display(self):
        if self.is_empty():
            print("Heap is empty")
            return
            
        print("\nCurrent Maintenance Requests (Priority Order):")
        for i, request in enumerate(self.heap):
            print(f"{i+1}. ID: {request.id}, Priority: {request.priority}, "
                  f"Building: {request.building}, Floor: {request.floor}, "
                  f"Description: {request.description}")
def main():
    maintenance_heap = MaintenanceHeap(10)
    requests = [
        MaintenanceRequest("REQ001", 1, "Water leak in ceiling", "Building A", "3rd", time.time()),
        MaintenanceRequest("REQ002", 3, "Light bulb replacement", "Building B", "2nd", time.time()),
        MaintenanceRequest("REQ003", 1, "Broken elevator", "Building A", "1st", time.time()),
        MaintenanceRequest("REQ004", 2, "AC not working", "Building C", "4th", time.time()),
        MaintenanceRequest("REQ005", 4, "Paint touch-up needed", "Building B", "5th", time.time())
    ]
    print("Inserting maintenance requests...")
    for request in requests:
        if maintenance_heap.insert(request):
            print(f"Inserted request {request.id} with priority {request.priority}")
        else:
            print(f"Could not insert request {request.id} - heap is full")
    maintenance_heap.display()
    print("\nProcessing highest priority requests:")
    try:
        for _ in range(3):
            request = maintenance_heap.extract_highest_priority()
            print(f"Processing: ID: {request.id}, Priority: {request.priority}, "
                  f"Description: {request.description}")
    except IndexError as e:
        print(f"No more requests to process: {e}")
    print("\nRemaining requests:")
    maintenance_heap.display()

if __name__ == "__main__":
    main()