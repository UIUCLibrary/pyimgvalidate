import py3exiv2bind
from imgvalidator import validation_profile


def validate_value(test_name, value, expected_value):
    if value != expected_value:
        return "{} validation failed. Expected '{}'. Received '{}'.".format(test_name, expected_value, value)


def find_icc_errors(image_file: py3exiv2bind.Image, expected_icc_profile_type):
    icc_profile = image_file.icc()
    icc_type = validation_profile.identify_icc_profile(icc_profile)
    if icc_type == validation_profile.IccProfileType.UNKNOWN:
        yield "Unidentified ICC color profile"
    else:
        if icc_type != expected_icc_profile_type:
            yield "ICC Color profile incorrect: Expected '{}'. Received '{}'.".format(expected_icc_profile_type.value, icc_type.value)


def validate_file(file_name, validation_profile: validation_profile.ValidationProfile):
    image_file = py3exiv2bind.Image(file_name)
    yield from find_embedded_errors(image_file, validation_profile.embedded_metadata_profile)
    if validation_profile.icc_profile_type:
        yield from find_icc_errors(image_file, validation_profile.icc_profile_type)


def find_embedded_errors(image_file, embedded_metadata_profile):
    for test_name, (key, expected_value) in embedded_metadata_profile.items():
        if not key in image_file.metadata:
            error = "Expected metadata '{}' missing".format(key)
        else:
            error = validate_value(test_name, image_file.metadata[key], expected_value=expected_value)
        if error:
            yield error

