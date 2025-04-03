class WastewaterSystem(object):
    def __init__(self, items):
        self.items = items

    def update_efficiency(self):
        for item in self.items:
            if item.name != "Aerator" and item.name != "Filter":
                if item.efficiency > 0:
                    if item.name != "Tank":
                        item.efficiency = item.efficiency - 1
            else:
                if item.efficiency < 50:
                    item.efficiency = item.efficiency + 1
                    if item.name == "Filter":
                        if item.service_life < 11:
                            if item.efficiency < 50:
                                item.efficiency = item.efficiency + 1
                        if item.service_life < 6:
                            if item.efficiency < 50:
                                item.efficiency = item.efficiency + 1

            if item.name != "Tank":
                item.service_life = item.service_life - 1

            if item.service_life < 0:
                if item.name != "Aerator":
                    if item.name != "Filter":
                        if item.efficiency > 0:
                            if item.name != "Tank":
                                item.efficiency = item.efficiency - 1

                    else:
                        item.efficiency = item.efficiency - item.efficiency

                else:
                    if item.efficiency < 50:
                        item.efficiency = item.efficiency + 1


class Item:
    def __init__(self, name, service_life, efficiency):
        self.name = name
        self.service_life = service_life
        self.efficiency = efficiency

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.service_life, self.efficiency)
