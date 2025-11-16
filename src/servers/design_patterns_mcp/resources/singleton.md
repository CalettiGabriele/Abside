### **Name**

Singleton

### **Synonyms**

Single Instance, Single Object

### **Short Description**

The Singleton pattern ensures that a class has exactly one instance throughout the program’s lifecycle and provides a global access point to it. It centralizes control of a shared resource, avoiding unnecessary duplication. This pattern is often used when managing configurations, logging, or shared connection pools. It enforces controlled instantiation and consistent behavior across the system.

### **Author and Historical Notes**

The Singleton pattern was formalized by the “Gang of Four” (Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides) in their 1994 book *Design Patterns: Elements of Reusable Object-Oriented Software*. Although the concept of single-instance objects predates the book, the GoF standardized the terminology and structure, making Singleton one of the most cited and foundational design patterns.

### **Related Design Patterns**

* Factory Method (often used to encapsulate object creation, sometimes combined with Singleton)
* Abstract Factory
* Facade
* Dependency Injection (a common alternative to avoid Singleton drawbacks)

### **Use Cases and When to Use It**

* When exactly one instance of a class is required (e.g., configuration manager, logger).
* When a single global entry point is beneficial or needed.
* When controlled access to a shared resource or service must be enforced.
* When the object is expensive to create or must not be duplicated.

### **Pros**

* Guarantees a single instance globally.
* Offers controlled access to a shared resource.
* Can enable lazy initialization and optimize resource usage.
* Simplifies access to global configurations.

### **Cons**

* Can easily become a hidden global dependency, harming modularity.
* Difficult to mock or replace in unit tests.
* Can introduce concurrency issues without careful synchronization.
* Often leads to tight coupling and anti-pattern–like usage if overused.

### **Low-Level Detailed Description**

At a low level, the Singleton relies on three main mechanisms:

1. **Private constructor** – prevents direct instantiation from outside the class.
2. **Static instance variable** – holds the single instance of the class.
3. **Static access method** – returns the instance, creating it only if it doesn’t exist (lazy initialization).
   In multithreaded environments, thread-safety must be enforced through mechanisms such as synchronized blocks, double-checked locking, or language constructs that ensure safe publication. The pattern may also use eager initialization if performance or simplicity is prioritized over laziness. Proper memory visibility guarantees are vital to avoid half-initialized instances.

### **Usage Example**

#### **Java Example**

```java
public class Singleton {
    private static volatile Singleton instance;

    // Private constructor
    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) { 
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }

    public void doSomething() {
        System.out.println("Singleton instance in action!");
    }
}

class Main {
    public static void main(String[] args) {
        Singleton s = Singleton.getInstance();
        s.doSomething();
    }
}
```

#### **Python Example**

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def do_something(self):
        print("Singleton instance in action!")

# Usage
s = Singleton()
s.do_something()
```