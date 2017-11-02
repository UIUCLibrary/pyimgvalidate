import os
import sys
import typing
from imgvalidator import validation_profile, validate, utils, report
import imgvalidator
import argparse


def source(path):
    if not os.path.exists(path):
        raise ValueError("{} is an invalid path".format(path))

    if not os.path.isdir(path) and not os.path.isfile(path):
        raise ValueError("{} is not a file or a directory".format(path))

    return os.path.abspath(path)


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=imgvalidator.__description__)

    parser.add_argument(
        '--version',
        action='version',
        version=imgvalidator.__version__
    )

    parser.add_argument(
        "source",
        type=source,
        help="Either a file or a directory"
    )

    parser.add_argument(
        "profile",
        choices=utils.get_profiles(),
        help="Validation profile to compare with"
    )

    debug_group = parser.add_argument_group("Debug")

    debug_group.add_argument(
        '--debug',
        action="store_true",
        help="Run script in debug mode")

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    profile_builder = validation_profile.ProfileBuilder(imgvalidator.get_profile_builder(args.profile))
    profile = profile_builder.build_profile()

    files = locate_files(args.source, profile)

    for result in validate_files(files, profile):
        print("\nValidation Result:")
        print(str(result))

    print("\nDone")


def locate_files(source, profile: validation_profile.ValidationProfile) -> typing.Generator["str", None, None]:
    """Generator function for locating the files to validate

    Args:
        source: path to a directory or a file
        profile: validation profile to validate against

    Returns:

    """

    if os.path.isdir(source):
        files = yield from get_files(source, extension=profile.file_extension)
    else:
        files = yield str(source)
    return files


def validate_files(files, profile):
    for file_name in files:
        result = report.ValidationData(file_name)
        print("\nScanning: {}".format(file_name))
        try:
            errors = list(validate.validate_file(file_name, profile))
            result.errors = errors
            if errors:
                result.valid = False
            else:
                result.valid = True
        except AssertionError as e:
            failure_message = "Validation of {} failed. Reason: {}".format(file_name, e)
            print(failure_message, file=sys.stderr)
        yield result


def get_files(path, extension):
    if not os.path.exists(path):
        raise FileNotFoundError()
    for root, dirs, files in os.walk(path):
        for f in files:
            if os.path.splitext(f)[1] != extension:
                continue
            yield os.path.join(root, f)
