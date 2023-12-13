
from typing import  Set, Optional, List
import datetime as dt
from terminusdb_client import Client
from terminusdb_client.woqlschema.woql_schema import (
    DocumentTemplate,
    EnumTemplate,
    WOQLSchema,
    LexicalKey,
)

import pandas as pd
from tqdm import tqdm
import tempfile
import random
schema = WOQLSchema()

class AccessInformation(DocumentTemplate):
	"""Attributes which specify how to access a resource, its availability, storage format, etc."""
	_schema = schema

	repositoryid : str
	availability : Optional['Availability']
	accessrights : Optional['AccessRights']
	accessurl : List['AccessURL']
	format : List['Format']
	encoding : Optional['Encoding']
	accessdirectorytemplate : Optional[str]
	accessfilenametemplate : Optional[str]
	dataextent : Optional['DataExtent']
	acknowledgement : Optional[str]

class AccessInformationOptional(DocumentTemplate):
	"""Attributes of the resource which pertain to how to accessing the resource, availability and storage format. This resource class is an exact copy of the AccessInformation container. However, as its name suggests, AccessInformationOptional is not a required element."""
	_schema = schema

	repositoryid : str
	availability : Optional['Availability']
	accessrights : Optional['AccessRights']
	accessurl : List['AccessURL']
	format : List['Format']
	encoding : Optional['Encoding']
	accessdirectorytemplate : Optional[str]
	accessfilenametemplate : Optional[str]
	dataextent : Optional['DataExtent']
	acknowledgement : Optional[str]

class AccessURL(DocumentTemplate):
	"""Attributes of the method for accessing a resource including a URL, name and description."""
	_schema = schema

	name : Optional[str]
	url : str
	style : Optional['Style']
	productkey : Set[str]
	description : Optional[str]
	language : Optional[str]

class Annotation(DocumentTemplate):
	"""Information which is explanatory or descriptive which is associated with another resource."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	imageurl : Optional[str]
	annotationtype : 'AnnotationType'
	phenomenontype : Set['PhenomenonType']
	classificationmethod : Optional['ClassificationMethod']
	confidencerating : Optional['ConfidenceRating']
	timespan : Set['TimeSpan']
	observationextent : Set['ObservationExtent']
	extension : Set[str]

class Association(DocumentTemplate):
	"""Attributes of a relationship a resource has with another resource."""
	_schema = schema

	associationid : str
	associationtype : 'AssociationType'
	note : Optional[str]

class AzimuthalAngleRange(DocumentTemplate):
	"""The range of possible azimuthal angles for a group of energy observations. Default units are degrees."""
	_schema = schema

	low : float
	high : float
	units : str
	bin : Set['Bin']

class Bin(DocumentTemplate):
	"""A grouping of observations according to a band or window of a common attribute."""
	_schema = schema

	bandname : Optional[str]
	low : float
	high : float

class BoundaryConditions(DocumentTemplate):
	"""Parameters associated to the model boundaries."""
	_schema = schema

	particleboundary : Optional[str]
	fieldboundary : Optional[str]

class Catalog(DocumentTemplate):
	"""A tabular listing of events or observational notes, especially those that have utility in aiding a user in locating data. Catalogs include lists of events, files in a product, and data availability. A Catalog resource is a type of "data product" which is a set of data that is uniformly processed and formatted, from one or more instruments, typically spanning the full duration of the observations of the relevant instrument(s). A data product may consist of a collection of granules of successive time spans, but may be a single high-level entity."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	accessinformation : List['AccessInformation']
	providername : Optional[str]
	providerresourcename : Optional[str]
	providerversion : Optional[str]
	instrumentid : Set[str]
	phenomenontype : List['PhenomenonType']
	timespan : Optional['TimeSpan']
	caveats : Optional[str]
	keyword : Set[str]
	inputresourceid : Set[str]
	parameter : Set['Parameter']
	extension : Set[str]

class Checksum(DocumentTemplate):
	"""A computed value that is dependent upon the contents of a digital data object. Primarily used to check whether errors or alterations have occurred during the transmission or storage of a data object."""
	_schema = schema

	hashvalue : str
	hashfunction : 'HashFunction'

class Collection(DocumentTemplate):
	"""An aggregation of resources, which may encompass collections of one resource type as well as those of mixed types. A collection is described as a group. Its parts may also be separately described. An example is an experiment which uses the data from multiple instruments (or sensors). Another example is a research effort that uses a set of display images of the Sun and Energetic particle data from the corresponding times for the images, and FITS files of AIA images, etc. All the resources that are part of the research effort can be described as a Collection. Yet another example is a coordinated set of time series used for determining an index."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	accessinformation : List['AccessInformation']
	member : List['Member']
	extension : Set[str]

class Contact(DocumentTemplate):
	"""The person or organization who may be able to provide special assistance or serve as a channel for communication for additional information about a resource."""
	_schema = schema

	personid : str
	role : List['Role']
	startdate : Optional[dt.datetime]
	stopdate : Optional[dt.datetime]
	note : Optional[str]

class CoordinateSystem(DocumentTemplate):
	"""The specification of the orientation of a set of (typically) orthogonal base axes."""
	_schema = schema

	coordinaterepresentation : 'CoordinateRepresentation'
	coordinatesystemname : 'CoordinateSystemName'

class DataExtent(DocumentTemplate):
	"""The area of storage in a file system required to store the contents of a resource. By default, the data extent is expressed in bytes."""
	_schema = schema

	quantity : float
	units : Optional[str]
	per : Optional[dt.timedelta]

class DiagnosisTimeStep(DocumentTemplate):
	"""Time at which a diagnosis is performed and quantity saved."""
	_schema = schema

	timestart : dt.datetime
	duration : dt.timedelta
	savedquantity : Set['SavedQuantity']

class DisplayData(DocumentTemplate):
	"""A graphical representation of data wherein the underlying numeric values are not (readily) accessible for analysis. Examples are line plots and spectrograms. A Display Data resource is a type of "data product" which is a set of data that is uniformly processed and formatted, from one or more instruments, typically spanning the full duration of the observations of the relevant instrument(s). A data product may consist of a collection of granules of successive time spans, but may be a single high-level entity."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	accessinformation : List['AccessInformation']
	processinglevel : Optional['ProcessingLevel']
	providername : Optional[str]
	providerresourcename : Optional[str]
	providerprocessinglevel : Optional[str]
	providerversion : Optional[str]
	instrumentid : Set[str]
	measurementtype : List['MeasurementType']
	temporaldescription : Optional['TemporalDescription']
	spectralrange : Set['SpectralRange']
	displaycadence : Optional[dt.timedelta]
	observedregion : Set['ObservedRegion']
	spatialcoverage : List['SpatialCoverage']
	caveats : Optional[str]
	keyword : Set[str]
	inputresourceid : Set[str]
	parameter : Set['Parameter']
	extension : Set[str]

class DisplayOutput(DocumentTemplate):
	"""A graphical representation of data wherein the underlying numeric values are not (readily) accessible for analysis. Examples are line plots and spectrograms. A Display Data resource is a type of "data product" which is a set of data that is uniformly processed and formatted, from one or more instruments, typically spanning the full duration of the observations of the relevant instrument(s). A data product may consist of a collection of granules of successive time spans, but may be a single high-level entity."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	accessinformation : List['AccessInformation']
	processinglevel : Optional['ProcessingLevel']
	providerresourcename : Optional[str]
	providerprocessinglevel : Optional[str]
	providerversion : Optional[str]
	modeledinstrumentid : Set[str]
	measurementtype : List['MeasurementType']
	temporaldescription : Optional['TemporalDescription']
	spatialdescription : Optional['SpatialDescription']
	spectralrange : Set['SpectralRange']
	displaycadence : Optional[dt.timedelta]
	modeledregion : Set['ModeledRegion']
	caveats : Optional[str]
	keyword : Set[str]
	inputresourceid : Set[str]
	parameter : Set['Parameter']
	modelproduct : Optional['ModelProduct']
	property : Set['Property']
	extension : Optional[str]

class Document(DocumentTemplate):
	"""A set of information designed and presented as an individual entity. A document may contain plain or formatted text, in-line graphics, sound, other multimedia data, or hypermedia references. A Document resource is intended for use on digital objects that have no other identifier (e.g., DOI or ISBN)."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	accessinformation : List['AccessInformation']
	keyword : Set[str]
	documenttype : 'DocumentType'
	mimetype : str
	inputresourceid : Set[str]

class Element(DocumentTemplate):
	"""A component or individual unit of a multiple value quantity such as an array or vector."""
	_schema = schema

	name : str
	qualifier : Set['Qualifier']
	
	parameterkey : Optional[str]
	units : Optional[str]
	unitsconversion : Optional[str]
	validmin : Optional[str]
	validmax : Optional[str]
	fillvalue : Optional[str]
	renderinghints : Optional['RenderingHints']

class ElementBoundary(DocumentTemplate):
	"""Parameters associated to the model boundaries."""
	_schema = schema

	caveats : Optional[str]
	frontwall : Optional[str]
	backwall : Optional[str]
	sidewall : Optional[str]
	obstacle : Optional[str]

class EnergyRange(DocumentTemplate):
	"""The minimum and maximum energy values of the particles represented by a given physical parameter description."""
	_schema = schema

	low : float
	high : float
	units : str
	bin : Set['Bin']

class ExecutionEnvironment(DocumentTemplate):
	"""An execution platform for software which includes an operating system and necessary hardware."""
	_schema = schema

	operatingsystem : str
	installer : 'Installer'
	cores : Optional[float]
	storage : Optional[str]
	memory : Optional[str]

class Field(DocumentTemplate):
	"""The space around a radiating body within which its electromagnetic attributes can exert force on another similar body that is not in direct contact."""
	_schema = schema

	qualifier : Set['Qualifier']
	fieldquantity : 'FieldQuantity'
	frequencyrange : Optional['FrequencyRange']

class FrequencyRange(DocumentTemplate):
	"""The range of possible values for the observed frequency."""
	_schema = schema

	spectralrange : Optional['SpectralRange']
	low : float
	high : float
	units : str
	bin : Set['Bin']

class Funding(DocumentTemplate):
	"""The source of financial support (funding) for the resource."""
	_schema = schema

	agency : str
	project : str
	awardnumber : Optional[str]

class Granule(DocumentTemplate):
	"""An accessible portion of another resource. A Granule may be composed of one or more physical pieces (files) which are considered inseparable. For example, a data storage format that maintains metadata and binary data in separate, but tightly coupled files. Granules should not be used to group files that have simple relationships or which are associated through a parent resource. For example, each file containing a time interval data for a Numerical Data resource would each be considered a Granule. The ParentID of a Granule resource must be a NumericalData resource. The attributes of a Granule supersede the corresponding attributes in the NumericalData resource."""
	_schema = schema

	resourceid : str
	releasedate : dt.datetime
	expirationdate : Optional[dt.datetime]
	parentid : str
	priorid : Set[str]
	startdate : dt.datetime
	stopdate : dt.datetime
	spatialcoverage : List['SpatialCoverage']
	source : List['Source']
	regionbegin : str
	regionend : str

class InformationURL(DocumentTemplate):
	"""Attributes of the method of acquiring additional information."""
	_schema = schema

	name : Optional[str]
	url : str
	description : Optional[str]
	language : Optional[str]

class InputField(DocumentTemplate):
	"""Parameters associated to a field imposed in the model."""
	_schema = schema

	name : str
	set : Set[str]
	parameterkey : Optional[str]
	description : Optional[str]
	caveats : Optional[str]
	modeledregion : Set['ModeledRegion']
	coordinatesystem : Optional['CoordinateSystem']
	qualifier : Set['Qualifier']
	fieldquantity : 'FieldQuantity'
	units : Optional[str]
	unitsconversion : Optional[str]
	inputlabel : Optional[str]
	fieldvalue : Optional[str]
	inputtableurl : Optional[str]
	validmin : Optional[str]
	validmax : Optional[str]
	fieldmodel : Optional[str]
	modelurl : Optional[str]

class InputParameter(DocumentTemplate):
	"""A container of information regarding an input parameter of the model run."""
	_schema = schema

	name : str
	description : Optional[str]
	caveats : Optional[str]
	modeledregion : Set['ModeledRegion']
	qualifier : Set['Qualifier']
	inputtableurl : Set[str]
	parameterquantity : Optional['ParameterQuantity']
	property : List['Property']

class InputPopulation(DocumentTemplate):
	"""A container element that specifies the characteristics of a particle population used as input to a model model."""
	_schema = schema

	name : str
	set : Set[str]
	parameterkey : Optional[str]
	description : Optional[str]
	caveats : Optional[str]
	modeledregion : Set['ModeledRegion']
	qualifier : Set['Qualifier']
	particletype : Optional['ParticleType']
	chemicalformula : Optional[str]
	atomicnumber : Optional[float]
	populationmassnumber : Optional[str]
	populationchargestate : Optional[float]
	populationdensity : Optional[str]
	populationtemperature : Optional[str]
	populationflowspeed : Optional[str]
	distribution : Optional[str]
	productionrate : Optional[str]
	totalproductionrate : Optional[str]
	inputtableurl : Optional[str]
	densityprofile : Optional[str]
	modelurl : Optional[str]

class InputProcess(DocumentTemplate):
	"""Parameters associated to a chemical process happening in the model."""
	_schema = schema

	name : str
	set : Set[str]
	parameterkey : Optional[str]
	description : Optional[str]
	caveats : Optional[str]
	modeledregion : Set['ModeledRegion']
	processtype : 'ProcessType'
	units : Optional[str]
	unitsconversion : Optional[str]
	processcoefficient : Optional[str]
	processcoefftype : Optional['ProcessCoeffType']
	processmodel : Optional[str]
	modelurl : Optional[str]

class InputProperties(DocumentTemplate):
	"""Properties."""
	_schema = schema

	property : Set['Property']

class InputProperty(DocumentTemplate):
	"""A container of attributes regarding an input property of an application."""
	_schema = schema

	name : str
	description : str
	caveats : Optional[str]
	units : Optional[str]
	validmin : Optional[str]
	validmax : Optional[str]

class Installer(DocumentTemplate):
	"""A piece of software that installs a program or package on a system."""
	_schema = schema

	availability : Optional['Availability']
	accessrights : Optional['AccessRights']
	acknowledgement : Optional[str]
	url : str

class Instrument(DocumentTemplate):
	"""A device that makes measurements used to characterize a physical phenomenon, or a family of like devices."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	instrumenttype : List['InstrumentType']
	instrumentgroupid : Optional[str]
	investigationname : List[str]
	operatingspan : Optional['OperatingSpan']
	observatoryid : str
	caveats : Optional[str]
	extension : Set[str]

class Location(DocumentTemplate):
	"""A position in space definable by a regional referencing system and geographic coordinates."""
	_schema = schema

	observatoryregion : List['ObservatoryRegion']
	coordinatesystemname : Optional['CoordinateSystemName']
	latitude : Optional[float]
	longitude : Optional[float]
	elevation : Optional[float]

class MassRange(DocumentTemplate):
	"""The range of possible mass for a group of particle observations."""
	_schema = schema

	low : float
	high : float
	units : str
	bin : Set['Bin']

class Member(DocumentTemplate):
	"""A constituent part of a collection. A Member is of a one of the supported resource types and in referenced by an identifier. Details about the member are part of its respective resource description."""
	_schema = schema

	resourcename : List[str]
	description : Optional[str]
	memberid : Optional[str]
	startdate : Optional[dt.datetime]
	stopdate : Optional[dt.datetime]
	spatialcoverage : Optional['SpatialCoverage']

class Mixed(DocumentTemplate):
	"""A parameter derived from more than one type of parameter. For example, plasma beta, the ratio of plasma particle energy density to the energy density of the magnetic field permeating the plasma, is mixed."""
	_schema = schema

	mixedquantity : 'MixedQuantity'
	particletype : Set['ParticleType']
	qualifier : Set['Qualifier']

class Model(DocumentTemplate):
	"""Attributes of a model."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	accessinformationoptional : Set['AccessInformationOptional']
	versions : Optional['Versions']
	modeltype : 'ModelType'
	codelanguage : Optional[str]
	temporaldependence : Optional['TemporalDependence']
	spatialdescription : Optional['SpatialDescription']
	modeledregion : Set['ModeledRegion']
	inputproperties : Optional['InputProperties']
	outputparameters : Optional['OutputParameters']
	modelurl : Optional[str]

