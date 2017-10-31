import os
import sys

from imgvalidator import profiles, validation_profile, validate
import imgvalidator
PATH = "/Volumes/HathiTrust/HenryTest-PSR_2/DCC/Lab/Access_BAD"
# PATH = "/Volumes/HathiTrust/HenryTest-PSR_2/DCC/Lab/Preservation_GOOD"
# PATH = "/Volumes/HathiTrust/HenryTest-PSR_2/DCC/ReadyToSubmit"
# PATH = "/Users/hborcher/Documents/demo_hathisubmit gui/"


def main():
    profile_builder = validation_profile.create_builder(imgvalidator.get_profile_builder("DSHathiAccessTiff"))
    profile = profile_builder.build_profile()

    for file_name in get_tiffs(path=PATH):
        print("\nScanning: {}".format(file_name))
        try:
            errors = list(validate.validate_file(file_name, profile))
            if errors:
                for error in errors:
                    print(error)
            else:
                print("Valid")
        except AssertionError as e:
            print("Validation of {} failed. Reason: {}".format(file_name, e), file=sys.stderr)


def get_tiffs(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            if os.path.splitext(f)[1] != ".tif":
                continue
            yield os.path.join(root, f)