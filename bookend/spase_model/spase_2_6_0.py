from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

__NAMESPACE__ = "http://www.spase-group.org/data/schema"


class AccessRights(Enum):
    """
    Identifiers for permissions granted or denied by the host of a product to allow
    other users to access and use the resource.

    :cvar OPEN: Access is granted to everyone.
    :cvar PARTIALLY_RESTRICTED: Some portions of the resource have
        restricted access, the rest is open access. Typically, this is
        for accumulating data collections where some data is under
        review before being publicly released.
    :cvar RESTRICTED: Access to the product is regulated and requires
        some form of identification.
    """

    OPEN = "Open"
    PARTIALLY_RESTRICTED = "PartiallyRestricted"
    RESTRICTED = "Restricted"


class AnnotationType(Enum):
    """
    Identifiers for an classification of an annotation.

    :cvar ANOMALY: An interval where measurements or observations may be
        adversely affected.
    :cvar EVENT: An action or observation which occurs at a point in
        time.
    :cvar FEATURE: A prominent or distinctive characteristic that occurs
        at a location or persists over a period of time.
    """

    ANOMALY = "Anomaly"
    EVENT = "Event"
    FEATURE = "Feature"


class ApplicationInterface(Enum):
    """
    Identifiers for the type of interface for the application.

    :cvar CLI: A command-line interface (CLI) is a form of interface
        where input to an application is provided as lines of text
        typically within a shell.
    :cvar GUI: A graphical user interface (GUI) is a form of user
        interface that allows users to interact with an application
        through graphical icons, forms and other elements with both a
        keyboard and a pointing device.
    :cvar API: An application programming interface (API) is a form of
        interface that allows applications to access the features or
        data of an operating system, application, or other service. An
        API may have a required protocol or set of principles. Some
        examples of protocols are SOAP, XML-RPC and JSON-RPC. An example
        of an API with a set of principles is REST.
    """

    CLI = "CLI"
    GUI = "GUI"
    API = "API"


class AssociationType(Enum):
    """
    Identifiers for resource associations.

    :cvar CHILD_EVENT_OF: A descendant or caused by another resource.
    :cvar DERIVED_FROM: A transformed or altered version of a resource
        instance.
    :cvar OBSERVED_BY: Detected or originating from another resource.
    :cvar OTHER: Not classified with more specific terms. The context of
        its usage may be described in related text.
    :cvar PART_OF: A portion of a larger resource.
    :cvar REVISION_OF: A modified version of a resource instance.
    """

    CHILD_EVENT_OF = "ChildEventOf"
    DERIVED_FROM = "DerivedFrom"
    OBSERVED_BY = "ObservedBy"
    OTHER = "Other"
    PART_OF = "PartOf"
    REVISION_OF = "RevisionOf"


class Availability(Enum):
    """
    Identifiers for indicating the method or service which may be used to access
    the resource.

    :cvar OFFLINE: Not directly accessible electronically. This includes
        resources which may to be moved to an online status in response
        to a given request.
    :cvar ONLINE: Directly accessible electronically.
    """

    OFFLINE = "Offline"
    ONLINE = "Online"


@dataclass
class Bin:
    """
    A grouping of observations according to a band or window of a common attribute.
    """

    band_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "BandName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    low: Optional[float] = field(
        default=None,
        metadata={
            "name": "Low",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    high: Optional[float] = field(
        default=None,
        metadata={
            "name": "High",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )


@dataclass
class BoundaryConditions:
    """
    Parameters associated to the model boundaries.
    """

    particle_boundary: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticleBoundary",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    field_boundary: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldBoundary",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


class ClassificationMethod(Enum):
    """
    Identifiers for the technique used to determine the characteristics of an
    object.

    :cvar AUTOMATIC: Determined by the analysis or assessment performed
        by a program or server.
    :cvar INFERRED: Determined by the analysis of other information or
        resources.
    :cvar INSPECTION: Determined by the analysis or assessment performed
        by a person.
    """

    AUTOMATIC = "Automatic"
    INFERRED = "Inferred"
    INSPECTION = "Inspection"


class ConfidenceRating(Enum):
    """
    Identifiers for the classification of the certainty of an assertion.

    :cvar PROBABLE: Likely given the available evidence. Considered in
        the range of 4 to 7 on a scale of 0 to 10.
    :cvar STRONG: Highly likely given the available evidence. Considered
        in the range of 7 to 10 on a scale of 0 to 10.
    :cvar UNLIKELY: Not likely given the available evidence. Considered
        equal to 0 on a scale of 0 to 10.
    :cvar WEAK: Slightly likely given the available evidence. Considered
        in the range of 1 to 4 on a scale of 0 to 10.
    """

    PROBABLE = "Probable"
    STRONG = "Strong"
    UNLIKELY = "Unlikely"
    WEAK = "Weak"


class CoordinateRepresentation(Enum):
    """
    Identifiers of the method or form for specifying a given point or vector in a
    given coordinate system.

    :cvar CARTESIAN: A representation in which a position vector or a
        measured vector (e.g., field or flow) is specified by its
        components along the base axes of the coordinate system.
    :cvar CYLINDRICAL: A coordinate representation of a position vector
        or measured vector (field or flow) by its k-component, the
        magnitude of its projection into the i-j plane, and the
        azimuthal angle of the i-j plane projection.
    :cvar SPHERICAL: A coordinate representation of a position vector or
        of a measured vector by its magnitude and two direction angles.
        The angles are relative to the base axes of the coordinate
        system used. Typically, the angles are phi [azimuth angle,
        =arctan (j/i)] and theta, where theta may be a polar angle,
        arctan {[sqrt(i^2+j^2)]/k}, or an elevation angle, arctan
        [k/sqrt(i^2+j^2)].
    """

    CARTESIAN = "Cartesian"
    CYLINDRICAL = "Cylindrical"
    SPHERICAL = "Spherical"


class CoordinateSystemName(Enum):
    """
    Identifiers of the origin and orientation of a set of typically orthogonal
    axes.

    :cvar CARRINGTON: A coordinate system which is centered at the Sun
        and is fixed with respect to the synodic rotation rate. The mean
        synodic value is about 27.2753 days. The Astronomical Almanac
        gives a value for Carrington longitude of 349.03 deg at 0000 UT
        on 1 January 1995.
    :cvar CGM: Corrected Geomagnetic - A coordinate system from a
        spatial point with GEO radial distance and geomagnetic latitude
        and longitude, follow the epoch-appropriate IGRF/DGRF model
        field vector through to the point where the field line crosses
        the geomagnetic dipole equatorial plane. Then trace the dipole
        magnetic field vector Earthward from that point on the
        equatorial plane, in the same hemisphere as the original point,
        until the initial radial distance is reached. Designate the
        dipole latitude and longitude at that point as the CGM latitude
        and longitude of the original point, see
        http://nssdc.gsfc.nasa.gov/space/cgm/cgmm_des.html.
    :cvar CSO: Corrected Solar Orbital - A coordinate system related to
        Earth where x-axis is anti-sunward and the y-axis points in the
        orbital velocity direction.
    :cvar DM: Dipole Meridian - A coordinate system centered at the
        observation point. The z-axis is parallel to the dipole axis of
        the Earth, positive northward. x-axis is in the plane defined by
        the z-axis and the line linking the observation point with the
        center of the Earth. The y-axis is positive eastward, see
        http://cdpp.cnes.fr/00428.pdf.
    :cvar ECD: Eccentric Dipole (ECD) coordinate system that aligns with
        a dipole whose origin and orientation may be different from the
        physical center and spin axis of the containing body. The
        IGRF-12 coefficients for 2015 are used to determine the origin
        for the Earth. The 2015 positions are North dip pole: latitude:
        86.29, longitude -160.06. South dip pole latitude: -64.28,
        longitude: 136.59, North geometric pole latitude: 80.37,
        longitude: -72.63, South geomagnetic pole latitude: -80.37,
        longitude: 107.37. ECD is defined in
        doi:10.1186/s40623-015-0228-9.
    :cvar ECEF: The Earth-Centered, Earth-Fixed (ECEF) coordinate system
        has point (0,0,0) defined as the center of mass of the Earth.
        Its axes are aligned with the International Reference Pole (IRP)
        and International Reference Meridian (IRM). The x-axis
        intersects the sphere of the Earth at 0 deg latitude (Equator)
        and 0 deg longitude (Greenwich). The z-axis points north. The
        y-axis completes the right-handed coordinate system.
    :cvar ENP: ENP (also called PEN) - The P-axis points northward,
        perpendicular to orbital plane. For an orbit with zero
        inclination, the P-axis is parallel to spin axis of the Earth.
        The E-axis is perpendicular to the P and N directions and points
        earthward. The N-axis is perpendicular to P and E and is
        positive eastward.
    :cvar GEI: GEI Geocentric Equatorial Inertial - A coordinate system
        where the z-axis is along spin axis of the Earth, positive
        northward. The x-axis points towards the first point of Aries
        (from the Earth towards the Sun at the vernal equinox), see
        Russell, 1971. When the x-axis is the direction of the mean
        vernal equinox of J2000, the coordinate system is also called
        GCI. Then the z-axis is also defined as being normal to the mean
        Earth equator of J2000.
    :cvar GEO: Geographic - geocentric corotating - A coordinate system
        where the z-axis is along spin axis of the Earth, positive
        northward. The x-axis lies in Greenwich meridian, positive
        towards Greenwich, see Russell, 1971.
    :cvar GPHIO: Kronian Solar Orbital - A coordinate system related to
        Saturn where the x-axis is anti-sunward and the y-axis points in
        the orbital velocity direction.
    :cvar GSE: Geocentric Solar Ecliptic - A coordinate system where the
        x-axis is from Earth to Sun. The z-axis is normal to the
        ecliptic, positive northward, see Russell, 1971.
    :cvar GSEQ: Geocentric Solar Equatorial - A coordinate system where
        the x-axis is from Earth to Sun. The y-axis is parallel to solar
        equatorial plane. The z-axis is positive northward, see Russell,
        1971.
    :cvar GSM: Geocentric Solar Magnetospheric - A coordinate system
        where the x-axis is from Earth to Sun, z-axis is northward in a
        plane containing the x-axis and the geomagnetic dipole axis, see
        Russell, 1971.
    :cvar HAE: Heliocentric Aries Ecliptic - A coordinate system where
        the z-axis is normal to the ecliptic plane, positive northward.
        The x-axis is positive towards the first point of Aries (from
        Earth to Sun at vernal equinox). Same as SE below, see Hapgood,
        1992.
    :cvar HCC: Heliocentric Cartesian - A 3-D orthonormal coordinate
        system that is primarily intended to specify with two dimensions
        a point on the solar disk. The z-axis points toward the
        observer. The y-axis lies in the plane defined by the solar spin
        vector and the z-axis is positive northward. The x-axis is
        perpendicular to the y-axis and z-axis, positive toward solar
        west. Standard representation for this system is based on (x,y)
        position of the point of interest expressed either as physical
        distances or as fractions of the solar disk radius.
    :cvar HCI: Heliographic Carrington Inertial.
    :cvar HCR: Heliocentric Radial - A 3-D orthonormal coordinate system
        that is primarily intended to specify with two dimensions a
        point on the solar disk. The z-axis points toward the observer.
        The y-axis lies in the plane defined by the solar spin vector
        and the z-axis, positive northward. The x-axis is perpendicular
        to the y-axis and z-axis, positive toward solar west. Standard
        representation for this system is based on distance rho from the
        z-axis (sqrt(x**2+y**2)) and the phase angle psi measured
        counterclockwise from the positive y-axis (arctan(-y/x)) of the
        point of interest.
    :cvar HEE: Heliocentric Earth Ecliptic - A coordinate system where
        the z-axis is normal to the ecliptic plane, positive northward.
        The x-axis points from Sun to Earth, see Hapgood, 1992.
    :cvar HEEQ: Heliocentric Earth Equatorial - A coordinate system
        where the z-axis is normal to the solar equatorial plane,
        positive northward. The x-axis is generally Earthward in the
        plane defined by the z-axis and the Sun-Earth direction, see
        Hapgood, 1992.
    :cvar HERTN: Helio-Ecliptic Radial Tangential Normal coordinate
        system. Typically centered at a spacecraft. The x-axis (radial)
        is set as the primary-axis, and is defined as the axis pointing
        from the spacecraft to the Sun. The z-axis (tangential) is set
        as the secondary-axis, and is defined as that portion of the
        ecliptic rotational axis which is perpendicular to the primary-
        axis. The y-axis (Normal) is defined as Z cross X.
    :cvar HG: Heliographic - A heliocentric rotating coordinate system
        where the z-axis is normal to the solar equatorial plane,
        positive northward. The x-axis and y-axis rotate with a period
        of 25.38 days. The zero longitude (x-axis) is defined as the
        longitude that passed through the ascending node of the solar
        equator on the ecliptic plane on 1 January, 1854 at 12 UT, see
        http://nssdc.gsfc.nasa.gov/space/helios/coor_des.html.
    :cvar HGI: Heliographic Inertial - A heliocentric coordinate system
        where the z-axis is normal to the solar equatorial plane,
        positive northward. The x-axis is along the intersection line
        between solar equatorial and ecliptic planes. The x-axis was
        positive at SE longitude of 74.367 deg on January 1, 1900. (See
        SE below.) See
        http://nssdc.gsfc.nasa.gov/space/helios/coor_des.html.
    :cvar HGRTN: Heliocentric Radial Tangential Normal coordinate system
        (also known as RTN). Typically centered at a spacecraft. Used
        for IMF and plasma V vectors. The x-axis (radial) is set as the
        primary-axis, and is defined as the axis pointing from the
        spacecraft to the Sun. The z-axis (tangential) is set as the
        secondary-axis, and is defined as that portion of the solar
        North rotational axis which is perpendicular to the primary-
        axis. The y-axis (normal) is defined as Z cross X.
    :cvar HPC: Helioprojective Cartesian=A 3-D orthonormal (left-handed)
        coordinate system that is primarily intended to specify with two
        dimensions a point on the solar disk. The z-axis points from the
        observer to the center of the solar disk. The y-axis lies in the
        plane defined by the solar spin vector and the z-axis, positive
        northward. The x-axis is perpendicular to the y-axis and z-axis,
        positive toward solar west. Given as the distance between the
        observer and the center of the solar disk, the standard
        representation of an (x,y) point on the solar disk is latitude
        (arctan(y/d)) and longitude (arctan (x/d)) of the point of
        interest.
    :cvar HPR: Helioprojective Radial - A 3-D orthonormal (left-handed)
        coordinate system that is primarily intended to specify with two
        dimensions a point on the solar disk. The z-axis points from the
        observer to the center of the solar disk. The y-axis lies in the
        plane defined by the solar spin vector and the z-axis, positive
        northward. The x-axis is perpendicular to the y-axis and z-axis,
        positive toward solar west. Given as the distance between the
        observer and the center of the solar disk, the standard
        representation for this system of an (x,y) point on the solar
        disk is latitude angle theta (arctan(sqrt(x**2+y**2)/d))) or
        equivalent declination parameter delta (theta-90 deg) and the
        phase angle psi as measured counterclockwise from the positive
        y-axis (psi=arctan(-y/x)) of the point of interest.
    :cvar HSM: Heliospheric Solar Magnetospheric - A coordinate system
        where the x-axis is from Earth to Sun, z-axis is northward in a
        plane containing the x-axis and the geomagnetic dipole axis.
    :cvar J2000: An astronomical coordinate system which uses the mean
        equator and equinox of Julian date 2451545.0 TT (Terrestrial
        Time), or January 1, 2000, noon TT to define a celestial
        reference frame.
    :cvar JSM: Jovian Solar Magnetospheric - A coordinate system related
        to Jupiter where the x-axis is from Jupiter to Sun, z-axis is
        northward in a plane containing the x-axis and the Jovian dipole
        axis.
    :cvar JSO: Jovian Solar Orbital - A coordinate system related to
        Jupiter where x-axis is anti-sunward and the y-axis points in
        the orbital velocity direction.
    :cvar KSM: Kronian Solar Magnetospheric - A coordinate system
        related to Saturn where the x-axis is anti-sunward, z-axis is
        northward in a plane containing the x-axis and the Kronian
        dipole axis.
    :cvar KSO: Kronian Solar Orbital - A coordinate system related to
        Saturn where x-axis is anti-sunward and the y-axis points in the
        orbital velocity direction.
    :cvar LGM: Local Geomagnetic - A coordinate system used mainly for
        Earth surface or near-Earth surface magnetic field data. The
        x-axis northward from observation point in a geographic
        meridian. The z-axis downward towards center of the Earth. In
        this system, the total horizontal component, H, is equal to
        sqrt(Bx^2+By^2) and declination angle, D is equal to
        arctan(By/Bx).
    :cvar MAG: Geomagnetic - geocentric. The z-axis is parallel to the
        geomagnetic dipole axis, positive north. The x-axis is in the
        plane defined by the z-axis and the rotation axis of the Earth.
        If N is a unit vector from the center of the Earth to the north
        geographic pole, the signs of the y-axis and x-axis are given by
        the vector cross products N cross z and y cross z, respectively,
        see Russell, 1971 and http://cdpp.cnes.fr/00428.pdf.
    :cvar MFA: Magnetic Field Aligned - A coordinate system spacecraft-
        centered system with the z-axis in the direction of the ambient
        magnetic field vector. The x-axis is in the plane defined by the
        z-axis and the spacecraft-Sun line, positive sunward, see
        http://cdpp.cnes.fr/00428.pdf.
    :cvar MSO: Mars/Mercury Solar Orbital A coordinate system related to
        Mars or Mercury. A coordinate system where, depending on the
        body (Mars or Mercury), the x-axis is anti-sunward and the
        y-axis points in the orbital velocity direction.
    :cvar RTN: Radial Tangential Normal. Typically centered at a
        spacecraft. Used for IMF and plasma V vectors. The x-axis
        (radial) is set as the primary-axis, and is defined as the axis
        pointing from the spacecraft to the Sun. The z-axis (tangential)
        is set as the secondary-axis, and is defined as that portion of
        the solar North rotational axis which is perpendicular to the
        primary-axis. The y-axis (normal) is defined as Z cross X.
    :cvar SC: Spacecraft - A coordinate system defined by the spacecraft
        geometry and/or spin. Often has z-axis parallel to spacecraft
        spin vector. The x-axis and y-axis may or may not corotate with
        the spacecraft, see SR and SR2 below.
    :cvar SE: Solar Ecliptic - A heliocentric coordinate system where
        the z-axis is normal to the ecliptic plane, positive northward.
        The x-axis is positive towards the first point of Aries (from
        Earth to Sun at vernal equinox). Same as HAE above, see
        http://nssdc.gsfc.nasa.gov/space/helios/coor_des.htmlr.
    :cvar SM: Solar Magnetic - A geocentric coordinate system where the
        z-axis is northward along dipole axis of the Earth, x-axis is in
        plane of z-axis and Earth-Sun line, positive sunward, see
        Russell, 1971.
    :cvar SPACECRAFT_ORBIT_PLANE: A coordinate system where x-axis lies
        in the plane normal to and in the direction of motion of the
        spacecraft, the z-axis is normal to this plane and the y-axis
        completes the triad to form a right-handed coordinate system.
    :cvar SR: Spin Reference - A special case of a Spacecraft (SC)
        coordinate system for a spinning spacecraft. The z-axis is
        parallel to the spacecraft spin vector. The x-axis and y-axis
        rotate with the spacecraft, see http://cdpp.cnes.fr/00428.pdf.
    :cvar SR2: Spin Reference 2 - A special case of a Spacecraft (SC)
        coordinate system for a spinning spacecraft. The z-axis is
        parallel to the spacecraft spin vector while the x-axis is in
        the plane defined by the z-axis and the spacecraft-Sun line,
        positive sunward, see http://cdpp.cnes.fr/00428.pdf.
    :cvar SSE: Spacecraft Solar Ecliptic - A coordinate system used for
        deep space spacecraft, i.e., consider the Helios spacecraft with
        the x-axis from spacecraft to Sun, the z-axis normal to ecliptic
        plane positive northward. Note that the angle between the normal
        to ecliptic plane and the normal to the Helios orbital plane is
        ~0.25 deg.
    :cvar SSE_L: Selenocentric Solar Ecliptic - The x-axis points from
        the center of the Moon to the Sun, the z-axis is normal to the
        ecliptic plane, positive northward. And the y-axis completes the
        right-handed set of axes.
    :cvar TIIS: Kronian Solar Orbital - A coordinate system related to
        Saturn where the x-axis is anti-sunward and the y-axis points in
        the orbital velocity direction.
    :cvar VSO: Venus Solar Orbital - A coordinate system related to
        Venus where the x-axis is anti-sunward and the y-axis point
        along the orbital velocity direction.
    :cvar WGS84: The World Geodetic System (WGS) defines a reference
        frame for the Earth, for use in geodesy and navigation. The
        WGS84 uses the zero meridian as defined by the Bureau
        International de l'Heure.
    """

    CARRINGTON = "Carrington"
    CGM = "CGM"
    CSO = "CSO"
    DM = "DM"
    ECD = "ECD"
    ECEF = "ECEF"
    ENP = "ENP"
    GEI = "GEI"
    GEO = "GEO"
    GPHIO = "GPHIO"
    GSE = "GSE"
    GSEQ = "GSEQ"
    GSM = "GSM"
    HAE = "HAE"
    HCC = "HCC"
    HCI = "HCI"
    HCR = "HCR"
    HEE = "HEE"
    HEEQ = "HEEQ"
    HERTN = "HERTN"
    HG = "HG"
    HGI = "HGI"
    HGRTN = "HGRTN"
    HPC = "HPC"
    HPR = "HPR"
    HSM = "HSM"
    J2000 = "J2000"
    JSM = "JSM"
    JSO = "JSO"
    KSM = "KSM"
    KSO = "KSO"
    LGM = "LGM"
    MAG = "MAG"
    MFA = "MFA"
    MSO = "MSO"
    RTN = "RTN"
    SC = "SC"
    SE = "SE"
    SM = "SM"
    SPACECRAFT_ORBIT_PLANE = "SpacecraftOrbitPlane"
    SR = "SR"
    SR2 = "SR2"
    SSE = "SSE"
    SSE_L = "SSE_L"
    TIIS = "TIIS"
    VSO = "VSO"
    WGS84 = "WGS84"


@dataclass
class DataExtent:
    """The area of storage in a file system required to store the contents of a
    resource.

    By default, the data extent is expressed in bytes.
    """

    quantity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    per: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Per",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


class DisplayType(Enum):
    """
    Identifiers for types or classes of rendered data.

    :cvar IMAGE: A 2-D representation of data with values at each
        element of the array related to an intensity or a color.
    :cvar PLASMAGRAM: The characterization of signal strengths in active
        sounding measurements as a function of virtual range or signal
        delay time and sounding frequency. A Plasmagram is also referred
        to as an Ionogram.
    :cvar SPECTROGRAM: The characterization of signal strengths as a
        function of frequency (or energy) and time.
    :cvar STACK_PLOT: A representation of data showing multiple sets of
        observations on a single plot, possibly offsetting each plot by
        some uniform amount.
    :cvar TIME_SERIES: A representation of data showing a set of
        observations taken at different points in time and charted as a
        time series.
    :cvar WAVE_FORM: Spatial or temporal variations of wave amplitude
        over wave period time scales.
    """

    IMAGE = "Image"
    PLASMAGRAM = "Plasmagram"
    SPECTROGRAM = "Spectrogram"
    STACK_PLOT = "StackPlot"
    TIME_SERIES = "TimeSeries"
    WAVE_FORM = "WaveForm"


class DocumentType(Enum):
    """
    Identifiers for the characterization of the content or purpose of a document.

    :cvar CONVENTION: A set of agreed, stipulated, or generally accepted
        approaches or methods of adopting a standard or implementing an
        approach.
    :cvar OTHER: Not classified with more specific terms. The context of
        its usage may be described in related text.
    :cvar POLICY: A deliberate system of principles to guide decisions
        and achieve rational outcomes. A policy is a statement of
        intent, and is implemented as a procedure or protocol.
    :cvar POSTER: A set of information arranged on a single page or
        sheet, typically in a large format.
    :cvar PRESENTATION: A set of information that is used when
        communicating to an audience.
    :cvar REPORT: A document which describes the findings of some
        individual or group.
    :cvar SPECIFICATION: A detailed description of the requirements and
        other aspects of an object or component that may be used to
        develop an implementation.
    :cvar TECHNICAL_NOTE: A document summarizing the performance and
        other technical characteristics of a product, machine,
        component, subsystem or software in sufficient detail to be used
        by an engineer or researcher.
    :cvar WHITE_PAPER: An authoritative report giving information or
        proposals on an issue.
    """

    CONVENTION = "Convention"
    OTHER = "Other"
    POLICY = "Policy"
    POSTER = "Poster"
    PRESENTATION = "Presentation"
    REPORT = "Report"
    SPECIFICATION = "Specification"
    TECHNICAL_NOTE = "TechnicalNote"
    WHITE_PAPER = "WhitePaper"


class Encoding(Enum):
    """
    Identifiers for unambiguous rules that establishes the representation of
    information within a file.

    :cvar ASCII: A sequence of characters that adheres to American
        Standard Code for Information Interchange (ASCII) which is a
        7-bit character-coding scheme.
    :cvar BASE64: A data encoding scheme whereby binary-encoded data is
        converted to printable ASCII characters. It is defined as a MIME
        content transfer encoding for use in Internet e-mail. The only
        characters used are the upper-case and lower-case Roman alphabet
        characters (A-z), the numerals (0-9), and the "+" and "/"
        symbols, with the "=" symbol as a special suffix (padding) code.
    :cvar BZIP2: An open standard algorithm by Julian Seward using
        Burrows-Wheeler block sorting and Huffman coding, see
        http://www.bzip.org/.
    :cvar GZIP: An open standard algorithm distributed by GHU based on
        LZ77 and Huffman coding, see
        http://www.gnu.org/software/gzip/gzip.html or
        http://www.gzip.org/.
    :cvar NONE: A lack or absence of anything.
    :cvar S3_BUCKET: A container of objects that comply with the Amazon
        Simple Storage Service (S3) specifications. A bucket has a
        unique, user-assigned key (name). A bucket can contain any
        number of objects with an aggregate size of 5 gigabytes. A
        bucket may be accompanied by up to 2 kilobytes of metadata.
    :cvar TAR: A file format used to collate collections of files into
        one larger file, for distribution or archiving, while preserving
        file system information such as user and group permissions,
        dates, and directory structures. The format was standardized by
        POSIX.1-1988 and later POSIX.1-2001.
    :cvar UNICODE: Text in multi-byte Unicode format.
    :cvar ZIP: An open standard for compression which is a variation of
        the LZW method and was originally used in the PKZIP utility.
    """

    ASCII = "ASCII"
    BASE64 = "Base64"
    BZIP2 = "BZIP2"
    GZIP = "GZIP"
    NONE = "None"
    S3_BUCKET = "S3_BUCKET"
    TAR = "TAR"
    UNICODE = "Unicode"
    ZIP = "ZIP"


@dataclass
class Extension:
    """A container of other metadata which is not part of the SPASE data model.

    The contents of this element are defined by individual usage. The
    organization and content are constrained by the implementation. For
    example, in an XML representation of the SPASE metadata the content
    must conform to the XML specifications.
    """

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
        },
    )


class FieldQuantity(Enum):
    """
    Identifiers for the physical attribute of the field.

    :cvar CURRENT: It is the scalar quantity giving the net charge
        (summed over charged particle species) per unit time flowing
        across a given surface.
    :cvar CURRENT_DENSITY: It is the vector quantity giving the net
        charge (summed over charged particle species) per unit cross-
        sectional area per unit time flowing through a given point.
        Measurements of current density are often provided in terms of
        the magnetic perturbations (superposed upon a background
        magnetic field, if present) associated with the current density.
    :cvar ELECTRIC: The physical attribute that exerts an electrical
        force.
    :cvar ELECTROMAGNETIC: Electric and magnetic field variations in
        time and space that propagate through a medium or a vacuum. The
        wave propagation direction, electric field vector, and magnetic
        field vector form an orthogonal triad. Waves in this category
        are detected by having their field quantities measured.
    :cvar GYROFREQUENCY: The number of gyrations around a magnetic
        guiding center (field line) a charged particle makes per unit
        time due to the Lorentz force.
    :cvar MAGNETIC: The physical attribute attributed to a magnet or its
        equivalent.
    :cvar PLASMA_FREQUENCY: A number density dependent characteristic
        frequency of a plasma.
    :cvar POTENTIAL: The work required per unit charge to move a charge
        from a reference point to a point at infinity (electric
        potential is defined to be zero). The electric potential of a
        spacecraft is often referred to as the spacecraft potential. The
        spacecraft potential is the electric potential of the spacecraft
        relative to the potential of the nearby plasma. The spacecraft
        potential is non-zero because the spacecraft charges to the
        level that the emitted photoelectron flux going to infinity is
        balanced by the plasma electron flux to the spacecraft.
    :cvar POYNTING_FLUX: Electromagnetic energy flux transported by a
        wave characterized as the rate of energy transport per unit area
        per steradian.
    """

    CURRENT = "Current"
    CURRENT_DENSITY = "CurrentDensity"
    ELECTRIC = "Electric"
    ELECTROMAGNETIC = "Electromagnetic"
    GYROFREQUENCY = "Gyrofrequency"
    MAGNETIC = "Magnetic"
    PLASMA_FREQUENCY = "PlasmaFrequency"
    POTENTIAL = "Potential"
    POYNTING_FLUX = "PoyntingFlux"


class Format(Enum):
    """
    Identifiers for data organized according to preset specifications.

    :cvar AVI: Audio Video Interleave (AVI) a digital format for movies
        that conforms to the Microsoft Windows Resource Interchange File
        Format (RIFF).
    :cvar BINARY: A direct representation of the bits which may be
        stored in memory on a computer.
    :cvar CDF: Common Data Format (CDF). A binary storage format
        developed at Goddard Space Flight Center (GSFC).
    :cvar CEF: Cluster Exchange Format (CEF) is a self-documenting ASCII
        format designed for the exchange of data. There are two versions
        of CEF which are not totally compatible.
    :cvar CEF1: Cluster Exchange Format (CEF), version 1, is a self-
        documenting ASCII format designed for the exchange of data. The
        metadata contains information compatible with the ISTP
        recommendations for CDF.
    :cvar CEF2: Cluster Exchange Format (CEF), version 2, is a self-
        documenting ASCII format designed for the exchange of data and
        introduced for Cluster Active Archive. Compared to version 1,
        the metadata description of vectors and tensors is different.
    :cvar CSV: Comma Separated Value - A data exchange format defined by
        RFC 4180.
    :cvar EXCEL: A Microsoft spreadsheet format used to hold a variety
        of data in tables which can include calculations.
    :cvar FITS: Flexible Image Transport System (FITS) is a digital
        format primarily designed to store scientific data sets
        consisting of multi-dimensional arrays (1-D spectra, 2-D images
        or 3-D data cubes) and 2-D tables containing rows and columns of
        data.
    :cvar GIF: Graphic Interchange Format (GIF) first introduced in 1987
        by CompuServe. GIF uses LZW compression and images are limited
        to 256 colors.
    :cvar HARDCOPY: A permanent reproduction, or copy in the form of a
        physical object, of any media suitable for direct use by a
        person.
    :cvar HARDCOPY_FILM: An image recording medium on which usually a
        negative analog image is registered. A positive analog image can
        be recovered or reproduced from film, which is usually made of
        flexible materials for ease of storage and transportation.
    :cvar HARDCOPY_MICROFICHE: A sheet of microfilm on which many pages
        of material have been photographed. A magnification system is
        used to read the material.
    :cvar HARDCOPY_MICROFILM: Film rolls on which materials are
        photographed at greatly reduced size. A magnification system is
        used to read the material.
    :cvar HARDCOPY_PHOTOGRAPH: An image (positive or negative)
        registered on a piece of photo-sensitive paper.
    :cvar HARDCOPY_PHOTOGRAPHIC_PLATE: A rigid (typically glass) medium
        that functions like film. Its rigidity is for guarding against
        image distortion due to medium deformation (caused by heat and
        humidity). Photographic plates are often used for astronomical
        photography.
    :cvar HARDCOPY_PRINT: A sheet of any written or printed material
        which may include notes or graphics. Multiple printed pages may
        be bound into a manuscript or book.
    :cvar HDF: Hierarchical Data Format.
    :cvar HDF4: Hierarchical Data Format, Version 4.
    :cvar HDF5: Hierarchical Data Format, Version 5.
    :cvar HTML: A text file containing structured information
        represented in the Hypertext Mark-up Language (HTML), see
        http://www.w3.org/MarkUp/.
    :cvar IDFS: Instrument Data File Set (IDFS) is a set of files
        written in a prescribed format which contain data, timing data,
        and metadata. IDFS was developed at Southwest Research Institute
        (SwRI).
    :cvar IDL: Interactive Data Language (IDL) save set. IDL is a
        proprietary format.
    :cvar JPEG: A binary format for still images defined by the Joint
        Photographic Experts Group.
    :cvar JSON: JavaScript Object Notation - A lightweight data-
        interchange format.
    :cvar MATLAB_4: MATLAB Workspace save set, version 4. MAT-files are
        double-precision, binary, MATLAB format files. MATLAB is a
        proprietary product of The MathWorks.
    :cvar MATLAB_6: MATLAB Workspace save set, version 6. MAT-files are
        double-precision, binary, MATLAB format files. MATLAB is a
        proprietary product of The MathWorks.
    :cvar MATLAB_7: MATLAB Workspace save set, version 7. MAT-files are
        double-precision, binary, MATLAB format files. Version 7
        includes data compression and Unicode encoding. MATLAB is a
        proprietary product of The MathWorks.
    :cvar MPEG: A digital format for movies defined by the Motion
        Picture Experts Group.
    :cvar NCAR: The National Center for Atmospheric Research (NCAR)
        format. A complete description of that standard is given in
        appendix C of the "Report on Establishment &amp; Operation of
        the Incoherent-Scatter Data Base", dated 1984-08-23, obtainable
        from NCAR, P.O. Box 3000 Boulder, Colorado 80307-3000.
    :cvar NET_CDF: The Network Common Data Form (NetCDF) supported and
        maintained by the Unidata Program Center. A self-describing
        portable data format for array-oriented data access, see
        http://my.unidata.ucar.edu/content/software/netcdf.
    :cvar PDF: A document expressed in the Portable Document Format
        (PDF) as defined by Adobe.
    :cvar PDS4: The Planetary Data System, version 4 (PDS4) standard
        provides guidelines on how a data producer should construct a
        data set suitable for long-term archiving. The standard contains
        a number of requirements in terms of dataset structure and
        documentation that should allow for any PDS compliant data set
        to be used and understood in the long term. Each PDS4 bundle
        consists of two files, one containing the data and the other an
        eXtensible Markup Language (XML) file containing the label. PDS4
        recognises four base data structures, array, table, parse-able
        byte stream and encoded byte stream with arrays and tables most
        commonly in use. The PDS4 standard is described at:
        https://pds.jpl.nasa.gov/datastandards/documents/current-
        version.shtml. The PDS4 archiving standard has been required for
        data archives from NASA-funded planetary missions and for small
        data archives since 2011.
    :cvar PDS3: The. Planetary Data System, version 3 (PDS3) standard
        provides guidelines on how a data producer should construct a
        data set suitable for long-term archiving. The standard contains
        a number of requirements in terms of dataset structure and
        documentation that should allow for any PDS compliant data set
        to be used and understood in the long term. Each PDS3 data
        product must be labeled in ASCII with full details on the
        structure and content of the product. The label can be attached
        to the data file itself or detached in a separate "label" file
        with the suffix LBL. The PDS3 standard is described at:
        https://pds.jpl.nasa.gov/datastandards/pds3/standards/. Since
        2011, PDS3 has superseded by the PDS4 archiving standard.
        However, many data files still exist that are stored by using
        the PDS3 standard.
    :cvar PNG: A digital format for still images. Portable Network
        Graphics (PNG).
    :cvar POSTSCRIPT: A page description programming language created by
        Adobe Systems Inc. that is a device-independent industry
        standard for representing text and graphics.
    :cvar QUICK_TIME: A format for digital movies, as defined by Apple
        Computer, see http://developer.apple.com/quicktime/.
    :cvar RINEX2: Receiver Independent Exchange Format (RINEX) - version
        2.*, is a data interchange format for raw satellite navigation
        system data. https://files.igs.org/pub/data/format/rinex211.txt.
    :cvar RINEX3: Receiver Independent Exchange Format (RINEX) - version
        3.*, is a data interchange format for raw satellite navigation
        system data. https://files.igs.org/pub/data/format/rinex300.pdf.
    :cvar TEXT: A sequence of characters which may have an imposed
        structure or organization.
    :cvar TEXT_ASCII: A sequence of characters that adheres to American
        Standard Code for Information Interchange (ASCII) which is a
        7-bit character-coding scheme.
    :cvar TEXT_UNICODE: Text in multi-byte Unicode format.
    :cvar TFCAT: Time-Frequency Catalogue (TFCat) is a catalogue model
        &amp; transfer format for spectro-temporal features.
        https://gitlab.obspm.fr/maser/catalogues/catalogue-format.
    :cvar TIFF: A binary format for still pictures. Tagged Image Format
        File (TIFF). Originally developed by Aldus and now controlled by
        Adobe.
    :cvar UDF: Universal Data Format (UDF). The Optical Technology
        Storage Association Universal Disk Format, based on ISO 13346,
        see http://www.osta.org/specs/index.htm.
    :cvar VOTABLE: A proposed IVOA standard designed as a flexible
        storage and exchange format for tabular data.
    :cvar XML: eXtensible Mark-up Language (XML). A structured format
        for representing information, see http://www.w3.org/XML/.
    """

    AVI = "AVI"
    BINARY = "Binary"
    CDF = "CDF"
    CEF = "CEF"
    CEF1 = "CEF1"
    CEF2 = "CEF2"
    CSV = "CSV"
    EXCEL = "Excel"
    FITS = "FITS"
    GIF = "GIF"
    HARDCOPY = "Hardcopy"
    HARDCOPY_FILM = "Hardcopy.Film"
    HARDCOPY_MICROFICHE = "Hardcopy.Microfiche"
    HARDCOPY_MICROFILM = "Hardcopy.Microfilm"
    HARDCOPY_PHOTOGRAPH = "Hardcopy.Photograph"
    HARDCOPY_PHOTOGRAPHIC_PLATE = "Hardcopy.PhotographicPlate"
    HARDCOPY_PRINT = "Hardcopy.Print"
    HDF = "HDF"
    HDF4 = "HDF4"
    HDF5 = "HDF5"
    HTML = "HTML"
    IDFS = "IDFS"
    IDL = "IDL"
    JPEG = "JPEG"
    JSON = "JSON"
    MATLAB_4 = "MATLAB_4"
    MATLAB_6 = "MATLAB_6"
    MATLAB_7 = "MATLAB_7"
    MPEG = "MPEG"
    NCAR = "NCAR"
    NET_CDF = "NetCDF"
    PDF = "PDF"
    PDS4 = "PDS4"
    PDS3 = "PDS3"
    PNG = "PNG"
    POSTSCRIPT = "Postscript"
    QUICK_TIME = "QuickTime"
    RINEX2 = "RINEX2"
    RINEX3 = "RINEX3"
    TEXT = "Text"
    TEXT_ASCII = "Text.ASCII"
    TEXT_UNICODE = "Text.Unicode"
    TFCAT = "TFCat"
    TIFF = "TIFF"
    UDF = "UDF"
    VOTABLE = "VOTable"
    XML = "XML"


