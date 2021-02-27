

units = {

# ---------------------------------- Length ---------------------------------- #

'PICOMETRES': 1E-12,
'NANOMETRES': 1E-9,
'MICROMETRES' : 1E-6,
'MILLIMETRES': 1E-3,
'CENTIMETRES': 0.01,
'METRES': 1,
'KILOMETRES': 1000,
'INCHES': 25.4E-3,
'FEET': 0.3048,
'YARDS': 0.9144,
'MILES': 1609.344,
'NAUTICAL MILES': 1852,

# ----------------------------------- Area ----------------------------------- #

'SQUARE MILLIMETRES': 1E-6,
'SQUARE CENTIMETRES': 1E-4,
'SQUARE METRES': 1,
'SQUARE KILOMETRES': 1E6,
'SQUARE INCHES': 6.4516E-4,
'SQUARE FEET': 0.09290304,
'SQUARE YARDS': 0.83612736,
'SQUARE MILES': 2.589988110336E6,
'ARES': 100,
'HECTARES': 1E4,
'ACRES': 4046.86,

# ---------------------------------- Volume ---------------------------------- #

'MILLILITRES': 1E-6,
'CUBIC CENTIMETRES': 1E-6,
'CENTILITRES': 1E-5,
'CUBIC METRES': 1,
'LITRES': 1E-3,
'CUBIC FEET': 1/35.3147,
'PINTS': 1/1759.75,
'GALLONS': 0.00454609,

# ----------------------------------- Mass ----------------------------------- #

'MILLIGRAMS': 1E-6,
'GRAMS': 1E-3,
'KILOGRAMS': 1,
'TONNES (METRIC TONS)': 1E3,
'KILOTONNES': 1E6,
'MEGATONNES': 1E9,
'OUNCES': 1/35.274,
'POUNDS': 1/2.20462,
'STONE': 6.35,

# ---------------------------------- Time --------------------------------- #

'MICROSECONDS': 1E-6,
'MILLISECONDS': 1E-3,
'SECONDS': 1,
'MINUTES': 60,
'HOURS': 3600,
'DAYS': 86400,
'WEEKS': 604800,
'MONTHS': 2629800,
'YEARS': 31557600,

# ----------------------------------- Speed ---------------------------------- #

'METRES/SECOND': 1,
'KILOMETRES/HOUR': 1/3.6,
'MILES/HOUR': 1/2.237,
'KNOTS': 1/1.944

}

def convert(value, unitFrom, unitTo):
    if units.get(str(unitFrom)) and units.get(str(unitTo)) is not None:
        print(f'Converting {value} {unitFrom} to {unitTo}')
        ans = value * units.get(str(unitFrom)) / units.get(str(unitTo))

        ans = f'{ans:.4}' # round to 4 sf
        print(f'{value} {unitFrom} is {ans} {unitTo}')
        
        return ans