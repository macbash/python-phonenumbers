"""Auto-generated file, do not edit by hand. NR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NR = PhoneMetadata(id='NR', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2}', possible_number_pattern='\\d{3}', possible_length=(3,)),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='11[0-2]', possible_number_pattern='\\d{3}', example_number='110', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:1[0-2]|23|92)', possible_number_pattern='\\d{3}', example_number='110', possible_length=(3,)),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    carrier_specific=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_data=True)