@dataclass
class Funding:
    """
    The source of financial support (funding) for the resource.
    """

    agency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Agency",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    project: Optional[str] = field(
        default=None,
        metadata={
            "name": "Project",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    award_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AwardNumber",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


class HashFunction(Enum):
    """
    Identifiers for functions or algorithms that convert a digital data object into
    a hash value.

    :cvar MD5: Message Digest 5 (MD5) is a 128-bit message digest
        algorithm created in 1991 by Professor Ronald Rivest.
    :cvar SHA1: Secure Hash Algorithm (SHA), a 160-bit message digest
        algorithm developed by the NSA and described in Federal
        Information Processing Standard (FIPS) publication 180-1.
    :cvar SHA256: Secure Hash Algorithm (SHA), a 256-bit message digest
        algorithm developed by the NSA and described in Federal
        Information Processing Standard (FIPS) publication 180-1.
    """

    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"


@dataclass
class InformationUrl:
    """
    Attributes of the method of acquiring additional information.
    """

    class Meta:
        name = "InformationURL"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class InputProperty:
    """
    A container of attributes regarding an input property of an application.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_min: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_max: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMax",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


class InstrumentType(Enum):
    """Identifiers for the type of experiment the instrument performs.

    This is the technique of observation.

    :cvar ANTENNA: A sensor used to measure electric potential.
    :cvar CHANNELTRON: An instrument that detects electrons, ions, and
        ultraviolet radiation, according to the principle of a secondary
        emission multiplier. It is typically used in electron
        spectroscopy and mass spectrometry.
    :cvar CORONOGRAPH: An instrument which can image things very close
        to the Sun by using a disk to block the bright surface of the
        sun or a star that reveals the faint corona of the Sun or other
        celestial objects.
    :cvar DOUBLE_SPHERE: A dipole antenna of which the active (sensor)
        elements are small spheres located at the ends of two wires
        deployed in the equatorial plane, on opposite sides of a
        spinning spacecraft.
    :cvar DUST_DETECTOR: An instrument which determines the mass and
        speed of ambient dust particles.
    :cvar ELECTRON_DRIFT_INSTRUMENT: An active experiment to measure the
        electron drift velocity based on sensing the displacement of a
        weak beam of electrons after one gyration in the ambient
        magnetic field.
    :cvar ELECTROSTATIC_ANALYSER: An instrument which uses charged
        plates to analyze the mass, charge and kinetic energies of
        charged particles which enter the instrument.
    :cvar ENERGETIC_PARTICLE_INSTRUMENT: An instrument that measures
        fluxes of charged particles as a function of time, direction of
        motion, mass, charge and/or species.
    :cvar EXPERIMENT: A collection of components which are designed to
        make coordinated observations of a phenomenon or object.
        Projects and missions may refer to an "experiment" by other
        names such as a "suite".
    :cvar FARADAY_CUP: An instrument consisting of an electrode from
        which electrical current is measured while a charged particle
        beam (electrons or ions) impinges on it. Used to determine
        energy spectrum and sometimes ion composition of the impinging
        particles.
    :cvar FLUX_FEEDBACK: A search coil whose bandwidth and signal/noise
        ratio are increased by the application of negative feedback at
        the sensor (flux) level by driving a collocated coil with a
        signal from the preamplifier.
    :cvar FOURIER_TRANSFORM_SPECTROGRAPH: An instrument that determines
        the spectra of a radiative source, using time domain
        measurements and a Fourier transform.
    :cvar GEIGER_MUELLER_TUBE: An instrument which measures density of
        ionizing radiation based on interactions with a gas.
    :cvar IMAGER: An instrument which samples the radiation from an area
        at one or more spectral ranges emitted or reflected by an
        object.
    :cvar IMAGING_SPECTROMETER: An instrument which is a multispectral
        scanner with a very large number of channels (typically from 64
        channels up to 256 channels) with very narrow bandwidths.
    :cvar INTERFEROMETER: An instrument to study the properties of two
        or more waves from the pattern of interference created by their
        superposition.
    :cvar ION_CHAMBER: A device in which the collected electrical charge
        from ionization in a gas-filled cavity is taken to be the
        proportion to some parameter (e.g., dose or exposure) of
        radiation field.
    :cvar ION_DRIFT: A device which measures the current produced by the
        displacement of ambient ions on a grid, thereby allowing the
        determination of the ion trajectory and velocity.
    :cvar ION_GAUGE: A device which measures low-pressure or vacuum
        neutral gas with pressures ranging from 10^-3 Torr to 10^-10
        Torr. An ion gauge is an electronic amplifying vacuum tube
        consisting of three electrodes inside an evacuated glass
        envelope, with the filament being the cathode.
    :cvar LANGMUIR_PROBE: A monopole antenna associated with an
        instrument. The instrument applies a potential to the antenna
        which is swept to determine the voltage/current characteristic.
        This provides information about the plasma surrounding the probe
        and spacecraft.
    :cvar LONG_WIRE: A dipole antenna constructed by two active sensing
        elements that are wires deployed in the equatorial plane on
        opposite sides of a spinning spacecraft. The, wire length is
        usually several times the spacecraft diameter.
    :cvar MAGNETOGRAPH: A special type of magnetometer that records a
        time plot of the local magnetic field near the instrument or a
        telescope capable of determining the magnetic field strength
        and/or direction on a distant object such as the Sun, using the
        Zeeman splitting or other spectral signatures of magnetization.
    :cvar MAGNETOMETER: An instrument which measures the ambient
        magnetic field.
    :cvar MASS_SPECTROMETER: An instrument which distinguishes chemical
        species in terms of their different isotopic masses.
    :cvar MICROCHANNEL_PLATE: An instrument used for the detection of
        elementary particles, ions, ultraviolet rays and soft X-rays
        constructed from very thin conductive glass capillaries.
    :cvar MULTISPECTRAL_IMAGER: An instrument which captures images at
        multiple spectral ranges.
    :cvar NEUTRAL_ATOM_IMAGER: An instrument which measures the quantity
        and properties of neutral particles over a range of angles.
        Measured properties can include mass and energy.
    :cvar NEUTRAL_PARTICLE_DETECTOR: An instrument which measures the
        quantity and properties of neutral particles. Measured
        properties can include mass and plasma bulk densities.
    :cvar PARTICLE_CORRELATOR: An instrument which correlates particle
        flux to help identify wave/particle interactions.
    :cvar PARTICLE_DETECTOR: An instrument which detects particle
        flux!!!.
    :cvar PHOTOMETER: An instrument which measures the strength of
        electromagnetic radiation within a spectral band which can range
        from ultraviolet to infrared and includes the visible spectrum.
    :cvar PHOTOMULTIPLIER_TUBE: A vacuum phototube that is an extremely
        sensitive detector of light in the ultraviolet, visible, and
        near-infrared ranges of the electromagnetic spectrum.
    :cvar PHOTOPOLARIMETER: An instrument which measures the intensity
        and polarization or radiant energy. A photopolarimeter is a
        combination of a photometer and a polarimeter.
    :cvar PLATFORM: A collection of components which can be positioned
        and oriented as a single unit. A platform may contain other
        platforms. For example, a spacecraft is a platform which may
        have components that can be articulated and are also considered
        platforms.
    :cvar PROPORTIONAL_COUNTER: An instrument which measures energy of
        ionization radiation based on interactions with a gas.
    :cvar QUADRISPHERICAL_ANALYSER: An instrument used for the 3-D
        detection of plasma, energetic electrons and ions, and for
        positive ion composition measurements.
    :cvar RADAR: An instrument that uses directional properties of
        returned power to infer spatial and/or other characteristics of
        a remote object.
    :cvar RADIOMETER: An instrument for detecting or measuring radiant
        energy. Radiometers are commonly limited to infrared radiation.
    :cvar RESONANCE_SOUNDER: A combination of a radio receiver and a
        pulsed transmitter used to study the plasma surrounding a
        spacecraft by identifying resonances or cut-offs (of the wave
        dispersion relation), whose frequencies are related to the
        ambient plasma density and magnetic field. When the transmitter
        is off it is essentially a high-frequency resolution spectral
        power receiver.
    :cvar RETARDING_POTENTIAL_ANALYSER: An instrument which measures ion
        temperatures and ion concentrations using a planar ion trap.
    :cvar RIOMETER: An instrument which measures the signal strength in
        various directions of the galactic radio signals. Variations in
        these signals are influenced by solar flare activity and
        geomagnetic storm and substorm processes.
    :cvar SCINTILLATION_DETECTOR: An instrument which detects
        fluorescence of a material which is excited by high-energy
        (ionizing) electromagnetic or charged particle radiation.
    :cvar SEARCH_COIL: An instrument which measures the time variation
        of the magnetic flux threading a loop by measurement of the
        electric potential difference induced between the ends of the
        wire.
    :cvar SOLID_STATE_DETECTOR: A detector of the charge carriers
        (electrons and holes) generated in semiconductors by energy
        deposited by gamma ray photons. Also known as a semiconductor
        detector".
    :cvar SOUNDER: An instrument which measures the radiances from an
        object. A sounder may measure radiances at multiple spectral
        ranges.
    :cvar SPACECRAFT_POTENTIAL_CONTROL: An instrument to control the
        electric potential of a spacecraft with respect to the ambient
        plasma by emitting a variable current of positive ions.
    :cvar SPECTRAL_POWER_RECEIVER: A radio receiver which determines the
        power spectral density of the electric or magnetic field, or
        both, at one or more frequencies.
    :cvar SPECTROMETER: An instrument that measures the component
        wavelengths of light (or other electromagnetic radiation) by
        splitting the light up into its component wavelengths.
    :cvar TIME_OF_FLIGHT: An instrument which measures the time it takes
        for a particle to travel between two detectors.
    :cvar UNSPECIFIED: A value which is not provided.
    :cvar WAVEFORM_RECEIVER: A radio receiver which outputs the value of
        one or more components of the electric and/or magnetic field as
        a function of time.
    """

    ANTENNA = "Antenna"
    CHANNELTRON = "Channeltron"
    CORONOGRAPH = "Coronograph"
    DOUBLE_SPHERE = "DoubleSphere"
    DUST_DETECTOR = "DustDetector"
    ELECTRON_DRIFT_INSTRUMENT = "ElectronDriftInstrument"
    ELECTROSTATIC_ANALYSER = "ElectrostaticAnalyser"
    ENERGETIC_PARTICLE_INSTRUMENT = "EnergeticParticleInstrument"
    EXPERIMENT = "Experiment"
    FARADAY_CUP = "FaradayCup"
    FLUX_FEEDBACK = "FluxFeedback"
    FOURIER_TRANSFORM_SPECTROGRAPH = "FourierTransformSpectrograph"
    GEIGER_MUELLER_TUBE = "GeigerMuellerTube"
    IMAGER = "Imager"
    IMAGING_SPECTROMETER = "ImagingSpectrometer"
    INTERFEROMETER = "Interferometer"
    ION_CHAMBER = "IonChamber"
    ION_DRIFT = "IonDrift"
    ION_GAUGE = "IonGauge"
    LANGMUIR_PROBE = "LangmuirProbe"
    LONG_WIRE = "LongWire"
    MAGNETOGRAPH = "Magnetograph"
    MAGNETOMETER = "Magnetometer"
    MASS_SPECTROMETER = "MassSpectrometer"
    MICROCHANNEL_PLATE = "MicrochannelPlate"
    MULTISPECTRAL_IMAGER = "MultispectralImager"
    NEUTRAL_ATOM_IMAGER = "NeutralAtomImager"
    NEUTRAL_PARTICLE_DETECTOR = "NeutralParticleDetector"
    PARTICLE_CORRELATOR = "ParticleCorrelator"
    PARTICLE_DETECTOR = "ParticleDetector"
    PHOTOMETER = "Photometer"
    PHOTOMULTIPLIER_TUBE = "PhotomultiplierTube"
    PHOTOPOLARIMETER = "Photopolarimeter"
    PLATFORM = "Platform"
    PROPORTIONAL_COUNTER = "ProportionalCounter"
    QUADRISPHERICAL_ANALYSER = "QuadrisphericalAnalyser"
    RADAR = "Radar"
    RADIOMETER = "Radiometer"
    RESONANCE_SOUNDER = "ResonanceSounder"
    RETARDING_POTENTIAL_ANALYSER = "RetardingPotentialAnalyser"
    RIOMETER = "Riometer"
    SCINTILLATION_DETECTOR = "ScintillationDetector"
    SEARCH_COIL = "SearchCoil"
    SOLID_STATE_DETECTOR = "SolidStateDetector"
    SOUNDER = "Sounder"
    SPACECRAFT_POTENTIAL_CONTROL = "SpacecraftPotentialControl"
    SPECTRAL_POWER_RECEIVER = "SpectralPowerReceiver"
    SPECTROMETER = "Spectrometer"
    TIME_OF_FLIGHT = "TimeOfFlight"
    UNSPECIFIED = "Unspecified"
    WAVEFORM_RECEIVER = "WaveformReceiver"


class MeasurementType(Enum):
    """
    Identifiers for the method of making an estimated value of a quantity that
    forms the basis of an observation.

    :cvar ACTIVITY_INDEX: An indication, derived from one or more
        measurements, of the level of activity of an object or region,
        such as sunspot number, F10.7 flux, Dst, or the Polar Cap
        Indices.
    :cvar DOPPLERGRAM: A map or image depicting the spatial distribution
        of line-of-sight velocities of the observed object.
    :cvar DUST: Free microscopic particles of solid material.
    :cvar ELECTRIC_FIELD: A region of space around a charged particle,
        or between two voltages within which a force is exerted on
        charged objects in its vicinity. An electric field is the
        electric force per unit charge.
    :cvar ENERGETIC_PARTICLES: Pieces of matter that are moving very
        fast. Energetic particles include protons, electrons, neutrons,
        neutrinos, the nuclei of atoms, and other sub-atomic particles.
    :cvar EPHEMERIS: The spatial coordinates of a body as a function of
        time. When used as an Instrument Type it represents the process
        or methods used to generate spatial coordinates.
    :cvar IMAGE_INTENSITY: Measurements of the 2-D distribution of the
        intensity of photons from some region or object such as the Sun
        or the polar auroral regions, can be in any wavelength band, and
        polarized, etc.
    :cvar INSTRUMENT_STATUS: A quantity directly related to the
        operation or function of an instrument.
    :cvar ION_COMPOSITION: In situ measurements of the relative flux or
        density of electrically charged particles in the space
        environment. May give simple fluxes, but full distribution
        functions are sometimes measured.
    :cvar IRRADIANCE: A radiometric term for the power of
        electromagnetic radiation at a surface, per unit area.
        Irradiance is used when the electromagnetic radiation is
        incident on the surface. Irradiance data may be reported in any
        units (i.e., counts/s) due to, for example, being at a
        particular wavelength, or to being a not fully calibrated
        relative measurement.
    :cvar MAGNETIC_FIELD: A region of space near a magnetized body where
        magnetic forces can be detected (as measured by methods such as
        Zeeman splitting, etc.).
    :cvar MAGNETOGRAM: Measurements of the vector or line-of-sight
        magnetic field determined from remote sensing measurements of
        the detailed structure of spectral lines, including their
        splitting and polarization.
    :cvar NEUTRAL_ATOM_IMAGES: Measurements of neutral atom fluxes as a
        function of look direction often related to remote energetic
        charged particles that lose their charge through charge-exchange
        and then reach the detector on a line-of-sight trajectory.
    :cvar NEUTRAL_GAS: Measurements of neutral atomic and molecular
        components of a gas.
    :cvar PROFILE: Measurements of a quantity as a function of height
        above an object such as the limb of a body.
    :cvar RADIANCE: A radiometric measurement that describes the amount
        of electromagnetic radiation that passes through or is emitted
        from a particular area, and falls within a given solid angle in
        a specified direction. They are used to characterize both
        emission from diffuse sources and reflection from diffuse
        surfaces.
    :cvar SPECTRUM: The distribution of a characteristic of a physical
        system or phenomenon, such as the energy emitted by a radiant
        source, arranged in the order of wavelengths.
    :cvar SPICE: SPICE is an ancillary information system that provides
        scientists and engineers the capability to include space
        geometry and event data into mission design, science observation
        planning, and science data analysis software. The staff of the
        NASA Navigation and Ancillary Information Facility, NAIF, which
        is located at JPL provides SPICE support for planetary,
        heliophysics, and Earth science missions, see
        https://naif.jpl.nasa.gov/naif/index.html. This SPICE has been
        adapted from text on NAF hosted web pages.
    :cvar THERMAL_PLASMA: Measurements of the plasma in the energy
        regime where the most of the plasma occurs. May be the basic
        fluxes in the form of distribution functions or the derived bulk
        parameters (density, flow velocity, etc.).
    :cvar WAVES: Data resulting from observations of wave experiments
        and natural wave phenomena. Wave experiments are typically
        active and natural wave phenomena are passive. Examples of wave
        experiments include coherent/incoherent scatter radars, radio
        soundings, VLF propagation studies, ionospheric scintillation of
        beacon satellite signals, etc. Examples of natural wave
        phenomena include micropulsations, mesospheric gravity waves,
        auroral/plasmaspheric hiss, Langmuir waves, AKR, Jovian
        decametric radiation, solar radio bursts, etc.
    :cvar WAVES_ACTIVE: Exerting an influence or producing a change or
        effect. An active measurement is one which produces a
        transmission or excitation as a part of the measurement cycle.
    :cvar WAVES_PASSIVE: Movement or effect produced by outside
        influence. A passive measurement is one which does not produce a
        transmission or excitation as a part of the measurement cycle.
    """

    ACTIVITY_INDEX = "ActivityIndex"
    DOPPLERGRAM = "Dopplergram"
    DUST = "Dust"
    ELECTRIC_FIELD = "ElectricField"
    ENERGETIC_PARTICLES = "EnergeticParticles"
    EPHEMERIS = "Ephemeris"
    IMAGE_INTENSITY = "ImageIntensity"
    INSTRUMENT_STATUS = "InstrumentStatus"
    ION_COMPOSITION = "IonComposition"
    IRRADIANCE = "Irradiance"
    MAGNETIC_FIELD = "MagneticField"
    MAGNETOGRAM = "Magnetogram"
    NEUTRAL_ATOM_IMAGES = "NeutralAtomImages"
    NEUTRAL_GAS = "NeutralGas"
    PROFILE = "Profile"
    RADIANCE = "Radiance"
    SPECTRUM = "Spectrum"
    SPICE = "SPICE"
    THERMAL_PLASMA = "ThermalPlasma"
    WAVES = "Waves"
    WAVES_ACTIVE = "Waves.Active"
    WAVES_PASSIVE = "Waves.Passive"


class MixedQuantity(Enum):
    """
    Identifiers for the combined attributes of a mixed parameter quantity.

    :cvar AKASOFU_EPSILON: A measure of the magnetopause energy flux and
        an indicator of the solar wind power available for subsequent
        magnetospheric energization. Defined as: V*B^2*l^2sin(theta/2)^4
        where B is the IMF, l is an empirical scaling parameter equal to
        7 R&lt;sub&gt;E&lt;/sub&gt;, and theta=tan(By/Bz)^-1 the IMF
        clock angle.
    :cvar ALFVEN_MACH_NUMBER: The ratio of the bulk flow speed to the
        Alfven speed.
    :cvar ALFVEN_VELOCITY: Phase velocity of the Alfven wave. In SI
        units it is the velocity of the magnetic field divided by the
        square root of the mass density times the permeability of free
        space (&amp;mu;&lt;sub&gt;0&lt;/sub&gt;).
    :cvar FREQUENCY_TO_GYROFREQUENCY_RATIO: The ratio of the
        characteristic frequency of a medium to gyrofrequency of a
        particle.
    :cvar IMFCLOCK_ANGLE: The clockwise angle of the direction of
        interplanetary magnetic field (IMF) measured in the plane of the
        body pole perpendicular to the line between the body and the
        Sun.
    :cvar MAGNETOSONIC_MACH_NUMBER: The ratio of the velocity of fast
        mode waves to the Alfven velocity.
    :cvar OTHER: Not classified with more specific terms. The context of
        its usage may be described in related text.
    :cvar PLASMA_BETA: The ratio of the plasma pressure (nkT) to the
        magnetic pressure (B^2/2&amp;mu;&lt;sub&gt;0&lt;/sub&gt;) in a
        single component plasma or the ratio of the plasma pressure sum
        over i of (n&lt;sub&gt;i&lt;/sub&gt;kT&lt;sub&gt;i&lt;/sub&gt;)
        for all species i to the magnetic pressure
        (B^2/2&amp;mu;&lt;sub&gt;0&lt;/sub&gt;) in a multi components
        plasma.
    :cvar SOLAR_UVFLUX: The amount of ultraviolet energy originating
        from the Sun passing through a unit area in a unit time.
    :cvar TOTAL_PRESSURE: In an MHD fluid it is the number density (N)
        times Boltzmann constant times the temperature in Kelvin.
    :cvar VCROSS_B: The cross product of the charge velocity (V) and the
        magnetic field (B). It is the electric field exerted on a point
        charge by a magnetic field.
    """

    AKASOFU_EPSILON = "AkasofuEpsilon"
    ALFVEN_MACH_NUMBER = "AlfvenMachNumber"
    ALFVEN_VELOCITY = "AlfvenVelocity"
    FREQUENCY_TO_GYROFREQUENCY_RATIO = "FrequencyToGyrofrequencyRatio"
    IMFCLOCK_ANGLE = "IMFClockAngle"
    MAGNETOSONIC_MACH_NUMBER = "MagnetosonicMachNumber"
    OTHER = "Other"
    PLASMA_BETA = "PlasmaBeta"
    SOLAR_UVFLUX = "SolarUVFlux"
    TOTAL_PRESSURE = "TotalPressure"
    VCROSS_B = "VCrossB"


@dataclass
class ModelSpecification:
    """Descriptor of model specifications: type of numerical scheme, versions, etc."""

    model_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModelID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    version_tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "VersionTag",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


class ModelType(Enum):
    """
    A characterization of the numerical scheme used in the model.

    :cvar EMPIRICAL: Information obtained through observation,
        experiment, or experience.
    :cvar HYBRID: A numerical scheme modeling ions as particles and
        electrons as a fluid.
    :cvar MHD: Hydrodynamic waves in a magnetized plasma in which the
        background magnetic field plays a key role in controlling the
        wave propagation characteristics.
    :cvar PIC: A numerical scheme modeling ions and electrons as
        macroparticles.
    :cvar PARABOLOID: A shape generated by the rotation of a parabola
        around its axis of symmetry.
    :cvar TEST_PARTICLE: A numerical scheme modeling the motion of
        charged particles in a prescribed field.
    """

    EMPIRICAL = "Empirical"
    HYBRID = "Hybrid"
    MHD = "MHD"
    PIC = "PIC"
    PARABOLOID = "Paraboloid"
    TEST_PARTICLE = "TestParticle"


@dataclass
class ModelVersion:
    """
    The version number of the model.
    """

    version_tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "VersionTag",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    release_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReleaseDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


class ModeledRegion(Enum):
    """
    Identifiers for areas of the physical world which may be occupied or observed.

    :cvar ASTEROID: A small extraterrestrial body consisting mostly of
        rock and metal that is in orbit around the Sun.
    :cvar CALLISTO: A second largest moon of Jupiter and the third
        largest moon in the solar system.
    :cvar COMET: A relatively small extraterrestrial body consisting of
        a frozen mass that travels around the Sun in a highly elliptical
        orbit.
    :cvar COMET_1_PHALLEY: 1P/Halley, is a short-period comet visible
        from Earth every 75 to 79 years. The comet was visited by the
        Halley Armada comprised of the ESA Giotto, Japanese Suisei and
        Sekigake, and Soviet Union Vega 1 and Vega 2 spacecraft in 1986.
    :cvar COMET_26_PGRIGG_SKJELLERUP: 26P/Grigg-Skjellerup is a periodic
        comet. It was visited by the ESA Giotto spacecraft in July 1992.
    :cvar COMET_67_PCHURYUMOV_GERASIMENKO: 67P/Churyumov-Gerasimenko is
        a Jupiter-family comet originally from the Kuiper belt. The ESA
        Rosetta spacecraft rendezvoused with Comet 67P on August 6, 2014
        and then orbited the comet from September 10, 2014 to September
        30, 2016. Philae, a lander carried by Rosetta, touched down on
        the comet surface on November 12, 2014.
    :cvar EARTH: The third planet from the Sun in our solar system.
    :cvar EARTH_MAGNETOSHEATH: The region between the bow shock and the
        magnetopause, characterized by very turbulent plasma.
    :cvar EARTH_MAGNETOSPHERE: The region of space above the atmosphere
        or surface of the planet and bounded by the magnetopause that is
        under the direct influence of the magnetic field of a planetary
        body.
    :cvar EARTH_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar EARTH_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar EARTH_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar EARTH_MAGNETOSPHERE_POLAR: The region near the pole of a body.
        For a magnetosphere the polar region is the area where magnetic
        field lines are open and includes the auroral zone.
    :cvar EARTH_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar EARTH_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar EARTH_MOON: The only natural satellite of the Earth.
    :cvar EARTH_NEAR_SURFACE: The gaseous and possibly ionized
        environment of a body extending from the surface to some
        specified altitude. For the Earth, this altitude is 2000 km.
    :cvar EARTH_NEAR_SURFACE_ATMOSPHERE: The neutral gases surrounding a
        body that extends from the surface and is bound to the body by
        virtue of the gravitational attraction.
    :cvar EARTH_NEAR_SURFACE_AURORAL_REGION: The region in the
        atmospheric where electrically-charged particles bombarding the
        upper atmosphere of a planet in the presence of a magnetic field
        produce an optical phenomenon.
    :cvar EARTH_NEAR_SURFACE_EQUATORIAL_REGION: A region centered on the
        equator and limited in latitude by approximately 23 deg north
        and south of the equator.
    :cvar EARTH_NEAR_SURFACE_IONOSPHERE: The charged or ionized gases
        surrounding a body that are nominally bound to the body by
        virtue of the gravitational attraction.
    :cvar EARTH_NEAR_SURFACE_IONOSPHERE_DREGION: The layer of the
        ionosphere that exists approximately 50 km to 95 km above the
        surface of the Earth. One of several layers in the ionosphere.
    :cvar EARTH_NEAR_SURFACE_IONOSPHERE_EREGION: A layer of ionized gas
        occurring at 90 km to 150 km above the ground. One of several
        layers in the ionosphere. Also called the Kennelly-Heaviside
        layer.
    :cvar EARTH_NEAR_SURFACE_IONOSPHERE_FREGION: A layer that contains
        ionized gases at a height of around 150-800 km above sea level,
        placing it in the thermosphere. the F region has the highest
        concentration of free electrons and ions anywhere in the
        atmosphere. It may be thought of as comprising two layers, the
        F1 layer and F2 layer. One of several layers in the ionosphere.
        Also known as the Appleton layer.
    :cvar EARTH_NEAR_SURFACE_IONOSPHERE_TOPSIDE: The region at the upper
        most areas of the ionosphere.
    :cvar EARTH_NEAR_SURFACE_MESOSPHERE: The layer of the atmosphere
        that extends from the Stratosphere to a range of 80 km to 85 km,
        temperature decreasing with height.
    :cvar EARTH_NEAR_SURFACE_MID_LATITUDE_REGION: When considering the
        case of the Earth, the mid-latitude region typically refers to
        two latitudinal bands, one in the northern hemisphere and the
        other in the southern hemisphere extending from about 23 deg to
        50 deg. The concept of mid-latitude regions does not apply to
        all bodies in the solar system and different latitudinal ranges
        would apply for each body case by case. The mid-latitude regions
        may be defined by using either planetographic or magnetic
        coordinates if the magnetic dipole is closely aligned with the
        spin axis of a magnetized body. Ground magnetometers located at
        mid-latitude on the Earth are well positioned to measure
        magnetic storm-time ring current variations.
    :cvar EARTH_NEAR_SURFACE_PLASMASPHERE: A region of the magnetosphere
        consisting of low energy (cool) plasma. It is located above the
        ionosphere. The outer boundary of the plasmasphere is known as
        the plasmapause, which is defined by an order of magnitude drop
        in plasma density.
    :cvar EARTH_NEAR_SURFACE_POLAR_CAP: The areas of the globe
        surrounding the poles and consisting of the region north of 60
        deg north latitude and the region south of 60 deg south
        latitude.
    :cvar EARTH_NEAR_SURFACE_SOUTH_ATLANTIC_ANOMALY_REGION: The region
        where the inner Van Allen radiation belt makes its closest
        approach to the surface of the Earth. The result is that, for a
        given altitude, the radiation intensity is higher over this
        region than elsewhere.
    :cvar EARTH_NEAR_SURFACE_STRATOSPHERE: The layer of the atmosphere
        that extends from the troposphere to about 30 km, temperature
        increases with height. The stratosphere contains the ozone
        layer.
    :cvar EARTH_NEAR_SURFACE_SUB_AURORAL_REGION: When considering the
        case of the Earth, the sub-auroral region typically refers to
        two latitudinal bands, one in the northern hemisphere and the
        other in the southern hemisphere extending from about 50 deg to
        low 60 deg latitude. The concept sub-auroral regions does not
        apply to all bodies in the solar system and different
        latitudinal ranges would apply for each body case by case. The
        sub-auroral regions may be defined by using either
        planetographic or magnetic coordinates if the magnetic dipole is
        closely aligned with the spin axis of a magnetized body. Ground
        magnetometers located at sub-auroral latitudes on the Earth
        measure a mixture of activity driven by auroral zone currents
        and the ring current.
    :cvar EARTH_NEAR_SURFACE_THERMOSPHERE: The layer of the atmosphere
        that extends from the Mesosphere to 640+ km, temperature
        increasing with height.
    :cvar EARTH_NEAR_SURFACE_TROPOSPHERE: The lowest layer of the
        atmosphere which begins at the surface and extends to between 7
        km (4.4 mi) at the poles and 17 km (10.6 mi) at the equator,
        with some variation due to weather factors.
    :cvar EARTH_SURFACE: The outermost area of a solid object.
    :cvar ENCELADUS: The sixth largest moon of Saturn. It is currently
        endogenously active. The smallest known body in the Solar System
        that is geologically active today.
    :cvar EUROPA: The sixth closest round moon of Jupiter.
    :cvar GANYMEDE: The biggest moon of Jupiter and in the solar system.
    :cvar HELIOSPHERE: The solar atmosphere extending roughly from the
        outer corona to the edge of the solar plasma at the heliopause
        separating primarily solar plasma from interstellar plasma.
    :cvar HELIOSPHERE_HELIOSHEATH: The region extending radially outward
        from the heliospheric termination shock and in which the
        decelerated solar wind plasma is still significant.
    :cvar HELIOSPHERE_INNER: The region of the heliosphere extending
        radially outward from the solar coronal base to just inside 1
        AU.
    :cvar HELIOSPHERE_NEAR_EARTH: The heliospheric region near the Earth
        which extends to and includes the area near the L1 and L2
        Lagrange point.
    :cvar HELIOSPHERE_OUTER: The region of the heliosphere extending
        radially outward from just outside 1 AU to the heliospheric
        termination shock.
    :cvar HELIOSPHERE_REMOTE1_AU: A roughly toroidal region that
        includes the orbit of the Earth, but exclusive of the region
        near the Earth.
    :cvar INCIDENT: Direction-dependent property.
    :cvar INTERSTELLAR: The region between stars outside of any stellar
        heliopause.
    :cvar IO: The innermost of the four round moons of the planet
        Jupiter.
    :cvar JUPITER: The fifth planet from the Sun in our solar system.
    :cvar JUPITER_CALLISTO: A second largest moon of Jupiter and the
        third largest moon in the solar system.
    :cvar JUPITER_EUROPA: The sixth closest round moon of Jupiter.
    :cvar JUPITER_GANYMEDE: The biggest moon of Jupiter and in the solar
        system.
    :cvar JUPITER_IO: The innermost of the four round moons of the
        planet Jupiter.
    :cvar JUPITER_MAGNETOSPHERE: The region of space above the
        atmosphere or surface of the planet and bounded by the
        magnetopause that is under the direct influence of the magnetic
        field of a planetary body.
    :cvar JUPITER_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar JUPITER_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar JUPITER_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar JUPITER_MAGNETOSPHERE_POLAR: The region near the pole of a
        body. For a magnetosphere the polar region is the area where
        magnetic field lines are open and includes the auroral zone.
    :cvar JUPITER_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar JUPITER_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar MARS: The fourth planet from the Sun in our solar system.
    :cvar MARS_DEIMOS: The smaller and outermost of the two natural
        satellites of Mars.
    :cvar MARS_MAGNETOSPHERE: The region of space above the atmosphere
        or surface of the planet and bounded by the magnetopause that is
        under the direct influence of the magnetic field of a planetary
        body.
    :cvar MARS_MAGNETOSPHERE_MAGNETOTAIL: The region of space within the
        magnetosphere of a magnetized planetary body where the nightside
        magnetic field is stretched out in the anti-stellar direction by
        stellar wind interaction into a windsock-like shape. For Earth,
        solar wind-magnetosphere interaction produces a magnetotail that
        extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar MARS_MAGNETOSPHERE_MAIN: The region of the magnetosphere where
        the magnetic field lines are closed, but does not include the
        gaseous region gravitationally bound to the body.
    :cvar MARS_MAGNETOSPHERE_PLASMASPHERE: A region of the magnetosphere
        consisting of low energy (cool) plasma. It is located above the
        ionosphere. The outer boundary of the plasmasphere is known as
        the plasmapause, which is defined by an order of magnitude drop
        in plasma density.
    :cvar MARS_MAGNETOSPHERE_POLAR: The region near the pole of a body.
        For a magnetosphere the polar region is the area where magnetic
        field lines are open and includes the auroral zone.
    :cvar MARS_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar MARS_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar MARS_PHOBOS: The larger and inner most moon of Mars.
    :cvar MERCURY: The first planet from the Sun in our solar system.
    :cvar MERCURY_MAGNETOSPHERE: The region of space above the
        atmosphere or surface of the planet and bounded by the
        magnetopause that is under the direct influence of the magnetic
        field of a planetary body.
    :cvar MERCURY_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar MERCURY_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar MERCURY_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar MERCURY_MAGNETOSPHERE_POLAR: The region near the pole of a
        body. For a magnetosphere the polar region is the area where
        magnetic field lines are open and includes the auroral zone.
    :cvar MERCURY_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar MERCURY_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar NEPTUNE: The seventh planet from the Sun in our solar system.
    :cvar NEPTUNE_MAGNETOSPHERE: The region of space above the
        atmosphere or surface of the planet and bounded by the
        magnetopause that is under the direct influence of the magnetic
        field of a planetary body.
    :cvar NEPTUNE_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar NEPTUNE_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar NEPTUNE_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar NEPTUNE_MAGNETOSPHERE_POLAR: The region near the pole of a
        body. For a magnetosphere the polar region is the area where
        magnetic field lines are open and includes the auroral zone.
    :cvar NEPTUNE_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar NEPTUNE_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar NEPTUNE_PROTEUS: The second largest moon of Neptune.
    :cvar NEPTUNE_TRITON: The largest moon of Neptune.
    :cvar PLANET: A planet is a large, rounded astronomical body that is
        neither a star nor a stellar remnant. In August 2006 the
        International Astronomical Union (IAU) defined that in the Solar
        System a planet is a celestial body that satisfies the following
        criteria (1) is in orbit around the Sun, (2) has sufficient mass
        to assume hydrostatic equilibrium (a nearly round shape), and
        (3) has "cleared the neighborhood" around its orbit. This
        definition is still controversial to this day. Many members of
        the community believe that Pluto, which was demoted to the
        status dwarf planet, should maintain its planet status.
    :cvar PLUTO: The ninth planet from the Sun in our solar system.
    :cvar RHEA: The second largest moon of Saturn and the ninth largest
        moon in the Solar System.
    :cvar SATURN: The sixth planet from the Sun in our solar system.
    :cvar SATURN_DIONE: The fourth largest moon of Saturn.
    :cvar SATURN_ENCELADUS: The sixth largest moon of Saturn. It is
        currently endogenously active. The smallest known body in the
        Solar System that is geologically active today.
    :cvar SATURN_IAPETUS: The third largest moon of Saturn and the
        eleventh largest in the Solar System.
    :cvar SATURN_MAGNETOSPHERE: The region of space above the atmosphere
        or surface of the planet and bounded by the magnetopause that is
        under the direct influence of the magnetic field of a planetary
        body.
    :cvar SATURN_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar SATURN_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar SATURN_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar SATURN_MAGNETOSPHERE_POLAR: The region near the pole of a
        body. For a magnetosphere the polar region is the area where
        magnetic field lines are open and includes the auroral zone.
    :cvar SATURN_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar SATURN_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar SATURN_MIMAS: The smallest and least massive of the round
        moons of Saturn.
    :cvar SATURN_RHEA: The second largest moon of Saturn and the ninth
        largest moon in the Solar System.
    :cvar SATURN_TETHYS: The fifth largest moon of Saturn and the
        sixteenth largest moon in the Solar System. The orbit Tethys is
        the third closest to Saturn of the major Cronian moons.
    :cvar SATURN_TITAN: The largest moon of Saturn and the second
        largest moon in the Solar System.
    :cvar SUN: The star upon which our solar system is centered.
    :cvar SUN_CHROMOSPHERE: The region of the solar (or stellar)
        atmosphere above the temperature minimum and below the
        Transition Region. The solar chromosphere is approximately 400
        km to 2100 km above the photosphere, and characterized by
        temperatures that range from 4500 K to 28000 K.
    :cvar SUN_CORONA: The outermost atmospheric region of the Sun or a
        star, characterized by ionization temperatures above 10^5 K. The
        solar corona starts at about 2100 km above the photosphere.
        There is no generally defined upper limit.
    :cvar SUN_INTERIOR: The region inside the body which is not visible
        from outside the body.
    :cvar SUN_PHOTOSPHERE: The atmospheric layer of the Sun or a star
        from which continuum radiation, especially optical, is emitted
        to space. For the Sun, the photosphere is about 500 km thick.
    :cvar SUN_TRANSITION_REGION: A very narrow (&lt;100 km) layer
        between the chromosphere and the corona where the temperature
        rises abruptly from about 8000 to about 500,000 K.
    :cvar TITAN: The largest moon of Saturn and the second largest moon
        in the Solar System.
    :cvar TITLE: The name of a published composition, set or data,
        images or other work.
    :cvar URANUS: The eighth planet from the Sun in our solar system.
    :cvar URANUS_ARIEL: The fourth largest moon of Uranus.
    :cvar URANUS_MAGNETOSPHERE: The region of space above the atmosphere
        or surface of the planet and bounded by the magnetopause that is
        under the direct influence of the magnetic field of a planetary
        body.
    :cvar URANUS_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar URANUS_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar URANUS_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar URANUS_MAGNETOSPHERE_POLAR: The region near the pole of a
        body. For a magnetosphere the polar region is the area where
        magnetic field lines are open and includes the auroral zone.
    :cvar URANUS_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar URANUS_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar URANUS_MIRANDA: The smallest and innermost round moon of
        Uranus.
    :cvar URANUS_OBERON: The second largest and second most massive moon
        of Uranus, and the ninth most massive moon in the Solar System.
    :cvar URANUS_PUCK: The largest inner spherical moon of Uranus.
    :cvar URANUS_TITANIA: The largest moon of Uranus and the eighth
        largest moon in the Solar System.
    :cvar URANUS_UMBRIEL: The third largest and fourth most massive moon
        of Uranus.
    :cvar VENUS: The second planet from the Sun in our solar system.
    :cvar VENUS_MAGNETOSPHERE: The region of space above the atmosphere
        or surface of the planet and bounded by the magnetopause that is
        under the direct influence of the magnetic field of a planetary
        body.
    :cvar VENUS_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar VENUS_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar VENUS_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar VENUS_MAGNETOSPHERE_POLAR: The region near the pole of a body.
        For a magnetosphere the polar region is the area where magnetic
        field lines are open and includes the auroral zone.
    :cvar VENUS_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar VENUS_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    """

    ASTEROID = "Asteroid"
    CALLISTO = "Callisto"
    COMET = "Comet"
    COMET_1_PHALLEY = "Comet.1PHalley"
    COMET_26_PGRIGG_SKJELLERUP = "Comet.26PGriggSkjellerup"
    COMET_67_PCHURYUMOV_GERASIMENKO = "Comet.67PChuryumovGerasimenko"
    EARTH = "Earth"
    EARTH_MAGNETOSHEATH = "Earth.Magnetosheath"
    EARTH_MAGNETOSPHERE = "Earth.Magnetosphere"
    EARTH_MAGNETOSPHERE_MAGNETOTAIL = "Earth.Magnetosphere.Magnetotail"
    EARTH_MAGNETOSPHERE_MAIN = "Earth.Magnetosphere.Main"
    EARTH_MAGNETOSPHERE_PLASMASPHERE = "Earth.Magnetosphere.Plasmasphere"
    EARTH_MAGNETOSPHERE_POLAR = "Earth.Magnetosphere.Polar"
    EARTH_MAGNETOSPHERE_RADIATION_BELT = "Earth.Magnetosphere.RadiationBelt"
    EARTH_MAGNETOSPHERE_RING_CURRENT = "Earth.Magnetosphere.RingCurrent"
    EARTH_MOON = "Earth.Moon"
    EARTH_NEAR_SURFACE = "Earth.NearSurface"
    EARTH_NEAR_SURFACE_ATMOSPHERE = "Earth.NearSurface.Atmosphere"
    EARTH_NEAR_SURFACE_AURORAL_REGION = "Earth.NearSurface.AuroralRegion"
    EARTH_NEAR_SURFACE_EQUATORIAL_REGION = "Earth.NearSurface.EquatorialRegion"
    EARTH_NEAR_SURFACE_IONOSPHERE = "Earth.NearSurface.Ionosphere"
    EARTH_NEAR_SURFACE_IONOSPHERE_DREGION = (
        "Earth.NearSurface.Ionosphere.DRegion"
    )
    EARTH_NEAR_SURFACE_IONOSPHERE_EREGION = (
        "Earth.NearSurface.Ionosphere.ERegion"
    )
    EARTH_NEAR_SURFACE_IONOSPHERE_FREGION = (
        "Earth.NearSurface.Ionosphere.FRegion"
    )
    EARTH_NEAR_SURFACE_IONOSPHERE_TOPSIDE = (
        "Earth.NearSurface.Ionosphere.Topside"
    )
    EARTH_NEAR_SURFACE_MESOSPHERE = "Earth.NearSurface.Mesosphere"
    EARTH_NEAR_SURFACE_MID_LATITUDE_REGION = (
        "Earth.NearSurface.MidLatitudeRegion"
    )
    EARTH_NEAR_SURFACE_PLASMASPHERE = "Earth.NearSurface.Plasmasphere"
    EARTH_NEAR_SURFACE_POLAR_CAP = "Earth.NearSurface.PolarCap"
    EARTH_NEAR_SURFACE_SOUTH_ATLANTIC_ANOMALY_REGION = (
        "Earth.NearSurface.SouthAtlanticAnomalyRegion"
    )
    EARTH_NEAR_SURFACE_STRATOSPHERE = "Earth.NearSurface.Stratosphere"
    EARTH_NEAR_SURFACE_SUB_AURORAL_REGION = (
        "Earth.NearSurface.SubAuroralRegion"
    )
    EARTH_NEAR_SURFACE_THERMOSPHERE = "Earth.NearSurface.Thermosphere"
    EARTH_NEAR_SURFACE_TROPOSPHERE = "Earth.NearSurface.Troposphere"
    EARTH_SURFACE = "Earth.Surface"
    ENCELADUS = "Enceladus"
    EUROPA = "Europa"
    GANYMEDE = "Ganymede"
    HELIOSPHERE = "Heliosphere"
    HELIOSPHERE_HELIOSHEATH = "Heliosphere.Heliosheath"
    HELIOSPHERE_INNER = "Heliosphere.Inner"
    HELIOSPHERE_NEAR_EARTH = "Heliosphere.NearEarth"
    HELIOSPHERE_OUTER = "Heliosphere.Outer"
    HELIOSPHERE_REMOTE1_AU = "Heliosphere.Remote1AU"
    INCIDENT = "Incident"
    INTERSTELLAR = "Interstellar"
    IO = "Io"
    JUPITER = "Jupiter"
    JUPITER_CALLISTO = "Jupiter.Callisto"
    JUPITER_EUROPA = "Jupiter.Europa"
    JUPITER_GANYMEDE = "Jupiter.Ganymede"
    JUPITER_IO = "Jupiter.Io"
    JUPITER_MAGNETOSPHERE = "Jupiter.Magnetosphere"
    JUPITER_MAGNETOSPHERE_MAGNETOTAIL = "Jupiter.Magnetosphere.Magnetotail"
    JUPITER_MAGNETOSPHERE_MAIN = "Jupiter.Magnetosphere.Main"
    JUPITER_MAGNETOSPHERE_PLASMASPHERE = "Jupiter.Magnetosphere.Plasmasphere"
    JUPITER_MAGNETOSPHERE_POLAR = "Jupiter.Magnetosphere.Polar"
    JUPITER_MAGNETOSPHERE_RADIATION_BELT = (
        "Jupiter.Magnetosphere.RadiationBelt"
    )
    JUPITER_MAGNETOSPHERE_RING_CURRENT = "Jupiter.Magnetosphere.RingCurrent"
    MARS = "Mars"
    MARS_DEIMOS = "Mars.Deimos"
    MARS_MAGNETOSPHERE = "Mars.Magnetosphere"
    MARS_MAGNETOSPHERE_MAGNETOTAIL = "Mars.Magnetosphere.Magnetotail"
    MARS_MAGNETOSPHERE_MAIN = "Mars.Magnetosphere.Main"
    MARS_MAGNETOSPHERE_PLASMASPHERE = "Mars.Magnetosphere.Plasmasphere"
    MARS_MAGNETOSPHERE_POLAR = "Mars.Magnetosphere.Polar"
    MARS_MAGNETOSPHERE_RADIATION_BELT = "Mars.Magnetosphere.RadiationBelt"
    MARS_MAGNETOSPHERE_RING_CURRENT = "Mars.Magnetosphere.RingCurrent"
    MARS_PHOBOS = "Mars.Phobos"
    MERCURY = "Mercury"
    MERCURY_MAGNETOSPHERE = "Mercury.Magnetosphere"
    MERCURY_MAGNETOSPHERE_MAGNETOTAIL = "Mercury.Magnetosphere.Magnetotail"
    MERCURY_MAGNETOSPHERE_MAIN = "Mercury.Magnetosphere.Main"
    MERCURY_MAGNETOSPHERE_PLASMASPHERE = "Mercury.Magnetosphere.Plasmasphere"
    MERCURY_MAGNETOSPHERE_POLAR = "Mercury.Magnetosphere.Polar"
    MERCURY_MAGNETOSPHERE_RADIATION_BELT = (
        "Mercury.Magnetosphere.RadiationBelt"
    )
    MERCURY_MAGNETOSPHERE_RING_CURRENT = "Mercury.Magnetosphere.RingCurrent"
    NEPTUNE = "Neptune"
    NEPTUNE_MAGNETOSPHERE = "Neptune.Magnetosphere"
    NEPTUNE_MAGNETOSPHERE_MAGNETOTAIL = "Neptune.Magnetosphere.Magnetotail"
    NEPTUNE_MAGNETOSPHERE_MAIN = "Neptune.Magnetosphere.Main"
    NEPTUNE_MAGNETOSPHERE_PLASMASPHERE = "Neptune.Magnetosphere.Plasmasphere"
    NEPTUNE_MAGNETOSPHERE_POLAR = "Neptune.Magnetosphere.Polar"
    NEPTUNE_MAGNETOSPHERE_RADIATION_BELT = (
        "Neptune.Magnetosphere.RadiationBelt"
    )
    NEPTUNE_MAGNETOSPHERE_RING_CURRENT = "Neptune.Magnetosphere.RingCurrent"
    NEPTUNE_PROTEUS = "Neptune.Proteus"
    NEPTUNE_TRITON = "Neptune.Triton"
    PLANET = "Planet"
    PLUTO = "Pluto"
    RHEA = "Rhea"
    SATURN = "Saturn"
    SATURN_DIONE = "Saturn.Dione"
    SATURN_ENCELADUS = "Saturn.Enceladus"
    SATURN_IAPETUS = "Saturn.Iapetus"
    SATURN_MAGNETOSPHERE = "Saturn.Magnetosphere"
    SATURN_MAGNETOSPHERE_MAGNETOTAIL = "Saturn.Magnetosphere.Magnetotail"
    SATURN_MAGNETOSPHERE_MAIN = "Saturn.Magnetosphere.Main"
    SATURN_MAGNETOSPHERE_PLASMASPHERE = "Saturn.Magnetosphere.Plasmasphere"
    SATURN_MAGNETOSPHERE_POLAR = "Saturn.Magnetosphere.Polar"
    SATURN_MAGNETOSPHERE_RADIATION_BELT = "Saturn.Magnetosphere.RadiationBelt"
    SATURN_MAGNETOSPHERE_RING_CURRENT = "Saturn.Magnetosphere.RingCurrent"
    SATURN_MIMAS = "Saturn.Mimas"
    SATURN_RHEA = "Saturn.Rhea"
    SATURN_TETHYS = "Saturn.Tethys"
    SATURN_TITAN = "Saturn.Titan"
    SUN = "Sun"
    SUN_CHROMOSPHERE = "Sun.Chromosphere"
    SUN_CORONA = "Sun.Corona"
    SUN_INTERIOR = "Sun.Interior"
    SUN_PHOTOSPHERE = "Sun.Photosphere"
    SUN_TRANSITION_REGION = "Sun.TransitionRegion"
    TITAN = "Titan"
    TITLE = "Title"
    URANUS = "Uranus"
    URANUS_ARIEL = "Uranus.Ariel"
    URANUS_MAGNETOSPHERE = "Uranus.Magnetosphere"
    URANUS_MAGNETOSPHERE_MAGNETOTAIL = "Uranus.Magnetosphere.Magnetotail"
    URANUS_MAGNETOSPHERE_MAIN = "Uranus.Magnetosphere.Main"
    URANUS_MAGNETOSPHERE_PLASMASPHERE = "Uranus.Magnetosphere.Plasmasphere"
    URANUS_MAGNETOSPHERE_POLAR = "Uranus.Magnetosphere.Polar"
    URANUS_MAGNETOSPHERE_RADIATION_BELT = "Uranus.Magnetosphere.RadiationBelt"
    URANUS_MAGNETOSPHERE_RING_CURRENT = "Uranus.Magnetosphere.RingCurrent"
    URANUS_MIRANDA = "Uranus.Miranda"
    URANUS_OBERON = "Uranus.Oberon"
    URANUS_PUCK = "Uranus.Puck"
    URANUS_TITANIA = "Uranus.Titania"
    URANUS_UMBRIEL = "Uranus.Umbriel"
    VENUS = "Venus"
    VENUS_MAGNETOSPHERE = "Venus.Magnetosphere"
    VENUS_MAGNETOSPHERE_MAGNETOTAIL = "Venus.Magnetosphere.Magnetotail"
    VENUS_MAGNETOSPHERE_MAIN = "Venus.Magnetosphere.Main"
    VENUS_MAGNETOSPHERE_PLASMASPHERE = "Venus.Magnetosphere.Plasmasphere"
    VENUS_MAGNETOSPHERE_POLAR = "Venus.Magnetosphere.Polar"
    VENUS_MAGNETOSPHERE_RADIATION_BELT = "Venus.Magnetosphere.RadiationBelt"
    VENUS_MAGNETOSPHERE_RING_CURRENT = "Venus.Magnetosphere.RingCurrent"


@dataclass
class OperatingSpan:
    """
    The interval in time from the first point at which an instrument or spacecraft
    was producing and sending data until the last such time, ignoring possible
    gaps.
    """

    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    stop_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StopDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class OutputProperty:
    """
    A container of attributes regarding an output property of an application.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_min: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_max: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMax",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


class ParameterQuantity(Enum):
    """
    Identifiers for all types of parameter quantities.

    :cvar VALUE_2_DCUTS: A set of 2-D arrays that contain the values of
        physical parameters, i.e., magnetic field vectors, particle
        densities, temperatures, etc., at the grid points located in a
        planar slice of a model volume.
    :cvar VALUE_3_DCUBES: A set of 3-D arrays that contain the values of
        physical parameters, i.e., magnetic field vectors, particle
        densities, temperatures, etc., at grid points in a model volume.
    :cvar ACELECTRIC_FIELD: Alternating electric field component of a
        wave.
    :cvar ACMAGNETIC_FIELD: Alternating magnetic field component of a
        wave.
    :cvar ABSORPTION: Decrease of radiant energy (relative to the
        background continuum spectrum).
    :cvar ACTIVITY_INDEX: An indication, derived from one or more
        measurements, of the level of activity of an object or region,
        such as sunspot number, F10.7 flux, Dst, or the Polar Cap
        Indices.
    :cvar ADIABATIC_INVARIANT: A property of a physical system usually
        related to periodic phenomena that remains constant under slowly
        varying conditions.
    :cvar ADIABATIC_INVARIANT_MAGNETIC_MOMENT: A constant of motion
        related to the gyromotion of a particle in a magnetic field that
        is either static or slowly varying with respect to the
        gyroperiod. The magnetic moment is usually denoted by using the
        lower-case Greek letter for mu, &amp;#956;, and can be
        calculated by using &amp;#956;=m(u^2/2B) where m is the particle
        mass, u is the velocity of the particle perpendicular to the
        constant or average magnetic field direction, and B is the
        magnitude of the magnetic field strength.
    :cvar ADIABATIC_INVARIANT_BOUNCE_MOTION: The second adiabatic
        invariant is associated with periodic bounce motion of charged
        particles trapped between two magnetic mirrors on a magnetic
        field line. The second invariant, termed J, is defined by using
        the integral J=m &amp;int; v||*ds where m is the mass of the
        charged particle, v|| is the particle velocity along the field
        line, and ds represents elemental arc lengths along the field
        line. The second adiabatic invariant is conserved as long as
        changes in the background magnetic field occur at time scales
        much longer than the bounce time of the charged particles.
    :cvar ADIABATIC_INVARIANT_DRIFT_MOTION: The third invariant for
        charged particle motion in a dipolar magnetic field is
        associated with drift of its guiding center in the equatorial
        plane. The conserved quantity, J&lt;sub&gt;2&lt;/sub&gt;, is
        equal to q&amp;phi; where q is the particle charge and &amp;phi;
        is the magnetic flux enclosed within the particle drift path.
    :cvar AEROSOL: A suspension of fine solid or liquid particles in a
        gas.
    :cvar AKASOFU_EPSILON: A measure of the magnetopause energy flux and
        an indicator of the solar wind power available for subsequent
        magnetospheric energization. Defined as: V*B^2*l^2sin(theta/2)^4
        where B is the IMF, l is an empirical scaling parameter equal to
        7 R&lt;sub&gt;E&lt;/sub&gt;, and theta=tan(By/Bz)^-1 the IMF
        clock angle.
    :cvar ALBEDO: The ratio of reflected radiation from the surface to
        incident radiation upon it.
    :cvar ALFVEN_MACH_NUMBER: The ratio of the bulk flow speed to the
        Alfven speed.
    :cvar ALFVEN_VELOCITY: Phase velocity of the Alfven wave. In SI
        units it is the velocity of the magnetic field divided by the
        square root of the mass density times the permeability of free
        space (&amp;mu;&lt;sub&gt;0&lt;/sub&gt;).
    :cvar ALPHA_PARTICLE: A positively charged nuclear particle that
        consists of two protons and two neutrons.
    :cvar ANTENNA: A sensor used to measure electric potential.
    :cvar ARRIVAL_DIRECTION: An angular measure of the direction from
        which an energetic particle or photon was incident on a
        detector. The angles may be measured in any coordinate system.
    :cvar ATOM: Matter consisting of a nucleus surrounded by electrons
        which has no net charge.
    :cvar ATOMIC_NUMBER_DETECTED: The number of protons in the nucleus
        of an atom as determined by a detector.
    :cvar AVERAGE_CHARGE_STATE: A measure of the composite deficit
        (positive) or excess (negative) of electrons with respect to
        protons.
    :cvar AZIMUTH_ANGLE: The angle between the projection into the I-J
        plane of a position or measured vector and the I-axis of the
        coordinate system. Mathematically defined as arctan(J/I). This
        term could be also applied to angles measured in different
        planes, i.e., the IMF clock angle defined as arctan(|By|/Bz).
    :cvar CA_K: A spectrum with a wavelength of range centered near
        393.5 nm. VSO nickname: Ca-K image with range of 391.9 nm to
        395.2 nm.
    :cvar CHANNELTRON: An instrument that detects electrons, ions, and
        ultraviolet radiation, according to the principle of a secondary
        emission multiplier. It is typically used in electron
        spectroscopy and mass spectrometry.
    :cvar CHARGE_EXCHANGE: Chemical process involving a charge transfer
        from an ion (which becomes neutral) to a neutral (which becomes
        ionized).
    :cvar CHARGE_FLUX: The number of ionized particles passing through a
        unit area per unit time, for instance as measured by a Faraday
        cup.
    :cvar CHARGE_STATE: Charge of a fully or partially stripped ion, in
        units of the charge of a proton. Charge state of a bare proton
        is equal to one.
    :cvar CORONOGRAPH: An instrument which can image things very close
        to the Sun by using a disk to block the bright surface of the
        sun or a star that reveals the faint corona of the Sun or other
        celestial objects.
    :cvar COUNT_RATE: The number of events per unit time.
    :cvar COUNTS: The number of detection events occurring in a detector
        over the detector accumulation time.
    :cvar CROSS_SECTION: Cross section of the reaction, when the
        reaction implies the collision of two particles.
    :cvar CURRENT: It is the scalar quantity giving the net charge
        (summed over charged particle species) per unit time flowing
        across a given surface.
    :cvar CURRENT_DENSITY: It is the vector quantity giving the net
        charge (summed over charged particle species) per unit cross-
        sectional area per unit time flowing through a given point.
        Measurements of current density are often provided in terms of
        the magnetic perturbations (superposed upon a background
        magnetic field, if present) associated with the current density.
    :cvar DATA_QUALITY: An ancillary parameter that denotes the standard
        or degree of accuracy, trustworthiness, or usefulness of another
        parameter.
    :cvar DISSOCIATIVE_RECOMBINATION: Chemical process by which an ion
        is neutralized by capturing an electron, and splits in two new
        neutral species.
    :cvar DOPPLER_FREQUENCY: Change in the frequency of a propagating
        wave due to motion of the source, the observer, the reflector,
        or the propagation medium.
    :cvar DOPPLERGRAM: A map or image depicting the spatial distribution
        of line-of-sight velocities of the observed object.
    :cvar DOUBLE_SPHERE: A dipole antenna of which the active (sensor)
        elements are small spheres located at the ends of two wires
        deployed in the equatorial plane, on opposite sides of a
        spinning spacecraft.
    :cvar DUST: Free microscopic particles of solid material.
    :cvar DUST_DETECTOR: An instrument which determines the mass and
        speed of ambient dust particles.
    :cvar DYNAMIC_PRESSURE: Dynamic pressure is a measure of the kinetic
        energy per unit volume of a fluid. For instance, the solar wind
        dynamic pressure or ram pressure for a purely proton plasma is
        equal to m&lt;sub&gt;p&lt;/sub&gt; n V&lt;sup&gt;2&lt;/sup&gt;
        where m&lt;sub&gt;p&lt;/sub&gt; is the proton mass, n is the
        proton number density, and V is the solar wind speed.
    :cvar ELECTRIC: The physical attribute that exerts an electrical
        force.
    :cvar ELECTRIC_FIELD: A region of space around a charged particle,
        or between two voltages within which a force is exerted on
        charged objects in its vicinity. An electric field is the
        electric force per unit charge.
    :cvar ELECTROMAGNETIC: Electric and magnetic field variations in
        time and space that propagate through a medium or a vacuum. The
        wave propagation direction, electric field vector, and magnetic
        field vector form an orthogonal triad. Waves in this category
        are detected by having their field quantities measured.
    :cvar ELECTRON: An elementary particle that has a negative charge
        equal to about 1.60218*10^-19 C and a rest mass equal to about
        9.10938*10^-31 kg.
    :cvar ELECTRON_DRIFT_INSTRUMENT: An active experiment to measure the
        electron drift velocity based on sensing the displacement of a
        weak beam of electrons after one gyration in the ambient
        magnetic field.
    :cvar ELECTRON_IMPACT: Chemical process by which a neutral is
        ionized thanks to the energy from the impact of an electron.
    :cvar ELECTROSTATIC: Collective longitudinal electric-field and
        plasma oscillations trapped within a body of plasma.
    :cvar ELECTROSTATIC_ANALYSER: An instrument which uses charged
        plates to analyze the mass, charge and kinetic energies of
        charged particles which enter the instrument.
    :cvar ELEVATION_ANGLE: The angle between the position or measured
        vector and the I-J plane of the coordinate system.
        Mathematically defined as arctan(K/sqrt(I^2+J^2)).
    :cvar EMISSIVITY: The energy emitted spontaneously per unit
        bandwidth (typically frequency) per unit time per unit mass of
        source. Emissivity is usually integrated over all
        directions/solid angles.
    :cvar ENERGETIC_PARTICLE_INSTRUMENT: An instrument that measures
        fluxes of charged particles as a function of time, direction of
        motion, mass, charge and/or species.
    :cvar ENERGETIC_PARTICLES: Pieces of matter that are moving very
        fast. Energetic particles include protons, electrons, neutrons,
        neutrinos, the nuclei of atoms, and other sub-atomic particles.
    :cvar ENERGY: The capacity for doing work as measured by the
        capability of doing work (potential energy) or the conversion of
        this capability to motion (kinetic energy).
    :cvar ENERGY_DENSITY: The amount of energy per unit volume.
    :cvar ENERGY_FLUX: The amount of energy passing through a unit area
        in a unit time.
    :cvar ENERGY_PER_CHARGE: The kinetic energy, E, per unit net charge,
        q, that is E/q, for an electron or an ionized atom, molecule, or
        dust particle.
    :cvar ENTROPY: A function of thermodynamic quantity, such as
        temperature, pressure, or composition, that is a measure of the
        energy that is not available for work during a thermodynamic
        process. It is often interpreted as the degree of disorder or
        randomness in the system.
    :cvar EPHEMERIS: The spatial coordinates of a body as a function of
        time. When used as an Instrument Type it represents the process
        or methods used to generate spatial coordinates.
    :cvar EQUIVALENT_WIDTH: The spectral width of a total absorption
        line having the amount of absorbed radiant energy being
        equivalent to that in an observed absorption line.
    :cvar EXPERIMENT: A collection of components which are designed to
        make coordinated observations of a phenomenon or object.
        Projects and missions may refer to an "experiment" by other
        names such as a "suite".
    :cvar EXTREME_ULTRAVIOLET: A spectrum with a wavelength range of 10
        nm to 125 nm. VSO nickname: EUV image with a range of 10 nm to
        125 nm.
    :cvar FAR_ULTRAVIOLET: A spectrum with a wavelength range of 122 nm
        to 200 nm. VSO nickname: FUV image with a range of 122 nm to 200
        nm.
    :cvar FARADAY_CUP: An instrument consisting of an electrode from
        which electrical current is measured while a charged particle
        beam (electrons or ions) impinges on it. Used to determine
        energy spectrum and sometimes ion composition of the impinging
        particles.
    :cvar FLOW_SPEED: The rate at which particles or energy is passing
        through a unit area in a unit time.
    :cvar FLOW_VELOCITY: The volume of matter passing through a unit
        area perpendicular to the direction of flow in a unit of time.
    :cvar FLUENCE: The time integral of a flux. A fluence is a not a
        measurement of flux per unit time.
    :cvar FLUX_FEEDBACK: A search coil whose bandwidth and signal/noise
        ratio are increased by the application of negative feedback at
        the sensor (flux) level by driving a collocated coil with a
        signal from the preamplifier.
    :cvar FOURIER_TRANSFORM_SPECTROGRAPH: An instrument that determines
        the spectra of a radiative source, using time domain
        measurements and a Fourier transform.
    :cvar FREQUENCY: The number of occurrences of a repeating event per
        unit time.
    :cvar FREQUENCY_TO_GYROFREQUENCY_RATIO: The ratio of the
        characteristic frequency of a medium to gyrofrequency of a
        particle.
    :cvar GAMMA_RAYS: Photons with a wavelength range: 0.00001 nm to
        0.001 nm.
    :cvar GEIGER_MUELLER_TUBE: An instrument which measures density of
        ionizing radiation based on interactions with a gas.
    :cvar GEOMETRIC_FACTOR: A measure of the gathering power of a
        particle detector. The geometric factor can be used to correct
        particle measurements by accounting for the fact that only a
        fraction of the source particles is able to gain entry through
        the aperture of a detector. For an isotopic source distribution,
        the geometric factor corresponds to the solid angle subtended by
        the aperture. In practice, determination of the geometric factor
        requires numerical modeling and depends on detector design and
        the characteristics of the source.
    :cvar GYROFREQUENCY: The number of gyrations around a magnetic
        guiding center (field line) a charged particle makes per unit
        time due to the Lorentz force.
    :cvar HALPHA: A spectrum with a wavelength range centered at 656.3
        nm. VSO nickname: H-alpha image with a spectrum range of 655.8
        nm to 656.8 nm.
    :cvar HARD_XRAYS: Photons with a wavelength range: 0.001 nm to 0.1
        nm and an energy range of 12 keV to 120 keV.
    :cvar HE10830: A spectrum with a wavelength range centered at 1082.9
        nm. VSO nickname: an He 10830 image with a range of 1082.5 nm to
        1083.3 nm.
    :cvar HE304: A spectrum centered around the resonance line of
        ionized helium at 304 Angstrom (30.4 nm).
    :cvar HEAT_FLUX: Flow of thermal energy through a gas or plasma
        typically computed as third moment of a distribution function.
    :cvar HOUSEKEEPING: Parameters that indicate the status or health
        state of instruments or monitoring devices as measured in
        physical units such as that for current, voltage, or
        temperature. Housekeeping data can be analyzed to determine
        whether instruments are working correctly and the knowledge of
        their values may be used to avoid errors or even device
        failures.
    :cvar HYDRODYNAMIC: Periodic or quasi-periodic oscillations of fluid
        quantities.
    :cvar IMFCLOCK_ANGLE: The clockwise angle of the direction of
        interplanetary magnetic field (IMF) measured in the plane of the
        body pole perpendicular to the line between the body and the
        Sun.
    :cvar IMAGE_INTENSITY: Measurements of the 2-D distribution of the
        intensity of photons from some region or object such as the Sun
        or the polar auroral regions, can be in any wavelength band, and
        polarized, etc.
    :cvar IMAGER: An instrument which samples the radiation from an area
        at one or more spectral ranges emitted or reflected by an
        object.
    :cvar IMAGING_SPECTROMETER: An instrument which is a multispectral
        scanner with a very large number of channels (typically from 64
        channels up to 256 channels) with very narrow bandwidths.
    :cvar INFRARED: Photons with a wavelength range: 760 nm to 10^6 nm.
    :cvar INSTRUMENT_MODE: An indication of a state (mode) in which the
        instrument is operating. How a mode influences the
        interpretation and representation of data is described in
        instrument related documentation.
    :cvar INSTRUMENT_STATUS: A quantity directly related to the
        operation or function of an instrument.
    :cvar INTENSITY: The measurement of radiant or wave energy per unit
        detector area per unit bandwidth per unit solid angle per unit
        time.
    :cvar INTERFEROMETER: An instrument to study the properties of two
        or more waves from the pattern of interference created by their
        superposition.
    :cvar ION: An atom that has acquired a net electric charge by
        gaining or losing one or more electrons (Note: Z&gt;2).
    :cvar ION_CHAMBER: A device in which the collected electrical charge
        from ionization in a gas-filled cavity is taken to be the
        proportion to some parameter (e.g., dose or exposure) of
        radiation field.
    :cvar ION_COMPOSITION: In situ measurements of the relative flux or
        density of electrically charged particles in the space
        environment. May give simple fluxes, but full distribution
        functions are sometimes measured.
    :cvar ION_DRIFT: A device which measures the current produced by the
        displacement of ambient ions on a grid, thereby allowing the
        determination of the ion trajectory and velocity.
    :cvar ION_GAUGE: A device which measures low-pressure or vacuum
        neutral gas with pressures ranging from 10^-3 Torr to 10^-10
        Torr. An ion gauge is an electronic amplifying vacuum tube
        consisting of three electrodes inside an evacuated glass
        envelope, with the filament being the cathode.
    :cvar IRRADIANCE: A radiometric term for the power of
        electromagnetic radiation at a surface, per unit area.
        Irradiance is used when the electromagnetic radiation is
        incident on the surface. Irradiance data may be reported in any
        units (i.e., counts/s) due to, for example, being at a
        particular wavelength, or to being a not fully calibrated
        relative measurement.
    :cvar K7699: A spectrum with a wavelength range centered at 769.9
        nm. VSO nickname: K-7699 dopplergram with a range of 769.8 nm to
        770.0 nm.
    :cvar LBHBAND: Lyman-Birge-Hopfield band in the far ultraviolet
        range with wavelength range of 140 nm to 170 nm.
    :cvar LSHELL: The L-shell is the magnetic equatorial radius (in
        units of planetary radii) of a dipole magnetic field line. For
        instance, if the L-shell value equals 6 say at Earth, the
        magnetic field lines cross the magnetic equator at six Earth
        radii. The L-shell concept can be applied generally to any
        magnetized planet or satellite with a dominant dipolar magnetic
        field moment.
    :cvar LANGMUIR_PROBE: A monopole antenna associated with an
        instrument. The instrument applies a potential to the antenna
        which is swept to determine the voltage/current characteristic.
        This provides information about the plasma surrounding the probe
        and spacecraft.
    :cvar LINE_DEPTH: The measure of the amount of absorption below the
        continuum (depth) in a particular wavelength or frequency in an
        absorption spectrum.
    :cvar LINES: A set of 1-D arrays that contain the values of physical
        parameters, i.e., magnetic field vectors, particle densities,
        temperatures, etc., at the grid points along a line though a
        model volume. For instance, the points of the line may
        correspond to the trajectory of a spacecraft through model
        space.
    :cvar LONG_WIRE: A dipole antenna constructed by two active sensing
        elements that are wires deployed in the equatorial plane on
        opposite sides of a spinning spacecraft. The, wire length is
        usually several times the spacecraft diameter.
    :cvar LOWER_HYBRID_FREQUENCY: Lower hybrid oscillations involve
        longitudinal motions of electrons and ions in a magnetized
        plasma. The propagation of lower hybrid waves must be close to
        perpendicular to the background magnetic field in so that
        electrons cannot move along field lines thus preventing wave
        growth. The lower hybrid frequency,
        &amp;phi;&lt;sub&gt;LH&lt;/sub&gt;, can be calculated by using
        &amp;phi;&lt;sub&gt;LH&lt;/sub&gt;=[(&amp;omega;&lt;sub&gt;ce&lt;/sub&gt;&amp;omega;&lt;sub&gt;ci&lt;/sub&gt;)&lt;sup&gt;-1&lt;/sup&gt;+&amp;phi;&lt;sub&gt;pi&lt;/sub&gt;&lt;sup&gt;-2&lt;/sup&gt;]&lt;sup&gt;-1/2&lt;/sup&gt;
        where &amp;omega;&lt;sub&gt;ce&lt;/sub&gt; and
        &amp;omega;&lt;sub&gt;ci&lt;/sub&gt; are the electron and ion
        cyclotron frequencies, respectively, and
        $phi;&lt;sub&gt;LH&lt;/sub&gt; is the ion plasma frequency.
    :cvar MHD: Hydrodynamic waves in a magnetized plasma in which the
        background magnetic field plays a key role in controlling the
        wave propagation characteristics.
    :cvar MAGNETIC: The physical attribute attributed to a magnet or its
        equivalent.
    :cvar MAGNETIC_FIELD: A region of space near a magnetized body where
        magnetic forces can be detected (as measured by methods such as
        Zeeman splitting, etc.).
    :cvar MAGNETOGRAM: Measurements of the vector or line-of-sight
        magnetic field determined from remote sensing measurements of
        the detailed structure of spectral lines, including their
        splitting and polarization.
    :cvar MAGNETOGRAPH: A special type of magnetometer that records a
        time plot of the local magnetic field near the instrument or a
        telescope capable of determining the magnetic field strength
        and/or direction on a distant object such as the Sun, using the
        Zeeman splitting or other spectral signatures of magnetization.
    :cvar MAGNETOMETER: An instrument which measures the ambient
        magnetic field.
    :cvar MAGNETOSONIC_MACH_NUMBER: The ratio of the velocity of fast
        mode waves to the Alfven velocity.
    :cvar MASS: The measure of inertia (mass) of individual objects
        (e.g., aerosols).
    :cvar MASS_DENSITY: The mass of particles per unit volume.
    :cvar MASS_NUMBER: The total number of protons and neutrons
        (together known as nucleons) in an atomic nucleus.
    :cvar MASS_PER_CHARGE: The mass, m, per unit net charge, q, that is
        m/q, for an electron or an ionized atom, molecule, or dust
        particle.
    :cvar MASS_SPECTROMETER: An instrument which distinguishes chemical
        species in terms of their different isotopic masses.
    :cvar MICROCHANNEL_PLATE: An instrument used for the detection of
        elementary particles, ions, ultraviolet rays and soft X-rays
        constructed from very thin conductive glass capillaries.
    :cvar MICROWAVE: Photons with a wavelength range: 10^6 nm to
        1.5*10^7 nm.
    :cvar MODE_AMPLITUDE: In helioseismology the magnitude of
        oscillation of waves of a particular geometry.
    :cvar MOLECULE: A group of atoms so united and combined by chemical
        affinity that they form a complete, integrated whole, being the
        smallest portion of any particular compound that can exist in a
        free state.
    :cvar MULTISPECTRAL_IMAGER: An instrument which captures images at
        multiple spectral ranges.
    :cvar NA_D: A spectrum with a wavelength range of centered at 589.3
        nm. VSO nickname: Na-D image with a range of 588.8 nm to 589.8
        nm.
    :cvar NEUTRAL_ATOM_IMAGER: An instrument which measures the quantity
        and properties of neutral particles over a range of angles.
        Measured properties can include mass and energy.
    :cvar NEUTRAL_ATOM_IMAGES: Measurements of neutral atom fluxes as a
        function of look direction often related to remote energetic
        charged particles that lose their charge through charge-exchange
        and then reach the detector on a line-of-sight trajectory.
    :cvar NEUTRAL_GAS: Measurements of neutral atomic and molecular
        components of a gas.
    :cvar NEUTRAL_PARTICLE_DETECTOR: An instrument which measures the
        quantity and properties of neutral particles. Measured
        properties can include mass and plasma bulk densities.
    :cvar NEUTRON: An elementary particle with neutral charge that is a
        constituent of atomic nuclei. Neutrons have a rest mass slightly
        large than that of a proton equal to about 1.67493*10^-24 kg.
    :cvar NI6768: A spectrum with a wavelength range centered at 676.8
        nm. VSO nickname: Ni-6768 dopplergram with a range of 676.7 nm
        to 676.9 nm.
    :cvar NUMBER_DENSITY: The number of particles per unit volume.
    :cvar NUMBER_FLUX: The number of particles passing a unit area in
        unit time, possibly also per unit energy (or equivalent) and/or
        per unit look direction.
    :cvar OPTICAL: Photons with a wavelength range: 380 nm to 760 nm.
    :cvar ORIENTATION: The specification of the directional alignment of
        an object or measurement in a reference coordinate system. The
        orientation such as a spacecraft spin axis attitude is usually
        expressed as one or more angles relative to the basis axes of
        some specified physical space usually together with the
        date/time of the observation.
    :cvar OTHER: Not classified with more specific terms. The context of
        its usage may be described in related text.
    :cvar PARTICLE_CORRELATOR: An instrument which correlates particle
        flux to help identify wave/particle interactions.
    :cvar PARTICLE_DETECTOR: An instrument which detects particle
        flux!!!.
    :cvar PARTICLE_RADIUS: The mean radius for a Gaussian distribution
        of particles with an axial ratio of 2 and a distribution width
        that varies as 0.5 radius. A value of zero means no cloud was
        detected.
    :cvar PARTICLE_RIGIDITY: The particle momentum per unit charge. The
        particle Rigidity, R, is equal to pc/Ze.
    :cvar PHASE_SPACE_DENSITY: The number of particles per unit volume
        in the six-dimensional space of position and velocity.
    :cvar PHOTO_IONIZATION: Chemical process by which a neutral is
        ionized thanks to the energy from a photon.
    :cvar PHOTOMETER: An instrument which measures the strength of
        electromagnetic radiation within a spectral band which can range
        from ultraviolet to infrared and includes the visible spectrum.
    :cvar PHOTOMULTIPLIER_TUBE: A vacuum phototube that is an extremely
        sensitive detector of light in the ultraviolet, visible, and
        near-infrared ranges of the electromagnetic spectrum.
    :cvar PHOTON: Electromagnetic waves detected by techniques that
        utilize their corpuscular character (e.g., CCD, CMOS, or
        Photomultiplier).
    :cvar PHOTOPOLARIMETER: An instrument which measures the intensity
        and polarization or radiant energy. A photopolarimeter is a
        combination of a photometer and a polarimeter.
    :cvar PLASMA_BETA: The ratio of the plasma pressure (nkT) to the
        magnetic pressure (B^2/2&amp;mu;&lt;sub&gt;0&lt;/sub&gt;) in a
        single component plasma or the ratio of the plasma pressure sum
        over i of (n&lt;sub&gt;i&lt;/sub&gt;kT&lt;sub&gt;i&lt;/sub&gt;)
        for all species i to the magnetic pressure
        (B^2/2&amp;mu;&lt;sub&gt;0&lt;/sub&gt;) in a multi components
        plasma.
    :cvar PLASMA_FREQUENCY: A number density dependent characteristic
        frequency of a plasma.
    :cvar PLASMA_WAVES: Self-consistent collective oscillations of
        particles and fields (electric and magnetic) in a plasma.
    :cvar PLATFORM: A collection of components which can be positioned
        and oriented as a single unit. A platform may contain other
        platforms. For example, a spacecraft is a platform which may
        have components that can be articulated and are also considered
        platforms.
    :cvar POLAR_ANGLE: The angle between the position or measured vector
        and the k-axis of the coordinate system. Mathematically defined
        as arctan([sqrt(i^2+j^2)]/k). This term could be also applied to
        angles between the vector and other components, for example the
        IMF cone angle defined as
        arccos(B&lt;sub&gt;x&lt;/sub&gt;/B&lt;sub&gt;t&lt;/sub&gt;).
    :cvar POLARIZATION: Direction of the electric vector of an
        electromagnetic wave. The wave can be linearly polarized in any
        direction perpendicular to the direction of travel, circularly
        polarized (clockwise or counterclockwise), unpolarized, or
        mixtures of the above.
    :cvar POSITIONAL: The specification of the location of an object or
        measurement within a reference coordinate system. The position
        is usually expressed as a set of values corresponding to the
        location along a set of orthogonal axes together with the
        date/time of the observation.
    :cvar POSITRON: An elementary particle that has a positive charge
        equal to about 1.60218*10^-19 C and a rest mass equal to about
        9.10938*10^-31 kg.
    :cvar POTENTIAL: The work required per unit charge to move a charge
        from a reference point to a point at infinity (electric
        potential is defined to be zero). The electric potential of a
        spacecraft is often referred to as the spacecraft potential. The
        spacecraft potential is the electric potential of the spacecraft
        relative to the potential of the nearby plasma. The spacecraft
        potential is non-zero because the spacecraft charges to the
        level that the emitted photoelectron flux going to infinity is
        balanced by the plasma electron flux to the spacecraft.
    :cvar POYNTING_FLUX: Electromagnetic energy flux transported by a
        wave characterized as the rate of energy transport per unit area
        per steradian.
    :cvar PRESSURE: The force per unit area exerted by a particle
        distribution or field.
    :cvar PROFILE: Measurements of a quantity as a function of height
        above an object such as the limb of a body.
    :cvar PROPAGATION_TIME: Time difference between transmission and
        reception of a wave in an active wave experiment.
    :cvar PROPORTIONAL_COUNTER: An instrument which measures energy of
        ionization radiation based on interactions with a gas.
    :cvar PROTON: An elementary particle that is a constituent of all
        atomic nuclei. Protons have a positive charge equal to about
        1.60218*10^-19 C and a rest mass equal to about 1.67262*10^-27
        kg.
    :cvar QUADRISPHERICAL_ANALYSER: An instrument used for the 3-D
        detection of plasma, energetic electrons and ions, and for
        positive ion composition measurements.
    :cvar RADAR: An instrument that uses directional properties of
        returned power to infer spatial and/or other characteristics of
        a remote object.
    :cvar RADIANCE: A radiometric measurement that describes the amount
        of electromagnetic radiation that passes through or is emitted
        from a particular area, and falls within a given solid angle in
        a specified direction. They are used to characterize both
        emission from diffuse sources and reflection from diffuse
        surfaces.
    :cvar RADIO_FREQUENCY: Photons with a wavelength range: 10^5 nm to
        10^11 nm.
    :cvar RADIOMETER: An instrument for detecting or measuring radiant
        energy. Radiometers are commonly limited to infrared radiation.
    :cvar RATE: Reaction rate: reaction production per unit of time.
    :cvar REMARK: A notice, comment, or observation.
    :cvar RESONANCE_SOUNDER: A combination of a radio receiver and a
        pulsed transmitter used to study the plasma surrounding a
        spacecraft by identifying resonances or cut-offs (of the wave
        dispersion relation), whose frequencies are related to the
        ambient plasma density and magnetic field. When the transmitter
        is off it is essentially a high-frequency resolution spectral
        power receiver.
    :cvar RETARDING_POTENTIAL_ANALYSER: An instrument which measures ion
        temperatures and ion concentrations using a planar ion trap.
    :cvar RIOMETER: An instrument which measures the signal strength in
        various directions of the galactic radio signals. Variations in
        these signals are influenced by solar flare activity and
        geomagnetic storm and substorm processes.
    :cvar ROTATION_MATRIX: A tensor that is used to perform vector data
        transformation from one coordinate system to another.
    :cvar SPICE: SPICE is an ancillary information system that provides
        scientists and engineers the capability to include space
        geometry and event data into mission design, science observation
        planning, and science data analysis software. The staff of the
        NASA Navigation and Ancillary Information Facility, NAIF, which
        is located at JPL provides SPICE support for planetary,
        heliophysics, and Earth science missions, see
        https://naif.jpl.nasa.gov/naif/index.html. This SPICE has been
        adapted from text on NAF hosted web pages.
    :cvar SCINTILLATION_DETECTOR: An instrument which detects
        fluorescence of a material which is excited by high-energy
        (ionizing) electromagnetic or charged particle radiation.
    :cvar SEARCH_COIL: An instrument which measures the time variation
        of the magnetic flux threading a loop by measurement of the
        electric potential difference induced between the ends of the
        wire.
    :cvar SOFT_XRAYS: X-Rays with an energy range of 0.12 keV to 12 keV.
    :cvar SOLAR_UVFLUX: The amount of ultraviolet energy originating
        from the Sun passing through a unit area in a unit time.
    :cvar SOLID_STATE_DETECTOR: A detector of the charge carriers
        (electrons and holes) generated in semiconductors by energy
        deposited by gamma ray photons. Also known as a semiconductor
        detector".
    :cvar SONIC_MACH_NUMBER: The ratio of the bulk flow speed to the
        speed of sound in the medium.
    :cvar SOUND_SPEED: The speed at which sound travels through a
        medium.
    :cvar SOUNDER: An instrument which measures the radiances from an
        object. A sounder may measure radiances at multiple spectral
        ranges.
    :cvar SPACECRAFT_POTENTIAL_CONTROL: An instrument to control the
        electric potential of a spacecraft with respect to the ambient
        plasma by emitting a variable current of positive ions.
    :cvar SPATIAL_SERIES: A set of 3-D arrays that contain the values of
        physical parameters, i.e., magnetic field vectors, particle
        densities, temperatures, etc., at grid points in a spacial
        volume.
    :cvar SPECTRA: A term that applies to any signal that can be
        measured or decomposed along a continuous variable such as the
        electromagnetic radiation which can be decomposed as a function
        of wavelength or frequency.
    :cvar SPECTRAL_POWER_RECEIVER: A radio receiver which determines the
        power spectral density of the electric or magnetic field, or
        both, at one or more frequencies.
    :cvar SPECTROMETER: An instrument that measures the component
        wavelengths of light (or other electromagnetic radiation) by
        splitting the light up into its component wavelengths.
    :cvar SPECTRUM: The distribution of a characteristic of a physical
        system or phenomenon, such as the energy emitted by a radiant
        source, arranged in the order of wavelengths.
    :cvar SPIN_PERIOD: The time required for an object such as a
        spacecraft or planet to perform one full rotation in a given
        frame of reference.
    :cvar SPIN_PHASE: An angular based or normalized parameter that
        specifies the spin state of an object such as a spacecraft or
        planet in a specific coordinate system usually together with the
        date/time of the observation.
    :cvar SPIN_RATE: The angular rate of change of the spin angle of an
        object such as a spacecraft or planet.
    :cvar STOKES_PARAMETERS: A set of four parameters (usually called
        I,Q, U and V) which describe the polarization state of an
        electromagnetic wave propagating through space.
    :cvar TELEMETRY: Parameters that include full packets of data from
        monitoring devices or the memory addresses of datum within
        telemetry packets. The data comprising telemetry packets are
        typically expressed by using non-physical engineering units and
        may be used to express a variety of device operating conditions
        such as command acceptance/execution, housekeeping, event
        characterization, memory dumps, and science data. Telemetry
        packets may be raw or unpacked.
    :cvar TEMPERATURE: A measure of the kinetic energy of random motion
        with respect to the average. Temperature is properly defined
        only for an equilibrium particle distribution (Maxwellian
        distribution).
    :cvar TEMPORAL: Pertaining to time.
    :cvar THERMAL_PLASMA: Measurements of the plasma in the energy
        regime where the most of the plasma occurs. May be the basic
        fluxes in the form of distribution functions or the derived bulk
        parameters (density, flow velocity, etc.).
    :cvar THERMAL_SPEED: For a Maxwellian distribution, the difference
        between the mean speed and the speed within 69% (one sigma) of
        all the members of the speed distribution occur.
    :cvar TIME_OF_FLIGHT: An instrument which measures the time it takes
        for a particle to travel between two detectors.
    :cvar TIME_SERIES: A representation of data showing a set of
        observations taken at different points in time and charted as a
        time series.
    :cvar TOTAL_PRESSURE: In an MHD fluid it is the number density (N)
        times Boltzmann constant times the temperature in Kelvin.
    :cvar ULTRAVIOLET: Photons with a wavelength range: 10 nm to 400 nm.
    :cvar UNSPECIFIED: A value which is not provided.
    :cvar UPPER_HYBRID_FREQUENCY: Upper hybrid oscillations involve
        longitudinal motions of electrons perpendicular to the magnetic
        field. The upper hybrid frequency,
        &amp;phi;&lt;sub&gt;UH&lt;/sub&gt;, is governed by the
        relationship
        &amp;phi;&lt;sub&gt;UH&lt;/sub&gt;^2=&amp;phi;&lt;sub&gt;pe&lt;/sub&gt;^2+&amp;theta;&lt;sub&gt;ce&lt;/sub&gt;^2
        where &amp;phi;&lt;sub&gt;pe&lt;/sub&gt; is electron plasma
        frequency and &amp;theta;&lt;sub&gt;ce&lt;/sub&gt; is the
        electron cyclotron frequency.
    :cvar VCROSS_B: The cross product of the charge velocity (V) and the
        magnetic field (B). It is the electric field exerted on a point
        charge by a magnetic field.
    :cvar VELOCITY: Rate of change of position. Also used for the
        average velocity of a collection of particles, also referred to
        as bulk velocity.
    :cvar VOLUME_EMISSION_RATE: The volume emission rate, e(r,t,l), is
        the number of photons emitted per unit source volume per second
        (photons/m^3/s), as measured along the line of sight between the
        source point and the observer. The Volume Emission Rate is in
        general a function of the line-of-sight distance, r, time, t,
        and wavelength, l. The Volume Emission Rate is actually not a
        directly measurable quantity. However, the term has been
        commonly used in both data product descriptions and research
        publications.
    :cvar WAVEFORM_RECEIVER: A radio receiver which outputs the value of
        one or more components of the electric and/or magnetic field as
        a function of time.
    :cvar WAVELENGTH: The peak-to-peak distance over one wave period.
    :cvar WAVES: Data resulting from observations of wave experiments
        and natural wave phenomena. Wave experiments are typically
        active and natural wave phenomena are passive. Examples of wave
        experiments include coherent/incoherent scatter radars, radio
        soundings, VLF propagation studies, ionospheric scintillation of
        beacon satellite signals, etc. Examples of natural wave
        phenomena include micropulsations, mesospheric gravity waves,
        auroral/plasmaspheric hiss, Langmuir waves, AKR, Jovian
        decametric radiation, solar radio bursts, etc.
    :cvar WAVES_ACTIVE: Exerting an influence or producing a change or
        effect. An active measurement is one which produces a
        transmission or excitation as a part of the measurement cycle.
    :cvar WAVES_PASSIVE: Movement or effect produced by outside
        influence. A passive measurement is one which does not produce a
        transmission or excitation as a part of the measurement cycle.
    :cvar WEB_RESOURCE: A Web page or file-based resource accessible by
        a URL.
    :cvar WEB_SERVICE: A Web-based service that uses SOAP, WSDL or UDDI
        open standards.
    :cvar WHITE_LIGHT: Photons with a wavelength in the visible range
        for humans.
    :cvar XRAYS: Photons with a wavelength range: 0.001 nm to 10 nm.
    """

    VALUE_2_DCUTS = "2DCuts"
    VALUE_3_DCUBES = "3DCubes"
    ACELECTRIC_FIELD = "ACElectricField"
    ACMAGNETIC_FIELD = "ACMagneticField"
    ABSORPTION = "Absorption"
    ACTIVITY_INDEX = "ActivityIndex"
    ADIABATIC_INVARIANT = "AdiabaticInvariant"
    ADIABATIC_INVARIANT_MAGNETIC_MOMENT = "AdiabaticInvariant.MagneticMoment"
    ADIABATIC_INVARIANT_BOUNCE_MOTION = "AdiabaticInvariant.BounceMotion"
    ADIABATIC_INVARIANT_DRIFT_MOTION = "AdiabaticInvariant.DriftMotion"
    AEROSOL = "Aerosol"
    AKASOFU_EPSILON = "AkasofuEpsilon"
    ALBEDO = "Albedo"
    ALFVEN_MACH_NUMBER = "AlfvenMachNumber"
    ALFVEN_VELOCITY = "AlfvenVelocity"
    ALPHA_PARTICLE = "AlphaParticle"
    ANTENNA = "Antenna"
    ARRIVAL_DIRECTION = "ArrivalDirection"
    ATOM = "Atom"
    ATOMIC_NUMBER_DETECTED = "AtomicNumberDetected"
    AVERAGE_CHARGE_STATE = "AverageChargeState"
    AZIMUTH_ANGLE = "AzimuthAngle"
    CA_K = "CaK"
    CHANNELTRON = "Channeltron"
    CHARGE_EXCHANGE = "ChargeExchange"
    CHARGE_FLUX = "ChargeFlux"
    CHARGE_STATE = "ChargeState"
    CORONOGRAPH = "Coronograph"
    COUNT_RATE = "CountRate"
    COUNTS = "Counts"
    CROSS_SECTION = "CrossSection"
    CURRENT = "Current"
    CURRENT_DENSITY = "CurrentDensity"
    DATA_QUALITY = "DataQuality"
    DISSOCIATIVE_RECOMBINATION = "DissociativeRecombination"
    DOPPLER_FREQUENCY = "DopplerFrequency"
    DOPPLERGRAM = "Dopplergram"
    DOUBLE_SPHERE = "DoubleSphere"
    DUST = "Dust"
    DUST_DETECTOR = "DustDetector"
    DYNAMIC_PRESSURE = "DynamicPressure"
    ELECTRIC = "Electric"
    ELECTRIC_FIELD = "ElectricField"
    ELECTROMAGNETIC = "Electromagnetic"
    ELECTRON = "Electron"
    ELECTRON_DRIFT_INSTRUMENT = "ElectronDriftInstrument"
    ELECTRON_IMPACT = "ElectronImpact"
    ELECTROSTATIC = "Electrostatic"
    ELECTROSTATIC_ANALYSER = "ElectrostaticAnalyser"
    ELEVATION_ANGLE = "ElevationAngle"
    EMISSIVITY = "Emissivity"
    ENERGETIC_PARTICLE_INSTRUMENT = "EnergeticParticleInstrument"
    ENERGETIC_PARTICLES = "EnergeticParticles"
    ENERGY = "Energy"
    ENERGY_DENSITY = "EnergyDensity"
    ENERGY_FLUX = "EnergyFlux"
    ENERGY_PER_CHARGE = "EnergyPerCharge"
    ENTROPY = "Entropy"
    EPHEMERIS = "Ephemeris"
    EQUIVALENT_WIDTH = "EquivalentWidth"
    EXPERIMENT = "Experiment"
    EXTREME_ULTRAVIOLET = "ExtremeUltraviolet"
    FAR_ULTRAVIOLET = "FarUltraviolet"
    FARADAY_CUP = "FaradayCup"
    FLOW_SPEED = "FlowSpeed"
    FLOW_VELOCITY = "FlowVelocity"
    FLUENCE = "Fluence"
    FLUX_FEEDBACK = "FluxFeedback"
    FOURIER_TRANSFORM_SPECTROGRAPH = "FourierTransformSpectrograph"
    FREQUENCY = "Frequency"
    FREQUENCY_TO_GYROFREQUENCY_RATIO = "FrequencyToGyrofrequencyRatio"
    GAMMA_RAYS = "GammaRays"
    GEIGER_MUELLER_TUBE = "GeigerMuellerTube"
    GEOMETRIC_FACTOR = "GeometricFactor"
    GYROFREQUENCY = "Gyrofrequency"
    HALPHA = "Halpha"
    HARD_XRAYS = "HardXRays"
    HE10830 = "He10830"
    HE304 = "He304"
    HEAT_FLUX = "HeatFlux"
    HOUSEKEEPING = "Housekeeping"
    HYDRODYNAMIC = "Hydrodynamic"
    IMFCLOCK_ANGLE = "IMFClockAngle"
    IMAGE_INTENSITY = "ImageIntensity"
    IMAGER = "Imager"
    IMAGING_SPECTROMETER = "ImagingSpectrometer"
    INFRARED = "Infrared"
    INSTRUMENT_MODE = "InstrumentMode"
    INSTRUMENT_STATUS = "InstrumentStatus"
    INTENSITY = "Intensity"
    INTERFEROMETER = "Interferometer"
    ION = "Ion"
    ION_CHAMBER = "IonChamber"
    ION_COMPOSITION = "IonComposition"
    ION_DRIFT = "IonDrift"
    ION_GAUGE = "IonGauge"
    IRRADIANCE = "Irradiance"
    K7699 = "K7699"
    LBHBAND = "LBHBand"
    LSHELL = "LShell"
    LANGMUIR_PROBE = "LangmuirProbe"
    LINE_DEPTH = "LineDepth"
    LINES = "Lines"
    LONG_WIRE = "LongWire"
    LOWER_HYBRID_FREQUENCY = "LowerHybridFrequency"
    MHD = "MHD"
    MAGNETIC = "Magnetic"
    MAGNETIC_FIELD = "MagneticField"
    MAGNETOGRAM = "Magnetogram"
    MAGNETOGRAPH = "Magnetograph"
    MAGNETOMETER = "Magnetometer"
    MAGNETOSONIC_MACH_NUMBER = "MagnetosonicMachNumber"
    MASS = "Mass"
    MASS_DENSITY = "MassDensity"
    MASS_NUMBER = "MassNumber"
    MASS_PER_CHARGE = "MassPerCharge"
    MASS_SPECTROMETER = "MassSpectrometer"
    MICROCHANNEL_PLATE = "MicrochannelPlate"
    MICROWAVE = "Microwave"
    MODE_AMPLITUDE = "ModeAmplitude"
    MOLECULE = "Molecule"
    MULTISPECTRAL_IMAGER = "MultispectralImager"
    NA_D = "NaD"
    NEUTRAL_ATOM_IMAGER = "NeutralAtomImager"
    NEUTRAL_ATOM_IMAGES = "NeutralAtomImages"
    NEUTRAL_GAS = "NeutralGas"
    NEUTRAL_PARTICLE_DETECTOR = "NeutralParticleDetector"
    NEUTRON = "Neutron"
    NI6768 = "Ni6768"
    NUMBER_DENSITY = "NumberDensity"
    NUMBER_FLUX = "NumberFlux"
    OPTICAL = "Optical"
    ORIENTATION = "Orientation"
    OTHER = "Other"
    PARTICLE_CORRELATOR = "ParticleCorrelator"
    PARTICLE_DETECTOR = "ParticleDetector"
    PARTICLE_RADIUS = "ParticleRadius"
    PARTICLE_RIGIDITY = "ParticleRigidity"
    PHASE_SPACE_DENSITY = "PhaseSpaceDensity"
    PHOTO_IONIZATION = "PhotoIonization"
    PHOTOMETER = "Photometer"
    PHOTOMULTIPLIER_TUBE = "PhotomultiplierTube"
    PHOTON = "Photon"
    PHOTOPOLARIMETER = "Photopolarimeter"
    PLASMA_BETA = "PlasmaBeta"
    PLASMA_FREQUENCY = "PlasmaFrequency"
    PLASMA_WAVES = "PlasmaWaves"
    PLATFORM = "Platform"
    POLAR_ANGLE = "PolarAngle"
    POLARIZATION = "Polarization"
    POSITIONAL = "Positional"
    POSITRON = "Positron"
    POTENTIAL = "Potential"
    POYNTING_FLUX = "PoyntingFlux"
    PRESSURE = "Pressure"
    PROFILE = "Profile"
    PROPAGATION_TIME = "PropagationTime"
    PROPORTIONAL_COUNTER = "ProportionalCounter"
    PROTON = "Proton"
    QUADRISPHERICAL_ANALYSER = "QuadrisphericalAnalyser"
    RADAR = "Radar"
    RADIANCE = "Radiance"
    RADIO_FREQUENCY = "RadioFrequency"
    RADIOMETER = "Radiometer"
    RATE = "Rate"
    REMARK = "Remark"
    RESONANCE_SOUNDER = "ResonanceSounder"
    RETARDING_POTENTIAL_ANALYSER = "RetardingPotentialAnalyser"
    RIOMETER = "Riometer"
    ROTATION_MATRIX = "RotationMatrix"
    SPICE = "SPICE"
    SCINTILLATION_DETECTOR = "ScintillationDetector"
    SEARCH_COIL = "SearchCoil"
    SOFT_XRAYS = "SoftXRays"
    SOLAR_UVFLUX = "SolarUVFlux"
    SOLID_STATE_DETECTOR = "SolidStateDetector"
    SONIC_MACH_NUMBER = "SonicMachNumber"
    SOUND_SPEED = "SoundSpeed"
    SOUNDER = "Sounder"
    SPACECRAFT_POTENTIAL_CONTROL = "SpacecraftPotentialControl"
    SPATIAL_SERIES = "SpatialSeries"
    SPECTRA = "Spectra"
    SPECTRAL_POWER_RECEIVER = "SpectralPowerReceiver"
    SPECTROMETER = "Spectrometer"
    SPECTRUM = "Spectrum"
    SPIN_PERIOD = "SpinPeriod"
    SPIN_PHASE = "SpinPhase"
    SPIN_RATE = "SpinRate"
    STOKES_PARAMETERS = "StokesParameters"
    TELEMETRY = "Telemetry"
    TEMPERATURE = "Temperature"
    TEMPORAL = "Temporal"
    THERMAL_PLASMA = "ThermalPlasma"
    THERMAL_SPEED = "ThermalSpeed"
    TIME_OF_FLIGHT = "TimeOfFlight"
    TIME_SERIES = "TimeSeries"
    TOTAL_PRESSURE = "TotalPressure"
    ULTRAVIOLET = "Ultraviolet"
    UNSPECIFIED = "Unspecified"
    UPPER_HYBRID_FREQUENCY = "UpperHybridFrequency"
    VCROSS_B = "VCrossB"
    VELOCITY = "Velocity"
    VOLUME_EMISSION_RATE = "VolumeEmissionRate"
    WAVEFORM_RECEIVER = "WaveformReceiver"
    WAVELENGTH = "Wavelength"
    WAVES = "Waves"
    WAVES_ACTIVE = "Waves.Active"
    WAVES_PASSIVE = "Waves.Passive"
    WEB_RESOURCE = "WebResource"
    WEB_SERVICE = "WebService"
    WHITE_LIGHT = "WhiteLight"
    XRAYS = "XRays"


class ParticleQuantity(Enum):
    """
    Identifiers for the characterization of the physical properties of the
    particle.

    :cvar ADIABATIC_INVARIANT: A property of a physical system usually
        related to periodic phenomena that remains constant under slowly
        varying conditions.
    :cvar ADIABATIC_INVARIANT_MAGNETIC_MOMENT: A constant of motion
        related to the gyromotion of a particle in a magnetic field that
        is either static or slowly varying with respect to the
        gyroperiod. The magnetic moment is usually denoted by using the
        lower-case Greek letter for mu, &amp;#956;, and can be
        calculated by using &amp;#956;=m(u^2/2B) where m is the particle
        mass, u is the velocity of the particle perpendicular to the
        constant or average magnetic field direction, and B is the
        magnitude of the magnetic field strength.
    :cvar ADIABATIC_INVARIANT_BOUNCE_MOTION: The second adiabatic
        invariant is associated with periodic bounce motion of charged
        particles trapped between two magnetic mirrors on a magnetic
        field line. The second invariant, termed J, is defined by using
        the integral J=m &amp;int; v||*ds where m is the mass of the
        charged particle, v|| is the particle velocity along the field
        line, and ds represents elemental arc lengths along the field
        line. The second adiabatic invariant is conserved as long as
        changes in the background magnetic field occur at time scales
        much longer than the bounce time of the charged particles.
    :cvar ADIABATIC_INVARIANT_DRIFT_MOTION: The third invariant for
        charged particle motion in a dipolar magnetic field is
        associated with drift of its guiding center in the equatorial
        plane. The conserved quantity, J&lt;sub&gt;2&lt;/sub&gt;, is
        equal to q&amp;phi; where q is the particle charge and &amp;phi;
        is the magnetic flux enclosed within the particle drift path.
    :cvar ARRIVAL_DIRECTION: An angular measure of the direction from
        which an energetic particle or photon was incident on a
        detector. The angles may be measured in any coordinate system.
    :cvar ATOMIC_NUMBER_DETECTED: The number of protons in the nucleus
        of an atom as determined by a detector.
    :cvar AVERAGE_CHARGE_STATE: A measure of the composite deficit
        (positive) or excess (negative) of electrons with respect to
        protons.
    :cvar CHARGE_FLUX: The number of ionized particles passing through a
        unit area per unit time, for instance as measured by a Faraday
        cup.
    :cvar CHARGE_STATE: Charge of a fully or partially stripped ion, in
        units of the charge of a proton. Charge state of a bare proton
        is equal to one.
    :cvar COUNT_RATE: The number of events per unit time.
    :cvar COUNTS: The number of detection events occurring in a detector
        over the detector accumulation time.
    :cvar CURRENT: It is the scalar quantity giving the net charge
        (summed over charged particle species) per unit time flowing
        across a given surface.
    :cvar CURRENT_DENSITY: It is the vector quantity giving the net
        charge (summed over charged particle species) per unit cross-
        sectional area per unit time flowing through a given point.
        Measurements of current density are often provided in terms of
        the magnetic perturbations (superposed upon a background
        magnetic field, if present) associated with the current density.
    :cvar DYNAMIC_PRESSURE: Dynamic pressure is a measure of the kinetic
        energy per unit volume of a fluid. For instance, the solar wind
        dynamic pressure or ram pressure for a purely proton plasma is
        equal to m&lt;sub&gt;p&lt;/sub&gt; n V&lt;sup&gt;2&lt;/sup&gt;
        where m&lt;sub&gt;p&lt;/sub&gt; is the proton mass, n is the
        proton number density, and V is the solar wind speed.
    :cvar ENERGY: The capacity for doing work as measured by the
        capability of doing work (potential energy) or the conversion of
        this capability to motion (kinetic energy).
    :cvar ENTROPY: A function of thermodynamic quantity, such as
        temperature, pressure, or composition, that is a measure of the
        energy that is not available for work during a thermodynamic
        process. It is often interpreted as the degree of disorder or
        randomness in the system.
    :cvar ENERGY_DENSITY: The amount of energy per unit volume.
    :cvar ENERGY_FLUX: The amount of energy passing through a unit area
        in a unit time.
    :cvar ENERGY_PER_CHARGE: The kinetic energy, E, per unit net charge,
        q, that is E/q, for an electron or an ionized atom, molecule, or
        dust particle.
    :cvar FLOW_SPEED: The rate at which particles or energy is passing
        through a unit area in a unit time.
    :cvar FLOW_VELOCITY: The volume of matter passing through a unit
        area perpendicular to the direction of flow in a unit of time.
    :cvar FLUENCE: The time integral of a flux. A fluence is a not a
        measurement of flux per unit time.
    :cvar GEOMETRIC_FACTOR: A measure of the gathering power of a
        particle detector. The geometric factor can be used to correct
        particle measurements by accounting for the fact that only a
        fraction of the source particles is able to gain entry through
        the aperture of a detector. For an isotopic source distribution,
        the geometric factor corresponds to the solid angle subtended by
        the aperture. In practice, determination of the geometric factor
        requires numerical modeling and depends on detector design and
        the characteristics of the source.
    :cvar GYROFREQUENCY: The number of gyrations around a magnetic
        guiding center (field line) a charged particle makes per unit
        time due to the Lorentz force.
    :cvar HEAT_FLUX: Flow of thermal energy through a gas or plasma
        typically computed as third moment of a distribution function.
    :cvar LSHELL: The L-shell is the magnetic equatorial radius (in
        units of planetary radii) of a dipole magnetic field line. For
        instance, if the L-shell value equals 6 say at Earth, the
        magnetic field lines cross the magnetic equator at six Earth
        radii. The L-shell concept can be applied generally to any
        magnetized planet or satellite with a dominant dipolar magnetic
        field moment.
    :cvar MASS: The measure of inertia (mass) of individual objects
        (e.g., aerosols).
    :cvar MASS_DENSITY: The mass of particles per unit volume.
    :cvar MASS_NUMBER: The total number of protons and neutrons
        (together known as nucleons) in an atomic nucleus.
    :cvar MASS_PER_CHARGE: The mass, m, per unit net charge, q, that is
        m/q, for an electron or an ionized atom, molecule, or dust
        particle.
    :cvar NUMBER_DENSITY: The number of particles per unit volume.
    :cvar NUMBER_FLUX: The number of particles passing a unit area in
        unit time, possibly also per unit energy (or equivalent) and/or
        per unit look direction.
    :cvar PARTICLE_RADIUS: The mean radius for a Gaussian distribution
        of particles with an axial ratio of 2 and a distribution width
        that varies as 0.5 radius. A value of zero means no cloud was
        detected.
    :cvar PARTICLE_RIGIDITY: The particle momentum per unit charge. The
        particle Rigidity, R, is equal to pc/Ze.
    :cvar PHASE_SPACE_DENSITY: The number of particles per unit volume
        in the six-dimensional space of position and velocity.
    :cvar PLASMA_FREQUENCY: A number density dependent characteristic
        frequency of a plasma.
    :cvar PRESSURE: The force per unit area exerted by a particle
        distribution or field.
    :cvar SONIC_MACH_NUMBER: The ratio of the bulk flow speed to the
        speed of sound in the medium.
    :cvar SOUND_SPEED: The speed at which sound travels through a
        medium.
    :cvar TEMPERATURE: A measure of the kinetic energy of random motion
        with respect to the average. Temperature is properly defined
        only for an equilibrium particle distribution (Maxwellian
        distribution).
    :cvar THERMAL_SPEED: For a Maxwellian distribution, the difference
        between the mean speed and the speed within 69% (one sigma) of
        all the members of the speed distribution occur.
    :cvar VELOCITY: Rate of change of position. Also used for the
        average velocity of a collection of particles, also referred to
        as bulk velocity.
    """

    ADIABATIC_INVARIANT = "AdiabaticInvariant"
    ADIABATIC_INVARIANT_MAGNETIC_MOMENT = "AdiabaticInvariant.MagneticMoment"
    ADIABATIC_INVARIANT_BOUNCE_MOTION = "AdiabaticInvariant.BounceMotion"
    ADIABATIC_INVARIANT_DRIFT_MOTION = "AdiabaticInvariant.DriftMotion"
    ARRIVAL_DIRECTION = "ArrivalDirection"
    ATOMIC_NUMBER_DETECTED = "AtomicNumberDetected"
    AVERAGE_CHARGE_STATE = "AverageChargeState"
    CHARGE_FLUX = "ChargeFlux"
    CHARGE_STATE = "ChargeState"
    COUNT_RATE = "CountRate"
    COUNTS = "Counts"
    CURRENT = "Current"
    CURRENT_DENSITY = "CurrentDensity"
    DYNAMIC_PRESSURE = "DynamicPressure"
    ENERGY = "Energy"
    ENTROPY = "Entropy"
    ENERGY_DENSITY = "EnergyDensity"
    ENERGY_FLUX = "EnergyFlux"
    ENERGY_PER_CHARGE = "EnergyPerCharge"
    FLOW_SPEED = "FlowSpeed"
    FLOW_VELOCITY = "FlowVelocity"
    FLUENCE = "Fluence"
    GEOMETRIC_FACTOR = "GeometricFactor"
    GYROFREQUENCY = "Gyrofrequency"
    HEAT_FLUX = "HeatFlux"
    LSHELL = "LShell"
    MASS = "Mass"
    MASS_DENSITY = "MassDensity"
    MASS_NUMBER = "MassNumber"
    MASS_PER_CHARGE = "MassPerCharge"
    NUMBER_DENSITY = "NumberDensity"
    NUMBER_FLUX = "NumberFlux"
    PARTICLE_RADIUS = "ParticleRadius"
    PARTICLE_RIGIDITY = "ParticleRigidity"
    PHASE_SPACE_DENSITY = "PhaseSpaceDensity"
    PLASMA_FREQUENCY = "PlasmaFrequency"
    PRESSURE = "Pressure"
    SONIC_MACH_NUMBER = "SonicMachNumber"
    SOUND_SPEED = "SoundSpeed"
    TEMPERATURE = "Temperature"
    THERMAL_SPEED = "ThermalSpeed"
    VELOCITY = "Velocity"


class ParticleType(Enum):
    """
    Identifiers for the characterization of the kind of particle observed by the
    measurement.

    :cvar AEROSOL: A suspension of fine solid or liquid particles in a
        gas.
    :cvar ALPHA_PARTICLE: A positively charged nuclear particle that
        consists of two protons and two neutrons.
    :cvar ATOM: Matter consisting of a nucleus surrounded by electrons
        which has no net charge.
    :cvar DUST: Free microscopic particles of solid material.
    :cvar ELECTRON: An elementary particle that has a negative charge
        equal to about 1.60218*10^-19 C and a rest mass equal to about
        9.10938*10^-31 kg.
    :cvar ION: An atom that has acquired a net electric charge by
        gaining or losing one or more electrons (Note: Z&gt;2).
    :cvar MOLECULE: A group of atoms so united and combined by chemical
        affinity that they form a complete, integrated whole, being the
        smallest portion of any particular compound that can exist in a
        free state.
    :cvar NEUTRON: An elementary particle with neutral charge that is a
        constituent of atomic nuclei. Neutrons have a rest mass slightly
        large than that of a proton equal to about 1.67493*10^-24 kg.
    :cvar PROTON: An elementary particle that is a constituent of all
        atomic nuclei. Protons have a positive charge equal to about
        1.60218*10^-19 C and a rest mass equal to about 1.67262*10^-27
        kg.
    :cvar POSITRON: An elementary particle that has a positive charge
        equal to about 1.60218*10^-19 C and a rest mass equal to about
        9.10938*10^-31 kg.
    """

    AEROSOL = "Aerosol"
    ALPHA_PARTICLE = "AlphaParticle"
    ATOM = "Atom"
    DUST = "Dust"
    ELECTRON = "Electron"
    ION = "Ion"
    MOLECULE = "Molecule"
    NEUTRON = "Neutron"
    PROTON = "Proton"
    POSITRON = "Positron"


class PhenomenonType(Enum):
    """Identifiers for the characteristics or categorization of an observation.

    Note: Joe King to provide.

    :cvar ACTIVE_REGION: A localized, transient volume of the solar
        atmosphere in which PLAGEs, SUNSPOTS, FACULAe, FLAREs, etc. may
        be observed.
    :cvar AURORA: A natural electrical phenomenon characterized by the
        appearance of streamers of reddish or greenish light in the sky,
        especially near the northern or southern magnetic pole. The
        effect is caused by the interaction of charged particles from
        the sun with atoms in the upper atmosphere. In northern and
        southern regions, it is respectively called aurora borealis or
        Northern Lights and aurora australis or Southern Lights.
    :cvar BOW_SHOCK_CROSSING: A crossing of the boundary between the
        undisturbed (except for foreshock effects) solar wind and the
        shocked, decelerated solar wind of the magnetosheath.
    :cvar CORONAL_HOLE: An extended region of the corona, exceptionally
        low in density and associated with unipolar photospheric
        regions. A coronal hole can be an open magnetic field in the
        corona and (perhaps) inner heliosphere which has a faster than
        average solar wind outflow velocity. A region of lower than
        quiet coronal ion densities and electron densities in the corona
        or a coronal region with lower peak electron temperature than
        that found under quiet coronal conditions.
    :cvar CORONAL_MASS_EJECTION: A solar event (CME) that involves a
        burst of plasma ejected into the interplanetary medium. CMEs may
        be observed remotely relatively near the Sun or in situ in the
        interplanetary medium. Note that CMEs are often referred to as
        Interplanetary CMEs (ICMEs).
    :cvar EITWAVE: A wave in the corona of the Sun that generates shock
        waves in the solar chromosphere (Moreton Waves). EIT Waves are
        produced by large solar flare and expand outward at about 1,000
        km/s. It usually appears as a slowly moving diffuse arc of
        brightening in H-alpha, and may travel for several hundred
        thousand km.
    :cvar ENERGETIC_SOLAR_PARTICLE_EVENT: An enhancement of
        interplanetary fluxes of energetic ions accelerated by
        interplanetary shocks and/or solar flares.
    :cvar FORBUSH_DECREASE: A rapid decrease in the observed galactic
        cosmic ray intensity following the passage of an outwardly
        convecting interplanetary magnetic field disturbance, such as
        those associated with large CMEs, that sweep some galactic
        cosmic rays away from Earth.
    :cvar GEOMAGNETIC_STORM: A magnetospheric disturbance typically
        defined by variations in the horizontal component of the surface
        magnetic field on the Earth. The variation typically starts with
        a field enhancement associated with a solar wind pressure pulse
        and continues with a field depression associated with an
        enhancement of the diamagnetic magnetospheric ring current.
    :cvar INTERPLANETARY_SHOCK: A shock propagating generally anti-
        sunward through the slower solar wind, often seen in front of
        CME-associated plasma clouds.
    :cvar MAGNETIC_CLOUD: A transient event observed in the solar wind
        characterized as a region of enhanced magnetic field strength,
        smooth rotation of the magnetic field vector and low proton
        density and temperature.
    :cvar MAGNETOPAUSE_CROSSING: A crossing of the interface between the
        shocked solar wind in the magnetosheath and the magnetic field
        and plasma in the magnetosphere.
    :cvar RADIO_BURST: Emissions of the Sun in radio wavelengths from
        centimeters to dekameters, under both quiet and disturbed
        conditions. Radio Bursts can be Type I consisting of many short,
        narrow-band bursts in the metric range (80 MHz to 200 MHz). Type
        II consisting of narrow-band emission that begins in the meter
        range (150 MHz) and sweeps slowly (tens of minutes) toward
        dekameter wavelengths (20 MHz). Type III consisting of narrow-
        band bursts that sweep rapidly (seconds) from decimeter to
        dekameter wavelengths (500 MHz to 20 MHz) and Type IV consisting
        of a smooth continuum of broadband bursts primarily in the meter
        range (10 MHz to 200 MHz).
    :cvar SECTOR_BOUNDARY_CROSSING: A sector boundary crossing is a
        transit by a spacecraft across the heliospheric current sheet
        separating the dominantly outward (away from the Sun)
        interplanetary magnetic field of one hemisphere of the
        heliosphere from the dominantly inward (towards the Sun)
        polarity of the other hemisphere. Such crossings have multi-day
        intervals of opposite IMF dominant polarities on either side.
    :cvar SOLAR_FLARE: An explosive event in the solar atmosphere which
        produces electromagnetic radiation across the electromagnetic
        spectrum at multiple wavelengths from long-wave radio to the
        shortest wavelength gamma rays.
    :cvar SOLAR_WIND_EXTREME: Intervals of unusually large or small
        values of solar wind attributes such as flow speed and ion
        density.
    :cvar STREAM_INTERACTION_REGION: The region where two solar wind
        streams, typically having differing characteristics and solar
        sources, abut up against (and possibly partially interpenetrate)
        each other. The abbreviation SIR is commonly used in place of
        Stream Interaction Region.
    :cvar SUBSTORM: A process by which plasma in the magnetotail becomes
        energized at a fast rate.
    """

    ACTIVE_REGION = "ActiveRegion"
    AURORA = "Aurora"
    BOW_SHOCK_CROSSING = "BowShockCrossing"
    CORONAL_HOLE = "CoronalHole"
    CORONAL_MASS_EJECTION = "CoronalMassEjection"
    EITWAVE = "EITWave"
    ENERGETIC_SOLAR_PARTICLE_EVENT = "EnergeticSolarParticleEvent"
    FORBUSH_DECREASE = "ForbushDecrease"
    GEOMAGNETIC_STORM = "GeomagneticStorm"
    INTERPLANETARY_SHOCK = "InterplanetaryShock"
    MAGNETIC_CLOUD = "MagneticCloud"
    MAGNETOPAUSE_CROSSING = "MagnetopauseCrossing"
    RADIO_BURST = "RadioBurst"
    SECTOR_BOUNDARY_CROSSING = "SectorBoundaryCrossing"
    SOLAR_FLARE = "SolarFlare"
    SOLAR_WIND_EXTREME = "SolarWindExtreme"
    STREAM_INTERACTION_REGION = "StreamInteractionRegion"
    SUBSTORM = "Substorm"


class ProcCoeffType(Enum):
    """
    Whether the model results are obtained from a stationary solution or are
    dynamically computed.

    :cvar CROSS_SECTION: Cross section of the reaction, when the
        reaction implies the collision of two particles.
    :cvar FREQUENCY: The number of occurrences of a repeating event per
        unit time.
    :cvar OTHER: Not classified with more specific terms. The context of
        its usage may be described in related text.
    :cvar RATE: Reaction rate: reaction production per unit of time.
    """

    CROSS_SECTION = "CrossSection"
    FREQUENCY = "Frequency"
    OTHER = "Other"
    RATE = "Rate"


class ProcessType(Enum):
    """
    Type of chemical process.

    :cvar CHARGE_EXCHANGE: Chemical process involving a charge transfer
        from an ion (which becomes neutral) to a neutral (which becomes
        ionized).
    :cvar DISSOCIATIVE_RECOMBINATION: Chemical process by which an ion
        is neutralized by capturing an electron, and splits in two new
        neutral species.
    :cvar ELECTRON_IMPACT: Chemical process by which a neutral is
        ionized thanks to the energy from the impact of an electron.
    :cvar PHOTO_IONIZATION: Chemical process by which a neutral is
        ionized thanks to the energy from a photon.
    """

    CHARGE_EXCHANGE = "ChargeExchange"
    DISSOCIATIVE_RECOMBINATION = "DissociativeRecombination"
    ELECTRON_IMPACT = "ElectronImpact"
    PHOTO_IONIZATION = "PhotoIonization"


class ProcessingLevel(Enum):
    """
    Identifiers to characterize the amount and type of manipulation which has been
    applied to the sampled data.

    :cvar CALIBRATED: Data wherein sensor outputs have been convolved
        with instrument response function, often irreversibly, to yield
        data in physical units. Similar to NASA Level 2.
    :cvar RAW: Data in its original state with no processing to account
        for calibration. Similar to NASA Level 0.
    :cvar UNCALIBRATED: Duplicate data are removed from the data stream
        and data are time ordered. Values are not adjusted for any
        potential biases or external factors. Similar to NASA Level 1.
    :cvar VALUE_ADDED: Calibrated data that has been mapped on uniform
        space-time grid scales with gaps, flags and out-of-range values
        replaced with appropriate values. Similar to NASA Level 3.
    """

    CALIBRATED = "Calibrated"
    RAW = "Raw"
    UNCALIBRATED = "Uncalibrated"
    VALUE_ADDED = "ValueAdded"


class Product(Enum):
    """
    Type of article or asset.

    :cvar VALUE_2_DCUTS: A set of 2-D arrays that contain the values of
        physical parameters, i.e., magnetic field vectors, particle
        densities, temperatures, etc., at the grid points located in a
        planar slice of a model volume.
    :cvar VALUE_3_DCUBES: A set of 3-D arrays that contain the values of
        physical parameters, i.e., magnetic field vectors, particle
        densities, temperatures, etc., at grid points in a model volume.
    :cvar LINES: A set of 1-D arrays that contain the values of physical
        parameters, i.e., magnetic field vectors, particle densities,
        temperatures, etc., at the grid points along a line though a
        model volume. For instance, the points of the line may
        correspond to the trajectory of a spacecraft through model
        space.
    :cvar SPATIAL_SERIES: A set of 3-D arrays that contain the values of
        physical parameters, i.e., magnetic field vectors, particle
        densities, temperatures, etc., at grid points in a spacial
        volume.
    :cvar SPECTRA: A term that applies to any signal that can be
        measured or decomposed along a continuous variable such as the
        electromagnetic radiation which can be decomposed as a function
        of wavelength or frequency.
    :cvar TIME_SERIES: A representation of data showing a set of
        observations taken at different points in time and charted as a
        time series.
    """

    VALUE_2_DCUTS = "2DCuts"
    VALUE_3_DCUBES = "3DCubes"
    LINES = "Lines"
    SPATIAL_SERIES = "SpatialSeries"
    SPECTRA = "Spectra"
    TIME_SERIES = "TimeSeries"


@dataclass
class PublicationInfo:
    """
    Information required to mint a DOI for the resource being described in SPASE.
    """

    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    authors: Optional[str] = field(
        default=None,
        metadata={
            "name": "Authors",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    publication_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PublicationDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    published_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublishedBy",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    landing_page_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "LandingPageURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


class Qualifier(Enum):
    """
    Identifiers for terms which refine the type or attribute of a quantity.

    :cvar INCIDENT: Direction-dependent property.
    :cvar ANISOTROPY: Direction-dependent property.
    :cvar ARRAY: A sequence of values corresponding to the elements in a
        rectilinear, n-dimension matrix. Each value can be referenced by
        a unique index.
    :cvar AUTO_SPECTRUM: The Fourier transform of the auto correlation
        function for physical or empirical observations, which describes
        the general dependence of the time series data values at one
        instant on the time series data values at another instant.
    :cvar AVERAGE: The statistical mean equal to the sum of a set of
        values divided by the number of values in the set.
    :cvar CHARACTERISTIC: A quantity which can be easily identified and
        measured in a given environment.
    :cvar CIRCULAR: Relative to polarization, right-handed circularly
        polarized light is defined such that the electric field is
        rotating clockwise as seen by an observer towards whom the wave
        is moving. Left-handed circularly polarized light is defined
        such that the electric field is rotating counterclockwise as
        seen by an observer towards whom the wave is moving. The
        polarization of magnetohydrodynamic waves is specified with
        respect to the ambient mean magnetic field. Right-handed
        polarized waves have a transverse electric field component which
        turns in a right-handed sense (that of the gyrating electrons)
        around the magnetic field.
    :cvar COHERENCE: The coherence between two signals x(t) and y(t),
        C&lt;sub&gt;xy&lt;/sub&gt;, is a real-valued function. The
        square of the coherence is defined by using:
        Cxy^2=|Gxy(f)|^2/Gxx(f)Gyy(f) where Gxy(f) is equal to the
        cross-spectral density between two time series denoted as x and
        y, respectively, and Gxx(f) and Gyy(f) are equal to the auto-
        spectral densities of the same two time series. Values of Cxy^2
        always lie in the range between zero and one, 0&lt;=Cxy^2&lt;=1,
        in accordance with the Cauchy-Schwarz inequality.
    :cvar COLUMN: A 2-D measure of a quantity. The column is the area
        over which the quantity is measured.
    :cvar COMPONENT: Projection of a vector along one of the base axes
        of a coordinate system.
    :cvar COMPONENT_I: Projection of a vector along the first named axis
        of a coordinate system. Typically, the x-axis, but could be the
        R-axis for an RTN coordinate system.
    :cvar COMPONENT_J: Projection of a vector along the second named
        axis of a coordinate system. Typically, the y-axis, but could be
        the T-axis for an RTN coordinate system.
    :cvar COMPONENT_K: Projection of a vector along the third named axis
        of a coordinate system. Typically, the z-axis, but could be the
        N-axis for an RTN coordinate system.
    :cvar CONFIDENCE: An expression of how certain that a quantity is
        valid or accurate.
    :cvar CORE: The central or main part of an object or calculated
        distribution. For example, the part of a distribution of
        particles at low energies that is a thermal (Maxwellian)
        population.
    :cvar CROSS_SPECTRUM: The Fourier transform of the cross correlation
        of two physical or empirical observations.
    :cvar DEVIATION: The difference between an observed value and the
        expected value of a quantity.
    :cvar DIFFERENTIAL: A measurement within a narrow range of energy
        and/or solid angle.
    :cvar DIRECTION: The spatial relation between an object and another
        object, the orientation of the object or the course along which
        the object points or moves.
    :cvar DIRECTIONAL: A measurement within a narrow range of solid
        angle.
    :cvar DIRECTION_ANGLE: The angle between a position vector or
        measured vector (or one of its projections onto a plane) and one
        of the base axes of the coordinate system.
    :cvar DIRECTION_ANGLE_AZIMUTH_ANGLE: The angle between the
        projection into the I-J plane of a position or measured vector
        and the I-axis of the coordinate system. Mathematically defined
        as arctan(J/I). This term could be also applied to angles
        measured in different planes, i.e., the IMF clock angle defined
        as arctan(|By|/Bz).
    :cvar DIRECTION_ANGLE_ELEVATION_ANGLE: The angle between the
        position or measured vector and the I-J plane of the coordinate
        system. Mathematically defined as arctan(K/sqrt(I^2+J^2)).
    :cvar DIRECTION_ANGLE_POLAR_ANGLE: The angle between the position or
        measured vector and the k-axis of the coordinate system.
        Mathematically defined as arctan([sqrt(i^2+j^2)]/k). This term
        could be also applied to angles between the vector and other
        components, for example the IMF cone angle defined as
        arccos(B&lt;sub&gt;x&lt;/sub&gt;/B&lt;sub&gt;t&lt;/sub&gt;).
    :cvar DIRECTION_COSINE: The cosine of the angle between two vectors
        usually between a vector and one of the basis axes defining a
        Cartesian coordinate system. Three angles and thus three
        direction cosines are required to define a vector direction in a
        3-D Euclidean space.
    :cvar DIRECTION_COSINE_I: Projection of a vector along the first
        named axis of a coordinate system. Typically, the x-axis, but
        could be the R-axis for an RTN coordinate system.
    :cvar DIRECTION_COSINE_J: Projection of a vector along the second
        named axis of a coordinate system. Typically, the y-axis, but
        could be the T-axis for an RTN coordinate system.
    :cvar DIRECTION_COSINE_K: Projection of a vector along the third
        named axis of a coordinate system. Typically, the z-axis, but
        could be the N-axis for an RTN coordinate system.
    :cvar ENCODED_PARAMETER: A variable that uses successive bits to
        encode, this is bitwise encode, a set of conditions by using a
        composited multi-bit numeric value. A common example is a
        bitwise encoded flag that denotes whether various possible
        errors that may affect a particular measurement. For example, a
        bit value equal to zero may indicate the absence of a particular
        error condition while a value equal to one would indicate the
        possibility that the associated datum should be ignored or used
        with caution due to the same error categorization.
    :cvar FIELD_ALIGNED: The component of a quantity which is oriented
        in the same direction of a field.
    :cvar FIT: Values that make a model agree with the data.
    :cvar GROUP: An assemblage of values that a certain relation or
        common characteristic.
    :cvar HALO: The part of an object or distribution surrounding some
        central body or distribution. For example, the particles above
        the core energies that show enhancements above the thermal
        population. Typically, a "power law tail" shows a break from the
        core Maxwellian at a particular energy.
    :cvar IMAGINARY_PART: Any number z can in general be represented by
        its complex form with z=a+ib where i, which is defined as the
        square root of -1, signifies the imaginary component of the
        number z. The coefficient b is called the imaginary part of the
        complex number z.
    :cvar INTEGRAL: A flux measurement in a broad range of energy and
        solid angle.
    :cvar INTEGRAL_AREA: Integration over the extent of a planar region,
        or of the surface of a solid.
    :cvar INTEGRAL_BANDWIDTH: Integration over the width a frequency
        band.
    :cvar INTEGRAL_SOLID_ANGLE: Integration over the angle in 3-D space
        that an object subtends at a point.
    :cvar LINEAR: Polarization where the E-field vector is confined to a
        given plane.
    :cvar LINE_OF_SIGHT: The line of sight is the line that connects the
        observer with the observed object. This expression is often used
        with measurements of Doppler velocity and magnetic field in
        magnetograms, where only the component of the vector field
        directed along the line of sight is measured.
    :cvar MAGNITUDE: A measure of the strength of a vector quantity or
        length of its representational vector.
    :cvar MAXIMUM: The largest value of a batch or sample or the upper
        bound of a probability distribution.
    :cvar MEDIAN: The measure of central tendency of a set of n values
        computed by ordering the values and taking the value at position
        (n+1)/2 when n is odd or the arithmetic mean of the values at
        positions n/2 and (n/2)+1 when n is even.
    :cvar MINIMUM: The smallest value of a batch or sample or the lower
        bound of a probability distribution.
    :cvar MOMENT: Parameters determined by integration over a
        distribution function convolved with a power of velocity.
    :cvar PARALLEL: Having the same direction as a given direction.
    :cvar PEAK: The maximum value for the quantity in question, over a
        period of time which is usually equal to the cadence.
    :cvar PERPENDICULAR: At right angles to a given direction.
    :cvar PERTURBATION: Variations in the state of a system.
    :cvar PHASE: A point or portion in a recurring series of changes.
    :cvar PHASE_ANGLE: Phase difference between two or more waves,
        normally expressed in degrees.
    :cvar POWER_SPECTRAL_DENSITY: The Power Spectral Density, PSD, is
        the measure of signal power content versus frequency, energy,
        wave number, etc. A PSD is typically used to characterize
        broadband random signals. The amplitude of the PSD is normalized
        by the spectral resolution employed to digitize the signal.
    :cvar PROJECTION: A measure of the length of a position or measured
        vector as projected into a plane of the coordinate system.
    :cvar PROJECTION_IJ: A measure of the length of a position or
        measured vector projected into the I-J (typically X-Y) plane of
        the coordinate system.
    :cvar PROJECTION_IK: A measure of the length of a position or
        measured vector projected into the I-K (typically X-Z) plane of
        the coordinate system.
    :cvar PROJECTION_JK: A measure of the length of a position or
        measured vector projected into the J-K (typically Y-Z) plane of
        the coordinate system.
    :cvar PSEUDO: Similar to or having the appearance of something else.
        Can be used to indicate an estimation or approximation of a
        particular quantity.
    :cvar RATIO: The relative magnitudes of two quantities.
    :cvar REAL_PART: Any number z can in general be represented by its
        complex form with z= a+ib where i, which is defined as the
        square root of -1, signifies the imaginary component of the
        number z. The coefficient a is called the real part of the
        complex number z.
    :cvar SCALAR: A quantity that is completely specified by its
        magnitude and has no direction.
    :cvar SPECTRAL: Characterized as a range or continuum of
        frequencies.
    :cvar STANDARD_DEVIATION: The square root of the average of the
        squares of deviations about the mean of a set of data. Standard
        deviation is a statistical measure of spread or variability.
    :cvar STOKES_PARAMETERS: A set of four parameters (usually called
        I,Q, U and V) which describe the polarization state of an
        electromagnetic wave propagating through space.
    :cvar STRAHL: A distribution of particles concentrated in a narrow
        energy band. The band may be may be aligned with a secondary
        feature. For example, it may occur in a narrow cone aligned with
        the mean magnetic field direction.
    :cvar SUPERHALO: The part of an object or distribution surrounding
        some central body or distribution evident in a second break in
        the distribution function (e.g., a different power law). It
        consists of a population with energies higher than that of
        coexisting halo population.
    :cvar SYMMETRIC: Equal distribution about one or more axes.
    :cvar TENSOR: A generalized linear quantity or geometrical entity
        that can be expressed as a multi-dimensional array relative to a
        choice of basis of the particular space on which it is defined.
    :cvar TOTAL: The summation of quantities over all possible species.
    :cvar TRACE: The sum of the elements on the main diagonal (the
        diagonal from the upper left to the lower right) of a square
        matrix.
    :cvar UNCERTAINTY: A statistically defined discrepancy between a
        measured quantity and the true value of that quantity that
        cannot be corrected by calculation or calibration.
    :cvar VARIANCE: A measure of dispersion of a set of data points
        around their mean value. The expectation value of the squared
        deviations from the mean.
    :cvar VECTOR: A set of parameter values each along some independent
        variable (e.g., components of a field in three orthogonal
        spatial directions, atmospheric temperature values at several
        altitudes, or at a given latitude and longitude).
    """

    INCIDENT = "Incident"
    ANISOTROPY = "Anisotropy"
    ARRAY = "Array"
    AUTO_SPECTRUM = "AutoSpectrum"
    AVERAGE = "Average"
    CHARACTERISTIC = "Characteristic"
    CIRCULAR = "Circular"
    COHERENCE = "Coherence"
    COLUMN = "Column"
    COMPONENT = "Component"
    COMPONENT_I = "Component.I"
    COMPONENT_J = "Component.J"
    COMPONENT_K = "Component.K"
    CONFIDENCE = "Confidence"
    CORE = "Core"
    CROSS_SPECTRUM = "CrossSpectrum"
    DEVIATION = "Deviation"
    DIFFERENTIAL = "Differential"
    DIRECTION = "Direction"
    DIRECTIONAL = "Directional"
    DIRECTION_ANGLE = "DirectionAngle"
    DIRECTION_ANGLE_AZIMUTH_ANGLE = "DirectionAngle.AzimuthAngle"
    DIRECTION_ANGLE_ELEVATION_ANGLE = "DirectionAngle.ElevationAngle"
    DIRECTION_ANGLE_POLAR_ANGLE = "DirectionAngle.PolarAngle"
    DIRECTION_COSINE = "DirectionCosine"
    DIRECTION_COSINE_I = "DirectionCosine.I"
    DIRECTION_COSINE_J = "DirectionCosine.J"
    DIRECTION_COSINE_K = "DirectionCosine.K"
    ENCODED_PARAMETER = "EncodedParameter"
    FIELD_ALIGNED = "FieldAligned"
    FIT = "Fit"
    GROUP = "Group"
    HALO = "Halo"
    IMAGINARY_PART = "ImaginaryPart"
    INTEGRAL = "Integral"
    INTEGRAL_AREA = "Integral.Area"
    INTEGRAL_BANDWIDTH = "Integral.Bandwidth"
    INTEGRAL_SOLID_ANGLE = "Integral.SolidAngle"
    LINEAR = "Linear"
    LINE_OF_SIGHT = "LineOfSight"
    MAGNITUDE = "Magnitude"
    MAXIMUM = "Maximum"
    MEDIAN = "Median"
    MINIMUM = "Minimum"
    MOMENT = "Moment"
    PARALLEL = "Parallel"
    PEAK = "Peak"
    PERPENDICULAR = "Perpendicular"
    PERTURBATION = "Perturbation"
    PHASE = "Phase"
    PHASE_ANGLE = "PhaseAngle"
    POWER_SPECTRAL_DENSITY = "PowerSpectralDensity"
    PROJECTION = "Projection"
    PROJECTION_IJ = "Projection.IJ"
    PROJECTION_IK = "Projection.IK"
    PROJECTION_JK = "Projection.JK"
    PSEUDO = "Pseudo"
    RATIO = "Ratio"
    REAL_PART = "RealPart"
    SCALAR = "Scalar"
    SPECTRAL = "Spectral"
    STANDARD_DEVIATION = "StandardDeviation"
    STOKES_PARAMETERS = "StokesParameters"
    STRAHL = "Strahl"
    SUPERHALO = "Superhalo"
    SYMMETRIC = "Symmetric"
    TENSOR = "Tensor"
    TOTAL = "Total"
    TRACE = "Trace"
    UNCERTAINTY = "Uncertainty"
    VARIANCE = "Variance"
    VECTOR = "Vector"


class Region(Enum):
    """
    Identifiers for areas of the physical world which may be occupied or observed.

    :cvar ASTEROID: A small extraterrestrial body consisting mostly of
        rock and metal that is in orbit around the Sun.
    :cvar COMET: A relatively small extraterrestrial body consisting of
        a frozen mass that travels around the Sun in a highly elliptical
        orbit.
    :cvar COMET_1_PHALLEY: 1P/Halley, is a short-period comet visible
        from Earth every 75 to 79 years. The comet was visited by the
        Halley Armada comprised of the ESA Giotto, Japanese Suisei and
        Sekigake, and Soviet Union Vega 1 and Vega 2 spacecraft in 1986.
    :cvar COMET_26_PGRIGG_SKJELLERUP: 26P/Grigg-Skjellerup is a periodic
        comet. It was visited by the ESA Giotto spacecraft in July 1992.
    :cvar COMET_67_PCHURYUMOV_GERASIMENKO: 67P/Churyumov-Gerasimenko is
        a Jupiter-family comet originally from the Kuiper belt. The ESA
        Rosetta spacecraft rendezvoused with Comet 67P on August 6, 2014
        and then orbited the comet from September 10, 2014 to September
        30, 2016. Philae, a lander carried by Rosetta, touched down on
        the comet surface on November 12, 2014.
    :cvar EARTH: The third planet from the Sun in our solar system.
    :cvar EARTH_MAGNETOSHEATH: The region between the bow shock and the
        magnetopause, characterized by very turbulent plasma.
    :cvar EARTH_MAGNETOSPHERE: The region of space above the atmosphere
        or surface of the planet and bounded by the magnetopause that is
        under the direct influence of the magnetic field of a planetary
        body.
    :cvar EARTH_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar EARTH_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar EARTH_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar EARTH_MAGNETOSPHERE_POLAR: The region near the pole of a body.
        For a magnetosphere the polar region is the area where magnetic
        field lines are open and includes the auroral zone.
    :cvar EARTH_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar EARTH_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar EARTH_MOON: The only natural satellite of the Earth.
    :cvar EARTH_NEAR_SURFACE: The gaseous and possibly ionized
        environment of a body extending from the surface to some
        specified altitude. For the Earth, this altitude is 2000 km.
    :cvar EARTH_NEAR_SURFACE_ATMOSPHERE: The neutral gases surrounding a
        body that extends from the surface and is bound to the body by
        virtue of the gravitational attraction.
    :cvar EARTH_NEAR_SURFACE_AURORAL_REGION: The region in the
        atmospheric where electrically-charged particles bombarding the
        upper atmosphere of a planet in the presence of a magnetic field
        produce an optical phenomenon.
    :cvar EARTH_NEAR_SURFACE_EQUATORIAL_REGION: A region centered on the
        equator and limited in latitude by approximately 23 deg north
        and south of the equator.
    :cvar EARTH_NEAR_SURFACE_IONOSPHERE: The charged or ionized gases
        surrounding a body that are nominally bound to the body by
        virtue of the gravitational attraction.
    :cvar EARTH_NEAR_SURFACE_IONOSPHERE_DREGION: The layer of the
        ionosphere that exists approximately 50 km to 95 km above the
        surface of the Earth. One of several layers in the ionosphere.
    :cvar EARTH_NEAR_SURFACE_IONOSPHERE_EREGION: A layer of ionized gas
        occurring at 90 km to 150 km above the ground. One of several
        layers in the ionosphere. Also called the Kennelly-Heaviside
        layer.
    :cvar EARTH_NEAR_SURFACE_IONOSPHERE_FREGION: A layer that contains
        ionized gases at a height of around 150-800 km above sea level,
        placing it in the thermosphere. the F region has the highest
        concentration of free electrons and ions anywhere in the
        atmosphere. It may be thought of as comprising two layers, the
        F1 layer and F2 layer. One of several layers in the ionosphere.
        Also known as the Appleton layer.
    :cvar EARTH_NEAR_SURFACE_IONOSPHERE_TOPSIDE: The region at the upper
        most areas of the ionosphere.
    :cvar EARTH_NEAR_SURFACE_MESOSPHERE: The layer of the atmosphere
        that extends from the Stratosphere to a range of 80 km to 85 km,
        temperature decreasing with height.
    :cvar EARTH_NEAR_SURFACE_MID_LATITUDE_REGION: When considering the
        case of the Earth, the mid-latitude region typically refers to
        two latitudinal bands, one in the northern hemisphere and the
        other in the southern hemisphere extending from about 23 deg to
        50 deg. The concept of mid-latitude regions does not apply to
        all bodies in the solar system and different latitudinal ranges
        would apply for each body case by case. The mid-latitude regions
        may be defined by using either planetographic or magnetic
        coordinates if the magnetic dipole is closely aligned with the
        spin axis of a magnetized body. Ground magnetometers located at
        mid-latitude on the Earth are well positioned to measure
        magnetic storm-time ring current variations.
    :cvar EARTH_NEAR_SURFACE_PLASMASPHERE: A region of the magnetosphere
        consisting of low energy (cool) plasma. It is located above the
        ionosphere. The outer boundary of the plasmasphere is known as
        the plasmapause, which is defined by an order of magnitude drop
        in plasma density.
    :cvar EARTH_NEAR_SURFACE_POLAR_CAP: The areas of the globe
        surrounding the poles and consisting of the region north of 60
        deg north latitude and the region south of 60 deg south
        latitude.
    :cvar EARTH_NEAR_SURFACE_SOUTH_ATLANTIC_ANOMALY_REGION: The region
        where the inner Van Allen radiation belt makes its closest
        approach to the surface of the Earth. The result is that, for a
        given altitude, the radiation intensity is higher over this
        region than elsewhere.
    :cvar EARTH_NEAR_SURFACE_STRATOSPHERE: The layer of the atmosphere
        that extends from the troposphere to about 30 km, temperature
        increases with height. The stratosphere contains the ozone
        layer.
    :cvar EARTH_NEAR_SURFACE_SUB_AURORAL_REGION: When considering the
        case of the Earth, the sub-auroral region typically refers to
        two latitudinal bands, one in the northern hemisphere and the
        other in the southern hemisphere extending from about 50 deg to
        low 60 deg latitude. The concept sub-auroral regions does not
        apply to all bodies in the solar system and different
        latitudinal ranges would apply for each body case by case. The
        sub-auroral regions may be defined by using either
        planetographic or magnetic coordinates if the magnetic dipole is
        closely aligned with the spin axis of a magnetized body. Ground
        magnetometers located at sub-auroral latitudes on the Earth
        measure a mixture of activity driven by auroral zone currents
        and the ring current.
    :cvar EARTH_NEAR_SURFACE_THERMOSPHERE: The layer of the atmosphere
        that extends from the Mesosphere to 640+ km, temperature
        increasing with height.
    :cvar EARTH_NEAR_SURFACE_TROPOSPHERE: The lowest layer of the
        atmosphere which begins at the surface and extends to between 7
        km (4.4 mi) at the poles and 17 km (10.6 mi) at the equator,
        with some variation due to weather factors.
    :cvar EARTH_SURFACE: The outermost area of a solid object.
    :cvar HELIOSPHERE: The solar atmosphere extending roughly from the
        outer corona to the edge of the solar plasma at the heliopause
        separating primarily solar plasma from interstellar plasma.
    :cvar HELIOSPHERE_HELIOSHEATH: The region extending radially outward
        from the heliospheric termination shock and in which the
        decelerated solar wind plasma is still significant.
    :cvar HELIOSPHERE_INNER: The region of the heliosphere extending
        radially outward from the solar coronal base to just inside 1
        AU.
    :cvar HELIOSPHERE_NEAR_EARTH: The heliospheric region near the Earth
        which extends to and includes the area near the L1 and L2
        Lagrange point.
    :cvar HELIOSPHERE_OUTER: The region of the heliosphere extending
        radially outward from just outside 1 AU to the heliospheric
        termination shock.
    :cvar HELIOSPHERE_REMOTE1_AU: A roughly toroidal region that
        includes the orbit of the Earth, but exclusive of the region
        near the Earth.
    :cvar INTERSTELLAR: The region between stars outside of any stellar
        heliopause.
    :cvar JUPITER: The fifth planet from the Sun in our solar system.
    :cvar JUPITER_CALLISTO: A second largest moon of Jupiter and the
        third largest moon in the solar system.
    :cvar JUPITER_EUROPA: The sixth closest round moon of Jupiter.
    :cvar JUPITER_GANYMEDE: The biggest moon of Jupiter and in the solar
        system.
    :cvar JUPITER_IO: The innermost of the four round moons of the
        planet Jupiter.
    :cvar JUPITER_MAGNETOSPHERE: The region of space above the
        atmosphere or surface of the planet and bounded by the
        magnetopause that is under the direct influence of the magnetic
        field of a planetary body.
    :cvar JUPITER_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar JUPITER_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar JUPITER_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar JUPITER_MAGNETOSPHERE_POLAR: The region near the pole of a
        body. For a magnetosphere the polar region is the area where
        magnetic field lines are open and includes the auroral zone.
    :cvar JUPITER_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar JUPITER_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar MARS: The fourth planet from the Sun in our solar system.
    :cvar MARS_DEIMOS: The smaller and outermost of the two natural
        satellites of Mars.
    :cvar MARS_MAGNETOSPHERE: The region of space above the atmosphere
        or surface of the planet and bounded by the magnetopause that is
        under the direct influence of the magnetic field of a planetary
        body.
    :cvar MARS_MAGNETOSPHERE_MAGNETOTAIL: The region of space within the
        magnetosphere of a magnetized planetary body where the nightside
        magnetic field is stretched out in the anti-stellar direction by
        stellar wind interaction into a windsock-like shape. For Earth,
        solar wind-magnetosphere interaction produces a magnetotail that
        extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar MARS_MAGNETOSPHERE_MAIN: The region of the magnetosphere where
        the magnetic field lines are closed, but does not include the
        gaseous region gravitationally bound to the body.
    :cvar MARS_MAGNETOSPHERE_PLASMASPHERE: A region of the magnetosphere
        consisting of low energy (cool) plasma. It is located above the
        ionosphere. The outer boundary of the plasmasphere is known as
        the plasmapause, which is defined by an order of magnitude drop
        in plasma density.
    :cvar MARS_MAGNETOSPHERE_POLAR: The region near the pole of a body.
        For a magnetosphere the polar region is the area where magnetic
        field lines are open and includes the auroral zone.
    :cvar MARS_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar MARS_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar MARS_PHOBOS: The larger and inner most moon of Mars.
    :cvar MERCURY: The first planet from the Sun in our solar system.
    :cvar MERCURY_MAGNETOSPHERE: The region of space above the
        atmosphere or surface of the planet and bounded by the
        magnetopause that is under the direct influence of the magnetic
        field of a planetary body.
    :cvar MERCURY_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar MERCURY_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar MERCURY_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar MERCURY_MAGNETOSPHERE_POLAR: The region near the pole of a
        body. For a magnetosphere the polar region is the area where
        magnetic field lines are open and includes the auroral zone.
    :cvar MERCURY_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar MERCURY_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar NEPTUNE: The seventh planet from the Sun in our solar system.
    :cvar NEPTUNE_MAGNETOSPHERE: The region of space above the
        atmosphere or surface of the planet and bounded by the
        magnetopause that is under the direct influence of the magnetic
        field of a planetary body.
    :cvar NEPTUNE_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar NEPTUNE_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar NEPTUNE_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar NEPTUNE_MAGNETOSPHERE_POLAR: The region near the pole of a
        body. For a magnetosphere the polar region is the area where
        magnetic field lines are open and includes the auroral zone.
    :cvar NEPTUNE_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar NEPTUNE_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar NEPTUNE_PROTEUS: The second largest moon of Neptune.
    :cvar NEPTUNE_TRITON: The largest moon of Neptune.
    :cvar PLUTO: The ninth planet from the Sun in our solar system.
    :cvar SATURN: The sixth planet from the Sun in our solar system.
    :cvar SATURN_DIONE: The fourth largest moon of Saturn.
    :cvar SATURN_ENCELADUS: The sixth largest moon of Saturn. It is
        currently endogenously active. The smallest known body in the
        Solar System that is geologically active today.
    :cvar SATURN_IAPETUS: The third largest moon of Saturn and the
        eleventh largest in the Solar System.
    :cvar SATURN_MAGNETOSPHERE: The region of space above the atmosphere
        or surface of the planet and bounded by the magnetopause that is
        under the direct influence of the magnetic field of a planetary
        body.
    :cvar SATURN_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar SATURN_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar SATURN_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar SATURN_MAGNETOSPHERE_POLAR: The region near the pole of a
        body. For a magnetosphere the polar region is the area where
        magnetic field lines are open and includes the auroral zone.
    :cvar SATURN_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar SATURN_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar SATURN_MIMAS: The smallest and least massive of the round
        moons of Saturn.
    :cvar SATURN_RHEA: The second largest moon of Saturn and the ninth
        largest moon in the Solar System.
    :cvar SATURN_TETHYS: The fifth largest moon of Saturn and the
        sixteenth largest moon in the Solar System. The orbit Tethys is
        the third closest to Saturn of the major Cronian moons.
    :cvar SATURN_TITAN: The largest moon of Saturn and the second
        largest moon in the Solar System.
    :cvar SUN: The star upon which our solar system is centered.
    :cvar SUN_CHROMOSPHERE: The region of the solar (or stellar)
        atmosphere above the temperature minimum and below the
        Transition Region. The solar chromosphere is approximately 400
        km to 2100 km above the photosphere, and characterized by
        temperatures that range from 4500 K to 28000 K.
    :cvar SUN_CORONA: The outermost atmospheric region of the Sun or a
        star, characterized by ionization temperatures above 10^5 K. The
        solar corona starts at about 2100 km above the photosphere.
        There is no generally defined upper limit.
    :cvar SUN_INTERIOR: The region inside the body which is not visible
        from outside the body.
    :cvar SUN_PHOTOSPHERE: The atmospheric layer of the Sun or a star
        from which continuum radiation, especially optical, is emitted
        to space. For the Sun, the photosphere is about 500 km thick.
    :cvar SUN_TRANSITION_REGION: A very narrow (&lt;100 km) layer
        between the chromosphere and the corona where the temperature
        rises abruptly from about 8000 to about 500,000 K.
    :cvar URANUS: The eighth planet from the Sun in our solar system.
    :cvar URANUS_ARIEL: The fourth largest moon of Uranus.
    :cvar URANUS_MAGNETOSPHERE: The region of space above the atmosphere
        or surface of the planet and bounded by the magnetopause that is
        under the direct influence of the magnetic field of a planetary
        body.
    :cvar URANUS_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar URANUS_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar URANUS_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar URANUS_MAGNETOSPHERE_POLAR: The region near the pole of a
        body. For a magnetosphere the polar region is the area where
        magnetic field lines are open and includes the auroral zone.
    :cvar URANUS_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar URANUS_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    :cvar URANUS_MIRANDA: The smallest and innermost round moon of
        Uranus.
    :cvar URANUS_OBERON: The second largest and second most massive moon
        of Uranus, and the ninth most massive moon in the Solar System.
    :cvar URANUS_PUCK: The largest inner spherical moon of Uranus.
    :cvar URANUS_TITANIA: The largest moon of Uranus and the eighth
        largest moon in the Solar System.
    :cvar URANUS_UMBRIEL: The third largest and fourth most massive moon
        of Uranus.
    :cvar VENUS: The second planet from the Sun in our solar system.
    :cvar VENUS_MAGNETOSPHERE: The region of space above the atmosphere
        or surface of the planet and bounded by the magnetopause that is
        under the direct influence of the magnetic field of a planetary
        body.
    :cvar VENUS_MAGNETOSPHERE_MAGNETOTAIL: The region of space within
        the magnetosphere of a magnetized planetary body where the
        nightside magnetic field is stretched out in the anti-stellar
        direction by stellar wind interaction into a windsock-like
        shape. For Earth, solar wind-magnetosphere interaction produces
        a magnetotail that extends tailward from a distance of about 10
        R&lt;sub&gt;E&lt;/sub&gt; on the nightside to downstream
        distances beyond 1000 R&lt;sub&gt;E&lt;/sub&gt;.
    :cvar VENUS_MAGNETOSPHERE_MAIN: The region of the magnetosphere
        where the magnetic field lines are closed, but does not include
        the gaseous region gravitationally bound to the body.
    :cvar VENUS_MAGNETOSPHERE_PLASMASPHERE: A region of the
        magnetosphere consisting of low energy (cool) plasma. It is
        located above the ionosphere. The outer boundary of the
        plasmasphere is known as the plasmapause, which is defined by an
        order of magnitude drop in plasma density.
    :cvar VENUS_MAGNETOSPHERE_POLAR: The region near the pole of a body.
        For a magnetosphere the polar region is the area where magnetic
        field lines are open and includes the auroral zone.
    :cvar VENUS_MAGNETOSPHERE_RADIATION_BELT: The region within a
        magnetosphere where high-energy particles could potentially be
        trapped in a magnetic field.
    :cvar VENUS_MAGNETOSPHERE_RING_CURRENT: One of the major current
        systems confined within planetary magnetospheres. The ring
        current circles in the magnetic equatorial plane of
        magnetospheres. It is generated by the longitudinal drift of
        energetic charged particles trapped on inner, dipole-like
        magnetospheric field lines. At the Earth, the ring current is
        carried by 10 keV to 200 keV charged particles typically located
        at L-shells between 3 and 6. The ring current is also the
        primary driver of the Sym H and Dst Indices of magnetic storm
        activity at the Earth.
    """

    ASTEROID = "Asteroid"
    COMET = "Comet"
    COMET_1_PHALLEY = "Comet.1PHalley"
    COMET_26_PGRIGG_SKJELLERUP = "Comet.26PGriggSkjellerup"
    COMET_67_PCHURYUMOV_GERASIMENKO = "Comet.67PChuryumovGerasimenko"
    EARTH = "Earth"
    EARTH_MAGNETOSHEATH = "Earth.Magnetosheath"
    EARTH_MAGNETOSPHERE = "Earth.Magnetosphere"
    EARTH_MAGNETOSPHERE_MAGNETOTAIL = "Earth.Magnetosphere.Magnetotail"
    EARTH_MAGNETOSPHERE_MAIN = "Earth.Magnetosphere.Main"
    EARTH_MAGNETOSPHERE_PLASMASPHERE = "Earth.Magnetosphere.Plasmasphere"
    EARTH_MAGNETOSPHERE_POLAR = "Earth.Magnetosphere.Polar"
    EARTH_MAGNETOSPHERE_RADIATION_BELT = "Earth.Magnetosphere.RadiationBelt"
    EARTH_MAGNETOSPHERE_RING_CURRENT = "Earth.Magnetosphere.RingCurrent"
    EARTH_MOON = "Earth.Moon"
    EARTH_NEAR_SURFACE = "Earth.NearSurface"
    EARTH_NEAR_SURFACE_ATMOSPHERE = "Earth.NearSurface.Atmosphere"
    EARTH_NEAR_SURFACE_AURORAL_REGION = "Earth.NearSurface.AuroralRegion"
    EARTH_NEAR_SURFACE_EQUATORIAL_REGION = "Earth.NearSurface.EquatorialRegion"
    EARTH_NEAR_SURFACE_IONOSPHERE = "Earth.NearSurface.Ionosphere"
    EARTH_NEAR_SURFACE_IONOSPHERE_DREGION = (
        "Earth.NearSurface.Ionosphere.DRegion"
    )
    EARTH_NEAR_SURFACE_IONOSPHERE_EREGION = (
        "Earth.NearSurface.Ionosphere.ERegion"
    )
    EARTH_NEAR_SURFACE_IONOSPHERE_FREGION = (
        "Earth.NearSurface.Ionosphere.FRegion"
    )
    EARTH_NEAR_SURFACE_IONOSPHERE_TOPSIDE = (
        "Earth.NearSurface.Ionosphere.Topside"
    )
    EARTH_NEAR_SURFACE_MESOSPHERE = "Earth.NearSurface.Mesosphere"
    EARTH_NEAR_SURFACE_MID_LATITUDE_REGION = (
        "Earth.NearSurface.MidLatitudeRegion"
    )
    EARTH_NEAR_SURFACE_PLASMASPHERE = "Earth.NearSurface.Plasmasphere"
    EARTH_NEAR_SURFACE_POLAR_CAP = "Earth.NearSurface.PolarCap"
    EARTH_NEAR_SURFACE_SOUTH_ATLANTIC_ANOMALY_REGION = (
        "Earth.NearSurface.SouthAtlanticAnomalyRegion"
    )
    EARTH_NEAR_SURFACE_STRATOSPHERE = "Earth.NearSurface.Stratosphere"
    EARTH_NEAR_SURFACE_SUB_AURORAL_REGION = (
        "Earth.NearSurface.SubAuroralRegion"
    )
    EARTH_NEAR_SURFACE_THERMOSPHERE = "Earth.NearSurface.Thermosphere"
    EARTH_NEAR_SURFACE_TROPOSPHERE = "Earth.NearSurface.Troposphere"
    EARTH_SURFACE = "Earth.Surface"
    HELIOSPHERE = "Heliosphere"
    HELIOSPHERE_HELIOSHEATH = "Heliosphere.Heliosheath"
    HELIOSPHERE_INNER = "Heliosphere.Inner"
    HELIOSPHERE_NEAR_EARTH = "Heliosphere.NearEarth"
    HELIOSPHERE_OUTER = "Heliosphere.Outer"
    HELIOSPHERE_REMOTE1_AU = "Heliosphere.Remote1AU"
    INTERSTELLAR = "Interstellar"
    JUPITER = "Jupiter"
    JUPITER_CALLISTO = "Jupiter.Callisto"
    JUPITER_EUROPA = "Jupiter.Europa"
    JUPITER_GANYMEDE = "Jupiter.Ganymede"
    JUPITER_IO = "Jupiter.Io"
    JUPITER_MAGNETOSPHERE = "Jupiter.Magnetosphere"
    JUPITER_MAGNETOSPHERE_MAGNETOTAIL = "Jupiter.Magnetosphere.Magnetotail"
    JUPITER_MAGNETOSPHERE_MAIN = "Jupiter.Magnetosphere.Main"
    JUPITER_MAGNETOSPHERE_PLASMASPHERE = "Jupiter.Magnetosphere.Plasmasphere"
    JUPITER_MAGNETOSPHERE_POLAR = "Jupiter.Magnetosphere.Polar"
    JUPITER_MAGNETOSPHERE_RADIATION_BELT = (
        "Jupiter.Magnetosphere.RadiationBelt"
    )
    JUPITER_MAGNETOSPHERE_RING_CURRENT = "Jupiter.Magnetosphere.RingCurrent"
    MARS = "Mars"
    MARS_DEIMOS = "Mars.Deimos"
    MARS_MAGNETOSPHERE = "Mars.Magnetosphere"
    MARS_MAGNETOSPHERE_MAGNETOTAIL = "Mars.Magnetosphere.Magnetotail"
    MARS_MAGNETOSPHERE_MAIN = "Mars.Magnetosphere.Main"
    MARS_MAGNETOSPHERE_PLASMASPHERE = "Mars.Magnetosphere.Plasmasphere"
    MARS_MAGNETOSPHERE_POLAR = "Mars.Magnetosphere.Polar"
    MARS_MAGNETOSPHERE_RADIATION_BELT = "Mars.Magnetosphere.RadiationBelt"
    MARS_MAGNETOSPHERE_RING_CURRENT = "Mars.Magnetosphere.RingCurrent"
    MARS_PHOBOS = "Mars.Phobos"
    MERCURY = "Mercury"
    MERCURY_MAGNETOSPHERE = "Mercury.Magnetosphere"
    MERCURY_MAGNETOSPHERE_MAGNETOTAIL = "Mercury.Magnetosphere.Magnetotail"
    MERCURY_MAGNETOSPHERE_MAIN = "Mercury.Magnetosphere.Main"
    MERCURY_MAGNETOSPHERE_PLASMASPHERE = "Mercury.Magnetosphere.Plasmasphere"
    MERCURY_MAGNETOSPHERE_POLAR = "Mercury.Magnetosphere.Polar"
    MERCURY_MAGNETOSPHERE_RADIATION_BELT = (
        "Mercury.Magnetosphere.RadiationBelt"
    )
    MERCURY_MAGNETOSPHERE_RING_CURRENT = "Mercury.Magnetosphere.RingCurrent"
    NEPTUNE = "Neptune"
    NEPTUNE_MAGNETOSPHERE = "Neptune.Magnetosphere"
    NEPTUNE_MAGNETOSPHERE_MAGNETOTAIL = "Neptune.Magnetosphere.Magnetotail"
    NEPTUNE_MAGNETOSPHERE_MAIN = "Neptune.Magnetosphere.Main"
    NEPTUNE_MAGNETOSPHERE_PLASMASPHERE = "Neptune.Magnetosphere.Plasmasphere"
    NEPTUNE_MAGNETOSPHERE_POLAR = "Neptune.Magnetosphere.Polar"
    NEPTUNE_MAGNETOSPHERE_RADIATION_BELT = (
        "Neptune.Magnetosphere.RadiationBelt"
    )
    NEPTUNE_MAGNETOSPHERE_RING_CURRENT = "Neptune.Magnetosphere.RingCurrent"
    NEPTUNE_PROTEUS = "Neptune.Proteus"
    NEPTUNE_TRITON = "Neptune.Triton"
    PLUTO = "Pluto"
    SATURN = "Saturn"
    SATURN_DIONE = "Saturn.Dione"
    SATURN_ENCELADUS = "Saturn.Enceladus"
    SATURN_IAPETUS = "Saturn.Iapetus"
    SATURN_MAGNETOSPHERE = "Saturn.Magnetosphere"
    SATURN_MAGNETOSPHERE_MAGNETOTAIL = "Saturn.Magnetosphere.Magnetotail"
    SATURN_MAGNETOSPHERE_MAIN = "Saturn.Magnetosphere.Main"
    SATURN_MAGNETOSPHERE_PLASMASPHERE = "Saturn.Magnetosphere.Plasmasphere"
    SATURN_MAGNETOSPHERE_POLAR = "Saturn.Magnetosphere.Polar"
    SATURN_MAGNETOSPHERE_RADIATION_BELT = "Saturn.Magnetosphere.RadiationBelt"
    SATURN_MAGNETOSPHERE_RING_CURRENT = "Saturn.Magnetosphere.RingCurrent"
    SATURN_MIMAS = "Saturn.Mimas"
    SATURN_RHEA = "Saturn.Rhea"
    SATURN_TETHYS = "Saturn.Tethys"
    SATURN_TITAN = "Saturn.Titan"
    SUN = "Sun"
    SUN_CHROMOSPHERE = "Sun.Chromosphere"
    SUN_CORONA = "Sun.Corona"
    SUN_INTERIOR = "Sun.Interior"
    SUN_PHOTOSPHERE = "Sun.Photosphere"
    SUN_TRANSITION_REGION = "Sun.TransitionRegion"
    URANUS = "Uranus"
    URANUS_ARIEL = "Uranus.Ariel"
    URANUS_MAGNETOSPHERE = "Uranus.Magnetosphere"
    URANUS_MAGNETOSPHERE_MAGNETOTAIL = "Uranus.Magnetosphere.Magnetotail"
    URANUS_MAGNETOSPHERE_MAIN = "Uranus.Magnetosphere.Main"
    URANUS_MAGNETOSPHERE_PLASMASPHERE = "Uranus.Magnetosphere.Plasmasphere"
    URANUS_MAGNETOSPHERE_POLAR = "Uranus.Magnetosphere.Polar"
    URANUS_MAGNETOSPHERE_RADIATION_BELT = "Uranus.Magnetosphere.RadiationBelt"
    URANUS_MAGNETOSPHERE_RING_CURRENT = "Uranus.Magnetosphere.RingCurrent"
    URANUS_MIRANDA = "Uranus.Miranda"
    URANUS_OBERON = "Uranus.Oberon"
    URANUS_PUCK = "Uranus.Puck"
    URANUS_TITANIA = "Uranus.Titania"
    URANUS_UMBRIEL = "Uranus.Umbriel"
    VENUS = "Venus"
    VENUS_MAGNETOSPHERE = "Venus.Magnetosphere"
    VENUS_MAGNETOSPHERE_MAGNETOTAIL = "Venus.Magnetosphere.Magnetotail"
    VENUS_MAGNETOSPHERE_MAIN = "Venus.Magnetosphere.Main"
    VENUS_MAGNETOSPHERE_PLASMASPHERE = "Venus.Magnetosphere.Plasmasphere"
    VENUS_MAGNETOSPHERE_POLAR = "Venus.Magnetosphere.Polar"
    VENUS_MAGNETOSPHERE_RADIATION_BELT = "Venus.Magnetosphere.RadiationBelt"
    VENUS_MAGNETOSPHERE_RING_CURRENT = "Venus.Magnetosphere.RingCurrent"


class RenderingAxis(Enum):
    """
    Identifiers for the reference component of a plot or rendering of data.

    :cvar COLOR_BAR: A spectrum or set of colors used to represent data
        values.
    :cvar HORIZONTAL: Parallel to or in the plane of the horizon or a
        base line.
    :cvar VERTICAL: Perpendicular to the plane of the horizon or a base
        line.
    """

    COLOR_BAR = "ColorBar"
    HORIZONTAL = "Horizontal"
    VERTICAL = "Vertical"


@dataclass
class RevisionEvent:
    """
    A specific change that improves or upgrades.
    """

    release_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReleaseDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )


class Role(Enum):
    """
    Identifiers for the assigned or assumed function or position of an individual.

    :cvar AUTHOR: The composer of a literary work. This can include
        presentations, articles, books, white papers or any similar
        published work.
    :cvar ARCHIVE_SPECIALIST: An individual who is an expert on a
        collection of resources and may also be knowledgeable of the
        phenomenon and related physics represented by the resources.
        This includes librarians, curators, archive scientists and other
        experts.
    :cvar CO_INVESTIGATOR: An individual who is a scientific peer and
        major participant in an investigation.
    :cvar CO_PI: An individual who is peer of a principal investigator
        and is an administrative and scientific lead for an
        investigation.
    :cvar CONTRIBUTOR: An entity responsible for making contributions to
        the content of the resource.
    :cvar DATA_PRODUCER: An individual who generated the resource and is
        familiar with its provenance.
    :cvar DEPUTY_PI: An individual who is an administrative or
        scientific leader for an investigation operating under the
        supervision of a Principal Investigator.
    :cvar DEVELOPER: The developer of a system to imitate a situation or
        process.
    :cvar FORMER_PI: An individual who had served as the administrative
        and scientific lead for an investigation, but no longer assumes
        that role.
    :cvar GENERAL_CONTACT: An individual who can provide information on
        a range of subjects or who can direct you to a domain expert.
    :cvar HOST_CONTACT: An individual who can provide specific
        information with regard the hosting of a resource or supporting
        software.
    :cvar INSTRUMENT_LEAD: An individual who is the designated leader of
        an instrument or instrument package.
    :cvar INSTRUMENT_SCIENTIST: A scientist associated with a science
        instrument team with special familiarity and expertise on
        specific aspects of the design and operations of the instrument
        and the responsibility of ensuring the measurement capabilities
        of the instrument.
    :cvar METADATA_CONTACT: An individual who can affect a change in the
        metadata describing a resource.
    :cvar MISSION_MANAGER: A Mission Manager is a role name used by the
        ESA. The Mission Manager corresponds to the Project Manager role
        used by NASA but the Mission Manager role only begins after the
        launch of the mission.
    :cvar MISSION_PRINCIPAL_INVESTIGATOR: An individual who is the
        administrative and scientific lead for a mission.
    :cvar PRINCIPAL_INVESTIGATOR: An individual who is the
        administrative and scientific lead for an investigation.
    :cvar PROGRAM_MANAGER: An individual whose major task entails
        direction of program team members such that the full
        organization achieves the objectives and goals of a program. The
        Program Manager is expected to provide clear guidance and
        resolve conflicts and issues while maintaining focus on
        achieving program success.
    :cvar PROGRAM_SCIENTIST: A program scientist is someone who performs
        a range of scientific program planning duties, takes
        responsibility for the science content of flight mission
        programs or projects. A program scientist develops, reviews, and
        provides recommendations for proposed program requirements,
        expected results, budgetary estimates and also establishes
        methods and procedures to reduce program costs, provides expert
        advice to management on strategic planning and program
        development, develops and manages research program, and presents
        issues and proposes solutions to senior management.
    :cvar PROJECT_ENGINEER: An engineer tasked with the full suite of
        responsibilities as a project undergoes the transition from the
        requirements derivation and preliminary design phases to
        controlled hardware development, assembly and environmental
        testing. The Project Engineer manages a team while developing
        the cadence of hardware manufacturing and assembly until
        instrument deployment and through the end of the mission.
    :cvar PROJECT_MANAGER: An individual whose major task entails
        direction of project team members such that the full
        organization achieves the objectives and goals of the mission.
        The Project Manager is expected to provide clear guidance and
        resolve conflicts and issues while maintaining focus on
        achieving mission success.
    :cvar PROJECT_SCIENTIST: An individual who is an expert in the
        phenomenon and related physics explored by the project. A
        project scientist may also have a managerial role within the
        project.
    :cvar PUBLISHER: An individual, organization, institution or
        government department responsible for the production and
        dissemination of a document.
    :cvar SCIENTIST: An individual who is an expert in the phenomenon
        and related physics represented by the resource.
    :cvar TEAM_LEADER: An individual who is the designated leader of an
        investigation.
    :cvar TEAM_MEMBER: An individual who is a major participant in an
        investigation.
    :cvar TECHNICAL_CONTACT: An individual who can provide specific
        information with regard to the resource or supporting software.
    :cvar USER: An individual who utilizes a resource or service.
    """

    AUTHOR = "Author"
    ARCHIVE_SPECIALIST = "ArchiveSpecialist"
    CO_INVESTIGATOR = "CoInvestigator"
    CO_PI = "CoPI"
    CONTRIBUTOR = "Contributor"
    DATA_PRODUCER = "DataProducer"
    DEPUTY_PI = "DeputyPI"
    DEVELOPER = "Developer"
    FORMER_PI = "FormerPI"
    GENERAL_CONTACT = "GeneralContact"
    HOST_CONTACT = "HostContact"
    INSTRUMENT_LEAD = "InstrumentLead"
    INSTRUMENT_SCIENTIST = "InstrumentScientist"
    METADATA_CONTACT = "MetadataContact"
    MISSION_MANAGER = "MissionManager"
    MISSION_PRINCIPAL_INVESTIGATOR = "MissionPrincipalInvestigator"
    PRINCIPAL_INVESTIGATOR = "PrincipalInvestigator"
    PROGRAM_MANAGER = "ProgramManager"
    PROGRAM_SCIENTIST = "ProgramScientist"
    PROJECT_ENGINEER = "ProjectEngineer"
    PROJECT_MANAGER = "ProjectManager"
    PROJECT_SCIENTIST = "ProjectScientist"
    PUBLISHER = "Publisher"
    SCIENTIST = "Scientist"
    TEAM_LEADER = "TeamLeader"
    TEAM_MEMBER = "TeamMember"
    TECHNICAL_CONTACT = "TechnicalContact"
    USER = "User"


class SavedQuantity(Enum):
    """
    Quantities that are saved during a given diagnosis.

    :cvar VALUE_2_DCUTS: A set of 2-D arrays that contain the values of
        physical parameters, i.e., magnetic field vectors, particle
        densities, temperatures, etc., at the grid points located in a
        planar slice of a model volume.
    :cvar VALUE_3_DCUBES: A set of 3-D arrays that contain the values of
        physical parameters, i.e., magnetic field vectors, particle
        densities, temperatures, etc., at grid points in a model volume.
    :cvar ACELECTRIC_FIELD: Alternating electric field component of a
        wave.
    :cvar ACMAGNETIC_FIELD: Alternating magnetic field component of a
        wave.
    :cvar ABSORPTION: Decrease of radiant energy (relative to the
        background continuum spectrum).
    :cvar ADIABATIC_INVARIANT: A property of a physical system usually
        related to periodic phenomena that remains constant under slowly
        varying conditions.
    :cvar ADIABATIC_INVARIANT_MAGNETIC_MOMENT: A constant of motion
        related to the gyromotion of a particle in a magnetic field that
        is either static or slowly varying with respect to the
        gyroperiod. The magnetic moment is usually denoted by using the
        lower-case Greek letter for mu, &amp;#956;, and can be
        calculated by using &amp;#956;=m(u^2/2B) where m is the particle
        mass, u is the velocity of the particle perpendicular to the
        constant or average magnetic field direction, and B is the
        magnitude of the magnetic field strength.
    :cvar ADIABATIC_INVARIANT_BOUNCE_MOTION: The second adiabatic
        invariant is associated with periodic bounce motion of charged
        particles trapped between two magnetic mirrors on a magnetic
        field line. The second invariant, termed J, is defined by using
        the integral J=m &amp;int; v||*ds where m is the mass of the
        charged particle, v|| is the particle velocity along the field
        line, and ds represents elemental arc lengths along the field
        line. The second adiabatic invariant is conserved as long as
        changes in the background magnetic field occur at time scales
        much longer than the bounce time of the charged particles.
    :cvar ADIABATIC_INVARIANT_DRIFT_MOTION: The third invariant for
        charged particle motion in a dipolar magnetic field is
        associated with drift of its guiding center in the equatorial
        plane. The conserved quantity, J&lt;sub&gt;2&lt;/sub&gt;, is
        equal to q&amp;phi; where q is the particle charge and &amp;phi;
        is the magnetic flux enclosed within the particle drift path.
    :cvar AKASOFU_EPSILON: A measure of the magnetopause energy flux and
        an indicator of the solar wind power available for subsequent
        magnetospheric energization. Defined as: V*B^2*l^2sin(theta/2)^4
        where B is the IMF, l is an empirical scaling parameter equal to
        7 R&lt;sub&gt;E&lt;/sub&gt;, and theta=tan(By/Bz)^-1 the IMF
        clock angle.
    :cvar ALBEDO: The ratio of reflected radiation from the surface to
        incident radiation upon it.
    :cvar ALFVEN_MACH_NUMBER: The ratio of the bulk flow speed to the
        Alfven speed.
    :cvar ALFVEN_VELOCITY: Phase velocity of the Alfven wave. In SI
        units it is the velocity of the magnetic field divided by the
        square root of the mass density times the permeability of free
        space (&amp;mu;&lt;sub&gt;0&lt;/sub&gt;).
    :cvar ARRIVAL_DIRECTION: An angular measure of the direction from
        which an energetic particle or photon was incident on a
        detector. The angles may be measured in any coordinate system.
    :cvar ATOMIC_NUMBER_DETECTED: The number of protons in the nucleus
        of an atom as determined by a detector.
    :cvar AVERAGE_CHARGE_STATE: A measure of the composite deficit
        (positive) or excess (negative) of electrons with respect to
        protons.
    :cvar CHARGE_FLUX: The number of ionized particles passing through a
        unit area per unit time, for instance as measured by a Faraday
        cup.
    :cvar CHARGE_STATE: Charge of a fully or partially stripped ion, in
        units of the charge of a proton. Charge state of a bare proton
        is equal to one.
    :cvar COUNT_RATE: The number of events per unit time.
    :cvar COUNTS: The number of detection events occurring in a detector
        over the detector accumulation time.
    :cvar CURRENT: It is the scalar quantity giving the net charge
        (summed over charged particle species) per unit time flowing
        across a given surface.
    :cvar CURRENT_DENSITY: It is the vector quantity giving the net
        charge (summed over charged particle species) per unit cross-
        sectional area per unit time flowing through a given point.
        Measurements of current density are often provided in terms of
        the magnetic perturbations (superposed upon a background
        magnetic field, if present) associated with the current density.
    :cvar DOPPLER_FREQUENCY: Change in the frequency of a propagating
        wave due to motion of the source, the observer, the reflector,
        or the propagation medium.
    :cvar DYNAMIC_PRESSURE: Dynamic pressure is a measure of the kinetic
        energy per unit volume of a fluid. For instance, the solar wind
        dynamic pressure or ram pressure for a purely proton plasma is
        equal to m&lt;sub&gt;p&lt;/sub&gt; n V&lt;sup&gt;2&lt;/sup&gt;
        where m&lt;sub&gt;p&lt;/sub&gt; is the proton mass, n is the
        proton number density, and V is the solar wind speed.
    :cvar ELECTRIC: The physical attribute that exerts an electrical
        force.
    :cvar ELECTROMAGNETIC: Electric and magnetic field variations in
        time and space that propagate through a medium or a vacuum. The
        wave propagation direction, electric field vector, and magnetic
        field vector form an orthogonal triad. Waves in this category
        are detected by having their field quantities measured.
    :cvar EMISSIVITY: The energy emitted spontaneously per unit
        bandwidth (typically frequency) per unit time per unit mass of
        source. Emissivity is usually integrated over all
        directions/solid angles.
    :cvar ENERGY: The capacity for doing work as measured by the
        capability of doing work (potential energy) or the conversion of
        this capability to motion (kinetic energy).
    :cvar ENERGY_DENSITY: The amount of energy per unit volume.
    :cvar ENERGY_FLUX: The amount of energy passing through a unit area
        in a unit time.
    :cvar ENERGY_PER_CHARGE: The kinetic energy, E, per unit net charge,
        q, that is E/q, for an electron or an ionized atom, molecule, or
        dust particle.
    :cvar ENTROPY: A function of thermodynamic quantity, such as
        temperature, pressure, or composition, that is a measure of the
        energy that is not available for work during a thermodynamic
        process. It is often interpreted as the degree of disorder or
        randomness in the system.
    :cvar EQUIVALENT_WIDTH: The spectral width of a total absorption
        line having the amount of absorbed radiant energy being
        equivalent to that in an observed absorption line.
    :cvar FLOW_SPEED: The rate at which particles or energy is passing
        through a unit area in a unit time.
    :cvar FLOW_VELOCITY: The volume of matter passing through a unit
        area perpendicular to the direction of flow in a unit of time.
    :cvar FLUENCE: The time integral of a flux. A fluence is a not a
        measurement of flux per unit time.
    :cvar FREQUENCY: The number of occurrences of a repeating event per
        unit time.
    :cvar FREQUENCY_TO_GYROFREQUENCY_RATIO: The ratio of the
        characteristic frequency of a medium to gyrofrequency of a
        particle.
    :cvar GEOMETRIC_FACTOR: A measure of the gathering power of a
        particle detector. The geometric factor can be used to correct
        particle measurements by accounting for the fact that only a
        fraction of the source particles is able to gain entry through
        the aperture of a detector. For an isotopic source distribution,
        the geometric factor corresponds to the solid angle subtended by
        the aperture. In practice, determination of the geometric factor
        requires numerical modeling and depends on detector design and
        the characteristics of the source.
    :cvar GYROFREQUENCY: The number of gyrations around a magnetic
        guiding center (field line) a charged particle makes per unit
        time due to the Lorentz force.
    :cvar HEAT_FLUX: Flow of thermal energy through a gas or plasma
        typically computed as third moment of a distribution function.
    :cvar IMFCLOCK_ANGLE: The clockwise angle of the direction of
        interplanetary magnetic field (IMF) measured in the plane of the
        body pole perpendicular to the line between the body and the
        Sun.
    :cvar INTENSITY: The measurement of radiant or wave energy per unit
        detector area per unit bandwidth per unit solid angle per unit
        time.
    :cvar LSHELL: The L-shell is the magnetic equatorial radius (in
        units of planetary radii) of a dipole magnetic field line. For
        instance, if the L-shell value equals 6 say at Earth, the
        magnetic field lines cross the magnetic equator at six Earth
        radii. The L-shell concept can be applied generally to any
        magnetized planet or satellite with a dominant dipolar magnetic
        field moment.
    :cvar LINE_DEPTH: The measure of the amount of absorption below the
        continuum (depth) in a particular wavelength or frequency in an
        absorption spectrum.
    :cvar LINES: A set of 1-D arrays that contain the values of physical
        parameters, i.e., magnetic field vectors, particle densities,
        temperatures, etc., at the grid points along a line though a
        model volume. For instance, the points of the line may
        correspond to the trajectory of a spacecraft through model
        space.
    :cvar LOWER_HYBRID_FREQUENCY: Lower hybrid oscillations involve
        longitudinal motions of electrons and ions in a magnetized
        plasma. The propagation of lower hybrid waves must be close to
        perpendicular to the background magnetic field in so that
        electrons cannot move along field lines thus preventing wave
        growth. The lower hybrid frequency,
        &amp;phi;&lt;sub&gt;LH&lt;/sub&gt;, can be calculated by using
        &amp;phi;&lt;sub&gt;LH&lt;/sub&gt;=[(&amp;omega;&lt;sub&gt;ce&lt;/sub&gt;&amp;omega;&lt;sub&gt;ci&lt;/sub&gt;)&lt;sup&gt;-1&lt;/sup&gt;+&amp;phi;&lt;sub&gt;pi&lt;/sub&gt;&lt;sup&gt;-2&lt;/sup&gt;]&lt;sup&gt;-1/2&lt;/sup&gt;
        where &amp;omega;&lt;sub&gt;ce&lt;/sub&gt; and
        &amp;omega;&lt;sub&gt;ci&lt;/sub&gt; are the electron and ion
        cyclotron frequencies, respectively, and
        $phi;&lt;sub&gt;LH&lt;/sub&gt; is the ion plasma frequency.
    :cvar MAGNETIC: The physical attribute attributed to a magnet or its
        equivalent.
    :cvar MAGNETIC_FIELD: A region of space near a magnetized body where
        magnetic forces can be detected (as measured by methods such as
        Zeeman splitting, etc.).
    :cvar MAGNETOSONIC_MACH_NUMBER: The ratio of the velocity of fast
        mode waves to the Alfven velocity.
    :cvar MASS: The measure of inertia (mass) of individual objects
        (e.g., aerosols).
    :cvar MASS_DENSITY: The mass of particles per unit volume.
    :cvar MASS_NUMBER: The total number of protons and neutrons
        (together known as nucleons) in an atomic nucleus.
    :cvar MASS_PER_CHARGE: The mass, m, per unit net charge, q, that is
        m/q, for an electron or an ionized atom, molecule, or dust
        particle.
    :cvar MODE_AMPLITUDE: In helioseismology the magnitude of
        oscillation of waves of a particular geometry.
    :cvar NUMBER_DENSITY: The number of particles per unit volume.
    :cvar NUMBER_FLUX: The number of particles passing a unit area in
        unit time, possibly also per unit energy (or equivalent) and/or
        per unit look direction.
    :cvar OTHER: Not classified with more specific terms. The context of
        its usage may be described in related text.
    :cvar PARTICLE_RADIUS: The mean radius for a Gaussian distribution
        of particles with an axial ratio of 2 and a distribution width
        that varies as 0.5 radius. A value of zero means no cloud was
        detected.
    :cvar PARTICLE_RIGIDITY: The particle momentum per unit charge. The
        particle Rigidity, R, is equal to pc/Ze.
    :cvar PHASE_SPACE_DENSITY: The number of particles per unit volume
        in the six-dimensional space of position and velocity.
    :cvar PLASMA_BETA: The ratio of the plasma pressure (nkT) to the
        magnetic pressure (B^2/2&amp;mu;&lt;sub&gt;0&lt;/sub&gt;) in a
        single component plasma or the ratio of the plasma pressure sum
        over i of (n&lt;sub&gt;i&lt;/sub&gt;kT&lt;sub&gt;i&lt;/sub&gt;)
        for all species i to the magnetic pressure
        (B^2/2&amp;mu;&lt;sub&gt;0&lt;/sub&gt;) in a multi components
        plasma.
    :cvar PLASMA_FREQUENCY: A number density dependent characteristic
        frequency of a plasma.
    :cvar POLARIZATION: Direction of the electric vector of an
        electromagnetic wave. The wave can be linearly polarized in any
        direction perpendicular to the direction of travel, circularly
        polarized (clockwise or counterclockwise), unpolarized, or
        mixtures of the above.
    :cvar POTENTIAL: The work required per unit charge to move a charge
        from a reference point to a point at infinity (electric
        potential is defined to be zero). The electric potential of a
        spacecraft is often referred to as the spacecraft potential. The
        spacecraft potential is the electric potential of the spacecraft
        relative to the potential of the nearby plasma. The spacecraft
        potential is non-zero because the spacecraft charges to the
        level that the emitted photoelectron flux going to infinity is
        balanced by the plasma electron flux to the spacecraft.
    :cvar POYNTING_FLUX: Electromagnetic energy flux transported by a
        wave characterized as the rate of energy transport per unit area
        per steradian.
    :cvar PRESSURE: The force per unit area exerted by a particle
        distribution or field.
    :cvar PROPAGATION_TIME: Time difference between transmission and
        reception of a wave in an active wave experiment.
    :cvar SOLAR_UVFLUX: The amount of ultraviolet energy originating
        from the Sun passing through a unit area in a unit time.
    :cvar SONIC_MACH_NUMBER: The ratio of the bulk flow speed to the
        speed of sound in the medium.
    :cvar SOUND_SPEED: The speed at which sound travels through a
        medium.
    :cvar SPATIAL_SERIES: A set of 3-D arrays that contain the values of
        physical parameters, i.e., magnetic field vectors, particle
        densities, temperatures, etc., at grid points in a spacial
        volume.
    :cvar SPECTRA: A term that applies to any signal that can be
        measured or decomposed along a continuous variable such as the
        electromagnetic radiation which can be decomposed as a function
        of wavelength or frequency.
    :cvar STOKES_PARAMETERS: A set of four parameters (usually called
        I,Q, U and V) which describe the polarization state of an
        electromagnetic wave propagating through space.
    :cvar TEMPERATURE: A measure of the kinetic energy of random motion
        with respect to the average. Temperature is properly defined
        only for an equilibrium particle distribution (Maxwellian
        distribution).
    :cvar THERMAL_SPEED: For a Maxwellian distribution, the difference
        between the mean speed and the speed within 69% (one sigma) of
        all the members of the speed distribution occur.
    :cvar TIME_SERIES: A representation of data showing a set of
        observations taken at different points in time and charted as a
        time series.
    :cvar TOTAL_PRESSURE: In an MHD fluid it is the number density (N)
        times Boltzmann constant times the temperature in Kelvin.
    :cvar UPPER_HYBRID_FREQUENCY: Upper hybrid oscillations involve
        longitudinal motions of electrons perpendicular to the magnetic
        field. The upper hybrid frequency,
        &amp;phi;&lt;sub&gt;UH&lt;/sub&gt;, is governed by the
        relationship
        &amp;phi;&lt;sub&gt;UH&lt;/sub&gt;^2=&amp;phi;&lt;sub&gt;pe&lt;/sub&gt;^2+&amp;theta;&lt;sub&gt;ce&lt;/sub&gt;^2
        where &amp;phi;&lt;sub&gt;pe&lt;/sub&gt; is electron plasma
        frequency and &amp;theta;&lt;sub&gt;ce&lt;/sub&gt; is the
        electron cyclotron frequency.
    :cvar VCROSS_B: The cross product of the charge velocity (V) and the
        magnetic field (B). It is the electric field exerted on a point
        charge by a magnetic field.
    :cvar VELOCITY: Rate of change of position. Also used for the
        average velocity of a collection of particles, also referred to
        as bulk velocity.
    :cvar VOLUME_EMISSION_RATE: The volume emission rate, e(r,t,l), is
        the number of photons emitted per unit source volume per second
        (photons/m^3/s), as measured along the line of sight between the
        source point and the observer. The Volume Emission Rate is in
        general a function of the line-of-sight distance, r, time, t,
        and wavelength, l. The Volume Emission Rate is actually not a
        directly measurable quantity. However, the term has been
        commonly used in both data product descriptions and research
        publications.
    :cvar WAVELENGTH: The peak-to-peak distance over one wave period.
    """

    VALUE_2_DCUTS = "2DCuts"
    VALUE_3_DCUBES = "3DCubes"
    ACELECTRIC_FIELD = "ACElectricField"
    ACMAGNETIC_FIELD = "ACMagneticField"
    ABSORPTION = "Absorption"
    ADIABATIC_INVARIANT = "AdiabaticInvariant"
    ADIABATIC_INVARIANT_MAGNETIC_MOMENT = "AdiabaticInvariant.MagneticMoment"
    ADIABATIC_INVARIANT_BOUNCE_MOTION = "AdiabaticInvariant.BounceMotion"
    ADIABATIC_INVARIANT_DRIFT_MOTION = "AdiabaticInvariant.DriftMotion"
    AKASOFU_EPSILON = "AkasofuEpsilon"
    ALBEDO = "Albedo"
    ALFVEN_MACH_NUMBER = "AlfvenMachNumber"
    ALFVEN_VELOCITY = "AlfvenVelocity"
    ARRIVAL_DIRECTION = "ArrivalDirection"
    ATOMIC_NUMBER_DETECTED = "AtomicNumberDetected"
    AVERAGE_CHARGE_STATE = "AverageChargeState"
    CHARGE_FLUX = "ChargeFlux"
    CHARGE_STATE = "ChargeState"
    COUNT_RATE = "CountRate"
    COUNTS = "Counts"
    CURRENT = "Current"
    CURRENT_DENSITY = "CurrentDensity"
    DOPPLER_FREQUENCY = "DopplerFrequency"
    DYNAMIC_PRESSURE = "DynamicPressure"
    ELECTRIC = "Electric"
    ELECTROMAGNETIC = "Electromagnetic"
    EMISSIVITY = "Emissivity"
    ENERGY = "Energy"
    ENERGY_DENSITY = "EnergyDensity"
    ENERGY_FLUX = "EnergyFlux"
    ENERGY_PER_CHARGE = "EnergyPerCharge"
    ENTROPY = "Entropy"
    EQUIVALENT_WIDTH = "EquivalentWidth"
    FLOW_SPEED = "FlowSpeed"
    FLOW_VELOCITY = "FlowVelocity"
    FLUENCE = "Fluence"
    FREQUENCY = "Frequency"
    FREQUENCY_TO_GYROFREQUENCY_RATIO = "FrequencyToGyrofrequencyRatio"
    GEOMETRIC_FACTOR = "GeometricFactor"
    GYROFREQUENCY = "Gyrofrequency"
    HEAT_FLUX = "HeatFlux"
    IMFCLOCK_ANGLE = "IMFClockAngle"
    INTENSITY = "Intensity"
    LSHELL = "LShell"
    LINE_DEPTH = "LineDepth"
    LINES = "Lines"
    LOWER_HYBRID_FREQUENCY = "LowerHybridFrequency"
    MAGNETIC = "Magnetic"
    MAGNETIC_FIELD = "MagneticField"
    MAGNETOSONIC_MACH_NUMBER = "MagnetosonicMachNumber"
    MASS = "Mass"
    MASS_DENSITY = "MassDensity"
    MASS_NUMBER = "MassNumber"
    MASS_PER_CHARGE = "MassPerCharge"
    MODE_AMPLITUDE = "ModeAmplitude"
    NUMBER_DENSITY = "NumberDensity"
    NUMBER_FLUX = "NumberFlux"
    OTHER = "Other"
    PARTICLE_RADIUS = "ParticleRadius"
    PARTICLE_RIGIDITY = "ParticleRigidity"
    PHASE_SPACE_DENSITY = "PhaseSpaceDensity"
    PLASMA_BETA = "PlasmaBeta"
    PLASMA_FREQUENCY = "PlasmaFrequency"
    POLARIZATION = "Polarization"
    POTENTIAL = "Potential"
    POYNTING_FLUX = "PoyntingFlux"
    PRESSURE = "Pressure"
    PROPAGATION_TIME = "PropagationTime"
    SOLAR_UVFLUX = "SolarUVFlux"
    SONIC_MACH_NUMBER = "SonicMachNumber"
    SOUND_SPEED = "SoundSpeed"
    SPATIAL_SERIES = "SpatialSeries"
    SPECTRA = "Spectra"
    STOKES_PARAMETERS = "StokesParameters"
    TEMPERATURE = "Temperature"
    THERMAL_SPEED = "ThermalSpeed"
    TIME_SERIES = "TimeSeries"
    TOTAL_PRESSURE = "TotalPressure"
    UPPER_HYBRID_FREQUENCY = "UpperHybridFrequency"
    VCROSS_B = "VCrossB"
    VELOCITY = "Velocity"
    VOLUME_EMISSION_RATE = "VolumeEmissionRate"
    WAVELENGTH = "Wavelength"


class ScaleType(Enum):
    """
    Identifiers for scaling applied to a set of numbers.

    :cvar LINEAR_SCALE: Intervals which are equally spaced.
    :cvar LOG_SCALE: Intervals which are spaced proportionally to the
        logarithms of the values being represented.
    """

    LINEAR_SCALE = "LinearScale"
    LOG_SCALE = "LogScale"


class SourceType(Enum):
    """
    Identifiers for the characterization of the function or purpose of a source.

    :cvar ANCILLARY: A complementary item which can be subordinate,
        subsidiary, auxiliary, supplementary to the primary item.
    :cvar BROWSE: A representation of an image which is suitable to
        reveal most or all of the details of the image.
    :cvar DATA: A collection of organized information, usually the
        results of experience, observation or experiment, or a set of
        premises. This may consist of numbers, words, or images,
        particularly as measurements or observations of a set of
        variables.
    :cvar LAYOUT: The structured arrangement of items in a collection.
    :cvar THUMBNAIL: A small representation of an image which is
        suitable to infer what the full-sized imaged is like.
    """

    ANCILLARY = "Ancillary"
    BROWSE = "Browse"
    DATA = "Data"
    LAYOUT = "Layout"
    THUMBNAIL = "Thumbnail"


class SpectralRange(Enum):
    """Identifiers for names associated with wavelengths.

    Based on the ISO 21348 Solar Irradiance Standard. Additions have
    been made to extend the frequency ranges to include those used in
    space physics. Those additions are indicated in blue text. The
    "Total Solar Irradiance" category has not been included since it is
    a type of measurement and not a specific spectral range. See
    Appendix A: Comparison of Spectrum Domains for a comparison of the
    spectral ranges with other systems.

    :cvar CA_K: A spectrum with a wavelength of range centered near
        393.5 nm. VSO nickname: Ca-K image with range of 391.9 nm to
        395.2 nm.
    :cvar EXTREME_ULTRAVIOLET: A spectrum with a wavelength range of 10
        nm to 125 nm. VSO nickname: EUV image with a range of 10 nm to
        125 nm.
    :cvar FAR_ULTRAVIOLET: A spectrum with a wavelength range of 122 nm
        to 200 nm. VSO nickname: FUV image with a range of 122 nm to 200
        nm.
    :cvar GAMMA_RAYS: Photons with a wavelength range: 0.00001 nm to
        0.001 nm.
    :cvar HALPHA: A spectrum with a wavelength range centered at 656.3
        nm. VSO nickname: H-alpha image with a spectrum range of 655.8
        nm to 656.8 nm.
    :cvar HARD_XRAYS: Photons with a wavelength range: 0.001 nm to 0.1
        nm and an energy range of 12 keV to 120 keV.
    :cvar HE10830: A spectrum with a wavelength range centered at 1082.9
        nm. VSO nickname: an He 10830 image with a range of 1082.5 nm to
        1083.3 nm.
    :cvar HE304: A spectrum centered around the resonance line of
        ionized helium at 304 Angstrom (30.4 nm).
    :cvar INFRARED: Photons with a wavelength range: 760 nm to 10^6 nm.
    :cvar K7699: A spectrum with a wavelength range centered at 769.9
        nm. VSO nickname: K-7699 dopplergram with a range of 769.8 nm to
        770.0 nm.
    :cvar LBHBAND: Lyman-Birge-Hopfield band in the far ultraviolet
        range with wavelength range of 140 nm to 170 nm.
    :cvar MICROWAVE: Photons with a wavelength range: 10^6 nm to
        1.5*10^7 nm.
    :cvar NA_D: A spectrum with a wavelength range of centered at 589.3
        nm. VSO nickname: Na-D image with a range of 588.8 nm to 589.8
        nm.
    :cvar NI6768: A spectrum with a wavelength range centered at 676.8
        nm. VSO nickname: Ni-6768 dopplergram with a range of 676.7 nm
        to 676.9 nm.
    :cvar OPTICAL: Photons with a wavelength range: 380 nm to 760 nm.
    :cvar RADIO_FREQUENCY: Photons with a wavelength range: 10^5 nm to
        10^11 nm.
    :cvar SOFT_XRAYS: X-Rays with an energy range of 0.12 keV to 12 keV.
    :cvar ULTRAVIOLET: Photons with a wavelength range: 10 nm to 400 nm.
    :cvar WHITE_LIGHT: Photons with a wavelength in the visible range
        for humans.
    :cvar XRAYS: Photons with a wavelength range: 0.001 nm to 10 nm.
    """

    CA_K = "CaK"
    EXTREME_ULTRAVIOLET = "ExtremeUltraviolet"
    FAR_ULTRAVIOLET = "FarUltraviolet"
    GAMMA_RAYS = "GammaRays"
    HALPHA = "Halpha"
    HARD_XRAYS = "HardXRays"
    HE10830 = "He10830"
    HE304 = "He304"
    INFRARED = "Infrared"
    K7699 = "K7699"
    LBHBAND = "LBHBand"
    MICROWAVE = "Microwave"
    NA_D = "NaD"
    NI6768 = "Ni6768"
    OPTICAL = "Optical"
    RADIO_FREQUENCY = "RadioFrequency"
    SOFT_XRAYS = "SoftXRays"
    ULTRAVIOLET = "Ultraviolet"
    WHITE_LIGHT = "WhiteLight"
    XRAYS = "XRays"


class Style(Enum):
    """
    Identifiers for the manner in which a response from a URL is presented.

    :cvar EPNTAP: Europlanet (EPN) Table Access Protocol (TAP) is a
        framework, which is using TAP with the EPNcore metadata
        dictionary. The EPNcore metadata dictionary defines the core
        components that are necessary to perform data discovery in the
        Solar System related science fields, see
        https://github.com/ivoa-std/EPNTAP.
    :cvar FILE: Access to a file containing the data.
    :cvar GIT: Git is a version control system for tracking changes in
        any set of files. It is known for its speed, data integrity, and
        support for distributed, non-linear workflows.
    :cvar HAPI: A Heliophysics Application Programmer Interface (HAPI)
        specification compliant access point.
    :cvar LISTING: A listing of files either through FTP or HTTP.
    :cvar SEARCH: A web search interface that requires additional input.
    :cvar TAP: The table access protocol (TAP) defines a service
        protocol for accessing general table data, including
        astronomical catalogs as well as general database tables. Access
        is provided for both database and table metadata as well as for
        actual table data.
        https://wiki.ivoa.net/twiki/bin/view/IVOA/TableAccess.
    :cvar TEMPLATE: A URI template that contains special fields as
        defined in URI Template specification
        http://tsds.org/uri_templates.
    :cvar OVERVIEW: A web page that provides and overview of available
        data and links.
    :cvar WEB_SERVICE: A Web-based service that uses SOAP, WSDL or UDDI
        open standards.
    """

    EPNTAP = "EPNTAP"
    FILE = "File"
    GIT = "Git"
    HAPI = "HAPI"
    LISTING = "Listing"
    SEARCH = "Search"
    TAP = "TAP"
    TEMPLATE = "Template"
    OVERVIEW = "Overview"
    WEB_SERVICE = "WebService"


class SupportQuantity(Enum):
    """
    Identifiers for the information useful in understanding the context of an
    observation, typically observed or measured coincidentally with a physical
    observation.

    :cvar DATA_QUALITY: An ancillary parameter that denotes the standard
        or degree of accuracy, trustworthiness, or usefulness of another
        parameter.
    :cvar HOUSEKEEPING: Parameters that indicate the status or health
        state of instruments or monitoring devices as measured in
        physical units such as that for current, voltage, or
        temperature. Housekeeping data can be analyzed to determine
        whether instruments are working correctly and the knowledge of
        their values may be used to avoid errors or even device
        failures.
    :cvar INSTRUMENT_MODE: An indication of a state (mode) in which the
        instrument is operating. How a mode influences the
        interpretation and representation of data is described in
        instrument related documentation.
    :cvar ORIENTATION: The specification of the directional alignment of
        an object or measurement in a reference coordinate system. The
        orientation such as a spacecraft spin axis attitude is usually
        expressed as one or more angles relative to the basis axes of
        some specified physical space usually together with the
        date/time of the observation.
    :cvar OTHER: Not classified with more specific terms. The context of
        its usage may be described in related text.
    :cvar POSITIONAL: The specification of the location of an object or
        measurement within a reference coordinate system. The position
        is usually expressed as a set of values corresponding to the
        location along a set of orthogonal axes together with the
        date/time of the observation.
    :cvar REMARK: A notice, comment, or observation.
    :cvar ROTATION_MATRIX: A tensor that is used to perform vector data
        transformation from one coordinate system to another.
    :cvar SPIN_PERIOD: The time required for an object such as a
        spacecraft or planet to perform one full rotation in a given
        frame of reference.
    :cvar SPIN_PHASE: An angular based or normalized parameter that
        specifies the spin state of an object such as a spacecraft or
        planet in a specific coordinate system usually together with the
        date/time of the observation.
    :cvar SPIN_RATE: The angular rate of change of the spin angle of an
        object such as a spacecraft or planet.
    :cvar TELEMETRY: Parameters that include full packets of data from
        monitoring devices or the memory addresses of datum within
        telemetry packets. The data comprising telemetry packets are
        typically expressed by using non-physical engineering units and
        may be used to express a variety of device operating conditions
        such as command acceptance/execution, housekeeping, event
        characterization, memory dumps, and science data. Telemetry
        packets may be raw or unpacked.
    :cvar TEMPORAL: Pertaining to time.
    :cvar VELOCITY: Rate of change of position. Also used for the
        average velocity of a collection of particles, also referred to
        as bulk velocity.
    :cvar WEB_RESOURCE: A Web page or file-based resource accessible by
        a URL.
    :cvar WEB_SERVICE: A Web-based service that uses SOAP, WSDL or UDDI
        open standards.
    """

    DATA_QUALITY = "DataQuality"
    HOUSEKEEPING = "Housekeeping"
    INSTRUMENT_MODE = "InstrumentMode"
    ORIENTATION = "Orientation"
    OTHER = "Other"
    POSITIONAL = "Positional"
    REMARK = "Remark"
    ROTATION_MATRIX = "RotationMatrix"
    SPIN_PERIOD = "SpinPeriod"
    SPIN_PHASE = "SpinPhase"
    SPIN_RATE = "SpinRate"
    TELEMETRY = "Telemetry"
    TEMPORAL = "Temporal"
    VELOCITY = "Velocity"
    WEB_RESOURCE = "WebResource"
    WEB_SERVICE = "WebService"


class Symmetry(Enum):
    """
    Symmetry of the model domain.

    :cvar AXIAL: Axial symmetry.
    :cvar CENTRAL: Central Symmetry.
    :cvar NONE: A lack or absence of anything.
    :cvar PLANE: Symmetry across a plane.
    """

    AXIAL = "Axial"
    CENTRAL = "Central"
    NONE = "None"
    PLANE = "Plane"


@dataclass
class TimeSpan:
    """
    The duration of an interval in time.
    """

    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    stop_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StopDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    relative_stop_date: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "RelativeStopDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


class Version(Enum):
    """
    Version number.
    """

    VALUE_2_6_0 = "2.6.0"


class WaveQuantity(Enum):
    """
    Identifiers for the characterization of the physical properties of a wave.

    :cvar ABSORPTION: Decrease of radiant energy (relative to the
        background continuum spectrum).
    :cvar ACELECTRIC_FIELD: Alternating electric field component of a
        wave.
    :cvar ACMAGNETIC_FIELD: Alternating magnetic field component of a
        wave.
    :cvar ALBEDO: The ratio of reflected radiation from the surface to
        incident radiation upon it.
    :cvar DOPPLER_FREQUENCY: Change in the frequency of a propagating
        wave due to motion of the source, the observer, the reflector,
        or the propagation medium.
    :cvar EMISSIVITY: The energy emitted spontaneously per unit
        bandwidth (typically frequency) per unit time per unit mass of
        source. Emissivity is usually integrated over all
        directions/solid angles.
    :cvar ENERGY_FLUX: The amount of energy passing through a unit area
        in a unit time.
    :cvar EQUIVALENT_WIDTH: The spectral width of a total absorption
        line having the amount of absorbed radiant energy being
        equivalent to that in an observed absorption line.
    :cvar FREQUENCY: The number of occurrences of a repeating event per
        unit time.
    :cvar GYROFREQUENCY: The number of gyrations around a magnetic
        guiding center (field line) a charged particle makes per unit
        time due to the Lorentz force.
    :cvar INTENSITY: The measurement of radiant or wave energy per unit
        detector area per unit bandwidth per unit solid angle per unit
        time.
    :cvar LINE_DEPTH: The measure of the amount of absorption below the
        continuum (depth) in a particular wavelength or frequency in an
        absorption spectrum.
    :cvar LOWER_HYBRID_FREQUENCY: Lower hybrid oscillations involve
        longitudinal motions of electrons and ions in a magnetized
        plasma. The propagation of lower hybrid waves must be close to
        perpendicular to the background magnetic field in so that
        electrons cannot move along field lines thus preventing wave
        growth. The lower hybrid frequency,
        &amp;phi;&lt;sub&gt;LH&lt;/sub&gt;, can be calculated by using
        &amp;phi;&lt;sub&gt;LH&lt;/sub&gt;=[(&amp;omega;&lt;sub&gt;ce&lt;/sub&gt;&amp;omega;&lt;sub&gt;ci&lt;/sub&gt;)&lt;sup&gt;-1&lt;/sup&gt;+&amp;phi;&lt;sub&gt;pi&lt;/sub&gt;&lt;sup&gt;-2&lt;/sup&gt;]&lt;sup&gt;-1/2&lt;/sup&gt;
        where &amp;omega;&lt;sub&gt;ce&lt;/sub&gt; and
        &amp;omega;&lt;sub&gt;ci&lt;/sub&gt; are the electron and ion
        cyclotron frequencies, respectively, and
        $phi;&lt;sub&gt;LH&lt;/sub&gt; is the ion plasma frequency.
    :cvar MAGNETIC_FIELD: A region of space near a magnetized body where
        magnetic forces can be detected (as measured by methods such as
        Zeeman splitting, etc.).
    :cvar MODE_AMPLITUDE: In helioseismology the magnitude of
        oscillation of waves of a particular geometry.
    :cvar PLASMA_FREQUENCY: A number density dependent characteristic
        frequency of a plasma.
    :cvar POLARIZATION: Direction of the electric vector of an
        electromagnetic wave. The wave can be linearly polarized in any
        direction perpendicular to the direction of travel, circularly
        polarized (clockwise or counterclockwise), unpolarized, or
        mixtures of the above.
    :cvar POYNTING_FLUX: Electromagnetic energy flux transported by a
        wave characterized as the rate of energy transport per unit area
        per steradian.
    :cvar PROPAGATION_TIME: Time difference between transmission and
        reception of a wave in an active wave experiment.
    :cvar STOKES_PARAMETERS: A set of four parameters (usually called
        I,Q, U and V) which describe the polarization state of an
        electromagnetic wave propagating through space.
    :cvar UPPER_HYBRID_FREQUENCY: Upper hybrid oscillations involve
        longitudinal motions of electrons perpendicular to the magnetic
        field. The upper hybrid frequency,
        &amp;phi;&lt;sub&gt;UH&lt;/sub&gt;, is governed by the
        relationship
        &amp;phi;&lt;sub&gt;UH&lt;/sub&gt;^2=&amp;phi;&lt;sub&gt;pe&lt;/sub&gt;^2+&amp;theta;&lt;sub&gt;ce&lt;/sub&gt;^2
        where &amp;phi;&lt;sub&gt;pe&lt;/sub&gt; is electron plasma
        frequency and &amp;theta;&lt;sub&gt;ce&lt;/sub&gt; is the
        electron cyclotron frequency.
    :cvar VELOCITY: Rate of change of position. Also used for the
        average velocity of a collection of particles, also referred to
        as bulk velocity.
    :cvar VOLUME_EMISSION_RATE: The volume emission rate, e(r,t,l), is
        the number of photons emitted per unit source volume per second
        (photons/m^3/s), as measured along the line of sight between the
        source point and the observer. The Volume Emission Rate is in
        general a function of the line-of-sight distance, r, time, t,
        and wavelength, l. The Volume Emission Rate is actually not a
        directly measurable quantity. However, the term has been
        commonly used in both data product descriptions and research
        publications.
    :cvar WAVELENGTH: The peak-to-peak distance over one wave period.
    """

    ABSORPTION = "Absorption"
    ACELECTRIC_FIELD = "ACElectricField"
    ACMAGNETIC_FIELD = "ACMagneticField"
    ALBEDO = "Albedo"
    DOPPLER_FREQUENCY = "DopplerFrequency"
    EMISSIVITY = "Emissivity"
    ENERGY_FLUX = "EnergyFlux"
    EQUIVALENT_WIDTH = "EquivalentWidth"
    FREQUENCY = "Frequency"
    GYROFREQUENCY = "Gyrofrequency"
    INTENSITY = "Intensity"
    LINE_DEPTH = "LineDepth"
    LOWER_HYBRID_FREQUENCY = "LowerHybridFrequency"
    MAGNETIC_FIELD = "MagneticField"
    MODE_AMPLITUDE = "ModeAmplitude"
    PLASMA_FREQUENCY = "PlasmaFrequency"
    POLARIZATION = "Polarization"
    POYNTING_FLUX = "PoyntingFlux"
    PROPAGATION_TIME = "PropagationTime"
    STOKES_PARAMETERS = "StokesParameters"
    UPPER_HYBRID_FREQUENCY = "UpperHybridFrequency"
    VELOCITY = "Velocity"
    VOLUME_EMISSION_RATE = "VolumeEmissionRate"
    WAVELENGTH = "Wavelength"


class WaveType(Enum):
    """
    Identifiers for the carrier or phenomenum of wave information observed by the
    measurement.

    :cvar ELECTROMAGNETIC: Electric and magnetic field variations in
        time and space that propagate through a medium or a vacuum. The
        wave propagation direction, electric field vector, and magnetic
        field vector form an orthogonal triad. Waves in this category
        are detected by having their field quantities measured.
    :cvar ELECTROSTATIC: Collective longitudinal electric-field and
        plasma oscillations trapped within a body of plasma.
    :cvar HYDRODYNAMIC: Periodic or quasi-periodic oscillations of fluid
        quantities.
    :cvar MHD: Hydrodynamic waves in a magnetized plasma in which the
        background magnetic field plays a key role in controlling the
        wave propagation characteristics.
    :cvar PHOTON: Electromagnetic waves detected by techniques that
        utilize their corpuscular character (e.g., CCD, CMOS, or
        Photomultiplier).
    :cvar PLASMA_WAVES: Self-consistent collective oscillations of
        particles and fields (electric and magnetic) in a plasma.
    """

    ELECTROMAGNETIC = "Electromagnetic"
    ELECTROSTATIC = "Electrostatic"
    HYDRODYNAMIC = "Hydrodynamic"
    MHD = "MHD"
    PHOTON = "Photon"
    PLASMA_WAVES = "PlasmaWaves"


class Yn(Enum):
    """
    Yes or No.

    :cvar NO: The negative response to a yes or no question.
    :cvar YES: The affirmative response to a yes or no question.
    """

    NO = "No"
    YES = "Yes"


@dataclass
class AccessUrl:
    """
    Attributes of the method for accessing a resource including a URL, name and
    description.
    """

    class Meta:
        name = "AccessURL"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    style: Optional[Style] = field(
        default=None,
        metadata={
            "name": "Style",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    product_key: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ProductKey",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Association:
    """
    Attributes of a relationship a resource has with another resource.
    """

    association_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssociationID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    association_type: Optional[AssociationType] = field(
        default=None,
        metadata={
            "name": "AssociationType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class AzimuthalAngleRange:
    """The range of possible azimuthal angles for a group of energy observations.

    Default units are degrees.
    """

    low: Optional[float] = field(
        default=None,
        metadata={
            "name": "Low",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    high: Optional[float] = field(
        default=None,
        metadata={
            "name": "High",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    bin: List[Bin] = field(
        default_factory=list,
        metadata={
            "name": "Bin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Checksum:
    """A computed value that is dependent upon the contents of a digital data
    object.

    Primarily used to check whether errors or alterations have occurred
    during the transmission or storage of a data object.
    """

    hash_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "HashValue",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    hash_function: Optional[HashFunction] = field(
        default=None,
        metadata={
            "name": "HashFunction",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )


@dataclass
class Contact:
    """
    The person or organization who may be able to provide special assistance or
    serve as a channel for communication for additional information about a
    resource.
    """

    person_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PersonID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    role: List[Role] = field(
        default_factory=list,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    stop_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StopDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class CoordinateSystem:
    """
    The specification of the orientation of a set of (typically) orthogonal base
    axes.
    """

    coordinate_representation: Optional[CoordinateRepresentation] = field(
        default=None,
        metadata={
            "name": "CoordinateRepresentation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    coordinate_system_name: Optional[CoordinateSystemName] = field(
        default=None,
        metadata={
            "name": "CoordinateSystemName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )


@dataclass
class DiagnosisTimeStep:
    """
    Time at which a diagnosis is performed and quantity saved.
    """

    time_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeStart",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    saved_quantity: List[SavedQuantity] = field(
        default_factory=list,
        metadata={
            "name": "SavedQuantity",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class EnergyRange:
    """
    The minimum and maximum energy values of the particles represented by a given
    physical parameter description.
    """

    low: Optional[float] = field(
        default=None,
        metadata={
            "name": "Low",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    high: Optional[float] = field(
        default=None,
        metadata={
            "name": "High",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    bin: List[Bin] = field(
        default_factory=list,
        metadata={
            "name": "Bin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class FrequencyRange:
    """
    The range of possible values for the observed frequency.
    """

    spectral_range: Optional[SpectralRange] = field(
        default=None,
        metadata={
            "name": "SpectralRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    low: Optional[float] = field(
        default=None,
        metadata={
            "name": "Low",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    high: Optional[float] = field(
        default=None,
        metadata={
            "name": "High",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    bin: List[Bin] = field(
        default_factory=list,
        metadata={
            "name": "Bin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class InputPopulation:
    """
    A container element that specifies the characteristics of a particle population
    used as input to a model model.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    set: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Set",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    parameter_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterKey",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    modeled_region: List[ModeledRegion] = field(
        default_factory=list,
        metadata={
            "name": "ModeledRegion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    qualifier: List[Qualifier] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    particle_type: Optional[ParticleType] = field(
        default=None,
        metadata={
            "name": "ParticleType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    chemical_formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChemicalFormula",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    atomic_number: Optional[float] = field(
        default=None,
        metadata={
            "name": "AtomicNumber",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    population_mass_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PopulationMassNumber",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    population_charge_state: Optional[float] = field(
        default=None,
        metadata={
            "name": "PopulationChargeState",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    population_density: Optional[str] = field(
        default=None,
        metadata={
            "name": "PopulationDensity",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    population_temperature: Optional[str] = field(
        default=None,
        metadata={
            "name": "PopulationTemperature",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    population_flow_speed: Optional[str] = field(
        default=None,
        metadata={
            "name": "PopulationFlowSpeed",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    distribution: Optional[str] = field(
        default=None,
        metadata={
            "name": "Distribution",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    production_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductionRate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    total_production_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalProductionRate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_table_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "InputTableURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    density_profile: Optional[str] = field(
        default=None,
        metadata={
            "name": "DensityProfile",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    model_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModelURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class InputProcess:
    """
    Parameters associated to a chemical process happening in the model.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    set: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Set",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    parameter_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterKey",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    modeled_region: List[ModeledRegion] = field(
        default_factory=list,
        metadata={
            "name": "ModeledRegion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    process_type: Optional[ProcessType] = field(
        default=None,
        metadata={
            "name": "ProcessType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    units_conversion: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitsConversion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    process_coefficient: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProcessCoefficient",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    process_coeff_type: Optional[ProcCoeffType] = field(
        default=None,
        metadata={
            "name": "ProcessCoeffType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    process_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProcessModel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    model_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModelURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Installer:
    """
    A piece of software that installs a program or package on a system.
    """

    availability: Optional[Availability] = field(
        default=None,
        metadata={
            "name": "Availability",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    access_rights: Optional[AccessRights] = field(
        default=None,
        metadata={
            "name": "AccessRights",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    acknowledgement: Optional[str] = field(
        default=None,
        metadata={
            "name": "Acknowledgement",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )


@dataclass
class Location:
    """
    A position in space definable by a regional referencing system and geographic
    coordinates.
    """

    observatory_region: List[Region] = field(
        default_factory=list,
        metadata={
            "name": "ObservatoryRegion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    coordinate_system_name: Optional[CoordinateSystemName] = field(
        default=None,
        metadata={
            "name": "CoordinateSystemName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    latitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    elevation: Optional[float] = field(
        default=None,
        metadata={
            "name": "Elevation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class MassRange:
    """
    The range of possible mass for a group of particle observations.
    """

    low: Optional[float] = field(
        default=None,
        metadata={
            "name": "Low",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    high: Optional[float] = field(
        default=None,
        metadata={
            "name": "High",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    bin: List[Bin] = field(
        default_factory=list,
        metadata={
            "name": "Bin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Mixed:
    """A parameter derived from more than one type of parameter.

    For example, plasma beta, the ratio of plasma particle energy
    density to the energy density of the magnetic field permeating the
    plasma, is mixed.
    """

    mixed_quantity: Optional[MixedQuantity] = field(
        default=None,
        metadata={
            "name": "MixedQuantity",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    particle_type: List[ParticleType] = field(
        default_factory=list,
        metadata={
            "name": "ParticleType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    qualifier: List[Qualifier] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class ObservationExtent:
    """
    The spatial area encompassed by an observation.
    """

    observed_region: Optional[Region] = field(
        default=None,
        metadata={
            "name": "ObservedRegion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    start_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartLocation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    stop_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopLocation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Person:
    """
    An individual human being.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    release_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReleaseDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    person_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PersonName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    organization_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrganizationName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    email: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    phone_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    fax_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNumber",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    orcidentifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ORCIdentifier",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class PitchAngleRange:
    """
    The range of possible pitch angles for a group of particle observations.
    """

    low: Optional[float] = field(
        default=None,
        metadata={
            "name": "Low",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    high: Optional[float] = field(
        default=None,
        metadata={
            "name": "High",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    bin: List[Bin] = field(
        default_factory=list,
        metadata={
            "name": "Bin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class PolarAngleRange:
    """The range of possible polar angles for a group of energy observations.

    Defaults units are degrees.
    """

    low: Optional[float] = field(
        default=None,
        metadata={
            "name": "Low",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    high: Optional[float] = field(
        default=None,
        metadata={
            "name": "High",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    bin: List[Bin] = field(
        default_factory=list,
        metadata={
            "name": "Bin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Property:
    """
    A container of attributes regarding the property of an application.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    property_quantity: Optional[ParameterQuantity] = field(
        default=None,
        metadata={
            "name": "PropertyQuantity",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    qualifier: List[Qualifier] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    units_conversion: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitsConversion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    property_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropertyLabel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    property_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropertyValue",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    property_table_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropertyTableURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_min: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_max: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMax",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    property_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropertyModel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    model_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModelURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class RenderingHints:
    """
    Attributes to aid in the rendering of parameter.
    """

    display_type: Optional[DisplayType] = field(
        default=None,
        metadata={
            "name": "DisplayType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    axis_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "AxisLabel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    rendering_axis: Optional[RenderingAxis] = field(
        default=None,
        metadata={
            "name": "RenderingAxis",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    index: List[int] = field(
        default_factory=list,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "tokens": True,
        },
    )
    value_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValueFormat",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    scale_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "ScaleMin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    scale_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "ScaleMax",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    scale_type: Optional[ScaleType] = field(
        default=None,
        metadata={
            "name": "ScaleType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class RevisionHistory:
    """
    A history of changes that improve or upgrade.
    """

    revision_event: List[RevisionEvent] = field(
        default_factory=list,
        metadata={
            "name": "RevisionEvent",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )


@dataclass
class Support:
    """
    Information useful in understanding the context of an observation, typically
    observed or measured coincidentally with a physical observation.
    """

    qualifier: List[Qualifier] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    support_quantity: Optional[SupportQuantity] = field(
        default=None,
        metadata={
            "name": "SupportQuantity",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )


@dataclass
class TemporalDescription:
    """
    A characterization of the time over which the measurement was taken.
    """

    time_span: Optional[TimeSpan] = field(
        default=None,
        metadata={
            "name": "TimeSpan",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    cadence: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Cadence",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    cadence_min: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "CadenceMin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    cadence_max: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "CadenceMax",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    exposure: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Exposure",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    exposure_min: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExposureMin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    exposure_max: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExposureMax",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Versions:
    """
    A container of one or more sets of version information.
    """

    model_version: List[ModelVersion] = field(
        default_factory=list,
        metadata={
            "name": "ModelVersion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class WavelengthRange:
    """
    The range of possible values for the observed wavelength.
    """

    spectral_range: Optional[SpectralRange] = field(
        default=None,
        metadata={
            "name": "SpectralRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    low: Optional[float] = field(
        default=None,
        metadata={
            "name": "Low",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    high: Optional[float] = field(
        default=None,
        metadata={
            "name": "High",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    bin: List[Bin] = field(
        default_factory=list,
        metadata={
            "name": "Bin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class AccessInformation:
    """
    Attributes which specify how to access a resource, its availability, storage
    format, etc.
    """

    repository_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RepositoryID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    availability: Optional[Availability] = field(
        default=None,
        metadata={
            "name": "Availability",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    access_rights: Optional[AccessRights] = field(
        default=None,
        metadata={
            "name": "AccessRights",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    access_url: List[AccessUrl] = field(
        default_factory=list,
        metadata={
            "name": "AccessURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    format: List[Format] = field(
        default_factory=list,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    encoding: Optional[Encoding] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    access_directory_template: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccessDirectoryTemplate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    access_filename_template: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccessFilenameTemplate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    data_extent: Optional[DataExtent] = field(
        default=None,
        metadata={
            "name": "DataExtent",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    acknowledgement: Optional[str] = field(
        default=None,
        metadata={
            "name": "Acknowledgement",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class AccessInformationOptional:
    """Attributes of the resource which pertain to how to accessing the resource,
    availability and storage format.

    This resource class is an exact copy of the AccessInformation
    container. However, as its name suggests, AccessInformationOptional
    is not a required element.
    """

    repository_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RepositoryID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    availability: Optional[Availability] = field(
        default=None,
        metadata={
            "name": "Availability",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    access_rights: Optional[AccessRights] = field(
        default=None,
        metadata={
            "name": "AccessRights",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    access_url: List[AccessUrl] = field(
        default_factory=list,
        metadata={
            "name": "AccessURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    format: List[Format] = field(
        default_factory=list,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    encoding: Optional[Encoding] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    access_directory_template: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccessDirectoryTemplate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    access_filename_template: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccessFilenameTemplate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    data_extent: Optional[DataExtent] = field(
        default=None,
        metadata={
            "name": "DataExtent",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    acknowledgement: Optional[str] = field(
        default=None,
        metadata={
            "name": "Acknowledgement",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Element:
    """
    A component or individual unit of a multiple value quantity such as an array or
    vector.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    qualifier: List[Qualifier] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    index: List[int] = field(
        default_factory=list,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "tokens": True,
        },
    )
    parameter_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterKey",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    units_conversion: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitsConversion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_min: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_max: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMax",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    fill_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "FillValue",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    rendering_hints: Optional[RenderingHints] = field(
        default=None,
        metadata={
            "name": "RenderingHints",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class ExecutionEnvironment:
    """
    An execution platform for software which includes an operating system and
    necessary hardware.
    """

    operating_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatingSystem",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    installer: Optional[Installer] = field(
        default=None,
        metadata={
            "name": "Installer",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    cores: Optional[float] = field(
        default=None,
        metadata={
            "name": "Cores",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    storage: Optional[str] = field(
        default=None,
        metadata={
            "name": "Storage",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    memory: Optional[str] = field(
        default=None,
        metadata={
            "name": "Memory",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class FieldType:
    """
    The space around a radiating body within which its electromagnetic attributes
    can exert force on another similar body that is not in direct contact.
    """

    class Meta:
        name = "Field"

    qualifier: List[Qualifier] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    field_quantity: Optional[FieldQuantity] = field(
        default=None,
        metadata={
            "name": "FieldQuantity",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    frequency_range: Optional[FrequencyRange] = field(
        default=None,
        metadata={
            "name": "FrequencyRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class InputField:
    """
    Parameters associated to a field imposed in the model.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    set: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Set",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    parameter_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterKey",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    modeled_region: List[ModeledRegion] = field(
        default_factory=list,
        metadata={
            "name": "ModeledRegion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "CoordinateSystem",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    qualifier: List[Qualifier] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    field_quantity: Optional[FieldQuantity] = field(
        default=None,
        metadata={
            "name": "FieldQuantity",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    units_conversion: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitsConversion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "InputLabel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    field_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldValue",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_table_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "InputTableURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_min: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_max: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMax",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    field_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldModel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    model_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModelURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class InputParameter:
    """
    A container of information regarding an input parameter of the model run.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    modeled_region: List[ModeledRegion] = field(
        default_factory=list,
        metadata={
            "name": "ModeledRegion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    qualifier: List[Qualifier] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_table_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InputTableURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    parameter_quantity: Optional[ParameterQuantity] = field(
        default=None,
        metadata={
            "name": "ParameterQuantity",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    property: List[Property] = field(
        default_factory=list,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )


@dataclass
class InputProperties:
    """
    Properties.
    """

    property: List[Property] = field(
        default_factory=list,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class ModelDomain:
    """
    Parameters associated to the model spatial domain.
    """

    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "CoordinateSystem",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    spatial_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpatialDimension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    velocity_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "VelocityDimension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    field_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "FieldDimension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    units_conversion: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitsConversion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    coordinates_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoordinatesLabel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_min: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_max: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMax",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    grid_structure: Optional[str] = field(
        default=None,
        metadata={
            "name": "GridStructure",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    grid_cell_size: Optional[str] = field(
        default=None,
        metadata={
            "name": "GridCellSize",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    symmetry: Optional[Symmetry] = field(
        default=None,
        metadata={
            "name": "Symmetry",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    boundary_conditions: Optional[BoundaryConditions] = field(
        default=None,
        metadata={
            "name": "BoundaryConditions",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class ModelTime:
    """
    Parameters associated to the model time.
    """

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    time_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeStart",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    time_stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeStop",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    time_step: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TimeStep",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    diagnosis_time_step: Optional[DiagnosisTimeStep] = field(
        default=None,
        metadata={
            "name": "DiagnosisTimeStep",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Particle:
    """A description of the types of particles observed in the measurement.

    This includes both direct observations and inferred observations.
    """

    particle_type: List[ParticleType] = field(
        default_factory=list,
        metadata={
            "name": "ParticleType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    qualifier: List[Qualifier] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    particle_quantity: Optional[ParticleQuantity] = field(
        default=None,
        metadata={
            "name": "ParticleQuantity",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    atomic_number: List[float] = field(
        default_factory=list,
        metadata={
            "name": "AtomicNumber",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    energy_range: Optional[EnergyRange] = field(
        default=None,
        metadata={
            "name": "EnergyRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    azimuthal_angle_range: Optional[AzimuthalAngleRange] = field(
        default=None,
        metadata={
            "name": "AzimuthalAngleRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    polar_angle_range: Optional[PolarAngleRange] = field(
        default=None,
        metadata={
            "name": "PolarAngleRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    mass_range: Optional[MassRange] = field(
        default=None,
        metadata={
            "name": "MassRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    pitch_angle_range: Optional[PitchAngleRange] = field(
        default=None,
        metadata={
            "name": "PitchAngleRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    chemical_formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChemicalFormula",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    population: Optional[str] = field(
        default=None,
        metadata={
            "name": "Population",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    population_mass_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PopulationMassNumber",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    population_charge_state: Optional[float] = field(
        default=None,
        metadata={
            "name": "PopulationChargeState",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class RegionParameter:
    """
    Radius of the Region in the model.
    """

    modeled_region: Optional[ModeledRegion] = field(
        default=None,
        metadata={
            "name": "ModeledRegion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    radius: Optional[str] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    sub_longitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubLongitude",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    period: Optional[str] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    object_mass: Optional[str] = field(
        default=None,
        metadata={
            "name": "ObjectMass",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_table_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "InputTableURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    property: List[Property] = field(
        default_factory=list,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class ResourceHeader:
    """
    Attributes of a resource which pertain to the provider of the resource and
    descriptive information about the resource.
    """

    resource_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    alternate_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AlternateName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    doi: Optional[str] = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    release_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReleaseDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    revision_history: Optional[RevisionHistory] = field(
        default=None,
        metadata={
            "name": "RevisionHistory",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    expiration_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    acknowledgement: Optional[str] = field(
        default=None,
        metadata={
            "name": "Acknowledgement",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    publication_info: Optional[PublicationInfo] = field(
        default=None,
        metadata={
            "name": "PublicationInfo",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    funding: List[Funding] = field(
        default_factory=list,
        metadata={
            "name": "Funding",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    contact: List[Contact] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    information_url: List[InformationUrl] = field(
        default_factory=list,
        metadata={
            "name": "InformationURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    association: List[Association] = field(
        default_factory=list,
        metadata={
            "name": "Association",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    prior_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PriorID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )


@dataclass
class Source:
    """
    The location and attributes of an object.
    """

    source_type: Optional[SourceType] = field(
        default=None,
        metadata={
            "name": "SourceType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    mirror_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MirrorURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    checksum: Optional[Checksum] = field(
        default=None,
        metadata={
            "name": "Checksum",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    data_extent: Optional[DataExtent] = field(
        default=None,
        metadata={
            "name": "DataExtent",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class SpatialCoverage:
    """
    A region of space defined by the latitude, longitude and altitude in a
    geographic coordinate system.
    """

    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "CoordinateSystem",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    center_latitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "CenterLatitude",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    northernmost_latitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "NorthernmostLatitude",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    southernmost_latitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "SouthernmostLatitude",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    center_longitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "CenterLongitude",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    easternmost_longitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "EasternmostLongitude",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    westernmost_longitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "WesternmostLongitude",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    center_elevation: Optional[str] = field(
        default=None,
        metadata={
            "name": "CenterElevation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    minimum_elevation: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinimumElevation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    maximum_elevation: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaximumElevation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    acknowledgement: Optional[str] = field(
        default=None,
        metadata={
            "name": "Acknowledgement",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class SpatialDescription:
    """
    A characterization of the spatial extent over which the measurement was taken.
    """

    dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "CoordinateSystem",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    units_conversion: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitsConversion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    coordinates_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoordinatesLabel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    cuts_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "CutsDescription",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    cubes_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "CubesDescription",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    plane_normal_vector: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaneNormalVector",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    plane_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlanePoint",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    region_begin: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegionBegin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    region_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegionEnd",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    step: Optional[str] = field(
        default=None,
        metadata={
            "name": "Step",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Wave:
    """
    Periodic or quasi-periodic (AC) variations of physical quantities in time and
    space, capable of propagating or being trapped within particular regimes.
    """

    wave_type: Optional[WaveType] = field(
        default=None,
        metadata={
            "name": "WaveType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    qualifier: List[Qualifier] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    wave_quantity: Optional[WaveQuantity] = field(
        default=None,
        metadata={
            "name": "WaveQuantity",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    energy_range: Optional[EnergyRange] = field(
        default=None,
        metadata={
            "name": "EnergyRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    frequency_range: Optional[FrequencyRange] = field(
        default=None,
        metadata={
            "name": "FrequencyRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    wavelength_range: Optional[WavelengthRange] = field(
        default=None,
        metadata={
            "name": "WavelengthRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Annotation:
    """
    Information which is explanatory or descriptive which is associated with
    another resource.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    image_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImageURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    annotation_type: Optional[AnnotationType] = field(
        default=None,
        metadata={
            "name": "AnnotationType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    phenomenon_type: List[PhenomenonType] = field(
        default_factory=list,
        metadata={
            "name": "PhenomenonType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    classification_method: Optional[ClassificationMethod] = field(
        default=None,
        metadata={
            "name": "ClassificationMethod",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    confidence_rating: Optional[ConfidenceRating] = field(
        default=None,
        metadata={
            "name": "ConfidenceRating",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    time_span: List[TimeSpan] = field(
        default_factory=list,
        metadata={
            "name": "TimeSpan",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    observation_extent: List[ObservationExtent] = field(
        default_factory=list,
        metadata={
            "name": "ObservationExtent",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Document:
    """A set of information designed and presented as an individual entity.

    A document may contain plain or formatted text, in-line graphics,
    sound, other multimedia data, or hypermedia references. A Document
    resource is intended for use on digital objects that have no other
    identifier (e.g., DOI or ISBN).
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    access_information: List[AccessInformation] = field(
        default_factory=list,
        metadata={
            "name": "AccessInformation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    document_type: Optional[DocumentType] = field(
        default=None,
        metadata={
            "name": "DocumentType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    mimetype: Optional[str] = field(
        default=None,
        metadata={
            "name": "MIMEType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    input_resource_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InputResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )


@dataclass
class Granule:
    """An accessible portion of another resource.

    A Granule may be composed of one or more physical pieces (files)
    which are considered inseparable. For example, a data storage format
    that maintains metadata and binary data in separate, but tightly
    coupled files. Granules should not be used to group files that have
    simple relationships or which are associated through a parent
    resource. For example, each file containing a time interval data for
    a Numerical Data resource would each be considered a Granule. The
    ParentID of a Granule resource must be a NumericalData resource. The
    attributes of a Granule supersede the corresponding attributes in
    the NumericalData resource.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    release_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReleaseDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    expiration_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    parent_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParentID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    prior_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PriorID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    stop_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StopDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    spatial_coverage: List[SpatialCoverage] = field(
        default_factory=list,
        metadata={
            "name": "SpatialCoverage",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    source: List[Source] = field(
        default_factory=list,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    region_begin: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegionBegin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    region_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegionEnd",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )


@dataclass
class Instrument:
    """
    A device that makes measurements used to characterize a physical phenomenon, or
    a family of like devices.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    instrument_type: List[InstrumentType] = field(
        default_factory=list,
        metadata={
            "name": "InstrumentType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    instrument_group_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrumentGroupID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    investigation_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InvestigationName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    operating_span: Optional[OperatingSpan] = field(
        default=None,
        metadata={
            "name": "OperatingSpan",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    observatory_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ObservatoryID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Member:
    """A constituent part of a collection.

    A Member is of a one of the supported resource types and in
    referenced by an identifier. Details about the member are part of
    its respective resource description.
    """

    resource_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResourceName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    member_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MemberID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    stop_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StopDate",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    spatial_coverage: Optional[SpatialCoverage] = field(
        default=None,
        metadata={
            "name": "SpatialCoverage",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class ModelRun:
    """
    Description of a model run, including the code ID, the run spatial and temporal
    description, and all the relevant inputs.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    access_information: List[AccessInformation] = field(
        default_factory=list,
        metadata={
            "name": "AccessInformation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_resource_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderResourceName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_processing_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderProcessingLevel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderVersion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    model_specification: Optional[ModelSpecification] = field(
        default=None,
        metadata={
            "name": "ModelSpecification",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    temporal_dependence: Optional[Yn] = field(
        default=None,
        metadata={
            "name": "TemporalDependence",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    modeled_region: List[ModeledRegion] = field(
        default_factory=list,
        metadata={
            "name": "ModeledRegion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    likelihood_rating: Optional[ConfidenceRating] = field(
        default=None,
        metadata={
            "name": "LikelihoodRating",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_resource_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InputResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    model_time: Optional[ModelTime] = field(
        default=None,
        metadata={
            "name": "ModelTime",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    model_domain: Optional[ModelDomain] = field(
        default=None,
        metadata={
            "name": "ModelDomain",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    region_parameter: List[RegionParameter] = field(
        default_factory=list,
        metadata={
            "name": "RegionParameter",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_parameter: List[InputParameter] = field(
        default_factory=list,
        metadata={
            "name": "InputParameter",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_population: List[InputPopulation] = field(
        default_factory=list,
        metadata={
            "name": "InputPopulation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_field: List[InputField] = field(
        default_factory=list,
        metadata={
            "name": "InputField",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_process: List[InputProcess] = field(
        default_factory=list,
        metadata={
            "name": "InputProcess",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Observatory:
    """
    The host (spacecraft, network, facility) for instruments making observations,
    or a family of closely related hosts.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    observatory_group_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ObservatoryGroupID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    location: List[Location] = field(
        default_factory=list,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    operating_span: List[OperatingSpan] = field(
        default_factory=list,
        metadata={
            "name": "OperatingSpan",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Registry:
    """
    A location or facility where resources are cataloged.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    access_url: Optional[AccessUrl] = field(
        default=None,
        metadata={
            "name": "AccessURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Repository:
    """
    A location or facility where resources are stored.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    access_url: Optional[AccessUrl] = field(
        default=None,
        metadata={
            "name": "AccessURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Service:
    """
    A location or facility that can perform a well-defined task.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    access_url: Optional[AccessUrl] = field(
        default=None,
        metadata={
            "name": "AccessURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Software:
    """
    An application which can be installed, built or readily used.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    access_information: List[AccessInformation] = field(
        default_factory=list,
        metadata={
            "name": "AccessInformation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    software_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "SoftwareVersion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    application_interface: List[ApplicationInterface] = field(
        default_factory=list,
        metadata={
            "name": "ApplicationInterface",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    code_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeLanguage",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    prerequisites: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Prerequisites",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    execution_environment: List[ExecutionEnvironment] = field(
        default_factory=list,
        metadata={
            "name": "ExecutionEnvironment",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    input_property: List[InputProperty] = field(
        default_factory=list,
        metadata={
            "name": "InputProperty",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    output_property: List[OutputProperty] = field(
        default_factory=list,
        metadata={
            "name": "OutputProperty",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Structure:
    """
    The organization and relationship of individual values within a quantity.
    """

    size: List[int] = field(
        default_factory=list,
        metadata={
            "name": "Size",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "tokens": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    element: List[Element] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Collection:
    """An aggregation of resources, which may encompass collections of one resource
    type as well as those of mixed types.

    A collection is described as a group. Its parts may also be
    separately described. An example is an experiment which uses the
    data from multiple instruments (or sensors). Another example is a
    research effort that uses a set of display images of the Sun and
    Energetic particle data from the corresponding times for the images,
    and FITS files of AIA images, etc. All the resources that are part
    of the research effort can be described as a Collection. Yet another
    example is a coordinated set of time series used for determining an
    index.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    access_information: List[AccessInformation] = field(
        default_factory=list,
        metadata={
            "name": "AccessInformation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    member: List[Member] = field(
        default_factory=list,
        metadata={
            "name": "Member",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Parameter:
    """A container of information regarding a parameter whose values are part of
    the product.

    Every product contains or can be related to one or more parameters.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    set: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Set",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    parameter_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterKey",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    ucd: Optional[str] = field(
        default=None,
        metadata={
            "name": "UCD",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    cadence: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Cadence",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    cadence_min: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "CadenceMin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    cadence_max: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "CadenceMax",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    units_conversion: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitsConversion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "CoordinateSystem",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    rendering_hints: List[RenderingHints] = field(
        default_factory=list,
        metadata={
            "name": "RenderingHints",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    structure: Optional[Structure] = field(
        default=None,
        metadata={
            "name": "Structure",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_min: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMin",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    valid_max: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidMax",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    fill_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "FillValue",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    field_value: Optional[FieldType] = field(
        default=None,
        metadata={
            "name": "Field",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    particle: Optional[Particle] = field(
        default=None,
        metadata={
            "name": "Particle",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    wave: Optional[Wave] = field(
        default=None,
        metadata={
            "name": "Wave",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    mixed: Optional[Mixed] = field(
        default=None,
        metadata={
            "name": "Mixed",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    support: Optional[Support] = field(
        default=None,
        metadata={
            "name": "Support",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Catalog:
    """A tabular listing of events or observational notes, especially those that
    have utility in aiding a user in locating data.

    Catalogs include lists of events, files in a product, and data
    availability. A Catalog resource is a type of "data product" which
    is a set of data that is uniformly processed and formatted, from one
    or more instruments, typically spanning the full duration of the
    observations of the relevant instrument(s). A data product may
    consist of a collection of granules of successive time spans, but
    may be a single high-level entity.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    access_information: List[AccessInformation] = field(
        default_factory=list,
        metadata={
            "name": "AccessInformation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    provider_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_resource_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderResourceName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderVersion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    instrument_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InstrumentID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    phenomenon_type: List[PhenomenonType] = field(
        default_factory=list,
        metadata={
            "name": "PhenomenonType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    time_span: Optional[TimeSpan] = field(
        default=None,
        metadata={
            "name": "TimeSpan",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_resource_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InputResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    parameter: List[Parameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class DisplayData:
    """A graphical representation of data wherein the underlying numeric values are
    not (readily) accessible for analysis.

    Examples are line plots and spectrograms. A Display Data resource is
    a type of "data product" which is a set of data that is uniformly
    processed and formatted, from one or more instruments, typically
    spanning the full duration of the observations of the relevant
    instrument(s). A data product may consist of a collection of
    granules of successive time spans, but may be a single high-level
    entity.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    access_information: List[AccessInformation] = field(
        default_factory=list,
        metadata={
            "name": "AccessInformation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    processing_level: Optional[ProcessingLevel] = field(
        default=None,
        metadata={
            "name": "ProcessingLevel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_resource_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderResourceName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_processing_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderProcessingLevel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderVersion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    instrument_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InstrumentID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    measurement_type: List[MeasurementType] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    temporal_description: Optional[TemporalDescription] = field(
        default=None,
        metadata={
            "name": "TemporalDescription",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    spectral_range: List[SpectralRange] = field(
        default_factory=list,
        metadata={
            "name": "SpectralRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    display_cadence: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DisplayCadence",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    observed_region: List[Region] = field(
        default_factory=list,
        metadata={
            "name": "ObservedRegion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    spatial_coverage: List[SpatialCoverage] = field(
        default_factory=list,
        metadata={
            "name": "SpatialCoverage",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_resource_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InputResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    parameter: List[Parameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class DisplayOutput:
    """A graphical representation of data wherein the underlying numeric values are
    not (readily) accessible for analysis.

    Examples are line plots and spectrograms. A Display Data resource is
    a type of "data product" which is a set of data that is uniformly
    processed and formatted, from one or more instruments, typically
    spanning the full duration of the observations of the relevant
    instrument(s). A data product may consist of a collection of
    granules of successive time spans, but may be a single high-level
    entity.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    access_information: List[AccessInformation] = field(
        default_factory=list,
        metadata={
            "name": "AccessInformation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    processing_level: Optional[ProcessingLevel] = field(
        default=None,
        metadata={
            "name": "ProcessingLevel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_resource_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderResourceName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_processing_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderProcessingLevel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderVersion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    modeled_instrument_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ModeledInstrumentID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    measurement_type: List[MeasurementType] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    temporal_description: Optional[TemporalDescription] = field(
        default=None,
        metadata={
            "name": "TemporalDescription",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    spatial_description: Optional[SpatialDescription] = field(
        default=None,
        metadata={
            "name": "SpatialDescription",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    spectral_range: List[SpectralRange] = field(
        default_factory=list,
        metadata={
            "name": "SpectralRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    display_cadence: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DisplayCadence",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    modeled_region: List[ModeledRegion] = field(
        default_factory=list,
        metadata={
            "name": "ModeledRegion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_resource_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InputResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    parameter: List[Parameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    model_product: Optional[Product] = field(
        default=None,
        metadata={
            "name": "ModelProduct",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    property: List[Property] = field(
        default_factory=list,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    extension: Optional[Extension] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class NumericalData:
    """Data stored as numerical values in one or more specified formats.

    A Numerical Data resource is a type of "data product" which is a set
    of data that is uniformly processed and formatted, from one or more
    instruments, typically spanning the full duration of the
    observations of the relevant instrument(s). A data product may
    consist of Parameters stored in a collection of granules of
    successive time spans or a single data granule.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    access_information: List[AccessInformation] = field(
        default_factory=list,
        metadata={
            "name": "AccessInformation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    processing_level: Optional[ProcessingLevel] = field(
        default=None,
        metadata={
            "name": "ProcessingLevel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_resource_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderResourceName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_processing_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderProcessingLevel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderVersion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    instrument_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InstrumentID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    measurement_type: List[MeasurementType] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    temporal_description: Optional[TemporalDescription] = field(
        default=None,
        metadata={
            "name": "TemporalDescription",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    spectral_range: List[SpectralRange] = field(
        default_factory=list,
        metadata={
            "name": "SpectralRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    observed_region: List[Region] = field(
        default_factory=list,
        metadata={
            "name": "ObservedRegion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    spatial_coverage: List[SpatialCoverage] = field(
        default_factory=list,
        metadata={
            "name": "SpatialCoverage",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_resource_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InputResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    parameter: List[Parameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class NumericalOutput:
    """Data stored as numerical values in a specified format.

    A Numerical Data resource is a type of "data product" which is a set
    of data that is uniformly processed and formatted, from one or more
    instruments, typically spanning the full duration of the
    observations of the relevant instrument(s). A data product may
    consist of a collection of granules of successive time spans, but
    may be a single high-level entity.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    access_information: List[AccessInformation] = field(
        default_factory=list,
        metadata={
            "name": "AccessInformation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    processing_level: Optional[ProcessingLevel] = field(
        default=None,
        metadata={
            "name": "ProcessingLevel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_resource_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderResourceName",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_processing_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderProcessingLevel",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    provider_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderVersion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    modeled_instrument_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ModeledInstrumentID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    measurement_type: List[MeasurementType] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "min_occurs": 1,
        },
    )
    temporal_description: Optional[TemporalDescription] = field(
        default=None,
        metadata={
            "name": "TemporalDescription",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    spatial_description: Optional[SpatialDescription] = field(
        default=None,
        metadata={
            "name": "SpatialDescription",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    spectral_range: List[SpectralRange] = field(
        default_factory=list,
        metadata={
            "name": "SpectralRange",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    modeled_region: List[ModeledRegion] = field(
        default_factory=list,
        metadata={
            "name": "ModeledRegion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    caveats: Optional[str] = field(
        default=None,
        metadata={
            "name": "Caveats",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_resource_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InputResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    parameter: List[Parameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    model_product: Optional[Product] = field(
        default=None,
        metadata={
            "name": "ModelProduct",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    property: List[Property] = field(
        default_factory=list,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    extension: Optional[Extension] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class OutputParameters:
    """
    A container of information regarding the output parameters of the model run.
    """

    parameter: List[Parameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Model:
    """
    Attributes of a model.
    """

    resource_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
            "pattern": r"[^:]+://[^/]+/.+",
        },
    )
    resource_header: Optional[ResourceHeader] = field(
        default=None,
        metadata={
            "name": "ResourceHeader",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    access_information_optional: List[AccessInformationOptional] = field(
        default_factory=list,
        metadata={
            "name": "AccessInformationOptional",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    versions: Optional[Versions] = field(
        default=None,
        metadata={
            "name": "Versions",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    model_type: Optional[ModelType] = field(
        default=None,
        metadata={
            "name": "ModelType",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    code_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeLanguage",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    temporal_dependence: Optional[Yn] = field(
        default=None,
        metadata={
            "name": "TemporalDependence",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    spatial_description: Optional[SpatialDescription] = field(
        default=None,
        metadata={
            "name": "SpatialDescription",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    modeled_region: List[ModeledRegion] = field(
        default_factory=list,
        metadata={
            "name": "ModeledRegion",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    input_properties: Optional[InputProperties] = field(
        default=None,
        metadata={
            "name": "InputProperties",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    output_parameters: Optional[OutputParameters] = field(
        default=None,
        metadata={
            "name": "OutputParameters",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    model_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModelURL",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )


@dataclass
class Spase:
    """Space Physics Archive Search and Extract (SPASE).

    The outermost container or envelope for SPASE metadata. This
    indicates the start of the SPASE metadata.
    """

    version: Optional[Version] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
            "required": True,
        },
    )
    catalog: List[Catalog] = field(
        default_factory=list,
        metadata={
            "name": "Catalog",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    display_data: List[DisplayData] = field(
        default_factory=list,
        metadata={
            "name": "DisplayData",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    numerical_data: List[NumericalData] = field(
        default_factory=list,
        metadata={
            "name": "NumericalData",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    granule: List[Granule] = field(
        default_factory=list,
        metadata={
            "name": "Granule",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    instrument: List[Instrument] = field(
        default_factory=list,
        metadata={
            "name": "Instrument",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    observatory: List[Observatory] = field(
        default_factory=list,
        metadata={
            "name": "Observatory",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    person: List[Person] = field(
        default_factory=list,
        metadata={
            "name": "Person",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    registry: List[Registry] = field(
        default_factory=list,
        metadata={
            "name": "Registry",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    repository: List[Repository] = field(
        default_factory=list,
        metadata={
            "name": "Repository",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    service: List[Service] = field(
        default_factory=list,
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "name": "Annotation",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    document: List[Document] = field(
        default_factory=list,
        metadata={
            "name": "Document",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    software: List[Software] = field(
        default_factory=list,
        metadata={
            "name": "Software",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    collection: List[Collection] = field(
        default_factory=list,
        metadata={
            "name": "Collection",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    model: List[Model] = field(
        default_factory=list,
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    model_run: List[ModelRun] = field(
        default_factory=list,
        metadata={
            "name": "ModelRun",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    display_output: List[DisplayOutput] = field(
        default_factory=list,
        metadata={
            "name": "DisplayOutput",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    numerical_output: List[NumericalOutput] = field(
        default_factory=list,
        metadata={
            "name": "NumericalOutput",
            "type": "Element",
            "namespace": "http://www.spase-group.org/data/schema",
        },
    )
    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
        },
    )
