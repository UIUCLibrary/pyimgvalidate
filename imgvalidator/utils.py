from . import profiles, validation_profile
import inspect


def get_profiles():
    active_profiles = dict()
    for profile_name, profile in inspect.getmembers(
            profiles, lambda m:
                            inspect.isclass(m)
                            and issubclass(m, validation_profile.AbsProfileBuilder)
                            and not inspect.isabstract(m)):
        active_profiles[profile_name] = profile
    return active_profiles
