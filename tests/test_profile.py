from imgvalidator import validation_profile, profiles


def test_DSPreservationTiff_profile():
    profile_builder = validation_profile.create_builder(validation_profile.get_profile_builder("DSPreservationTiff"))
    profile = profile_builder.build_profile()
    assert isinstance(profile, validation_profile.ValidationProfile)
    assert profile.icc_profile_type == validation_profile.IccProfileType.ADOBE_RGB
    assert "Creator" in profile.embedded_metadata_profile


def test_DSHathiAccessTiff_profile():
    profile_builder = validation_profile.create_builder(validation_profile.get_profile_builder("DSHathiAccessTiff"))
    profile = profile_builder.build_profile()
    assert isinstance(profile, validation_profile.ValidationProfile)
    assert profile.icc_profile_type == validation_profile.IccProfileType.SRGB
    assert "Creator" in profile.embedded_metadata_profile

#
def test_get_profile():
    profile_builder = validation_profile.get_profile_builder("DSPreservationTiff")
    assert isinstance(profile_builder, profiles.DSPreservationTiff)
