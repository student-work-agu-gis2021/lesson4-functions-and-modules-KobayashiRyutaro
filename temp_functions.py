def fahr_to_celsius(temp_fahrenheit):



  converted_temp = (temp_fahrenheit - 32) / 1.8;

#Create a function `converted_temp` to convert Fahrenheit temperature to Celsius.


  return converted_temp


def temp_classifier(temp_celsius):

  if (temp_celsius < -2):
    return 0

#Class 1 when the temperature is below -2 degrees Celsius and less than 2 degrees Celsius
  elif(-2 <= temp_celsius and temp_celsius < 2):
    return 1

#Class 2 when the temperature is below 2 degrees Celsius and below 15 degrees Celsius.
  elif(2 <= temp_celsius and temp_celsius < 15):
    return 2

#Class 3 for all other times.
  else:
    return 3