class ModelDomain(DocumentTemplate):
	"""Parameters associated to the model spatial domain."""
	_schema = schema

	coordinatesystem : 'CoordinateSystem'
	description : Optional[str]
	caveats : Optional[str]
	spatialdimension : int
	velocitydimension : Optional[int]
	fielddimension : Optional[int]
	units : str
	unitsconversion : Optional[str]
	coordinateslabel : Optional[str]
	validmin : Optional[str]
	validmax : Optional[str]
	gridstructure : Optional[str]
	gridcellsize : Optional[str]
	symmetry : Optional['Symmetry']
	boundaryconditions : Optional['BoundaryConditions']

class ModelRun(DocumentTemplate):
	"""Description of a model run, including the code ID, the run spatial and temporal description, and all the relevant inputs."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	accessinformation : Set['AccessInformation']
	providerresourcename : Optional[str]
	providerprocessinglevel : Optional[str]
	providerversion : Optional[str]
	modelspecification : Optional['ModelSpecification']
	temporaldependence : Optional['TemporalDependence']
	modeledregion : List['ModeledRegion']
	likelihoodrating : Optional['LikelihoodRating']
	caveats : Optional[str]
	keyword : Set[str]
	inputresourceid : Set[str]
	modeltime : Optional['ModelTime']
	modeldomain : Optional['ModelDomain']
	regionparameter : List['RegionParameter']
	inputparameter : List['InputParameter']
	inputpopulation : List['InputPopulation']
	inputfield : List['InputField']
	inputprocess : List['InputProcess']
	extension : Set[str]

class ModelSpecification(DocumentTemplate):
	"""Descriptor of model specifications: type of numerical scheme, versions, etc."""
	_schema = schema

	modelid : Optional[str]
	versiontag : Optional[str]

class ModelTime(DocumentTemplate):
	"""Parameters associated to the model time."""
	_schema = schema

	description : Optional[str]
	caveats : Optional[str]
	duration : Optional[dt.timedelta]
	timestart : Optional[dt.datetime]
	timestop : Optional[dt.datetime]
	timestep : Optional[dt.timedelta]
	diagnosistimestep : Optional['DiagnosisTimeStep']

class ModelVersion(DocumentTemplate):
	"""The version number of the model."""
	_schema = schema

	versiontag : Optional[str]
	releasedate : dt.datetime
	description : Optional[str]
	caveats : Optional[str]

class NumericalData(DocumentTemplate):
	"""Data stored as numerical values in one or more specified formats. A Numerical Data resource is a type of "data product" which is a set of data that is uniformly processed and formatted, from one or more instruments, typically spanning the full duration of the observations of the relevant instrument(s). A data product may consist of Parameters stored in a collection of granules of successive time spans or a single data granule."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	accessinformation : List['AccessInformation']
	processinglevel : Optional['ProcessingLevel']
	providername : Optional[str]
	providerresourcename : Optional[str]
	providerprocessinglevel : Optional[str]
	providerversion : Optional[str]
	instrumentid : Set[str]
	measurementtype : List['MeasurementType']
	temporaldescription : Optional['TemporalDescription']
	spectralrange : Set['SpectralRange']
	observedregion : Set['ObservedRegion']
	spatialcoverage : Set['SpatialCoverage']
	caveats : Optional[str]
	keyword : Set[str]
	inputresourceid : Set[str]
	parameter : Set['Parameter']
	extension : Set[str]

class NumericalOutput(DocumentTemplate):
	"""Data stored as numerical values in a specified format. A Numerical Data resource is a type of "data product" which is a set of data that is uniformly processed and formatted, from one or more instruments, typically spanning the full duration of the observations of the relevant instrument(s). A data product may consist of a collection of granules of successive time spans, but may be a single high-level entity."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	accessinformation : List['AccessInformation']
	processinglevel : Optional['ProcessingLevel']
	providerresourcename : Optional[str]
	providerprocessinglevel : Optional[str]
	providerversion : Optional[str]
	modeledinstrumentid : Set[str]
	measurementtype : List['MeasurementType']
	temporaldescription : Optional['TemporalDescription']
	spatialdescription : Optional['SpatialDescription']
	spectralrange : Set['SpectralRange']
	modeledregion : Set['ModeledRegion']
	caveats : Optional[str]
	keyword : Set[str]
	inputresourceid : Set[str]
	parameter : Set['Parameter']
	modelproduct : Optional['ModelProduct']
	property : Set['Property']
	extension : Optional[str]

class ObservationExtent(DocumentTemplate):
	"""The spatial area encompassed by an observation."""
	_schema = schema

	observedregion : Optional['ObservedRegion']
	startlocation : str
	stoplocation : str
	note : Set[str]

class Observatory(DocumentTemplate):
	"""The host (spacecraft, network, facility) for instruments making observations, or a family of closely related hosts."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	observatorygroupid : Set[str]
	location : List['Location']
	operatingspan : List['OperatingSpan']
	extension : Set[str]

class OperatingSpan(DocumentTemplate):
	"""The interval in time from the first point at which an instrument or spacecraft was producing and sending data until the last such time, ignoring possible gaps."""
	_schema = schema

	startdate : dt.datetime
	stopdate : Optional[dt.datetime]
	note : Set[str]

class OutputParameters(DocumentTemplate):
	"""A container of information regarding the output parameters of the model run."""
	_schema = schema

	parameter : Set['Parameter']

class OutputProperty(DocumentTemplate):
	"""A container of attributes regarding an output property of an application."""
	_schema = schema

	name : str
	description : str
	caveats : Optional[str]
	units : Optional[str]
	validmin : Optional[str]
	validmax : Optional[str]

class Parameter(DocumentTemplate):
	"""A container of information regarding a parameter whose values are part of the product. Every product contains or can be related to one or more parameters."""
	_schema = schema

	name : str
	set : Set[str]
	parameterkey : Optional[str]
	description : Optional[str]
	ucd : Optional[str]
	caveats : Optional[str]
	cadence : Optional[dt.timedelta]
	cadencemin : Optional[dt.timedelta]
	cadencemax : Optional[dt.timedelta]
	units : Optional[str]
	unitsconversion : Optional[str]
	coordinatesystem : Optional['CoordinateSystem']
	renderinghints : Set['RenderingHints']
	structure : Optional['Structure']
	validmin : Optional[str]
	validmax : Optional[str]
	fillvalue : Optional[str]
	field : 'Field'
	particle : 'Particle'
	wave : 'Wave'
	mixed : 'Mixed'
	support : 'Support'

class Particle(DocumentTemplate):
	"""A description of the types of particles observed in the measurement. This includes both direct observations and inferred observations."""
	_schema = schema

	particletype : List['ParticleType']
	qualifier : Set['Qualifier']
	particlequantity : 'ParticleQuantity'
	atomicnumber : Set[float]
	energyrange : Optional['EnergyRange']
	azimuthalanglerange : Optional['AzimuthalAngleRange']
	polaranglerange : Optional['PolarAngleRange']
	massrange : Optional['MassRange']
	pitchanglerange : Optional['PitchAngleRange']
	chemicalformula : Optional[str]
	population : Optional[str]
	populationmassnumber : Optional[str]
	populationchargestate : Optional[float]

class Person(DocumentTemplate):
	"""An individual human being."""
	_schema = schema

	resourceid : str
	releasedate : Optional[dt.datetime]
	personname : Optional[str]
	organizationname : str
	address : Optional[str]
	email : Set[str]
	phonenumber : Set[str]
	faxnumber : Optional[str]
	orcidentifier : Optional[str]
	note : Optional[str]
	extension : Set[str]

class PitchAngleRange(DocumentTemplate):
	"""The range of possible pitch angles for a group of particle observations."""
	_schema = schema

	low : float
	high : float
	units : str
	bin : Set['Bin']

class PolarAngleRange(DocumentTemplate):
	"""The range of possible polar angles for a group of energy observations. Defaults units are degrees."""
	_schema = schema

	low : float
	high : float
	units : str
	bin : Set['Bin']

class Property(DocumentTemplate):
	"""A container of attributes regarding the property of an application."""
	_schema = schema

	name : Optional[str]
	description : Optional[str]
	caveats : Optional[str]
	propertyquantity : 'PropertyQuantity'
	qualifier : Set['Qualifier']
	units : Optional[str]
	unitsconversion : Optional[str]
	propertylabel : Optional[str]
	propertyvalue : Optional[str]
	propertytableurl : Optional[str]
	validmin : Optional[str]
	validmax : Optional[str]
	propertymodel : Optional[str]
	modelurl : Optional[str]

class PublicationInfo(DocumentTemplate):
	"""Information required to mint a DOI for the resource being described in SPASE."""
	_schema = schema

	title : Optional[str]
	authors : str
	publicationdate : dt.datetime
	publishedby : str
	landingpageurl : Optional[str]

class RegionParameter(DocumentTemplate):
	"""Radius of the Region in the model."""
	_schema = schema

	modeledregion : Optional['ModeledRegion']
	description : Optional[str]
	caveats : Optional[str]
	radius : Optional[str]
	sublongitude : Optional[str]
	period : Optional[str]
	objectmass : Optional[str]
	inputtableurl : Optional[str]
	property : Set['Property']

class Registry(DocumentTemplate):
	"""A location or facility where resources are cataloged."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	accessurl : 'AccessURL'
	extension : Set[str]

class RenderingHints(DocumentTemplate):
	"""Attributes to aid in the rendering of parameter."""
	_schema = schema

	displaytype : Optional['DisplayType']
	axislabel : Optional[str]
	renderingaxis : Optional['RenderingAxis']
	
	valueformat : Optional[str]
	scalemin : Optional[float]
	scalemax : Optional[float]
	scaletype : Optional['ScaleType']

class Repository(DocumentTemplate):
	"""A location or facility where resources are stored."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	accessurl : 'AccessURL'
	extension : Set[str]

class ResourceHeader(DocumentTemplate):
	"""Attributes of a resource which pertain to the provider of the resource and descriptive information about the resource."""
	_schema = schema

	resourcename : str
	alternatename : Set[str]
	doi : Optional[str]
	releasedate : dt.datetime
	revisionhistory : Optional['RevisionHistory']
	expirationdate : Optional[dt.datetime]
	description : str
	acknowledgement : Optional[str]
	publicationinfo : Optional['PublicationInfo']
	funding : Set['Funding']
	contact : List['Contact']
	informationurl : Set['InformationURL']
	association : Set['Association']
	priorid : Set[str]

class RevisionEvent(DocumentTemplate):
	"""A specific change that improves or upgrades."""
	_schema = schema

	releasedate : dt.datetime
	note : str

class RevisionHistory(DocumentTemplate):
	"""A history of changes that improve or upgrade."""
	_schema = schema

	revisionevent : List['RevisionEvent']

