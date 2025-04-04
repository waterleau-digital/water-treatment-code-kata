from .wastewater_system import Item


def get_sample_items():
    """
    Return a list of sample items for testing. This is framework-agnostic.
    These items represent a variety of equipment with different behaviors.
    """
    return [
        Item(name="Pump", service_life=10, efficiency=50),
        Item(name="Valve", service_life=8, efficiency=40),
        Item(name="Sensor", service_life=15, efficiency=30),
        Item(name="Blower", service_life=5, efficiency=20),
        Item(name="Conveyor", service_life=7, efficiency=25),
        Item(name="Aerator", service_life=3, efficiency=40),
        Item(name="Separator", service_life=1, efficiency=45),
        Item(name="Tank", service_life=12, efficiency=100),
        Item(name="Filter", service_life=12, efficiency=30),
        Item(name="Chemical", service_life=2, efficiency=25),
    ]
