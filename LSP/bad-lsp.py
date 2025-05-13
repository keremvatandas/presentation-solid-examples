class BadParentKirby:
    def introduce(self):
        return "I'm parent Kirby"

    def make_coffee(self):
        return "I make coffee"


class BadChildKirby(BadParentKirby):
    def introduce(self):
        return "I'm child Kirby"

    def make_coffee(self):
        # Subclass is changing the behavior of the parent class and suggesting tea instead of coffee
        # This violates LSP because it changes the expected behavior
        return "No but do you want tea instead?"


print("BAD EXAMPLE - LSP Violation:")
parent = BadParentKirby()
child = BadChildKirby()

print(f"Parent: {parent.introduce()} & {parent.make_coffee()}")
print(f"Child: {child.introduce()}")

print("\nParent's coffee request:")
print(f"- Can you make me coffee? - {parent.make_coffee()}")

print("\nChild's coffee request:")
print(f"- Can you make me coffee? - {child.make_coffee()}")
print("- Ugh you violated LSP")
print("This is a bad example because ChildKirby cannot replace ParentKirby!")
