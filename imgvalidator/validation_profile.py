import abc
from imgvalidator import utils
from enum import Enum
from collections import namedtuple
ValidationPair = namedtuple("ValidationPair", ("field", "expected_value"))
# my_profile = inspect.getmembers(imgvalidator.profiles)
class IccProfileType(Enum):
    UNKNOWN = "Unknown ICC profile"
    SRGB = "sRGB"
    ADOBE_RGB = "Adobe RGB"


class ValidationProfile:
    def __init__(self):
        self.embedded_metadata_profile = dict()
        self.icc_profile_type = None
        self.name = None
        self.file_extension = None


class AbsProfileBuilder(metaclass=abc.ABCMeta):
    def __init__(self):
        self._profile = ValidationProfile()

    def new_profile(self) -> None:
        """set the a profile_builder to a new empty profile to create"""
        self._profile = ValidationProfile()

    @abc.abstractmethod
    def set_embedded_metadata_profile(self):
        pass

    @abc.abstractmethod
    def set_icc_profile_type(self):
        pass

    def get_profile(self):
        return self._profile

    @abc.abstractmethod
    def set_file_extension(self):
        pass


def identify_icc_profile(profile) -> IccProfileType:
    if str(profile['device_model']) == "sRGB":
        return IccProfileType.SRGB
    if str(profile['color_space']) == "RGB" and str(profile['creator_sig']) == "ADBE":
        return IccProfileType.ADOBE_RGB
    else:
        return IccProfileType.UNKNOWN


class ProfileBuilder:
    def __init__(self, profile_builder: AbsProfileBuilder) -> None:
        self._profile_builder = profile_builder

    def build_profile(self)->ValidationProfile:
        self._profile_builder.new_profile()
        self._profile_builder.set_embedded_metadata_profile()
        self._profile_builder.set_icc_profile_type()
        self._profile_builder.set_file_extension()
        return self._profile_builder.get_profile()


def get_profile_builder(name):
    profiles = utils.get_profiles()
    return profiles[name]()
