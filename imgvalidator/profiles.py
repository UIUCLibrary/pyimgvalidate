from imgvalidator import validation_profile


class DSHathiAccessTiff(validation_profile.AbsProfileBuilder):

    def set_embedded_metadata_profile(self):
        self._profile.embedded_metadata_profile = {
            "DPI: Horizontal": validation_profile.ValidationPair(
                field="Exif.Image.XResolution",
                expected_value="400/1"
            ),
            "DPI: Vertical": validation_profile.ValidationPair(
                field="Exif.Image.YResolution",
                expected_value="400/1"
            ),
            "Bit depth": validation_profile.ValidationPair(
                field="Exif.Image.BitsPerSample",
                expected_value="8 8 8"
            ),
            "Creator": validation_profile.ValidationPair(
                field="Xmp.dc.creator",
                expected_value="University of Illinois Library"
            ),
            "Address": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiAdrExtadr",
                expected_value="1408 W. Gregory Drive"
            ),
            "City": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiAdrCity",
                expected_value="Urbana"
            ),
            "State": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiAdrRegion",
                expected_value="Illinois"
            ),
            "Zip code": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiAdrPcode",
                expected_value="61801"
            ),
            "Country": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiAdrCtry",
                expected_value="United States"
            ),
            "Phone number": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiTelWork",
                expected_value="+1(217)2442062"
            ),
            "Email": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiEmailWork",
                expected_value="digidcc@library.illinois.edu"
            ),
            "Website": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiUrlWork",
                expected_value="http://www.library.illinois.edu"
            ),
        }

    def set_icc_profile_type(self):
        self._profile.icc_profile_type = validation_profile.IccProfileType.SRGB


class DSPreservationTiff(validation_profile.AbsProfileBuilder):

    def set_embedded_metadata_profile(self):
        self._profile.embedded_metadata_profile = {
            "DPI: Horizontal": validation_profile.ValidationPair(
                field="Exif.Image.XResolution",
                expected_value="600/1"
            ),
            "DPI: Vertical": validation_profile.ValidationPair(
                field="Exif.Image.YResolution",
                expected_value="600/1"
            ),
            "Bit depth": validation_profile.ValidationPair(
                field="Exif.Image.BitsPerSample",
                expected_value="16 16 16"
            ),
            "Creator": validation_profile.ValidationPair(
                field="Xmp.dc.creator",
                expected_value="University of Illinois Library"
            ),
            "Address": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiAdrExtadr",
                expected_value="1408 W. Gregory Drive"
            ),
            "City": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiAdrCity",
                expected_value="Urbana"
            ),
            "State": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiAdrRegion",
                expected_value="Illinois"
            ),
            "Zip code": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiAdrPcode",
                expected_value="61801"
            ),
            "Country": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiAdrCtry",
                expected_value="United States"
            ),
            "Phone number": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiTelWork",
                expected_value="+1(217)2442062"
            ),
            "Email": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiEmailWork",
                expected_value="digidcc@library.illinois.edu"
            ),
            "Website": validation_profile.ValidationPair(
                field="Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiUrlWork",
                expected_value="http://www.library.illinois.edu"
            ),
        }

    def set_icc_profile_type(self):
        self._profile.icc_profile_type = validation_profile.IccProfileType.ADOBE_RGB
