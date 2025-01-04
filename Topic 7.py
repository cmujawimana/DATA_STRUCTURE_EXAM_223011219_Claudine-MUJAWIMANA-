class MaintenanceRequest:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
    def __repr__(self):
        return f"[Priority: {self.priority}] {self.description}"
def insertion_sort(requests):
    for i in range(1, len(requests)):
        key = requests[i]
        j = i - 1
        while j >= 0 and requests[j].priority > key.priority:
            requests[j + 1] = requests[j]
            j -= 1
        requests[j + 1] = key

requests = [
    MaintenanceRequest("Fix broken elevator", 3),
    MaintenanceRequest("Repair leaking pipe in Apartment 402", 1),
    MaintenanceRequest("Replace lobby light fixtures", 2),
    MaintenanceRequest("Clean rooftop water tank", 4),
]
print("Before Sorting:")
for request in requests:
    print(request)
insertion_sort(requests)
print("\nAfter Sorting:")
for request in requests:
    print(request)
