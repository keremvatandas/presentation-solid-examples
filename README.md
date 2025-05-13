# SOLID Principles Examples

This repository contains examples demonstrating the SOLID principles of object-oriented design using Python. Each principle is illustrated with both good and bad examples to help understand the concepts better.

## What are SOLID Principles?

SOLID is an acronym for five design principles in object-oriented programming that make software designs more understandable, flexible, and maintainable:

1. **S**ingle Responsibility Principle (SRP)
2. **O**pen/Closed Principle (OCP)
3. **L**iskov Substitution Principle (LSP)
4. **I**nterface Segregation Principle (ISP)
5. **D**ependency Inversion Principle (DIP)

## Examples

### 1. Single Responsibility Principle (SRP)

- **Location**: `SRP/` directory
- **Description**: A class should have only one reason to change
- **Examples**:
  - `bad-single.py`: A class that handles both singing and dancing
  - `good-single.py`: Separate classes for singing and dancing responsibilities

### 2. Open/Closed Principle (OCP)

- **Location**: `OCP/` directory
- **Description**: Software entities should be open for extension but closed for modification
- **Examples**:
  - `bad-ocp.py`: Modifying existing code to add new functionality
  - `good-ocp.py`: Extending functionality through inheritance without modifying existing code

### 3. Liskov Substitution Principle (LSP)

- **Location**: `LSP/` directory
- **Description**: Objects of a superclass should be replaceable with objects of its subclasses without breaking the application
- **Examples**:
  - `bad-lsp.py`: Subclass that breaks the contract of the parent class
  - `good-lsp.py`: Subclass that properly maintains the parent class contract

### 4. Interface Segregation Principle (ISP)

- **Location**: `ISP/` directory
- **Description**: Clients should not be forced to depend on interfaces they do not use
- **Examples**:
  - `bad-isp.py`: Large interface forcing clients to implement unnecessary methods
  - `good-isp.py`: Segregated interfaces with only relevant methods

### 5. Dependency Inversion Principle (DIP)

- **Location**: `DIP/` directory
- **Description**: High-level modules should not depend on low-level modules. Both should depend on abstractions
- **Examples**:
  - `bad-dip.py`: Direct dependency on concrete implementations
  - `good-dip.py`: Dependency on abstractions with dependency injection

## How to Run Examples

Each example can be run directly using Python:

```bash
python SRP/good-single.py
python OCP/good-ocp.py
python LSP/good-lsp.py
python ISP/good-isp.py
python DIP/good-dip.py
```

## Project Structure

```
.
├── SRP/
│   ├── good-single.py
│   └── bad-single.py
├── OCP/
│   ├── good-ocp.py
│   └── bad-ocp.py
├── LSP/
│   ├── good-lsp.py
│   └── bad-lsp.py
├── ISP/
│   ├── good-isp.py
│   └── bad-isp.py
├── DIP/
│   ├── good-dip.py
│   └── bad-dip.py
└── README.md
```

## Requirements

- Python 3.x

## Contributing

Feel free to contribute to this repository by:

1. Forking the repository
2. Creating a new branch
3. Making your changes
4. Submitting a pull request

## License

This project is open source and available under the MIT License.
