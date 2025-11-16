### **Name**

Observer

### **Synonyms**

Publisher–Subscriber, Pub/Sub, Listener Pattern, Dependents Pattern

### **Short Description**

The Observer pattern defines a one-to-many relationship between objects so that when one object (the subject) changes state, all its dependents (observers) are automatically notified and updated. It decouples subjects from observers, allowing each to vary independently. This pattern helps implement event-driven architectures by propagating changes efficiently. It is widely used in GUI frameworks, messaging systems, and reactive programming.

### **Author and Historical Notes**

The Observer pattern was formalized by the “Gang of Four” in their 1994 book *Design Patterns: Elements of Reusable Object-Oriented Software*. However, the conceptual origins predate GoF and appear in early event-driven and Smalltalk systems. The GoF provided a standardized structure and terminology, making Observer a foundational building block for modern UI toolkits and publish-subscribe systems.

### **Related Design Patterns**

* Mediator (centralizes communication, sometimes used instead of multiple observers)
* MVC (Model–View–Controller uses Observer between model and views)
* Event Bus / Message Broker (architectural extensions of pub/sub)
* Reactive Programming patterns (Observer is foundational)

### **Use Cases and When to Use It**

* When multiple objects need to react to changes in another object.
* When the number of dependent objects is unknown or should change dynamically.
* When implementing event-driven systems such as UIs, notifications, or distributed systems.
* When you want to reduce coupling between publishers and subscribers.

### **Pros**

* Promotes loose coupling between subject and observers.
* Supports dynamic subscription and unsubscription at runtime.
* Makes it easy to broadcast state changes to multiple receivers.
* Encourages modular and extensible event-driven architectures.

### **Cons**

* Can cause performance issues if many observers are registered or updates are frequent.
* Harder to debug due to indirect, decoupled communication.
* Risk of memory leaks if observers are not properly deregistered.
* Order of notification may be unpredictable or inconsistent.

### **Low-Level Detailed Description**

At a low level, the Observer pattern relies on two main abstractions: **Subject** and **Observer**.
The Subject maintains a list of observers and provides methods to attach, detach, and notify them. When its internal state changes, it triggers the notification mechanism, often passing context or updated data to observers.
Observers implement an interface with an update method, defining how they respond to notifications. The subject does not know the concrete classes of its observers, only the interface they follow, ensuring loose coupling.
Efficient implementations optimize storage of observers, asynchronous notification, and safe iteration when observers modify the list during updates. Thread-safe variants use locks, concurrent collections, or event dispatchers.

---

### **Usage Example**

#### **Java Example**

```java
// Observer interface
interface Observer {
    void update(int newValue);
}

// Subject (observable)
class Subject {
    private List<Observer> observers = new ArrayList<>();
    private int state;

    public void attach(Observer observer) {
        observers.add(observer);
    }

    public void detach(Observer observer) {
        observers.remove(observer);
    }

    public void setState(int state) {
        this.state = state;
        notifyObservers();
    }

    private void notifyObservers() {
        for (Observer o : observers) {
            o.update(state);
        }
    }
}

// Concrete observer
class ConcreteObserver implements Observer {
    private String name;

    public ConcreteObserver(String name) {
        this.name = name;
    }

    public void update(int newValue) {
        System.out.println(name + " received update: " + newValue);
    }
}

// Usage
public class Main {
    public static void main(String[] args) {
        Subject subject = new Subject();

        Observer o1 = new ConcreteObserver("Observer 1");
        Observer o2 = new ConcreteObserver("Observer 2");

        subject.attach(o1);
        subject.attach(o2);

        subject.setState(42);
        subject.setState(100);
    }
}
```

#### **Python Example**

```python
# Observer interface
class Observer:
    def update(self, new_value):
        raise NotImplementedError

# Subject (observable)
class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def set_state(self, value):
        self._state = value
        self.notify_observers()

    def notify_observers(self):
        for obs in self._observers:
            obs.update(self._state)

# Concrete observer
class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, new_value):
        print(f"{self.name} received update: {new_value}")

# Usage
subject = Subject()

o1 = ConcreteObserver("Observer 1")
o2 = ConcreteObserver("Observer 2")

subject.attach(o1)
subject.attach(o2)

subject.set_state(42)
subject.set_state(100)
```