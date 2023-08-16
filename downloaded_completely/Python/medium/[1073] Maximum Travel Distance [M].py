"""
####  Maximum Travel Distance  ####

Write a function that takes fuel (liters), fuel_usage (liters/100km), passengers, air_con (boolean) and returns maximum distance that car can travel.
___
*) fuel is the number of liters of fuel in the fuel tank.
*) fuel_usage is basic fuel consumption per 100 km (with the driver inside only).
*) Every additional passenger is increasing basic fuel consumption by 5%.
*) If the air conditioner is ON True, its increasing total (not basic) fuel consumption by 10%.
___



[Examples]

___
total_distance(70.0, 7.0, 0, False) ➞ 1000.0

total_distance(36.1, 8.6, 3, True) ➞ 331.8

total_distance(55.5, 5.5, 5, false) ➞ 807.3
_____



[Notes]

___
*) fuel and fuel_usage are always greater than 1.
*) passengers are always greater or equal to 0.
*) Round your answer to the nearest tenth.
___



[algebra] [algorithms] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Estimating the Cost of Fuel for a Trip
https://www.racq.com.au/cars-and-driving/cars/owning-and-maintaining-a-car/fuel-saving-tips/estimating-the-cost-of-fuel-for-a-trip
Do you need to estimate the cost of fuel for a trip? Learn how to and read our helpful hints.
_________
_________
round() Function
https://www.w3schools.com/python/ref_func_round.asp
Returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
_________

"""
#Your code should go here:

