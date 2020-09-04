#!/usr/bin/env python3

class Location:
    def __init__(self, country, capital, region):
        self._country = country
        self._capital = capital
        self._region = region
    
    def country(self):
        return self._country
    def capital(self):
        return self._capital
    def region(self):
        return self._region

def print_location(l):
    if not isinstance(l, Location):
        raise TypeError("print_location(): requires a location")
    print('{} is the capital of {} and is located in {}.'.format(l.capital(), l.country(), l.region()))
    
def main():
    location_one = Location('Bosnia and Herzegovina', 'Sarejevo', 'Eastern Europe')
    location_two = Location('New Zealand', 'Wellington', 'Oceania')
    location_three = Location('Canada', 'Ottawa', 'North America')
    location_four = Location('Azerbaijan', 'Baku', 'The Middle East')
    
    locations = [location_one, location_two, location_three, location_four]
    for location in locations:
        print_location(location)
        
if __name__ == '__main__': main()
