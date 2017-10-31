import imgvalidator.cli
import imgvalidator.profiles
from imgvalidator import validation_profile
from imgvalidator import validate


def test_for_errors():
    test_path = "/Volumes/HathiTrust/HenryTest-PSR_2/DCC/Lab/Access_BAD"

    profile_builder = validation_profile.create_builder(validation_profile.get_profile_builder("DSHathiAccessTiff"))
    my_validation_profile = profile_builder.build_profile()
    all_errors = dict()
    for file_name in imgvalidator.cli.get_tiffs(test_path):
        errors = list(validate.validate_file(file_name, my_validation_profile ))
        all_errors[file_name] = errors

    first_file_errors =  all_errors['/Volumes/HathiTrust/HenryTest-PSR_2/DCC/Lab/Access_BAD/7209692/00000001.tif']
    assert "Phone number validation failed. Expected \'+1(217)2442062\'. Received \'+1+1(217)2442062\'." in first_file_errors

    bad_color_file_errors = all_errors['/Volumes/HathiTrust/HenryTest-PSR_2/DCC/Lab/Access_BAD/7210438/00000017.tif']
    assert 'Color Format incorrect: Expected \'sRGB\'. Received \'Adobe RGB\'.' in bad_color_file_errors