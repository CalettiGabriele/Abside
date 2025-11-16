### **Name**

Factory Method

### **Synonyms**

Virtual Constructor, Creator Method

### **Short Description**

The Factory Method pattern defines an interface for creating objects but lets subclasses decide which concrete class to instantiate. It decouples object creation from its usage, promoting flexibility and scalability. This allows systems to introduce new product types without modifying existing code. It is especially helpful when dealing with complex or variable object creation processes.

### **Author and Historical Notes**

The Factory Method pattern was formally described by the “Gang of Four” (Gamma, Helm, Johnson, Vlissides) in their landmark 1994 book *Design Patterns: Elements of Reusable Object-Oriented Software*. It originates from the need to avoid hard-coding concrete classes and to support open/closed principle–aligned architectures. Over time, it has become one of the most widely adopted creational patterns in object-oriented design.

### **Related Design Patterns**

* Abstract Factory (often built on top of Factory Method)
* Template Method (Factory Method is sometimes used within template hooks)
* Dependency Injection (an alternative to manual object creation)
* Prototype (another creational approach)

### **Use Cases and When to Use It**

* When a class cannot anticipate the exact type of objects it must create.
* When you want to delegate the decision of which object to instantiate to subclasses.
* When families of related products must be supported and extended.
* When object creation is complex, conditional, or requires configuration.

### **Pros**

* Promotes loose coupling by abstracting object creation.
* Makes it easy to introduce new concrete product types.
* Enhances flexibility and supports adherence to the Open/Closed Principle.
* Encapsulates complex creation logic.

### **Cons**

* Can introduce additional subclasses and structural complexity.
* May lead to more boilerplate if overused.
* The indirection can make code harder to follow for small/simple systems.

### **Low-Level Detailed Description**

At a low level, the Factory Method pattern uses a **creator class** that defines a method—often abstract—that returns an abstract product type. Subclasses override this method to instantiate specific concrete product classes. The creator may include core business logic that operates on the abstract product interface, ensuring that product-specific behavior is abstracted away.
The pattern structurally consists of:

1. **Product interface** – defines a common contract.
2. **Concrete Products** – implementations of the product interface.
3. **Creator base class** – declares the factory method and may include default logic.
4. **Concrete Creators** – implement the factory method, deciding which product is created.
   This ensures object creation is centralized and modifiable through subclassing rather than direct instantiation.

### **Usage Example**

#### **Java Example**

```java
// Product interface
interface Transport {
    void deliver();
}

// Concrete products
class Truck implements Transport {
    public void deliver() {
        System.out.println("Delivering by land in a truck.");
    }
}

class Ship implements Transport {
    public void deliver() {
        System.out.println("Delivering by sea in a ship.");
    }
}

// Creator
abstract class Logistics {
    public void planDelivery() {
        Transport t = createTransport();
        t.deliver();
    }

    protected abstract Transport createTransport(); // Factory Method
}

// Concrete creators
class RoadLogistics extends Logistics {
    protected Transport createTransport() {
        return new Truck();
    }
}

class SeaLogistics extends Logistics {
    protected Transport createTransport() {
        return new Ship();
    }
}

// Usage
public class Main {
    public static void main(String[] args) {
        Logistics logistics = new RoadLogistics();
        logistics.planDelivery();

        logistics = new SeaLogistics();
        logistics.planDelivery();
    }
}
```

#### **Python Example**

```python
from abc import ABC, abstractmethod

# Product interface
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# Concrete products
class Truck(Transport):
    def deliver(self):
        print("Delivering by land in a truck.")

class Ship(Transport):
    def deliver(self):
        print("Delivering by sea in a ship.")

# Creator
class Logistics(ABC):
    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver()

    @abstractmethod
    def create_transport(self):
        pass

# Concrete creators
class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()

# Usage
logistics = RoadLogistics()
logistics.plan_delivery()

logistics = SeaLogistics()
logistics.plan_delivery()
```