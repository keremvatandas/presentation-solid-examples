class GoodParentKirby:
    def introduce(self):
        return "I'm parent Kirby"

    def make_coffee(self):
        return "I make coffee"


class GoodChildKirby(GoodParentKirby):
    def introduce(self):
        return "I'm child Kirby"

    def make_coffee(self):
        # Subclass is keeping the behavior of the parent class
        # Coffee making ability is kept
        coffee = super().make_coffee()
        return "Ok sure"  # Coffee making functionality is kept


print("\nGOOD EXAMPLE - LSP Compliant:")
good_parent = GoodParentKirby()
good_child = GoodChildKirby()

print(f"Parent: {good_parent.introduce()} & {good_parent.make_coffee()}")
print(f"Child: {good_child.introduce()}")

print("\nParent's coffee request:")
print(f"- Can you make me coffee? - {good_parent.make_coffee()}")

print("\nChild's coffee request:")
print(f"- Can you make me coffee? - {good_child.make_coffee()}")
print("- Nice one")
print("This is a good example because ChildKirby can replace ParentKirby!")