class Service(DocumentTemplate):
	"""A location or facility that can perform a well-defined task."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	accessurl : 'AccessURL'
	extension : Set[str]

class Software(DocumentTemplate):
	"""An application which can be installed, built or readily used."""
	_schema = schema

	resourceid : str
	resourceheader : 'ResourceHeader'
	accessinformation : Set['AccessInformation']
	softwareversion : Optional[str]
	applicationinterface : Set['ApplicationInterface']
	codelanguage : Optional[str]
	prerequisites : List[str]
	executionenvironment : List['ExecutionEnvironment']
	inputproperty : Set['InputProperty']
	outputproperty : Set['OutputProperty']

class Source(DocumentTemplate):
	"""The location and attributes of an object."""
	_schema = schema

	sourcetype : 'SourceType'
	url : str
	mirrorurl : Set[str]
	checksum : Optional['Checksum']
	dataextent : Optional['DataExtent']

class Spase(DocumentTemplate):
	"""Space Physics Archive Search and Extract (SPASE). The outermost container or envelope for SPASE metadata. This indicates the start of the SPASE metadata."""
	_schema = schema

	version : str
	catalog : List['Catalog']
	displaydata : List['DisplayData']
	numericaldata : List['NumericalData']
	granule : List['Granule']
	instrument : List['Instrument']
	observatory : List['Observatory']
	person : List['Person']
	registry : List['Registry']
	repository : List['Repository']
	service : List['Service']
	annotation : List['Annotation']
	document : List['Document']
	software : List['Software']
	collection : List['Collection']
	model : List['Model']
	modelrun : List['ModelRun']
	displayoutput : List['DisplayOutput']
	numericaloutput : List['NumericalOutput']

class SpatialCoverage(DocumentTemplate):
	"""A region of space defined by the latitude, longitude and altitude in a geographic coordinate system."""
	_schema = schema

	coordinatesystem : 'CoordinateSystem'
	centerlatitude : Optional[str]
	northernmostlatitude : Optional[str]
	southernmostlatitude : Optional[str]
	centerlongitude : Optional[str]
	easternmostlongitude : Optional[str]
	westernmostlongitude : Optional[str]
	centerelevation : Optional[str]
	minimumelevation : Optional[str]
	maximumelevation : Optional[str]
	acknowledgement : Optional[str]
	description : Optional[str]

class SpatialDescription(DocumentTemplate):
	"""A characterization of the spatial extent over which the measurement was taken."""
	_schema = schema

	dimension : int
	coordinatesystem : 'CoordinateSystem'
	units : str
	unitsconversion : Optional[str]
	coordinateslabel : Optional[str]
	cutsdescription : str
	cubesdescription : str
	planenormalvector : str
	planepoint : str
	regionbegin : str
	regionend : str
	step : Optional[str]

class Structure(DocumentTemplate):
	"""The organization and relationship of individual values within a quantity."""
	_schema = schema

	
	description : Optional[str]
	element : Set['Element']

class Support(DocumentTemplate):
	"""Information useful in understanding the context of an observation, typically observed or measured coincidentally with a physical observation."""
	_schema = schema

	qualifier : Set['Qualifier']
	supportquantity : 'SupportQuantity'

class TemporalDescription(DocumentTemplate):
	"""A characterization of the time over which the measurement was taken."""
	_schema = schema

	timespan : 'TimeSpan'
	cadence : Optional[dt.timedelta]
	cadencemin : Optional[dt.timedelta]
	cadencemax : Optional[dt.timedelta]
	exposure : Optional[dt.timedelta]
	exposuremin : Optional[dt.timedelta]
	exposuremax : Optional[dt.timedelta]

class TimeSpan(DocumentTemplate):
	"""The duration of an interval in time."""
	_schema = schema

	startdate : dt.datetime
	stopdate : dt.datetime
	relativestopdate : dt.timedelta
	note : Set[str]

class Versions(DocumentTemplate):
	"""A container of one or more sets of version information."""
	_schema = schema

	modelversion : Set['ModelVersion']

class Wave(DocumentTemplate):
	"""Periodic or quasi-periodic (AC) variations of physical quantities in time and space, capable of propagating or being trapped within particular regimes."""
	_schema = schema

	wavetype : Optional['WaveType']
	qualifier : Set['Qualifier']
	wavequantity : 'WaveQuantity'
	energyrange : Optional['EnergyRange']
	frequencyrange : Optional['FrequencyRange']
	wavelengthrange : Optional['WavelengthRange']

class WavelengthRange(DocumentTemplate):
	"""The range of possible values for the observed wavelength."""
	_schema = schema

	spectralrange : Optional['SpectralRange']
	low : float
	high : float
	units : str
	bin : Set['Bin']

 #enum templates:
class AccessRights(EnumTemplate):
	"""Permissions granted or denied by the host of a product to allow other users to access and use the resource."""
	_schema = schema
	
	
	Open = 'Open'
	PartiallyRestricted = 'PartiallyRestricted'
	Restricted = 'Restricted'
class AdiabaticInvariant(EnumTemplate):
	"""A property of a physical system usually related to periodic phenomena that remains constant under slowly varying conditions."""
	_schema = schema
	
	
	MagneticMoment = 'MagneticMoment'
	BounceMotion = 'BounceMotion'
	DriftMotion = 'DriftMotion'
class AnnotationType(EnumTemplate):
	"""A classification for an annotation."""
	_schema = schema
	
	
	Anomaly = 'Anomaly'
	Event = 'Event'
	Feature = 'Feature'
class ApplicationInterface(EnumTemplate):
	"""The type of interface for the application."""
	_schema = schema
	
	
	CLI = 'CLI'
	GUI = 'GUI'
	API = 'API'
class AssociationType(EnumTemplate):
	"""A characterization of the role or purpose of an associated resource."""
	_schema = schema
	
	
	ChildEventOf = 'ChildEventOf'
	DerivedFrom = 'DerivedFrom'
	ObservedBy = 'ObservedBy'
	Other = 'Other'
	PartOf = 'PartOf'
	RevisionOf = 'RevisionOf'
class Availability(EnumTemplate):
	"""An indication of the method or service which may be used to access the resource."""
	_schema = schema
	
	
	Offline = 'Offline'
	Online = 'Online'
class ClassificationMethod(EnumTemplate):
	"""The technique used to determine the characteristics of an object."""
	_schema = schema
	
	
	Automatic = 'Automatic'
	Inferred = 'Inferred'
	Inspection = 'Inspection'
class Component(EnumTemplate):
	"""Projection of a vector along one of the base axes of a coordinate system."""
	_schema = schema
	
	
	I = 'I'
	J = 'J'
	K = 'K'
class ConfidenceRating(EnumTemplate):
	"""A classification of the certainty of an assertion."""
	_schema = schema
	
	
	Probable = 'Probable'
	Strong = 'Strong'
	Unlikely = 'Unlikely'
	Weak = 'Weak'
class CoordinateRepresentation(EnumTemplate):
	"""The method or form for specifying a given point or vector in a given coordinate system."""
	_schema = schema
	
	
	Cartesian = 'Cartesian'
	Cylindrical = 'Cylindrical'
	Spherical = 'Spherical'
class CoordinateSystemName(EnumTemplate):
	"""Identifies the coordinate system in which the position, direction or observation has been expressed."""
	_schema = schema
	
	
	Carrington = 'Carrington'
	CGM = 'CGM'
	CSO = 'CSO'
	DM = 'DM'
	ECD = 'ECD'
	ECEF = 'ECEF'
	ENP = 'ENP'
	GEI = 'GEI'
	GEO = 'GEO'
	GPHIO = 'GPHIO'
	GSE = 'GSE'
	GSEQ = 'GSEQ'
	GSM = 'GSM'
	HAE = 'HAE'
	HCC = 'HCC'
	HCI = 'HCI'
	HCR = 'HCR'
	HEE = 'HEE'
	HEEQ = 'HEEQ'
	HERTN = 'HERTN'
	HG = 'HG'
	HGI = 'HGI'
	HGRTN = 'HGRTN'
	HPC = 'HPC'
	HPR = 'HPR'
	HSM = 'HSM'
	J2000 = 'J2000'
	JSM = 'JSM'
	JSO = 'JSO'
	KSM = 'KSM'
	KSO = 'KSO'
	LGM = 'LGM'
	MAG = 'MAG'
	MFA = 'MFA'
	MSO = 'MSO'
	RTN = 'RTN'
	SC = 'SC'
	SE = 'SE'
	SM = 'SM'
	SpacecraftOrbitPlane = 'SpacecraftOrbitPlane'
	SR = 'SR'
	SR2 = 'SR2'
	SSE = 'SSE'
	SSE_L = 'SSE_L'
	TIIS = 'TIIS'
	VSO = 'VSO'
	WGS84 = 'WGS84'
class DirectionAngle(EnumTemplate):
	"""The angle between a position vector or measured vector (or one of its projections onto a plane) and one of the base axes of the coordinate system."""
	_schema = schema
	
	
	AzimuthAngle = 'AzimuthAngle'
	ElevationAngle = 'ElevationAngle'
	PolarAngle = 'PolarAngle'
class DirectionCosine(EnumTemplate):
	"""The cosine of the angle between two vectors usually between a vector and one of the basis axes defining a Cartesian coordinate system. Three angles and thus three direction cosines are required to define a vector direction in a 3-D Euclidean space."""
	_schema = schema
	
	
	I = 'I'
	J = 'J'
	K = 'K'
class DisplayType(EnumTemplate):
	"""The general styling or type of plot that is suitable for the variable."""
	_schema = schema
	
	
	Image = 'Image'
	Plasmagram = 'Plasmagram'
	Spectrogram = 'Spectrogram'
	StackPlot = 'StackPlot'
	TimeSeries = 'TimeSeries'
	WaveForm = 'WaveForm'
class DocumentType(EnumTemplate):
	"""A characterization of the content, purpose, or style of the document."""
	_schema = schema
	
	
	Convention = 'Convention'
	Other = 'Other'
	Policy = 'Policy'
	Poster = 'Poster'
	Presentation = 'Presentation'
	Report = 'Report'
	Specification = 'Specification'
	TechnicalNote = 'TechnicalNote'
	WhitePaper = 'WhitePaper'
class Earth(EnumTemplate):
	"""The third planet from the Sun in our solar system."""
	_schema = schema
	
	
	Magnetosheath = 'Magnetosheath'
	Magnetosphere = 'Magnetosphere'
	Magnetosphere_Magnetotail = 'Magnetosphere.Magnetotail'
	Magnetosphere_Main = 'Magnetosphere.Main'
	Magnetosphere_Plasmasphere = 'Magnetosphere.Plasmasphere'
	Magnetosphere_Polar = 'Magnetosphere.Polar'
	Magnetosphere_RadiationBelt = 'Magnetosphere.RadiationBelt'
	Magnetosphere_RingCurrent = 'Magnetosphere.RingCurrent'
	Moon = 'Moon'
	NearSurface = 'NearSurface'
	NearSurface_Atmosphere = 'NearSurface.Atmosphere'
	NearSurface_AuroralRegion = 'NearSurface.AuroralRegion'
	NearSurface_EquatorialRegion = 'NearSurface.EquatorialRegion'
	NearSurface_Ionosphere = 'NearSurface.Ionosphere'
	NearSurface_Ionosphere_DRegion = 'NearSurface.Ionosphere.DRegion'
	NearSurface_Ionosphere_ERegion = 'NearSurface.Ionosphere.ERegion'
	NearSurface_Ionosphere_FRegion = 'NearSurface.Ionosphere.FRegion'
	NearSurface_Ionosphere_Topside = 'NearSurface.Ionosphere.Topside'
	NearSurface_Mesosphere = 'NearSurface.Mesosphere'
	NearSurface_MidLatitudeRegion = 'NearSurface.MidLatitudeRegion'
	NearSurface_Plasmasphere = 'NearSurface.Plasmasphere'
	NearSurface_PolarCap = 'NearSurface.PolarCap'
	NearSurface_SouthAtlanticAnomalyRegion = 'NearSurface.SouthAtlanticAnomalyRegion'
	NearSurface_Stratosphere = 'NearSurface.Stratosphere'
	NearSurface_SubAuroralRegion = 'NearSurface.SubAuroralRegion'
	NearSurface_Thermosphere = 'NearSurface.Thermosphere'
	NearSurface_Troposphere = 'NearSurface.Troposphere'
	Surface = 'Surface'
class Encoding(EnumTemplate):
	"""A set of unambiguous rules that establishes the representation of information within a file."""
	_schema = schema
	
	
	ASCII = 'ASCII'
	Base64 = 'Base64'
	BZIP2 = 'BZIP2'
	GZIP = 'GZIP'
	None_ = 'None'
	S3_BUCKET = 'S3_BUCKET'
	TAR = 'TAR'
	Unicode = 'Unicode'
	ZIP = 'ZIP'
class FieldQuantity(EnumTemplate):
	"""The physical attribute of the field."""
	_schema = schema
	
	
	Current = 'Current'
	CurrentDensity = 'CurrentDensity'
	Electric = 'Electric'
	Electromagnetic = 'Electromagnetic'
	Gyrofrequency = 'Gyrofrequency'
	Magnetic = 'Magnetic'
	PlasmaFrequency = 'PlasmaFrequency'
	Potential = 'Potential'
	PoyntingFlux = 'PoyntingFlux'
class Format(EnumTemplate):
	"""The organization of data according to preset specifications. The value is selected from a list of accepted names for known, well documented formats."""
	_schema = schema
	
	
	AVI = 'AVI'
	Binary = 'Binary'
	CDF = 'CDF'
	CEF = 'CEF'
	CEF1 = 'CEF1'
	CEF2 = 'CEF2'
	CSV = 'CSV'
	Excel = 'Excel'
	FITS = 'FITS'
	GIF = 'GIF'
	Hardcopy = 'Hardcopy'
	Hardcopy_Film = 'Hardcopy.Film'
	Hardcopy_Microfiche = 'Hardcopy.Microfiche'
	Hardcopy_Microfilm = 'Hardcopy.Microfilm'
	Hardcopy_Photograph = 'Hardcopy.Photograph'
	Hardcopy_PhotographicPlate = 'Hardcopy.PhotographicPlate'
	Hardcopy_Print = 'Hardcopy.Print'
	HDF = 'HDF'
	HDF4 = 'HDF4'
	HDF5 = 'HDF5'
	HTML = 'HTML'
	IDFS = 'IDFS'
	IDL = 'IDL'
	JPEG = 'JPEG'
	JSON = 'JSON'
	MATLAB_4 = 'MATLAB_4'
	MATLAB_6 = 'MATLAB_6'
	MATLAB_7 = 'MATLAB_7'
	MPEG = 'MPEG'
	NCAR = 'NCAR'
	NetCDF = 'NetCDF'
	PDF = 'PDF'
	PDS4 = 'PDS4'
	PDS3 = 'PDS3'
	PNG = 'PNG'
	Postscript = 'Postscript'
	QuickTime = 'QuickTime'
	RINEX2 = 'RINEX2'
	RINEX3 = 'RINEX3'
	Text = 'Text'
	Text_ASCII = 'Text.ASCII'
	Text_Unicode = 'Text.Unicode'
	TFCat = 'TFCat'
	TIFF = 'TIFF'
	UDF = 'UDF'
	VOTable = 'VOTable'
	XML = 'XML'
class Hardcopy(EnumTemplate):
	"""A permanent reproduction, or copy in the form of a physical object, of any media suitable for direct use by a person."""
	_schema = schema
	
	
	Film = 'Film'
	Microfiche = 'Microfiche'
	Microfilm = 'Microfilm'
	Photograph = 'Photograph'
	PhotographicPlate = 'PhotographicPlate'
	Print = 'Print'
class HashFunction(EnumTemplate):
	"""A function or algorithm that converts a digital data object into a hash value. Typically, the hash value is small and concise when compared to the digital data object."""
	_schema = schema
	
	
	MD5 = 'MD5'
	SHA1 = 'SHA1'
	SHA256 = 'SHA256'
class Heliosphere(EnumTemplate):
	"""The solar atmosphere extending roughly from the outer corona to the edge of the solar plasma at the heliopause separating primarily solar plasma from interstellar plasma."""
	_schema = schema
	
	
	Heliosheath = 'Heliosheath'
	Inner = 'Inner'
	NearEarth = 'NearEarth'
	Outer = 'Outer'
	Remote1AU = 'Remote1AU'
class InstrumentType(EnumTemplate):
	"""A characterization of an integrated collection of software and hardware containing one or more sensors and associated controls used to produce data on an environment."""
	_schema = schema
	
	
	Antenna = 'Antenna'
	Channeltron = 'Channeltron'
	Coronograph = 'Coronograph'
	DoubleSphere = 'DoubleSphere'
	DustDetector = 'DustDetector'
	ElectronDriftInstrument = 'ElectronDriftInstrument'
	ElectrostaticAnalyser = 'ElectrostaticAnalyser'
	EnergeticParticleInstrument = 'EnergeticParticleInstrument'
	Experiment = 'Experiment'
	FaradayCup = 'FaradayCup'
	FluxFeedback = 'FluxFeedback'
	FourierTransformSpectrograph = 'FourierTransformSpectrograph'
	GeigerMuellerTube = 'GeigerMuellerTube'
	Imager = 'Imager'
	ImagingSpectrometer = 'ImagingSpectrometer'
	Interferometer = 'Interferometer'
	IonChamber = 'IonChamber'
	IonDrift = 'IonDrift'
	IonGauge = 'IonGauge'
	LangmuirProbe = 'LangmuirProbe'
	LongWire = 'LongWire'
	Magnetograph = 'Magnetograph'
	Magnetometer = 'Magnetometer'
	MassSpectrometer = 'MassSpectrometer'
	MicrochannelPlate = 'MicrochannelPlate'
	MultispectralImager = 'MultispectralImager'
	NeutralAtomImager = 'NeutralAtomImager'
	NeutralParticleDetector = 'NeutralParticleDetector'
	ParticleCorrelator = 'ParticleCorrelator'
	ParticleDetector = 'ParticleDetector'
	Photometer = 'Photometer'
	PhotomultiplierTube = 'PhotomultiplierTube'
	Photopolarimeter = 'Photopolarimeter'
	Platform = 'Platform'
	ProportionalCounter = 'ProportionalCounter'
	QuadrisphericalAnalyser = 'QuadrisphericalAnalyser'
	Radar = 'Radar'
	Radiometer = 'Radiometer'
	ResonanceSounder = 'ResonanceSounder'
	RetardingPotentialAnalyser = 'RetardingPotentialAnalyser'
	Riometer = 'Riometer'
	ScintillationDetector = 'ScintillationDetector'
	SearchCoil = 'SearchCoil'
	SolidStateDetector = 'SolidStateDetector'
	Sounder = 'Sounder'
	SpacecraftPotentialControl = 'SpacecraftPotentialControl'
	SpectralPowerReceiver = 'SpectralPowerReceiver'
	Spectrometer = 'Spectrometer'
	TimeOfFlight = 'TimeOfFlight'
	Unspecified = 'Unspecified'
	WaveformReceiver = 'WaveformReceiver'
class Integral(EnumTemplate):
	"""A flux measurement in a broad range of energy and solid angle."""
	_schema = schema
	
	
	Area = 'Area'
	Bandwidth = 'Bandwidth'
	SolidAngle = 'SolidAngle'
class Ionosphere(EnumTemplate):
	"""The charged or ionized gases surrounding a body that are nominally bound to the body by virtue of the gravitational attraction."""
	_schema = schema
	
	
	DRegion = 'DRegion'
	ERegion = 'ERegion'
	FRegion = 'FRegion'
	Topside = 'Topside'
class Jupiter(EnumTemplate):
	"""The fifth planet from the Sun in our solar system."""
	_schema = schema
	
	
	Callisto = 'Callisto'
	Europa = 'Europa'
	Ganymede = 'Ganymede'
	Io = 'Io'
	Magnetosphere = 'Magnetosphere'
	Magnetosphere_Magnetotail = 'Magnetosphere.Magnetotail'
	Magnetosphere_Main = 'Magnetosphere.Main'
	Magnetosphere_Plasmasphere = 'Magnetosphere.Plasmasphere'
	Magnetosphere_Polar = 'Magnetosphere.Polar'
	Magnetosphere_RadiationBelt = 'Magnetosphere.RadiationBelt'
	Magnetosphere_RingCurrent = 'Magnetosphere.RingCurrent'
class LikelihoodRating(EnumTemplate):
	"""The probability that something is true or possible."""
	_schema = schema
	
	
	Probable = 'Probable'
	Strong = 'Strong'
	Unlikely = 'Unlikely'
	Weak = 'Weak'
class Magnetosphere(EnumTemplate):
	"""The region of space above the atmosphere or surface of the planet and bounded by the magnetopause that is under the direct influence of the magnetic field of a planetary body."""
	_schema = schema
	
	
	Magnetotail = 'Magnetotail'
	Main = 'Main'
	Plasmasphere = 'Plasmasphere'
	Polar = 'Polar'
	RadiationBelt = 'RadiationBelt'
	RingCurrent = 'RingCurrent'
class Mars(EnumTemplate):
	"""The fourth planet from the Sun in our solar system."""
	_schema = schema
	
	
	Deimos = 'Deimos'
	Magnetosphere = 'Magnetosphere'
	Magnetosphere_Magnetotail = 'Magnetosphere.Magnetotail'
	Magnetosphere_Main = 'Magnetosphere.Main'
	Magnetosphere_Plasmasphere = 'Magnetosphere.Plasmasphere'
	Magnetosphere_Polar = 'Magnetosphere.Polar'
	Magnetosphere_RadiationBelt = 'Magnetosphere.RadiationBelt'
	Magnetosphere_RingCurrent = 'Magnetosphere.RingCurrent'
	Phobos = 'Phobos'
class MeasurementType(EnumTemplate):
	"""The enumeration of the specific measurement target (e.g., EnergeticParticles or IonComposition), method of measurement (e.g., Interferometry), or the particular compilation of measurements (e.g., a composite dataset consisting of measurements from multiple instruments or platforms, such as Dopplergram, Keogram, and ElectronColumnDensity (TEC)) that reflect a richer context (e.g., structure or dynamics) of the observational target."""
	_schema = schema
	
	
	ActivityIndex = 'ActivityIndex'
	Dopplergram = 'Dopplergram'
	Dust = 'Dust'
	ElectricField = 'ElectricField'
	EnergeticParticles = 'EnergeticParticles'
	Ephemeris = 'Ephemeris'
	ImageIntensity = 'ImageIntensity'
	InstrumentStatus = 'InstrumentStatus'
	IonComposition = 'IonComposition'
	Irradiance = 'Irradiance'
	MagneticField = 'MagneticField'
	Magnetogram = 'Magnetogram'
	NeutralAtomImages = 'NeutralAtomImages'
	NeutralGas = 'NeutralGas'
	Profile = 'Profile'
	Radiance = 'Radiance'
	Spectrum = 'Spectrum'
	SPICE = 'SPICE'
	ThermalPlasma = 'ThermalPlasma'
	Waves = 'Waves'
	Waves_Active = 'Waves.Active'
	Waves_Passive = 'Waves.Passive'
class Mercury(EnumTemplate):
	"""The first planet from the Sun in our solar system."""
	_schema = schema
	
	
	Magnetosphere = 'Magnetosphere'
	Magnetosphere_Magnetotail = 'Magnetosphere.Magnetotail'
	Magnetosphere_Main = 'Magnetosphere.Main'
	Magnetosphere_Plasmasphere = 'Magnetosphere.Plasmasphere'
	Magnetosphere_Polar = 'Magnetosphere.Polar'
	Magnetosphere_RadiationBelt = 'Magnetosphere.RadiationBelt'
	Magnetosphere_RingCurrent = 'Magnetosphere.RingCurrent'
class MixedQuantity(EnumTemplate):
	"""A characterization of the combined attributes of a quantity."""
	_schema = schema
	
	
	AkasofuEpsilon = 'AkasofuEpsilon'
	AlfvenMachNumber = 'AlfvenMachNumber'
	AlfvenVelocity = 'AlfvenVelocity'
	FrequencyToGyrofrequencyRatio = 'FrequencyToGyrofrequencyRatio'
	IMFClockAngle = 'IMFClockAngle'
	MagnetosonicMachNumber = 'MagnetosonicMachNumber'
	Other = 'Other'
	PlasmaBeta = 'PlasmaBeta'
	SolarUVFlux = 'SolarUVFlux'
	TotalPressure = 'TotalPressure'
	VCrossB = 'VCrossB'
class NearSurface(EnumTemplate):
	"""The gaseous and possibly ionized environment of a body extending from the surface to some specified altitude. For the Earth, this altitude is 2000 km."""
	_schema = schema
	
	
	Atmosphere = 'Atmosphere'
	AuroralRegion = 'AuroralRegion'
	EquatorialRegion = 'EquatorialRegion'
	Ionosphere = 'Ionosphere'
	Ionosphere_DRegion = 'Ionosphere.DRegion'
	Ionosphere_ERegion = 'Ionosphere.ERegion'
	Ionosphere_FRegion = 'Ionosphere.FRegion'
	Ionosphere_Topside = 'Ionosphere.Topside'
	Mesosphere = 'Mesosphere'
	MidLatitudeRegion = 'MidLatitudeRegion'
	Plasmasphere = 'Plasmasphere'
	PolarCap = 'PolarCap'
	SouthAtlanticAnomalyRegion = 'SouthAtlanticAnomalyRegion'
	Stratosphere = 'Stratosphere'
	SubAuroralRegion = 'SubAuroralRegion'
	Thermosphere = 'Thermosphere'
	Troposphere = 'Troposphere'
class Neptune(EnumTemplate):
	"""The seventh planet from the Sun in our solar system."""
	_schema = schema
	
	
	Magnetosphere = 'Magnetosphere'
	Magnetosphere_Magnetotail = 'Magnetosphere.Magnetotail'
	Magnetosphere_Main = 'Magnetosphere.Main'
	Magnetosphere_Plasmasphere = 'Magnetosphere.Plasmasphere'
	Magnetosphere_Polar = 'Magnetosphere.Polar'
	Magnetosphere_RadiationBelt = 'Magnetosphere.RadiationBelt'
	Magnetosphere_RingCurrent = 'Magnetosphere.RingCurrent'
	Proteus = 'Proteus'
	Triton = 'Triton'
class ObservatoryRegion(EnumTemplate):
	"""A spatial location distinguished by certain natural features or physical characteristics where an observatory is located."""
	_schema = schema
	
	
	Asteroid = 'Asteroid'
	Comet = 'Comet'
	Comet_1P_Halley = 'Comet.1P-Halley'
	Comet_26P_Grigg_Skjellerup = 'Comet.26P-Grigg-Skjellerup'
	Comet_67P_Churyumov_Gerasimenko = 'Comet.67P-Churyumov-Gerasimenko'
	Earth = 'Earth'
	Earth_Magnetosheath = 'Earth.Magnetosheath'
	Earth_Magnetosphere = 'Earth.Magnetosphere'
	Earth_Magnetosphere_Magnetotail = 'Earth.Magnetosphere.Magnetotail'
	Earth_Magnetosphere_Main = 'Earth.Magnetosphere.Main'
	Earth_Magnetosphere_Plasmasphere = 'Earth.Magnetosphere.Plasmasphere'
	Earth_Magnetosphere_Polar = 'Earth.Magnetosphere.Polar'
	Earth_Magnetosphere_RadiationBelt = 'Earth.Magnetosphere.RadiationBelt'
	Earth_Magnetosphere_RingCurrent = 'Earth.Magnetosphere.RingCurrent'
	Earth_Moon = 'Earth.Moon'
	Earth_NearSurface = 'Earth.NearSurface'
	Earth_NearSurface_Atmosphere = 'Earth.NearSurface.Atmosphere'
	Earth_NearSurface_AuroralRegion = 'Earth.NearSurface.AuroralRegion'
	Earth_NearSurface_EquatorialRegion = 'Earth.NearSurface.EquatorialRegion'
	Earth_NearSurface_Ionosphere = 'Earth.NearSurface.Ionosphere'
	Earth_NearSurface_Ionosphere_DRegion = 'Earth.NearSurface.Ionosphere.DRegion'
	Earth_NearSurface_Ionosphere_ERegion = 'Earth.NearSurface.Ionosphere.ERegion'
	Earth_NearSurface_Ionosphere_FRegion = 'Earth.NearSurface.Ionosphere.FRegion'
	Earth_NearSurface_Ionosphere_Topside = 'Earth.NearSurface.Ionosphere.Topside'
	Earth_NearSurface_Mesosphere = 'Earth.NearSurface.Mesosphere'
	Earth_NearSurface_MidLatitudeRegion = 'Earth.NearSurface.MidLatitudeRegion'
	Earth_NearSurface_Plasmasphere = 'Earth.NearSurface.Plasmasphere'
	Earth_NearSurface_PolarCap = 'Earth.NearSurface.PolarCap'
	Earth_NearSurface_SouthAtlanticAnomalyRegion = 'Earth.NearSurface.SouthAtlanticAnomalyRegion'
	Earth_NearSurface_Stratosphere = 'Earth.NearSurface.Stratosphere'
	Earth_NearSurface_SubAuroralRegion = 'Earth.NearSurface.SubAuroralRegion'
	Earth_NearSurface_Thermosphere = 'Earth.NearSurface.Thermosphere'
	Earth_NearSurface_Troposphere = 'Earth.NearSurface.Troposphere'
	Earth_Surface = 'Earth.Surface'
	Heliosphere = 'Heliosphere'
	Heliosphere_Heliosheath = 'Heliosphere.Heliosheath'
	Heliosphere_Inner = 'Heliosphere.Inner'
	Heliosphere_NearEarth = 'Heliosphere.NearEarth'
	Heliosphere_Outer = 'Heliosphere.Outer'
	Heliosphere_Remote1AU = 'Heliosphere.Remote1AU'
	Interstellar = 'Interstellar'
	Jupiter = 'Jupiter'
	Jupiter_Callisto = 'Jupiter.Callisto'
	Jupiter_Europa = 'Jupiter.Europa'
	Jupiter_Ganymede = 'Jupiter.Ganymede'
	Jupiter_Io = 'Jupiter.Io'
	Jupiter_Magnetosphere = 'Jupiter.Magnetosphere'
	Jupiter_Magnetosphere_Magnetotail = 'Jupiter.Magnetosphere.Magnetotail'
	Jupiter_Magnetosphere_Main = 'Jupiter.Magnetosphere.Main'
	Jupiter_Magnetosphere_Plasmasphere = 'Jupiter.Magnetosphere.Plasmasphere'
	Jupiter_Magnetosphere_Polar = 'Jupiter.Magnetosphere.Polar'
	Jupiter_Magnetosphere_RadiationBelt = 'Jupiter.Magnetosphere.RadiationBelt'
	Jupiter_Magnetosphere_RingCurrent = 'Jupiter.Magnetosphere.RingCurrent'
	Mars = 'Mars'
	Mars_Deimos = 'Mars.Deimos'
	Mars_Magnetosphere = 'Mars.Magnetosphere'
	Mars_Magnetosphere_Magnetotail = 'Mars.Magnetosphere.Magnetotail'
	Mars_Magnetosphere_Main = 'Mars.Magnetosphere.Main'
	Mars_Magnetosphere_Plasmasphere = 'Mars.Magnetosphere.Plasmasphere'
	Mars_Magnetosphere_Polar = 'Mars.Magnetosphere.Polar'
	Mars_Magnetosphere_RadiationBelt = 'Mars.Magnetosphere.RadiationBelt'
	Mars_Magnetosphere_RingCurrent = 'Mars.Magnetosphere.RingCurrent'
	Mars_Phobos = 'Mars.Phobos'
	Mercury = 'Mercury'
	Mercury_Magnetosphere = 'Mercury.Magnetosphere'
	Mercury_Magnetosphere_Magnetotail = 'Mercury.Magnetosphere.Magnetotail'
	Mercury_Magnetosphere_Main = 'Mercury.Magnetosphere.Main'
	Mercury_Magnetosphere_Plasmasphere = 'Mercury.Magnetosphere.Plasmasphere'
	Mercury_Magnetosphere_Polar = 'Mercury.Magnetosphere.Polar'
	Mercury_Magnetosphere_RadiationBelt = 'Mercury.Magnetosphere.RadiationBelt'
	Mercury_Magnetosphere_RingCurrent = 'Mercury.Magnetosphere.RingCurrent'
	Neptune = 'Neptune'
	Neptune_Magnetosphere = 'Neptune.Magnetosphere'
	Neptune_Magnetosphere_Magnetotail = 'Neptune.Magnetosphere.Magnetotail'
	Neptune_Magnetosphere_Main = 'Neptune.Magnetosphere.Main'
	Neptune_Magnetosphere_Plasmasphere = 'Neptune.Magnetosphere.Plasmasphere'
	Neptune_Magnetosphere_Polar = 'Neptune.Magnetosphere.Polar'
	Neptune_Magnetosphere_RadiationBelt = 'Neptune.Magnetosphere.RadiationBelt'
	Neptune_Magnetosphere_RingCurrent = 'Neptune.Magnetosphere.RingCurrent'
	Neptune_Proteus = 'Neptune.Proteus'
	Neptune_Triton = 'Neptune.Triton'
	Pluto = 'Pluto'
	Saturn = 'Saturn'
	Saturn_Dione = 'Saturn.Dione'
	Saturn_Enceladus = 'Saturn.Enceladus'
	Saturn_Iapetus = 'Saturn.Iapetus'
	Saturn_Magnetosphere = 'Saturn.Magnetosphere'
	Saturn_Magnetosphere_Magnetotail = 'Saturn.Magnetosphere.Magnetotail'
	Saturn_Magnetosphere_Main = 'Saturn.Magnetosphere.Main'
	Saturn_Magnetosphere_Plasmasphere = 'Saturn.Magnetosphere.Plasmasphere'
	Saturn_Magnetosphere_Polar = 'Saturn.Magnetosphere.Polar'
	Saturn_Magnetosphere_RadiationBelt = 'Saturn.Magnetosphere.RadiationBelt'
	Saturn_Magnetosphere_RingCurrent = 'Saturn.Magnetosphere.RingCurrent'
	Saturn_Mimas = 'Saturn.Mimas'
	Saturn_Rhea = 'Saturn.Rhea'
	Saturn_Tethys = 'Saturn.Tethys'
	Saturn_Titan = 'Saturn.Titan'
	Sun = 'Sun'
	Sun_Chromosphere = 'Sun.Chromosphere'
	Sun_Corona = 'Sun.Corona'
	Sun_Interior = 'Sun.Interior'
	Sun_Photosphere = 'Sun.Photosphere'
	Sun_TransitionRegion = 'Sun.TransitionRegion'
	Uranus = 'Uranus'
	Uranus_Ariel = 'Uranus.Ariel'
	Uranus_Magnetosphere = 'Uranus.Magnetosphere'
	Uranus_Magnetosphere_Magnetotail = 'Uranus.Magnetosphere.Magnetotail'
	Uranus_Magnetosphere_Main = 'Uranus.Magnetosphere.Main'
	Uranus_Magnetosphere_Plasmasphere = 'Uranus.Magnetosphere.Plasmasphere'
	Uranus_Magnetosphere_Polar = 'Uranus.Magnetosphere.Polar'
	Uranus_Magnetosphere_RadiationBelt = 'Uranus.Magnetosphere.RadiationBelt'
	Uranus_Magnetosphere_RingCurrent = 'Uranus.Magnetosphere.RingCurrent'
	Uranus_Miranda = 'Uranus.Miranda'
	Uranus_Oberon = 'Uranus.Oberon'
	Uranus_Puck = 'Uranus.Puck'
	Uranus_Titania = 'Uranus.Titania'
	Uranus_Umbriel = 'Uranus.Umbriel'
	Venus = 'Venus'
	Venus_Magnetosphere = 'Venus.Magnetosphere'
	Venus_Magnetosphere_Magnetotail = 'Venus.Magnetosphere.Magnetotail'
	Venus_Magnetosphere_Main = 'Venus.Magnetosphere.Main'
	Venus_Magnetosphere_Plasmasphere = 'Venus.Magnetosphere.Plasmasphere'
	Venus_Magnetosphere_Polar = 'Venus.Magnetosphere.Polar'
	Venus_Magnetosphere_RadiationBelt = 'Venus.Magnetosphere.RadiationBelt'
	Venus_Magnetosphere_RingCurrent = 'Venus.Magnetosphere.RingCurrent'
class ObservedRegion(EnumTemplate):
	"""The portion of space measured by the instrument at the time of an observation. A region is distinguished by certain natural features or physical characteristics. It is the location of the observatory for in situ data, the location or region sensed by remote sensing observatories and the location-of-relevance for parameters that are derived from observational data."""
	_schema = schema
	
	
	Asteroid = 'Asteroid'
	Comet = 'Comet'
	Comet_1P_Halley = 'Comet.1P-Halley'
	Comet_26P_Grigg_Skjellerup = 'Comet.26P-Grigg-Skjellerup'
	Comet_67P_Churyumov_Gerasimenko = 'Comet.67P-Churyumov-Gerasimenko'
	Earth = 'Earth'
	Earth_Magnetosheath = 'Earth.Magnetosheath'
	Earth_Magnetosphere = 'Earth.Magnetosphere'
	Earth_Magnetosphere_Magnetotail = 'Earth.Magnetosphere.Magnetotail'
	Earth_Magnetosphere_Main = 'Earth.Magnetosphere.Main'
	Earth_Magnetosphere_Plasmasphere = 'Earth.Magnetosphere.Plasmasphere'
	Earth_Magnetosphere_Polar = 'Earth.Magnetosphere.Polar'
	Earth_Magnetosphere_RadiationBelt = 'Earth.Magnetosphere.RadiationBelt'
	Earth_Magnetosphere_RingCurrent = 'Earth.Magnetosphere.RingCurrent'
	Earth_Moon = 'Earth.Moon'
	Earth_NearSurface = 'Earth.NearSurface'
	Earth_NearSurface_Atmosphere = 'Earth.NearSurface.Atmosphere'
	Earth_NearSurface_AuroralRegion = 'Earth.NearSurface.AuroralRegion'
	Earth_NearSurface_EquatorialRegion = 'Earth.NearSurface.EquatorialRegion'
	Earth_NearSurface_Ionosphere = 'Earth.NearSurface.Ionosphere'
	Earth_NearSurface_Ionosphere_DRegion = 'Earth.NearSurface.Ionosphere.DRegion'
	Earth_NearSurface_Ionosphere_ERegion = 'Earth.NearSurface.Ionosphere.ERegion'
	Earth_NearSurface_Ionosphere_FRegion = 'Earth.NearSurface.Ionosphere.FRegion'
	Earth_NearSurface_Ionosphere_Topside = 'Earth.NearSurface.Ionosphere.Topside'
	Earth_NearSurface_Mesosphere = 'Earth.NearSurface.Mesosphere'
	Earth_NearSurface_MidLatitudeRegion = 'Earth.NearSurface.MidLatitudeRegion'
	Earth_NearSurface_Plasmasphere = 'Earth.NearSurface.Plasmasphere'
	Earth_NearSurface_PolarCap = 'Earth.NearSurface.PolarCap'
	Earth_NearSurface_SouthAtlanticAnomalyRegion = 'Earth.NearSurface.SouthAtlanticAnomalyRegion'
	Earth_NearSurface_Stratosphere = 'Earth.NearSurface.Stratosphere'
	Earth_NearSurface_SubAuroralRegion = 'Earth.NearSurface.SubAuroralRegion'
	Earth_NearSurface_Thermosphere = 'Earth.NearSurface.Thermosphere'
	Earth_NearSurface_Troposphere = 'Earth.NearSurface.Troposphere'
	Earth_Surface = 'Earth.Surface'
	Heliosphere = 'Heliosphere'
	Heliosphere_Heliosheath = 'Heliosphere.Heliosheath'
	Heliosphere_Inner = 'Heliosphere.Inner'
	Heliosphere_NearEarth = 'Heliosphere.NearEarth'
	Heliosphere_Outer = 'Heliosphere.Outer'
	Heliosphere_Remote1AU = 'Heliosphere.Remote1AU'
	Interstellar = 'Interstellar'
	Jupiter = 'Jupiter'
	Jupiter_Callisto = 'Jupiter.Callisto'
	Jupiter_Europa = 'Jupiter.Europa'
	Jupiter_Ganymede = 'Jupiter.Ganymede'
	Jupiter_Io = 'Jupiter.Io'
	Jupiter_Magnetosphere = 'Jupiter.Magnetosphere'
	Jupiter_Magnetosphere_Magnetotail = 'Jupiter.Magnetosphere.Magnetotail'
	Jupiter_Magnetosphere_Main = 'Jupiter.Magnetosphere.Main'
	Jupiter_Magnetosphere_Plasmasphere = 'Jupiter.Magnetosphere.Plasmasphere'
	Jupiter_Magnetosphere_Polar = 'Jupiter.Magnetosphere.Polar'
	Jupiter_Magnetosphere_RadiationBelt = 'Jupiter.Magnetosphere.RadiationBelt'
	Jupiter_Magnetosphere_RingCurrent = 'Jupiter.Magnetosphere.RingCurrent'
	Mars = 'Mars'
	Mars_Deimos = 'Mars.Deimos'
	Mars_Magnetosphere = 'Mars.Magnetosphere'
	Mars_Magnetosphere_Magnetotail = 'Mars.Magnetosphere.Magnetotail'
	Mars_Magnetosphere_Main = 'Mars.Magnetosphere.Main'
	Mars_Magnetosphere_Plasmasphere = 'Mars.Magnetosphere.Plasmasphere'
	Mars_Magnetosphere_Polar = 'Mars.Magnetosphere.Polar'
	Mars_Magnetosphere_RadiationBelt = 'Mars.Magnetosphere.RadiationBelt'
	Mars_Magnetosphere_RingCurrent = 'Mars.Magnetosphere.RingCurrent'
	Mars_Phobos = 'Mars.Phobos'
	Mercury = 'Mercury'
	Mercury_Magnetosphere = 'Mercury.Magnetosphere'
	Mercury_Magnetosphere_Magnetotail = 'Mercury.Magnetosphere.Magnetotail'
	Mercury_Magnetosphere_Main = 'Mercury.Magnetosphere.Main'
	Mercury_Magnetosphere_Plasmasphere = 'Mercury.Magnetosphere.Plasmasphere'
	Mercury_Magnetosphere_Polar = 'Mercury.Magnetosphere.Polar'
	Mercury_Magnetosphere_RadiationBelt = 'Mercury.Magnetosphere.RadiationBelt'
	Mercury_Magnetosphere_RingCurrent = 'Mercury.Magnetosphere.RingCurrent'
	Neptune = 'Neptune'
	Neptune_Magnetosphere = 'Neptune.Magnetosphere'
	Neptune_Magnetosphere_Magnetotail = 'Neptune.Magnetosphere.Magnetotail'
	Neptune_Magnetosphere_Main = 'Neptune.Magnetosphere.Main'
	Neptune_Magnetosphere_Plasmasphere = 'Neptune.Magnetosphere.Plasmasphere'
	Neptune_Magnetosphere_Polar = 'Neptune.Magnetosphere.Polar'
	Neptune_Magnetosphere_RadiationBelt = 'Neptune.Magnetosphere.RadiationBelt'
	Neptune_Magnetosphere_RingCurrent = 'Neptune.Magnetosphere.RingCurrent'
	Neptune_Proteus = 'Neptune.Proteus'
	Neptune_Triton = 'Neptune.Triton'
	Pluto = 'Pluto'
	Saturn = 'Saturn'
	Saturn_Dione = 'Saturn.Dione'
	Saturn_Enceladus = 'Saturn.Enceladus'
	Saturn_Iapetus = 'Saturn.Iapetus'
	Saturn_Magnetosphere = 'Saturn.Magnetosphere'
	Saturn_Magnetosphere_Magnetotail = 'Saturn.Magnetosphere.Magnetotail'
	Saturn_Magnetosphere_Main = 'Saturn.Magnetosphere.Main'
	Saturn_Magnetosphere_Plasmasphere = 'Saturn.Magnetosphere.Plasmasphere'
	Saturn_Magnetosphere_Polar = 'Saturn.Magnetosphere.Polar'
	Saturn_Magnetosphere_RadiationBelt = 'Saturn.Magnetosphere.RadiationBelt'
	Saturn_Magnetosphere_RingCurrent = 'Saturn.Magnetosphere.RingCurrent'
	Saturn_Mimas = 'Saturn.Mimas'
	Saturn_Rhea = 'Saturn.Rhea'
	Saturn_Tethys = 'Saturn.Tethys'
	Saturn_Titan = 'Saturn.Titan'
	Sun = 'Sun'
	Sun_Chromosphere = 'Sun.Chromosphere'
	Sun_Corona = 'Sun.Corona'
	Sun_Interior = 'Sun.Interior'
	Sun_Photosphere = 'Sun.Photosphere'
	Sun_TransitionRegion = 'Sun.TransitionRegion'
	Uranus = 'Uranus'
	Uranus_Ariel = 'Uranus.Ariel'
	Uranus_Magnetosphere = 'Uranus.Magnetosphere'
	Uranus_Magnetosphere_Magnetotail = 'Uranus.Magnetosphere.Magnetotail'
	Uranus_Magnetosphere_Main = 'Uranus.Magnetosphere.Main'
	Uranus_Magnetosphere_Plasmasphere = 'Uranus.Magnetosphere.Plasmasphere'
	Uranus_Magnetosphere_Polar = 'Uranus.Magnetosphere.Polar'
	Uranus_Magnetosphere_RadiationBelt = 'Uranus.Magnetosphere.RadiationBelt'
	Uranus_Magnetosphere_RingCurrent = 'Uranus.Magnetosphere.RingCurrent'
	Uranus_Miranda = 'Uranus.Miranda'
	Uranus_Oberon = 'Uranus.Oberon'
	Uranus_Puck = 'Uranus.Puck'
	Uranus_Titania = 'Uranus.Titania'
	Uranus_Umbriel = 'Uranus.Umbriel'
	Venus = 'Venus'
	Venus_Magnetosphere = 'Venus.Magnetosphere'
	Venus_Magnetosphere_Magnetotail = 'Venus.Magnetosphere.Magnetotail'
	Venus_Magnetosphere_Main = 'Venus.Magnetosphere.Main'
	Venus_Magnetosphere_Plasmasphere = 'Venus.Magnetosphere.Plasmasphere'
	Venus_Magnetosphere_Polar = 'Venus.Magnetosphere.Polar'
	Venus_Magnetosphere_RadiationBelt = 'Venus.Magnetosphere.RadiationBelt'
	Venus_Magnetosphere_RingCurrent = 'Venus.Magnetosphere.RingCurrent'
class ParameterQuantity(EnumTemplate):
	"""The value associated with a parameter."""
	_schema = schema
	
	
	_2DCuts = '2DCuts'
	_3DCubes = '3DCubes'
	ACElectricField = 'ACElectricField'
	ACMagneticField = 'ACMagneticField'
	Absorption = 'Absorption'
	ActivityIndex = 'ActivityIndex'
	AdiabaticInvariant = 'AdiabaticInvariant'
	AdiabaticInvariant_MagneticMoment = 'AdiabaticInvariant.MagneticMoment'
	AdiabaticInvariant_BounceMotion = 'AdiabaticInvariant.BounceMotion'
	AdiabaticInvariant_DriftMotion = 'AdiabaticInvariant.DriftMotion'
	Aerosol = 'Aerosol'
	AkasofuEpsilon = 'AkasofuEpsilon'
	Albedo = 'Albedo'
	AlfvenMachNumber = 'AlfvenMachNumber'
	AlfvenVelocity = 'AlfvenVelocity'
	AlphaParticle = 'AlphaParticle'
	Antenna = 'Antenna'
	ArrivalDirection = 'ArrivalDirection'
	Atom = 'Atom'
	AtomicNumberDetected = 'AtomicNumberDetected'
	AverageChargeState = 'AverageChargeState'
	AzimuthAngle = 'AzimuthAngle'
	CaK = 'CaK'
	Channeltron = 'Channeltron'
	ChargeExchange = 'ChargeExchange'
	ChargeFlux = 'ChargeFlux'
	ChargeState = 'ChargeState'
	Coronograph = 'Coronograph'
	CountRate = 'CountRate'
	Counts = 'Counts'
	CrossSection = 'CrossSection'
	Current = 'Current'
	CurrentDensity = 'CurrentDensity'
	DataQuality = 'DataQuality'
	DissociativeRecombination = 'DissociativeRecombination'
	DopplerFrequency = 'DopplerFrequency'
	Dopplergram = 'Dopplergram'
	DoubleSphere = 'DoubleSphere'
	Dust = 'Dust'
	DustDetector = 'DustDetector'
	DynamicPressure = 'DynamicPressure'
	Electric = 'Electric'
	ElectricField = 'ElectricField'
	Electromagnetic = 'Electromagnetic'
	Electron = 'Electron'
	ElectronDriftInstrument = 'ElectronDriftInstrument'
	ElectronImpact = 'ElectronImpact'
	Electrostatic = 'Electrostatic'
	ElectrostaticAnalyser = 'ElectrostaticAnalyser'
	ElevationAngle = 'ElevationAngle'
	Emissivity = 'Emissivity'
	EnergeticParticleInstrument = 'EnergeticParticleInstrument'
	EnergeticParticles = 'EnergeticParticles'
	Energy = 'Energy'
	EnergyDensity = 'EnergyDensity'
	EnergyFlux = 'EnergyFlux'
	EnergyPerCharge = 'EnergyPerCharge'
	Entropy = 'Entropy'
	Ephemeris = 'Ephemeris'
	EquivalentWidth = 'EquivalentWidth'
	Experiment = 'Experiment'
	ExtremeUltraviolet = 'ExtremeUltraviolet'
	FarUltraviolet = 'FarUltraviolet'
	FaradayCup = 'FaradayCup'
	FlowSpeed = 'FlowSpeed'
	FlowVelocity = 'FlowVelocity'
	Fluence = 'Fluence'
	FluxFeedback = 'FluxFeedback'
	FourierTransformSpectrograph = 'FourierTransformSpectrograph'
	Frequency = 'Frequency'
	FrequencyToGyrofrequencyRatio = 'FrequencyToGyrofrequencyRatio'
	GammaRays = 'GammaRays'
	GeigerMuellerTube = 'GeigerMuellerTube'
	GeometricFactor = 'GeometricFactor'
	Gyrofrequency = 'Gyrofrequency'
	Halpha = 'Halpha'
	HardXRays = 'HardXRays'
	He10830 = 'He10830'
	He304 = 'He304'
	HeatFlux = 'HeatFlux'
	Housekeeping = 'Housekeeping'
	Hydrodynamic = 'Hydrodynamic'
	IMFClockAngle = 'IMFClockAngle'
	ImageIntensity = 'ImageIntensity'
	Imager = 'Imager'
	ImagingSpectrometer = 'ImagingSpectrometer'
	Infrared = 'Infrared'
	InstrumentMode = 'InstrumentMode'
	InstrumentStatus = 'InstrumentStatus'
	Intensity = 'Intensity'
	Interferometer = 'Interferometer'
	Ion = 'Ion'
	IonChamber = 'IonChamber'
	IonComposition = 'IonComposition'
	IonDrift = 'IonDrift'
	IonGauge = 'IonGauge'
	Irradiance = 'Irradiance'
	K7699 = 'K7699'
	LBHBand = 'LBHBand'
	LShell = 'LShell'
	LangmuirProbe = 'LangmuirProbe'
	LineDepth = 'LineDepth'
	Lines = 'Lines'
	LongWire = 'LongWire'
	LowerHybridFrequency = 'LowerHybridFrequency'
	MHD = 'MHD'
	Magnetic = 'Magnetic'
	MagneticField = 'MagneticField'
	Magnetogram = 'Magnetogram'
	Magnetograph = 'Magnetograph'
	Magnetometer = 'Magnetometer'
	MagnetosonicMachNumber = 'MagnetosonicMachNumber'
	Mass = 'Mass'
	MassDensity = 'MassDensity'
	MassNumber = 'MassNumber'
	MassPerCharge = 'MassPerCharge'
	MassSpectrometer = 'MassSpectrometer'
	MicrochannelPlate = 'MicrochannelPlate'
	Microwave = 'Microwave'
	ModeAmplitude = 'ModeAmplitude'
	Molecule = 'Molecule'
	MultispectralImager = 'MultispectralImager'
	NaD = 'NaD'
	NeutralAtomImager = 'NeutralAtomImager'
	NeutralAtomImages = 'NeutralAtomImages'
	NeutralGas = 'NeutralGas'
	NeutralParticleDetector = 'NeutralParticleDetector'
	Neutron = 'Neutron'
	Ni6768 = 'Ni6768'
	NumberDensity = 'NumberDensity'
	NumberFlux = 'NumberFlux'
	Optical = 'Optical'
	Orientation = 'Orientation'
	Other = 'Other'
	ParticleCorrelator = 'ParticleCorrelator'
	ParticleDetector = 'ParticleDetector'
	ParticleRadius = 'ParticleRadius'
	ParticleRigidity = 'ParticleRigidity'
	PhaseSpaceDensity = 'PhaseSpaceDensity'
	PhotoIonization = 'PhotoIonization'
	Photometer = 'Photometer'
	PhotomultiplierTube = 'PhotomultiplierTube'
	Photon = 'Photon'
	Photopolarimeter = 'Photopolarimeter'
	PlasmaBeta = 'PlasmaBeta'
	PlasmaFrequency = 'PlasmaFrequency'
	PlasmaWaves = 'PlasmaWaves'
	Platform = 'Platform'
	PolarAngle = 'PolarAngle'
	Polarization = 'Polarization'
	Positional = 'Positional'
	Positron = 'Positron'
	Potential = 'Potential'
	PoyntingFlux = 'PoyntingFlux'
	Pressure = 'Pressure'
	Profile = 'Profile'
	PropagationTime = 'PropagationTime'
	ProportionalCounter = 'ProportionalCounter'
	Proton = 'Proton'
	QuadrisphericalAnalyser = 'QuadrisphericalAnalyser'
	Radar = 'Radar'
	Radiance = 'Radiance'
	RadioFrequency = 'RadioFrequency'
	Radiometer = 'Radiometer'
	Rate = 'Rate'
	Remark = 'Remark'
	ResonanceSounder = 'ResonanceSounder'
	RetardingPotentialAnalyser = 'RetardingPotentialAnalyser'
	Riometer = 'Riometer'
	RotationMatrix = 'RotationMatrix'
	SPICE = 'SPICE'
	ScintillationDetector = 'ScintillationDetector'
	SearchCoil = 'SearchCoil'
	SoftXRays = 'SoftXRays'
	SolarUVFlux = 'SolarUVFlux'
	SolidStateDetector = 'SolidStateDetector'
	SonicMachNumber = 'SonicMachNumber'
	SoundSpeed = 'SoundSpeed'
	Sounder = 'Sounder'
	SpacecraftPotentialControl = 'SpacecraftPotentialControl'
	SpatialSeries = 'SpatialSeries'
	Spectra = 'Spectra'
	SpectralPowerReceiver = 'SpectralPowerReceiver'
	Spectrometer = 'Spectrometer'
	Spectrum = 'Spectrum'
	SpinPeriod = 'SpinPeriod'
	SpinPhase = 'SpinPhase'
	SpinRate = 'SpinRate'
	StokesParameters = 'StokesParameters'
	Telemetry = 'Telemetry'
	Temperature = 'Temperature'
	Temporal = 'Temporal'
	ThermalPlasma = 'ThermalPlasma'
	ThermalSpeed = 'ThermalSpeed'
	TimeOfFlight = 'TimeOfFlight'
	TimeSeries = 'TimeSeries'
	TotalPressure = 'TotalPressure'
	Ultraviolet = 'Ultraviolet'
	Unspecified = 'Unspecified'
	UpperHybridFrequency = 'UpperHybridFrequency'
	VCrossB = 'VCrossB'
	Velocity = 'Velocity'
	VolumeEmissionRate = 'VolumeEmissionRate'
	WaveformReceiver = 'WaveformReceiver'
	Wavelength = 'Wavelength'
	Waves = 'Waves'
	Waves_Active = 'Waves.Active'
	Waves_Passive = 'Waves.Passive'
	WebResource = 'WebResource'
	WebService = 'WebService'
	WhiteLight = 'WhiteLight'
	XRays = 'XRays'
class ParticleQuantity(EnumTemplate):
	"""A characterization of the physical properties of the particle."""
	_schema = schema
	
	
	AdiabaticInvariant = 'AdiabaticInvariant'
	AdiabaticInvariant_MagneticMoment = 'AdiabaticInvariant.MagneticMoment'
	AdiabaticInvariant_BounceMotion = 'AdiabaticInvariant.BounceMotion'
	AdiabaticInvariant_DriftMotion = 'AdiabaticInvariant.DriftMotion'
	ArrivalDirection = 'ArrivalDirection'
	AtomicNumberDetected = 'AtomicNumberDetected'
	AverageChargeState = 'AverageChargeState'
	ChargeFlux = 'ChargeFlux'
	ChargeState = 'ChargeState'
	CountRate = 'CountRate'
	Counts = 'Counts'
	Current = 'Current'
	CurrentDensity = 'CurrentDensity'
	DynamicPressure = 'DynamicPressure'
	Energy = 'Energy'
	Entropy = 'Entropy'
	EnergyDensity = 'EnergyDensity'
	EnergyFlux = 'EnergyFlux'
	EnergyPerCharge = 'EnergyPerCharge'
	FlowSpeed = 'FlowSpeed'
	FlowVelocity = 'FlowVelocity'
	Fluence = 'Fluence'
	GeometricFactor = 'GeometricFactor'
	Gyrofrequency = 'Gyrofrequency'
	HeatFlux = 'HeatFlux'
	LShell = 'LShell'
	Mass = 'Mass'
	MassDensity = 'MassDensity'
	MassNumber = 'MassNumber'
	MassPerCharge = 'MassPerCharge'
	NumberDensity = 'NumberDensity'
	NumberFlux = 'NumberFlux'
	ParticleRadius = 'ParticleRadius'
	ParticleRigidity = 'ParticleRigidity'
	PhaseSpaceDensity = 'PhaseSpaceDensity'
	PlasmaFrequency = 'PlasmaFrequency'
	Pressure = 'Pressure'
	SonicMachNumber = 'SonicMachNumber'
	SoundSpeed = 'SoundSpeed'
	Temperature = 'Temperature'
	ThermalSpeed = 'ThermalSpeed'
	Velocity = 'Velocity'
class ParticleType(EnumTemplate):
	"""A characterization of the kind of particle observed by the measurement."""
	_schema = schema
	
	
	Aerosol = 'Aerosol'
	AlphaParticle = 'AlphaParticle'
	Atom = 'Atom'
	Dust = 'Dust'
	Electron = 'Electron'
	Ion = 'Ion'
	Molecule = 'Molecule'
	Neutron = 'Neutron'
	Proton = 'Proton'
	Positron = 'Positron'
class PhenomenonType(EnumTemplate):
	"""The characteristics or categorization of an event type."""
	_schema = schema
	
	
	ActiveRegion = 'ActiveRegion'
	Aurora = 'Aurora'
	BowShockCrossing = 'BowShockCrossing'
	CoronalHole = 'CoronalHole'
	CoronalMassEjection = 'CoronalMassEjection'
	EITWave = 'EITWave'
	EnergeticSolarParticleEvent = 'EnergeticSolarParticleEvent'
	ForbushDecrease = 'ForbushDecrease'
	GeomagneticStorm = 'GeomagneticStorm'
	InterplanetaryShock = 'InterplanetaryShock'
	MagneticCloud = 'MagneticCloud'
	MagnetopauseCrossing = 'MagnetopauseCrossing'
	RadioBurst = 'RadioBurst'
	SectorBoundaryCrossing = 'SectorBoundaryCrossing'
	SolarFlare = 'SolarFlare'
	SolarWindExtreme = 'SolarWindExtreme'
	StreamInteractionRegion = 'StreamInteractionRegion'
	Substorm = 'Substorm'
class ProcessCoeffType(EnumTemplate):
	"""Whether the model results are obtained from a stationary solution or are dynamically computed."""
	_schema = schema
	
	
	CrossSection = 'CrossSection'
	Frequency = 'Frequency'
	Other = 'Other'
	Rate = 'Rate'
class ProcessingLevel(EnumTemplate):
	"""The standard classification of the processing performed on the product."""
	_schema = schema
	
	
	Calibrated = 'Calibrated'
	Raw = 'Raw'
	Uncalibrated = 'Uncalibrated'
	ValueAdded = 'ValueAdded'
class ProcessType(EnumTemplate):
	"""Type of chemical process."""
	_schema = schema
	
	
	ChargeExchange = 'ChargeExchange'
	DissociativeRecombination = 'DissociativeRecombination'
	ElectronImpact = 'ElectronImpact'
	PhotoIonization = 'PhotoIonization'
class Projection(EnumTemplate):
	"""A measure of the length of a position or measured vector as projected into a plane of the coordinate system."""
	_schema = schema
	
	
	IJ = 'IJ'
	IK = 'IK'
	JK = 'JK'
class PropertyQuantity(EnumTemplate):
	"""The value associated with a property."""
	_schema = schema
	
	
	_2DCuts = '2DCuts'
	_3DCubes = '3DCubes'
	ACElectricField = 'ACElectricField'
	ACMagneticField = 'ACMagneticField'
	Absorption = 'Absorption'
	ActivityIndex = 'ActivityIndex'
	AdiabaticInvariant = 'AdiabaticInvariant'
	AdiabaticInvariant_MagneticMoment = 'AdiabaticInvariant.MagneticMoment'
	AdiabaticInvariant_BounceMotion = 'AdiabaticInvariant.BounceMotion'
	AdiabaticInvariant_DriftMotion = 'AdiabaticInvariant.DriftMotion'
	Aerosol = 'Aerosol'
	AkasofuEpsilon = 'AkasofuEpsilon'
	Albedo = 'Albedo'
	AlfvenMachNumber = 'AlfvenMachNumber'
	AlfvenVelocity = 'AlfvenVelocity'
	AlphaParticle = 'AlphaParticle'
	Antenna = 'Antenna'
	ArrivalDirection = 'ArrivalDirection'
	Atom = 'Atom'
	AtomicNumberDetected = 'AtomicNumberDetected'
	AverageChargeState = 'AverageChargeState'
	AzimuthAngle = 'AzimuthAngle'
	CaK = 'CaK'
	Channeltron = 'Channeltron'
	ChargeExchange = 'ChargeExchange'
	ChargeFlux = 'ChargeFlux'
	ChargeState = 'ChargeState'
	Coronograph = 'Coronograph'
	CountRate = 'CountRate'
	Counts = 'Counts'
	CrossSection = 'CrossSection'
	Current = 'Current'
	CurrentDensity = 'CurrentDensity'
	DataQuality = 'DataQuality'
	DissociativeRecombination = 'DissociativeRecombination'
	DopplerFrequency = 'DopplerFrequency'
	Dopplergram = 'Dopplergram'
	DoubleSphere = 'DoubleSphere'
	Dust = 'Dust'
	DustDetector = 'DustDetector'
	DynamicPressure = 'DynamicPressure'
	Electric = 'Electric'
	ElectricField = 'ElectricField'
	Electromagnetic = 'Electromagnetic'
	Electron = 'Electron'
	ElectronDriftInstrument = 'ElectronDriftInstrument'
	ElectronImpact = 'ElectronImpact'
	Electrostatic = 'Electrostatic'
	ElectrostaticAnalyser = 'ElectrostaticAnalyser'
	ElevationAngle = 'ElevationAngle'
	Emissivity = 'Emissivity'
	EnergeticParticleInstrument = 'EnergeticParticleInstrument'
	EnergeticParticles = 'EnergeticParticles'
	Energy = 'Energy'
	EnergyDensity = 'EnergyDensity'
	EnergyFlux = 'EnergyFlux'
	EnergyPerCharge = 'EnergyPerCharge'
	Entropy = 'Entropy'
	Ephemeris = 'Ephemeris'
	EquivalentWidth = 'EquivalentWidth'
	Experiment = 'Experiment'
	ExtremeUltraviolet = 'ExtremeUltraviolet'
	FarUltraviolet = 'FarUltraviolet'
	FaradayCup = 'FaradayCup'
	FlowSpeed = 'FlowSpeed'
	FlowVelocity = 'FlowVelocity'
	Fluence = 'Fluence'
	FluxFeedback = 'FluxFeedback'
	FourierTransformSpectrograph = 'FourierTransformSpectrograph'
	Frequency = 'Frequency'
	FrequencyToGyrofrequencyRatio = 'FrequencyToGyrofrequencyRatio'
	GammaRays = 'GammaRays'
	GeigerMuellerTube = 'GeigerMuellerTube'
	GeometricFactor = 'GeometricFactor'
	Gyrofrequency = 'Gyrofrequency'
	Halpha = 'Halpha'
	HardXRays = 'HardXRays'
	He10830 = 'He10830'
	He304 = 'He304'
	HeatFlux = 'HeatFlux'
	Housekeeping = 'Housekeeping'
	Hydrodynamic = 'Hydrodynamic'
	IMFClockAngle = 'IMFClockAngle'
	ImageIntensity = 'ImageIntensity'
	Imager = 'Imager'
	ImagingSpectrometer = 'ImagingSpectrometer'
	Infrared = 'Infrared'
	InstrumentMode = 'InstrumentMode'
	InstrumentStatus = 'InstrumentStatus'
	Intensity = 'Intensity'
	Interferometer = 'Interferometer'
	Ion = 'Ion'
	IonChamber = 'IonChamber'
	IonComposition = 'IonComposition'
	IonDrift = 'IonDrift'
	IonGauge = 'IonGauge'
	Irradiance = 'Irradiance'
	K7699 = 'K7699'
	LBHBand = 'LBHBand'
	LShell = 'LShell'
	LangmuirProbe = 'LangmuirProbe'
	LineDepth = 'LineDepth'
	Lines = 'Lines'
	LongWire = 'LongWire'
	LowerHybridFrequency = 'LowerHybridFrequency'
	MHD = 'MHD'
	Magnetic = 'Magnetic'
	MagneticField = 'MagneticField'
	Magnetogram = 'Magnetogram'
	Magnetograph = 'Magnetograph'
	Magnetometer = 'Magnetometer'
	MagnetosonicMachNumber = 'MagnetosonicMachNumber'
	Mass = 'Mass'
	MassDensity = 'MassDensity'
	MassNumber = 'MassNumber'
	MassPerCharge = 'MassPerCharge'
	MassSpectrometer = 'MassSpectrometer'
	MicrochannelPlate = 'MicrochannelPlate'
	Microwave = 'Microwave'
	ModeAmplitude = 'ModeAmplitude'
	Molecule = 'Molecule'
	MultispectralImager = 'MultispectralImager'
	NaD = 'NaD'
	NeutralAtomImager = 'NeutralAtomImager'
	NeutralAtomImages = 'NeutralAtomImages'
	NeutralGas = 'NeutralGas'
	NeutralParticleDetector = 'NeutralParticleDetector'
	Neutron = 'Neutron'
	Ni6768 = 'Ni6768'
	NumberDensity = 'NumberDensity'
	NumberFlux = 'NumberFlux'
	Optical = 'Optical'
	Orientation = 'Orientation'
	Other = 'Other'
	ParticleCorrelator = 'ParticleCorrelator'
	ParticleDetector = 'ParticleDetector'
	ParticleRadius = 'ParticleRadius'
	ParticleRigidity = 'ParticleRigidity'
	PhaseSpaceDensity = 'PhaseSpaceDensity'
	PhotoIonization = 'PhotoIonization'
	Photometer = 'Photometer'
	PhotomultiplierTube = 'PhotomultiplierTube'
	Photon = 'Photon'
	Photopolarimeter = 'Photopolarimeter'
	PlasmaBeta = 'PlasmaBeta'
	PlasmaFrequency = 'PlasmaFrequency'
	PlasmaWaves = 'PlasmaWaves'
	Platform = 'Platform'
	PolarAngle = 'PolarAngle'
	Polarization = 'Polarization'
	Positional = 'Positional'
	Positron = 'Positron'
	Potential = 'Potential'
	PoyntingFlux = 'PoyntingFlux'
	Pressure = 'Pressure'
	Profile = 'Profile'
	PropagationTime = 'PropagationTime'
	ProportionalCounter = 'ProportionalCounter'
	Proton = 'Proton'
	QuadrisphericalAnalyser = 'QuadrisphericalAnalyser'
	Radar = 'Radar'
	Radiance = 'Radiance'
	RadioFrequency = 'RadioFrequency'
	Radiometer = 'Radiometer'
	Rate = 'Rate'
	Remark = 'Remark'
	ResonanceSounder = 'ResonanceSounder'
	RetardingPotentialAnalyser = 'RetardingPotentialAnalyser'
	Riometer = 'Riometer'
	RotationMatrix = 'RotationMatrix'
	SPICE = 'SPICE'
	ScintillationDetector = 'ScintillationDetector'
	SearchCoil = 'SearchCoil'
	SoftXRays = 'SoftXRays'
	SolarUVFlux = 'SolarUVFlux'
	SolidStateDetector = 'SolidStateDetector'
	SonicMachNumber = 'SonicMachNumber'
	SoundSpeed = 'SoundSpeed'
	Sounder = 'Sounder'
	SpacecraftPotentialControl = 'SpacecraftPotentialControl'
	SpatialSeries = 'SpatialSeries'
	Spectra = 'Spectra'
	SpectralPowerReceiver = 'SpectralPowerReceiver'
	Spectrometer = 'Spectrometer'
	Spectrum = 'Spectrum'
	SpinPeriod = 'SpinPeriod'
	SpinPhase = 'SpinPhase'
	SpinRate = 'SpinRate'
	StokesParameters = 'StokesParameters'
	Telemetry = 'Telemetry'
	Temperature = 'Temperature'
	Temporal = 'Temporal'
	ThermalPlasma = 'ThermalPlasma'
	ThermalSpeed = 'ThermalSpeed'
	TimeOfFlight = 'TimeOfFlight'
	TimeSeries = 'TimeSeries'
	TotalPressure = 'TotalPressure'
	Ultraviolet = 'Ultraviolet'
	Unspecified = 'Unspecified'
	UpperHybridFrequency = 'UpperHybridFrequency'
	VCrossB = 'VCrossB'
	Velocity = 'Velocity'
	VolumeEmissionRate = 'VolumeEmissionRate'
	WaveformReceiver = 'WaveformReceiver'
	Wavelength = 'Wavelength'
	Waves = 'Waves'
	Waves_Active = 'Waves.Active'
	Waves_Passive = 'Waves.Passive'
	WebResource = 'WebResource'
	WebService = 'WebService'
	WhiteLight = 'WhiteLight'
	XRays = 'XRays'
class Qualifier(EnumTemplate):
	"""Characterizes the refinement to apply to a type or attribute of a quantity."""
	_schema = schema
	
	
	Incident = 'Incident'
	Anisotropy = 'Anisotropy'
	Array = 'Array'
	AutoSpectrum = 'AutoSpectrum'
	Average = 'Average'
	Characteristic = 'Characteristic'
	Circular = 'Circular'
	Coherence = 'Coherence'
	Column = 'Column'
	Component = 'Component'
	Component_I = 'Component.I'
	Component_J = 'Component.J'
	Component_K = 'Component.K'
	Confidence = 'Confidence'
	Core = 'Core'
	CrossSpectrum = 'CrossSpectrum'
	Deviation = 'Deviation'
	Differential = 'Differential'
	Direction = 'Direction'
	Directional = 'Directional'
	DirectionAngle = 'DirectionAngle'
	DirectionAngle_AzimuthAngle = 'DirectionAngle.AzimuthAngle'
	DirectionAngle_ElevationAngle = 'DirectionAngle.ElevationAngle'
	DirectionAngle_PolarAngle = 'DirectionAngle.PolarAngle'
	DirectionCosine = 'DirectionCosine'
	DirectionCosine_I = 'DirectionCosine.I'
	DirectionCosine_J = 'DirectionCosine.J'
	DirectionCosine_K = 'DirectionCosine.K'
	EncodedParameter = 'EncodedParameter'
	FieldAligned = 'FieldAligned'
	Fit = 'Fit'
	Group = 'Group'
	Halo = 'Halo'
	ImaginaryPart = 'ImaginaryPart'
	Integral = 'Integral'
	Integral_Area = 'Integral.Area'
	Integral_Bandwidth = 'Integral.Bandwidth'
	Integral_SolidAngle = 'Integral.SolidAngle'
	Linear = 'Linear'
	LineOfSight = 'LineOfSight'
	Magnitude = 'Magnitude'
	Maximum = 'Maximum'
	Median = 'Median'
	Minimum = 'Minimum'
	Moment = 'Moment'
	Parallel = 'Parallel'
	Peak = 'Peak'
	Perpendicular = 'Perpendicular'
	Perturbation = 'Perturbation'
	Phase = 'Phase'
	PhaseAngle = 'PhaseAngle'
	PowerSpectralDensity = 'PowerSpectralDensity'
	Projection = 'Projection'
	Projection_IJ = 'Projection.IJ'
	Projection_IK = 'Projection.IK'
	Projection_JK = 'Projection.JK'
	Pseudo = 'Pseudo'
	Ratio = 'Ratio'
	RealPart = 'RealPart'
	Scalar = 'Scalar'
	Spectral = 'Spectral'
	StandardDeviation = 'StandardDeviation'
	StokesParameters = 'StokesParameters'
	Strahl = 'Strahl'
	Superhalo = 'Superhalo'
	Symmetric = 'Symmetric'
	Tensor = 'Tensor'
	Total = 'Total'
	Trace = 'Trace'
	Uncertainty = 'Uncertainty'
	Variance = 'Variance'
	Vector = 'Vector'
class RenderingAxis(EnumTemplate):
	"""A reference component of a plot or rendering of data. A plot typically is a 2-D rendering with a horizontal axis and vertical axis. A third dimension can be introduced with a color coding of the rendered data."""
	_schema = schema
	
	
	ColorBar = 'ColorBar'
	Horizontal = 'Horizontal'
	Vertical = 'Vertical'
class Role(EnumTemplate):
	"""The assigned or assumed function or position of an individual."""
	_schema = schema
	
	
	Author = 'Author'
	ArchiveSpecialist = 'ArchiveSpecialist'
	CoInvestigator = 'CoInvestigator'
	CoPI = 'CoPI'
	Contributor = 'Contributor'
	DataProducer = 'DataProducer'
	DeputyPI = 'DeputyPI'
	Developer = 'Developer'
	FormerPI = 'FormerPI'
	GeneralContact = 'GeneralContact'
	HostContact = 'HostContact'
	InstrumentLead = 'InstrumentLead'
	InstrumentScientist = 'InstrumentScientist'
	MetadataContact = 'MetadataContact'
	MissionManager = 'MissionManager'
	MissionPrincipalInvestigator = 'MissionPrincipalInvestigator'
	PrincipalInvestigator = 'PrincipalInvestigator'
	ProgramManager = 'ProgramManager'
	ProgramScientist = 'ProgramScientist'
	ProjectEngineer = 'ProjectEngineer'
	ProjectManager = 'ProjectManager'
	ProjectScientist = 'ProjectScientist'
	Publisher = 'Publisher'
	Scientist = 'Scientist'
	TeamLeader = 'TeamLeader'
	TeamMember = 'TeamMember'
	TechnicalContact = 'TechnicalContact'
	User = 'User'
class Saturn(EnumTemplate):
	"""The sixth planet from the Sun in our solar system."""
	_schema = schema
	
	
	Dione = 'Dione'
	Enceladus = 'Enceladus'
	Iapetus = 'Iapetus'
	Magnetosphere = 'Magnetosphere'
	Magnetosphere_Magnetotail = 'Magnetosphere.Magnetotail'
	Magnetosphere_Main = 'Magnetosphere.Main'
	Magnetosphere_Plasmasphere = 'Magnetosphere.Plasmasphere'
	Magnetosphere_Polar = 'Magnetosphere.Polar'
	Magnetosphere_RadiationBelt = 'Magnetosphere.RadiationBelt'
	Magnetosphere_RingCurrent = 'Magnetosphere.RingCurrent'
	Mimas = 'Mimas'
	Rhea = 'Rhea'
	Tethys = 'Tethys'
	Titan = 'Titan'
class SavedQuantity(EnumTemplate):
	"""Quantities that are saved during a given diagnosis."""
	_schema = schema
	
	
	_2DCuts = '2DCuts'
	_3DCubes = '3DCubes'
	ACElectricField = 'ACElectricField'
	ACMagneticField = 'ACMagneticField'
	Absorption = 'Absorption'
	AdiabaticInvariant = 'AdiabaticInvariant'
	AdiabaticInvariant_MagneticMoment = 'AdiabaticInvariant.MagneticMoment'
	AdiabaticInvariant_BounceMotion = 'AdiabaticInvariant.BounceMotion'
	AdiabaticInvariant_DriftMotion = 'AdiabaticInvariant.DriftMotion'
	AkasofuEpsilon = 'AkasofuEpsilon'
	Albedo = 'Albedo'
	AlfvenMachNumber = 'AlfvenMachNumber'
	AlfvenVelocity = 'AlfvenVelocity'
	ArrivalDirection = 'ArrivalDirection'
	AtomicNumberDetected = 'AtomicNumberDetected'
	AverageChargeState = 'AverageChargeState'
	ChargeFlux = 'ChargeFlux'
	ChargeState = 'ChargeState'
	CountRate = 'CountRate'
	Counts = 'Counts'
	Current = 'Current'
	CurrentDensity = 'CurrentDensity'
	DopplerFrequency = 'DopplerFrequency'
	DynamicPressure = 'DynamicPressure'
	Electric = 'Electric'
	Electromagnetic = 'Electromagnetic'
	Emissivity = 'Emissivity'
	Energy = 'Energy'
	EnergyDensity = 'EnergyDensity'
	EnergyFlux = 'EnergyFlux'
	EnergyPerCharge = 'EnergyPerCharge'
	Entropy = 'Entropy'
	EquivalentWidth = 'EquivalentWidth'
	FlowSpeed = 'FlowSpeed'
	FlowVelocity = 'FlowVelocity'
	Fluence = 'Fluence'
	Frequency = 'Frequency'
	FrequencyToGyrofrequencyRatio = 'FrequencyToGyrofrequencyRatio'
	GeometricFactor = 'GeometricFactor'
	Gyrofrequency = 'Gyrofrequency'
	HeatFlux = 'HeatFlux'
	IMFClockAngle = 'IMFClockAngle'
	Intensity = 'Intensity'
	LShell = 'LShell'
	LineDepth = 'LineDepth'
	Lines = 'Lines'
	LowerHybridFrequency = 'LowerHybridFrequency'
	Magnetic = 'Magnetic'
	MagneticField = 'MagneticField'
	MagnetosonicMachNumber = 'MagnetosonicMachNumber'
	Mass = 'Mass'
	MassDensity = 'MassDensity'
	MassNumber = 'MassNumber'
	MassPerCharge = 'MassPerCharge'
	ModeAmplitude = 'ModeAmplitude'
	NumberDensity = 'NumberDensity'
	NumberFlux = 'NumberFlux'
	Other = 'Other'
	ParticleRadius = 'ParticleRadius'
	ParticleRigidity = 'ParticleRigidity'
	PhaseSpaceDensity = 'PhaseSpaceDensity'
	PlasmaBeta = 'PlasmaBeta'
	PlasmaFrequency = 'PlasmaFrequency'
	Polarization = 'Polarization'
	Potential = 'Potential'
	PoyntingFlux = 'PoyntingFlux'
	Pressure = 'Pressure'
	PropagationTime = 'PropagationTime'
	SolarUVFlux = 'SolarUVFlux'
	SonicMachNumber = 'SonicMachNumber'
	SoundSpeed = 'SoundSpeed'
	SpatialSeries = 'SpatialSeries'
	Spectra = 'Spectra'
	StokesParameters = 'StokesParameters'
	Temperature = 'Temperature'
	ThermalSpeed = 'ThermalSpeed'
	TimeSeries = 'TimeSeries'
	TotalPressure = 'TotalPressure'
	UpperHybridFrequency = 'UpperHybridFrequency'
	VCrossB = 'VCrossB'
	Velocity = 'Velocity'
	VolumeEmissionRate = 'VolumeEmissionRate'
	Wavelength = 'Wavelength'
class ScaleType(EnumTemplate):
	"""The scaling to apply to an axis. If this attribute is not present, linear scale should be assumed."""
	_schema = schema
	
	
	LinearScale = 'LinearScale'
	LogScale = 'LogScale'
class ModeledRegion(EnumTemplate):
	"""The portion of space modeled by the code at the time of a diagnosis. A region is distinguished by certain natural features or physical characteristics. It is the location of the observatory for in situ data, the location or region sensed by remote sensing observatories and the location-of-relevance for parameters that are derived from observational data."""
	_schema = schema
	
	
	Asteroid = 'Asteroid'
	Callisto = 'Callisto'
	Comet = 'Comet'
	Comet_1P_Halley = 'Comet.1P-Halley'
	Comet_26P_Grigg_Skjellerup = 'Comet.26P-Grigg-Skjellerup'
	Comet_67P_Churyumov_Gerasimenko = 'Comet.67P-Churyumov-Gerasimenko'
	Earth = 'Earth'
	Earth_Magnetosheath = 'Earth.Magnetosheath'
	Earth_Magnetosphere = 'Earth.Magnetosphere'
	Earth_Magnetosphere_Magnetotail = 'Earth.Magnetosphere.Magnetotail'
	Earth_Magnetosphere_Main = 'Earth.Magnetosphere.Main'
	Earth_Magnetosphere_Plasmasphere = 'Earth.Magnetosphere.Plasmasphere'
	Earth_Magnetosphere_Polar = 'Earth.Magnetosphere.Polar'
	Earth_Magnetosphere_RadiationBelt = 'Earth.Magnetosphere.RadiationBelt'
	Earth_Magnetosphere_RingCurrent = 'Earth.Magnetosphere.RingCurrent'
	Earth_Moon = 'Earth.Moon'
	Earth_NearSurface = 'Earth.NearSurface'
	Earth_NearSurface_Atmosphere = 'Earth.NearSurface.Atmosphere'
	Earth_NearSurface_AuroralRegion = 'Earth.NearSurface.AuroralRegion'
	Earth_NearSurface_EquatorialRegion = 'Earth.NearSurface.EquatorialRegion'
	Earth_NearSurface_Ionosphere = 'Earth.NearSurface.Ionosphere'
	Earth_NearSurface_Ionosphere_DRegion = 'Earth.NearSurface.Ionosphere.DRegion'
	Earth_NearSurface_Ionosphere_ERegion = 'Earth.NearSurface.Ionosphere.ERegion'
	Earth_NearSurface_Ionosphere_FRegion = 'Earth.NearSurface.Ionosphere.FRegion'
	Earth_NearSurface_Ionosphere_Topside = 'Earth.NearSurface.Ionosphere.Topside'
	Earth_NearSurface_Mesosphere = 'Earth.NearSurface.Mesosphere'
	Earth_NearSurface_MidLatitudeRegion = 'Earth.NearSurface.MidLatitudeRegion'
	Earth_NearSurface_Plasmasphere = 'Earth.NearSurface.Plasmasphere'
	Earth_NearSurface_PolarCap = 'Earth.NearSurface.PolarCap'
	Earth_NearSurface_SouthAtlanticAnomalyRegion = 'Earth.NearSurface.SouthAtlanticAnomalyRegion'
	Earth_NearSurface_Stratosphere = 'Earth.NearSurface.Stratosphere'
	Earth_NearSurface_SubAuroralRegion = 'Earth.NearSurface.SubAuroralRegion'
	Earth_NearSurface_Thermosphere = 'Earth.NearSurface.Thermosphere'
	Earth_NearSurface_Troposphere = 'Earth.NearSurface.Troposphere'
	Earth_Surface = 'Earth.Surface'
	Enceladus = 'Enceladus'
	Europa = 'Europa'
	Ganymede = 'Ganymede'
	Heliosphere = 'Heliosphere'
	Heliosphere_Heliosheath = 'Heliosphere.Heliosheath'
	Heliosphere_Inner = 'Heliosphere.Inner'
	Heliosphere_NearEarth = 'Heliosphere.NearEarth'
	Heliosphere_Outer = 'Heliosphere.Outer'
	Heliosphere_Remote1AU = 'Heliosphere.Remote1AU'
	Incident = 'Incident'
	Interstellar = 'Interstellar'
	Io = 'Io'
	Jupiter = 'Jupiter'
	Jupiter_Callisto = 'Jupiter.Callisto'
	Jupiter_Europa = 'Jupiter.Europa'
	Jupiter_Ganymede = 'Jupiter.Ganymede'
	Jupiter_Io = 'Jupiter.Io'
	Jupiter_Magnetosphere = 'Jupiter.Magnetosphere'
	Jupiter_Magnetosphere_Magnetotail = 'Jupiter.Magnetosphere.Magnetotail'
	Jupiter_Magnetosphere_Main = 'Jupiter.Magnetosphere.Main'
	Jupiter_Magnetosphere_Plasmasphere = 'Jupiter.Magnetosphere.Plasmasphere'
	Jupiter_Magnetosphere_Polar = 'Jupiter.Magnetosphere.Polar'
	Jupiter_Magnetosphere_RadiationBelt = 'Jupiter.Magnetosphere.RadiationBelt'
	Jupiter_Magnetosphere_RingCurrent = 'Jupiter.Magnetosphere.RingCurrent'
	Mars = 'Mars'
	Mars_Deimos = 'Mars.Deimos'
	Mars_Magnetosphere = 'Mars.Magnetosphere'
	Mars_Magnetosphere_Magnetotail = 'Mars.Magnetosphere.Magnetotail'
	Mars_Magnetosphere_Main = 'Mars.Magnetosphere.Main'
	Mars_Magnetosphere_Plasmasphere = 'Mars.Magnetosphere.Plasmasphere'
	Mars_Magnetosphere_Polar = 'Mars.Magnetosphere.Polar'
	Mars_Magnetosphere_RadiationBelt = 'Mars.Magnetosphere.RadiationBelt'
	Mars_Magnetosphere_RingCurrent = 'Mars.Magnetosphere.RingCurrent'
	Mars_Phobos = 'Mars.Phobos'
	Mercury = 'Mercury'
	Mercury_Magnetosphere = 'Mercury.Magnetosphere'
	Mercury_Magnetosphere_Magnetotail = 'Mercury.Magnetosphere.Magnetotail'
	Mercury_Magnetosphere_Main = 'Mercury.Magnetosphere.Main'
	Mercury_Magnetosphere_Plasmasphere = 'Mercury.Magnetosphere.Plasmasphere'
	Mercury_Magnetosphere_Polar = 'Mercury.Magnetosphere.Polar'
	Mercury_Magnetosphere_RadiationBelt = 'Mercury.Magnetosphere.RadiationBelt'
	Mercury_Magnetosphere_RingCurrent = 'Mercury.Magnetosphere.RingCurrent'
	Neptune = 'Neptune'
	Neptune_Magnetosphere = 'Neptune.Magnetosphere'
	Neptune_Magnetosphere_Magnetotail = 'Neptune.Magnetosphere.Magnetotail'
	Neptune_Magnetosphere_Main = 'Neptune.Magnetosphere.Main'
	Neptune_Magnetosphere_Plasmasphere = 'Neptune.Magnetosphere.Plasmasphere'
	Neptune_Magnetosphere_Polar = 'Neptune.Magnetosphere.Polar'
	Neptune_Magnetosphere_RadiationBelt = 'Neptune.Magnetosphere.RadiationBelt'
	Neptune_Magnetosphere_RingCurrent = 'Neptune.Magnetosphere.RingCurrent'
	Neptune_Proteus = 'Neptune.Proteus'
	Neptune_Triton = 'Neptune.Triton'
	Planet = 'Planet'
	Pluto = 'Pluto'
	Rhea = 'Rhea'
	Saturn = 'Saturn'
	Saturn_Dione = 'Saturn.Dione'
	Saturn_Enceladus = 'Saturn.Enceladus'
	Saturn_Iapetus = 'Saturn.Iapetus'
	Saturn_Magnetosphere = 'Saturn.Magnetosphere'
	Saturn_Magnetosphere_Magnetotail = 'Saturn.Magnetosphere.Magnetotail'
	Saturn_Magnetosphere_Main = 'Saturn.Magnetosphere.Main'
	Saturn_Magnetosphere_Plasmasphere = 'Saturn.Magnetosphere.Plasmasphere'
	Saturn_Magnetosphere_Polar = 'Saturn.Magnetosphere.Polar'
	Saturn_Magnetosphere_RadiationBelt = 'Saturn.Magnetosphere.RadiationBelt'
	Saturn_Magnetosphere_RingCurrent = 'Saturn.Magnetosphere.RingCurrent'
	Saturn_Mimas = 'Saturn.Mimas'
	Saturn_Rhea = 'Saturn.Rhea'
	Saturn_Tethys = 'Saturn.Tethys'
	Saturn_Titan = 'Saturn.Titan'
	Sun = 'Sun'
	Sun_Chromosphere = 'Sun.Chromosphere'
	Sun_Corona = 'Sun.Corona'
	Sun_Interior = 'Sun.Interior'
	Sun_Photosphere = 'Sun.Photosphere'
	Sun_TransitionRegion = 'Sun.TransitionRegion'
	Titan = 'Titan'
	Title = 'Title'
	Uranus = 'Uranus'
	Uranus_Ariel = 'Uranus.Ariel'
	Uranus_Magnetosphere = 'Uranus.Magnetosphere'
	Uranus_Magnetosphere_Magnetotail = 'Uranus.Magnetosphere.Magnetotail'
	Uranus_Magnetosphere_Main = 'Uranus.Magnetosphere.Main'
	Uranus_Magnetosphere_Plasmasphere = 'Uranus.Magnetosphere.Plasmasphere'
	Uranus_Magnetosphere_Polar = 'Uranus.Magnetosphere.Polar'
	Uranus_Magnetosphere_RadiationBelt = 'Uranus.Magnetosphere.RadiationBelt'
	Uranus_Magnetosphere_RingCurrent = 'Uranus.Magnetosphere.RingCurrent'
	Uranus_Miranda = 'Uranus.Miranda'
	Uranus_Oberon = 'Uranus.Oberon'
	Uranus_Puck = 'Uranus.Puck'
	Uranus_Titania = 'Uranus.Titania'
	Uranus_Umbriel = 'Uranus.Umbriel'
	Venus = 'Venus'
	Venus_Magnetosphere = 'Venus.Magnetosphere'
	Venus_Magnetosphere_Magnetotail = 'Venus.Magnetosphere.Magnetotail'
	Venus_Magnetosphere_Main = 'Venus.Magnetosphere.Main'
	Venus_Magnetosphere_Plasmasphere = 'Venus.Magnetosphere.Plasmasphere'
	Venus_Magnetosphere_Polar = 'Venus.Magnetosphere.Polar'
	Venus_Magnetosphere_RadiationBelt = 'Venus.Magnetosphere.RadiationBelt'
	Venus_Magnetosphere_RingCurrent = 'Venus.Magnetosphere.RingCurrent'
class ModelProduct(EnumTemplate):
	"""The type of product produced from the model."""
	_schema = schema
	
	
	_2DCuts = '2DCuts'
	_3DCubes = '3DCubes'
	Lines = 'Lines'
	SpatialSeries = 'SpatialSeries'
	Spectra = 'Spectra'
	TimeSeries = 'TimeSeries'
class ModelType(EnumTemplate):
	"""A characterization of the numerical scheme used in the model."""
	_schema = schema
	
	
	Empirical = 'Empirical'
	Hybrid = 'Hybrid'
	MHD = 'MHD'
	PIC = 'PIC'
	Paraboloid = 'Paraboloid'
	TestParticle = 'TestParticle'
class SourceType(EnumTemplate):
	"""A characterization of the function or purpose of the source."""
	_schema = schema
	
	
	Ancillary = 'Ancillary'
	Browse = 'Browse'
	Data = 'Data'
	Layout = 'Layout'
	Thumbnail = 'Thumbnail'
class SpecificModeledRegion(EnumTemplate):
	"""Identifiers for areas of the physical world which may be occupied or observed."""
	_schema = schema
	
	
	Callisto = 'Callisto'
	Enceladus = 'Enceladus'
	Europa = 'Europa'
	Ganymede = 'Ganymede'
	Io = 'Io'
	Planet = 'Planet'
	Rhea = 'Rhea'
	Titan = 'Titan'
	Incident = 'Incident'
	Title = 'Title'
class SpectralRange(EnumTemplate):
	"""The general term used to describe wavelengths or frequencies within a given span of values for those quantities."""
	_schema = schema
	
	
	CaK = 'CaK'
	ExtremeUltraviolet = 'ExtremeUltraviolet'
	FarUltraviolet = 'FarUltraviolet'
	GammaRays = 'GammaRays'
	Halpha = 'Halpha'
	HardXRays = 'HardXRays'
	He10830 = 'He10830'
	He304 = 'He304'
	Infrared = 'Infrared'
	K7699 = 'K7699'
	LBHBand = 'LBHBand'
	Microwave = 'Microwave'
	NaD = 'NaD'
	Ni6768 = 'Ni6768'
	Optical = 'Optical'
	RadioFrequency = 'RadioFrequency'
	SoftXRays = 'SoftXRays'
	Ultraviolet = 'Ultraviolet'
	WhiteLight = 'WhiteLight'
	XRays = 'XRays'
class Style(EnumTemplate):
	"""The manner in which a response from a URL is presented."""
	_schema = schema
	
	
	EPNTAP = 'EPNTAP'
	File = 'File'
	Git = 'Git'
	HAPI = 'HAPI'
	Listing = 'Listing'
	Search = 'Search'
	TAP = 'TAP'
	Template = 'Template'
	Overview = 'Overview'
	WebService = 'WebService'
class Sun(EnumTemplate):
	"""The star upon which our solar system is centered."""
	_schema = schema
	
	
	Chromosphere = 'Chromosphere'
	Corona = 'Corona'
	Interior = 'Interior'
	Photosphere = 'Photosphere'
	TransitionRegion = 'TransitionRegion'
class SupportQuantity(EnumTemplate):
	"""A characterization of the support information."""
	_schema = schema
	
	
	DataQuality = 'DataQuality'
	Housekeeping = 'Housekeeping'
	InstrumentMode = 'InstrumentMode'
	Orientation = 'Orientation'
	Other = 'Other'
	Positional = 'Positional'
	Remark = 'Remark'
	RotationMatrix = 'RotationMatrix'
	SpinPeriod = 'SpinPeriod'
	SpinPhase = 'SpinPhase'
	SpinRate = 'SpinRate'
	Telemetry = 'Telemetry'
	Temporal = 'Temporal'
	Velocity = 'Velocity'
	WebResource = 'WebResource'
	WebService = 'WebService'
class Symmetry(EnumTemplate):
	"""Symmetry of the model domain."""
	_schema = schema
	
	
	Axial = 'Axial'
	Central = 'Central'
	None_ = 'None'
	Plane = 'Plane'
class TemporalDependence(EnumTemplate):
	"""Whether the model results are obtained from a stationary solution or are dynamically computed."""
	_schema = schema
	
	
	No = 'No'
	Yes = 'Yes'
class Text(EnumTemplate):
	"""A sequence of characters which may have an imposed structure or organization."""
	_schema = schema
	
	
	ASCII = 'ASCII'
	Unicode = 'Unicode'
class Uranus(EnumTemplate):
	"""The eighth planet from the Sun in our solar system."""
	_schema = schema
	
	
	Ariel = 'Ariel'
	Magnetosphere = 'Magnetosphere'
	Magnetosphere_Magnetotail = 'Magnetosphere.Magnetotail'
	Magnetosphere_Main = 'Magnetosphere.Main'
	Magnetosphere_Plasmasphere = 'Magnetosphere.Plasmasphere'
	Magnetosphere_Polar = 'Magnetosphere.Polar'
	Magnetosphere_RadiationBelt = 'Magnetosphere.RadiationBelt'
	Magnetosphere_RingCurrent = 'Magnetosphere.RingCurrent'
	Miranda = 'Miranda'
	Oberon = 'Oberon'
	Puck = 'Puck'
	Titania = 'Titania'
	Umbriel = 'Umbriel'
class Venus(EnumTemplate):
	"""The second planet from the Sun in our solar system."""
	_schema = schema
	
	
	Magnetosphere = 'Magnetosphere'
	Magnetosphere_Magnetotail = 'Magnetosphere.Magnetotail'
	Magnetosphere_Main = 'Magnetosphere.Main'
	Magnetosphere_Plasmasphere = 'Magnetosphere.Plasmasphere'
	Magnetosphere_Polar = 'Magnetosphere.Polar'
	Magnetosphere_RadiationBelt = 'Magnetosphere.RadiationBelt'
	Magnetosphere_RingCurrent = 'Magnetosphere.RingCurrent'
class WaveQuantity(EnumTemplate):
	"""A characterization of the physical properties of a wave."""
	_schema = schema
	
	
	Absorption = 'Absorption'
	ACElectricField = 'ACElectricField'
	ACMagneticField = 'ACMagneticField'
	Albedo = 'Albedo'
	DopplerFrequency = 'DopplerFrequency'
	Emissivity = 'Emissivity'
	EnergyFlux = 'EnergyFlux'
	EquivalentWidth = 'EquivalentWidth'
	Frequency = 'Frequency'
	Gyrofrequency = 'Gyrofrequency'
	Intensity = 'Intensity'
	LineDepth = 'LineDepth'
	LowerHybridFrequency = 'LowerHybridFrequency'
	MagneticField = 'MagneticField'
	ModeAmplitude = 'ModeAmplitude'
	PlasmaFrequency = 'PlasmaFrequency'
	Polarization = 'Polarization'
	PoyntingFlux = 'PoyntingFlux'
	PropagationTime = 'PropagationTime'
	StokesParameters = 'StokesParameters'
	UpperHybridFrequency = 'UpperHybridFrequency'
	Velocity = 'Velocity'
	VolumeEmissionRate = 'VolumeEmissionRate'
	Wavelength = 'Wavelength'
class Waves(EnumTemplate):
	"""Data resulting from observations of wave experiments and natural wave phenomena. Wave experiments are typically active and natural wave phenomena are passive. Examples of wave experiments include coherent/incoherent scatter radars, radio soundings, VLF propagation studies, ionospheric scintillation of beacon satellite signals, etc. Examples of natural wave phenomena include micropulsations, mesospheric gravity waves, auroral/plasmaspheric hiss, Langmuir waves, AKR, Jovian decametric radiation, solar radio bursts, etc."""
	_schema = schema
	
	
	Active = 'Active'
	Passive = 'Passive'
class WaveType(EnumTemplate):
	"""A characterization of the carrier or phenomenon of wave information observed by the measurement."""
	_schema = schema
	
	
	Electromagnetic = 'Electromagnetic'
	Electrostatic = 'Electrostatic'
	Hydrodynamic = 'Hydrodynamic'
	MHD = 'MHD'
	Photon = 'Photon'
	PlasmaWaves = 'PlasmaWaves'