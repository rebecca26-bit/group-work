class Waypoint:
    def __init__(self, location, description):
        # Initialize a Waypoint object with location and description attributes
        self.location = location
        self.description = description
        # Initialize next and previous pointers to None
        self.next = None
        self.previous = None


class Route:
    def __init__(self):
        # Initialize an empty Route with head set to None
        self.head = None

    def add_waypoint(self, location, description):
        # Add a new waypoint to the end of the route
        new_waypoint = Waypoint(location, description)
        if not self.head:
            # If the route is empty, set the head to the new waypoint
            self.head = new_waypoint
        else:
            # Traverse to the end of the route and add the new waypoint
            current = self.head
            while current.next:
                current = current.next
            current.next = new_waypoint

    def insert_waypoint_after(self, target, location, description):
        # Insert a new waypoint after a specified target waypoint
        new_waypoint = Waypoint(location, description)
        if not self.head:
            # If the route is empty, set the head to the new waypoint
            self.head = new_waypoint
            return
        current = self.head
        while current:
            if current == target:
                # Insert the new waypoint after the target waypoint
                new_waypoint.next = current.next
                current.next = new_waypoint
                new_waypoint.previous = current
                if new_waypoint.next:
                    new_waypoint.next.previous = new_waypoint
                break
            current = current.next

    def remove_waypoint(self, location):
        # Remove a waypoint from the route by its location
        if not self.head:
            return
        if self.head.location == location:
            # If the head is the target waypoint, set the head to the next waypoint
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.location == location:
                # Remove the waypoint by updating pointers
                current.next = current.next.next
                if current.next:
                    current.next.previous = current
                break
            current = current.next


class BidirectionalRoute(Route):
    def __init__(self):
        # Initialize a BidirectionalRoute with head and tail set to None
        super().__init__()
        self.tail = None

    def add_waypoint(self, location, description):
        # Add a new waypoint to the end of the route, updating tail pointer
        new_waypoint = Waypoint(location, description)
        if not self.head:
            # If the route is empty, set both head and tail to the new waypoint
            self.head = new_waypoint
            self.tail = new_waypoint
        else:
            # Update pointers and set the tail to the new waypoint
            new_waypoint.previous = self.tail
            self.tail.next = new_waypoint
            self.tail = new_waypoint

    def insert_waypoint_after(self, target, location, description):
        # Insert a new waypoint after a specified target waypoint
        new_waypoint = Waypoint(location, description)
        if not self.head:
            # If the route is empty, set the head to the new waypoint
            self.head = new_waypoint
            return
        current = self.head
        while current:
            if current == target:
                # Insert the new waypoint after the target waypoint, updating pointers
                new_waypoint.next = current.next
                new_waypoint.previous = current
                if current.next:
                    current.next.previous = new_waypoint
                else:
                    self.tail = new_waypoint
                current.next = new_waypoint
                break
            current = current.next

    def next_waypoint(self):
        # Return the next waypoint in the route
        if not self.head:
            return None
        current = self.head
        while current.next:
            current = current.next
        return current

    def previous_waypoint(self):
        # Return the previous waypoint in the route
        if not self.tail:
            return None
        current = self.tail
        while current.previous:
            current = current.previous
        return current

# Create a new route
route = BidirectionalRoute()

# Add 5 waypoints
route.add_waypoint("A", "Start")
route.add_waypoint("B", "Midpoint")
route.add_waypoint("C", "Destination")
route.add_waypoint("D", "End")

# Demonstrate adding a waypoint
route.add_waypoint("E", "Extra")

# Demonstrate inserting a waypoint
target = route.head.next
route.insert_waypoint_after(target, "F", "Inserted")

# Demonstrate removing a waypoint
route.remove_waypoint("B")

# Traverse the route in a single direction
print("Traverse the route in a single direction:")
current = route.head
while current:
    print(current.location)
    current = current.next

# Traverse the route in both directions using BidirectionalRoute
print("\nTraverse the route in both directions:")
current = route.head
while current:
    print(current.location)
    current = current.next

print("\nTraverse the route in reverse:")
current = route.tail
while current:
    print(current.location)
    current = current.previous
