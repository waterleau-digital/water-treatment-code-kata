# Wastewater Treatment System Maintenance
---
## Introduction 

Hi, and welcome to the technical challenge! In this exercise, we are going to simulate the operation and maintenance of a wastewater treatment plant. Don’t panic! We don’t expect you to have any knowledge of the industry. 

In our system, the equipment items continuously degrade in performance (efficiency) as they age, and some items require special care as their service life decreases. Hence, we have a system in place that updates automatically the efficiency of our items every day. It was initially developed by a set of Engineers in the company before the Developers took over. 

## Water Treatment System 

### Description

These are the rules of the system:

- All `items` have a `service_life` value, which denotes the number of days we have before the item needs maintenance or replacement.

- All `items` have an `efficiency value`, which denotes how effectively the equipment performs its task. The higher the value, the more efficient the item is.

- At the end of each day, our system updates both values for every item.

### System Rules

Pretty simple, right? Well, here’s where it gets interesting:

- Once the `service_life` has passed, `efficiency` degrades twice as fast.

- The `efficiency` of an item can never be negative and will never exceed `50`.

- An `Aerator` is a critical component that improves in efficiency as its `service_life` approaches zero.

- A `Tank`, as a stable part of the system, does not degrade in efficiency over time and its `efficiency` is always `100`. 

- A `Filter` increases in `efficiency` based on the remaining `service_life`:

    - `efficiency` increases by `2` when there are 10 days or fewer remaining, and by `3` when there are 5 days or fewer remaining, 

    - but once the `service_life` ends, efficiency drops to `0`

- All other items (`Pump`, `Valve`, …) degrade in `efficiency` as their `service_life` runs out.

### Task

We’ve recently signed a supplier of `Chemicals`, which are a new item category. These items degrade in efficiency twice as fast as normal items.

Feel free to make any changes to the `update_efficiency` method and add any new code as long as everything still works correctly. However, do not alter the `Item` class or the list of items, as these belong to another part of the team (they'll be really upset if we mess with them). 