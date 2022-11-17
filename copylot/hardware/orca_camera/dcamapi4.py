# flake8: noqa
# dcamapi4.py : Jun 18, 2021
#
# Copyright (C) 2021 Hamamatsu Photonics K.K.. All right reserved.


import platform
from enum import IntEnum
from ctypes import *


# ==== load shared library ====

# abosorb platform dependency

__platform_system = platform.system()
if __platform_system == "Windows":
    __dll = windll.LoadLibrary("dcamapi.dll")
else:  # Linux
    __dll = cdll.LoadLibrary("/usr/local/lib/libdcamapi.so")


# ==== declare constants ====


class DCAMERR(IntEnum):
    # status error
    BUSY = -2147483391  # 0x80000101, API cannot process in busy state.
    NOTREADY = -2147483389  # 0x80000103, API requires ready state.
    NOTSTABLE = -2147483388  # 0x80000104, API requires stable or unstable state.
    UNSTABLE = -2147483387  # 0x80000105, API does not support in unstable state.
    NOTBUSY = -2147483385  # 0x80000107, API requires busy state.
    EXCLUDED = -2147483376  # 0x80000110, some resource is exclusive and already used
    COOLINGTROUBLE = -2147482878  # 0x80000302, something happens near cooler
    NOTRIGGER = (
        -2147482877
    )  # 0x80000303, no trigger when necessary. Some camera supports this error.
    TEMPERATURE_TROUBLE = -2147482876  # 0x80000304, camera warns its temperature
    TOOFREQUENTTRIGGER = (
        -2147482875
    )  # 0x80000305, input too frequent trigger. Some camera supports this error.
    # wait error
    ABORT = -2147483390  # 0x80000102, abort process
    TIMEOUT = -2147483386  # 0x80000106, timeout
    LOSTFRAME = -2147482879  # 0x80000301, frame data is lost
    MISSINGFRAME_TROUBLE = (
        -2147479802
    )  # 0x80000f06, frame is lost but reason is low lever driver's bug
    INVALIDIMAGE = -2147482847  # 0x80000321, hpk format data is invalid data
    # initialization error
    NORESOURCE = -2147483135  # 0x80000201, not enough resource except memory
    NOMEMORY = -2147483133  # 0x80000203, not enough memory
    NOMODULE = -2147483132  # 0x80000204, no sub module
    NODRIVER = -2147483131  # 0x80000205, no driver
    NOCAMERA = -2147483130  # 0x80000206, no camera
    NOGRABBER = -2147483129  # 0x80000207, no grabber
    NOCOMBINATION = -2147483128  # 0x80000208, no combination on registry
    FAILOPEN = -2147479551  # 0x80001001, DEPRECATED
    FRAMEGRABBER_NEEDS_FIRMWAREUPDATE = (
        -2147479550
    )  # 0x80001002, need to update frame grabber firmware to use the camera
    INVALIDMODULE = -2147483119  # 0x80000211, dcam_init() found invalid module
    INVALIDCOMMPORT = -2147483118  # 0x80000212, invalid serial port
    FAILOPENBUS = -2130702335  # 0x81001001, the bus or driver are not available
    FAILOPENCAMERA = -2113925119  # 0x82001001, camera report error during opening
    DEVICEPROBLEM = -2113925118  # 0x82001002, initialization failed(for maico)
    # calling error
    INVALIDCAMERA = -2147481594  # 0x80000806, invalid camera
    INVALIDHANDLE = -2147481593  # 0x80000807, invalid camera handle
    INVALIDPARAM = -2147481592  # 0x80000808, invalid parameter
    INVALIDVALUE = -2147481567  # 0x80000821, invalid property value
    OUTOFRANGE = -2147481566  # 0x80000822, value is out of range
    NOTWRITABLE = -2147481565  # 0x80000823, the property is not writable
    NOTREADABLE = -2147481564  # 0x80000824, the property is not readable
    INVALIDPROPERTYID = -2147481563  # 0x80000825, the property id is invalid
    NEWAPIREQUIRED = (
        -2147481562
    )  # 0x80000826, old API cannot present the value because only new API need to be used
    WRONGHANDSHAKE = (
        -2147481561
    )  # 0x80000827, this error happens DCAM get error code from camera unexpectedly
    NOPROPERTY = (
        -2147481560
    )  # 0x80000828, there is no altenative or influence id, or no more property id
    INVALIDCHANNEL = (
        -2147481559
    )  # 0x80000829, the property id specifies channel but channel is invalid
    INVALIDVIEW = (
        -2147481558
    )  # 0x8000082a, the property id specifies channel but channel is invalid
    INVALIDSUBARRAY = (
        -2147481557
    )  # 0x8000082b, the combination of subarray values are invalid. e.g. DCAM_IDPROP_SUBARRAYHPOS + DCAM_IDPROP_SUBARRAYHSIZE is greater than the number of horizontal pixel of sensor.
    ACCESSDENY = (
        -2147481556
    )  # 0x8000082c, the property cannot access during this DCAM STATUS
    NOVALUETEXT = -2147481555  # 0x8000082d, the property does not have value text
    WRONGPROPERTYVALUE = -2147481554  # 0x8000082e, at least one property value is wrong
    DISHARMONY = (
        -2147481552
    )  # 0x80000830, the paired camera does not have same parameter
    FRAMEBUNDLESHOULDBEOFF = (
        -2147481550
    )  # 0x80000832, framebundle mode should be OFF under current property settings
    INVALIDFRAMEINDEX = -2147481549  # 0x80000833, the frame index is invalid
    INVALIDSESSIONINDEX = -2147481548  # 0x80000834, the session index is invalid
    NOCORRECTIONDATA = (
        -2147481544
    )  # 0x80000838, not take the dark and shading correction data yet.
    CHANNELDEPENDENTVALUE = (
        -2147481543
    )  # 0x80000839, each channel has own property value so can't return overall property value.
    VIEWDEPENDENTVALUE = (
        -2147481542
    )  # 0x8000083a, each view has own property value so can't return overall property value.
    NODEVICEBUFFER = (
        -2147481541
    )  # 0x8000083b, the frame count is larger than device momory size on using device memory.
    REQUIREDSNAP = (
        -2147481540
    )  # 0x8000083c, the capture mode is sequence on using device memory.
    LESSSYSTEMMEMORY = (
        -2147481537
    )  # 0x8000083f, the sysmte memory size is too small. PC doesn't have enough memory or is limited memory by 32bit OS.
    NOTSUPPORT = (
        -2147479805
    )  # 0x80000f03, camera does not support the function or property with current settings
    # camera or bus trouble
    FAILREADCAMERA = -2097147902  # 0x83001002, failed to read data from camera
    FAILWRITECAMERA = -2097147901  # 0x83001003, failed to write data to the camera
    CONFLICTCOMMPORT = -2097147900  # 0x83001004, conflict the com port name user set
    OPTICS_UNPLUGGED = (
        -2097147899
    )  # 0x83001005, Optics part is unplugged so please check it.
    FAILCALIBRATION = -2097147898  # 0x83001006, fail calibration
    MISMATCH_CONFIGURATION = (
        -2097147887
    )  # 0x83001011, mismatch between camera output(connection) and frame grabber specs
    # 0x84000100 - 0x840001FF, DCAMERR_INVALIDMEMBER_x
    INVALIDMEMBER_3 = -2080374525  # 0x84000103, 3th member variable is invalid value
    INVALIDMEMBER_5 = -2080374523  # 0x84000105, 5th member variable is invalid value
    INVALIDMEMBER_7 = -2080374521  # 0x84000107, 7th member variable is invalid value
    INVALIDMEMBER_8 = -2080374520  # 0x84000108, 7th member variable is invalid value
    INVALIDMEMBER_9 = -2080374519  # 0x84000109, 9th member variable is invalid value
    FAILEDOPENRECFILE = -2080370687  # 0x84001001, DCAMREC failed to open the file
    INVALIDRECHANDLE = -2080370686  # 0x84001002, DCAMREC is invalid handle
    FAILEDWRITEDATA = -2080370685  # 0x84001003, DCAMREC failed to write the data
    FAILEDREADDATA = -2080370684  # 0x84001004, DCAMREC failed to read the data
    NOWRECORDING = -2080370683  # 0x84001005, DCAMREC is recording data now
    WRITEFULL = -2080370682  # 0x84001006, DCAMREC writes full frame of the session
    ALREADYOCCUPIED = (
        -2080370681
    )  # 0x84001007, DCAMREC handle is already occupied by other HDCAM
    TOOLARGEUSERDATASIZE = (
        -2080370680
    )  # 0x84001008, DCAMREC is set the large value to user data size
    INVALIDWAITHANDLE = -2080366591  # 0x84002001, DCAMWAIT is invalid handle
    NEWRUNTIMEREQUIRED = (
        -2080366590
    )  # 0x84002002, DCAM Module Version is older than the version that the camera requests
    VERSIONMISMATCH = (
        -2080366589
    )  # 0x84002003, Camre returns the error on setting parameter to limit version
    RUNAS_FACTORYMODE = -2080366588  # 0x84002004, Camera is running as a factory mode
    IMAGE_UNKNOWNSIGNATURE = (
        -2080362495
    )  # 0x84003001, sigunature of image header is unknown or corrupted
    IMAGE_NEWRUNTIMEREQUIRED = (
        -2080362494
    )  # 0x84003002, version of image header is newer than version that used DCAM supports
    IMAGE_ERRORSTATUSEXIST = -2080362493  # 0x84003003, image header stands error status
    IMAGE_HEADERCORRUPTED = -2080358396  # 0x84004004, image header value is strange
    IMAGE_BROKENCONTENT = -2080358395  # 0x84004005, image content is corrupted
    # calling error for DCAM-API 2.1.3
    UNKNOWNMSGID = -2147481599  # 0x80000801, unknown message id
    UNKNOWNSTRID = -2147481598  # 0x80000802, unknown string id
    UNKNOWNPARAMID = -2147481597  # 0x80000803, unkown parameter id
    UNKNOWNBITSTYPE = -2147481596  # 0x80000804, unknown bitmap bits type
    UNKNOWNDATATYPE = -2147481595  # 0x80000805, unknown frame data type
    # internal error
    NONE = 0  # 0, no error, nothing to have done
    INSTALLATIONINPROGRESS = -2147479808  # 0x80000f00, installation progress
    UNREACH = -2147479807  # 0x80000f01, internal error
    UNLOADED = -2147479804  # 0x80000f04, calling after process terminated
    THRUADAPTER = -2147479803  # 0x80000f05
    NOCONNECTION = -2147479801  # 0x80000f07, HDCAM lost connection to camera
    NOTIMPLEMENT = -2147479806  # 0x80000f02, not yet implementation
    DELAYEDFRAME = (
        -2147479799
    )  # 0x80000f09, the frame waiting re-load from hardware buffer with SNAPSHOT of DEVICEBUFFER MODE
    DEVICEINITIALIZING = -1342177279  # 0xb0000001
    APIINIT_INITOPTIONBYTES = (
        -1543438333
    )  # 0xa4010003, DCAMAPI_INIT::initoptionbytes is invalid
    APIINIT_INITOPTION = -1543438332  # 0xa4010004, DCAMAPI_INIT::initoption is invalid
    INITOPTION_COLLISION_BASE = -1543389184  # 0xa401C000
    INITOPTION_COLLISION_MAX = -1543372801  # 0xa401FFFF
    # Between DCAMERR_INITOPTION_COLLISION_BASE and DCAMERR_INITOPTION_COLLISION_MAX means there is collision with initoption in DCAMAPI_INIT.
    # The value "(error code) - DCAMERR_INITOPTION_COLLISION_BASE" indicates the index which second INITOPTION group happens.
    MISSPROP_TRIGGERSOURCE = (
        -535822064
    )  # 0xE0100110, the trigger mode is internal or syncreadout on using device memory.
    # success
    SUCCESS = (
        1  # 1, no error, general success code, app should check the value is positive
    )

    ALREADYINITIALIZED = -520093695  # 0xE1000001
    ALREADYOPENED = -520093694  # 0xE1000002
    INVALIDPIXELTYPE = -520093440  # 0xE1000100

    SUCCESS_PROP_GETATTR = 88  # dcamprop_getattr() returns this value at SUCCESS

    def is_failed(self):
        return True if int(self) < 0 else False

    def is_timeout(self):
        return True if int(self) == DCAMERR.TIMEOUT else False


class DCAM_PIXELTYPE(IntEnum):
    NONE = 0  # no pixeltype specified
    MONO8 = 1  # B/W 8 bit
    MONO16 = 2  # B/W 16 bit


class DCAMCAP_STATUS(IntEnum):
    ERROR = 0x0000
    BUSY = 0x0001
    READY = 0x0002
    STABLE = 0x0003
    UNSTABLE = 0x0004


class DCAMWAIT_CAPEVENT(IntEnum):
    TRANSFERRED = 0x0001
    FRAMEREADY = 0x0002
    CYCLEEND = 0x0004
    EXPOSUREEND = 0x0008
    STOPPED = 0x0010


class DCAMWAIT_RECEVENT(IntEnum):
    STOPPED = 0x0100
    WARNING = 0x0200
    MISSED = 0x0400
    DISKFULL = 0x1000
    WRITEFAULT = 0x2000
    SKIPPED = 0x4000


class DCAMCAP_START(IntEnum):
    SEQUENCE = -1
    SNAP = 0


class DCAM_IDSTR(IntEnum):
    BUS = 0x04000101
    CAMERAID = 0x04000102
    VENDOR = 0x04000103
    MODEL = 0x04000104
    CAMERAVERSION = 0x04000105
    DRIVERVERSION = 0x04000106
    MODULEVERSION = 0x04000107
    DCAMAPIVERSION = 0x04000108
    CAMERA_SERIESNAME = 0x0400012C


class DCAMAPI_INITOPTION(IntEnum):
    """
    Initialize parameter.
    """

    APIVER__LATEST = 0x00000001
    APIVER__4_0 = 0x00000400
    ENDMARK = 0x00000000


class DCAM_CODEPAGE(IntEnum):
    SHIFT_JIS = 932  # Shift JIS
    UTF16_LE = 1200  # UTF-16 (Little Endian)
    UTF16_BE = 1201  # UTF-16 (Big Endian)
    UTF7 = 65000  # UTF-7 translation
    UTF8 = 65001  # UTF-8 translation
    NONE = 0


class DCAM_IDPROP(IntEnum):
    # 0x00000000 - 0x00100000, reserved
    # Group: TIMING
    TRIGGERSOURCE = 1048848  # 0x00100110, R/W, mode,   "TRIGGER SOURCE"
    TRIGGERACTIVE = 1048864  # 0x00100120, R/W, mode,   "TRIGGER ACTIVE"
    TRIGGER_MODE = 1049104  # 0x00100210, R/W, mode,    "TRIGGER MODE"
    TRIGGERPOLARITY = 1049120  # 0x00100220, R/W, mode, "TRIGGER POLARITY"
    TRIGGER_CONNECTOR = 1049136  # 0x00100230, R/W, mode,   "TRIGGER CONNECTOR"
    TRIGGERTIMES = 1049152  # 0x00100240, R/W, long,    "TRIGGER TIMES"
    # 0x00100250 is reserved
    TRIGGERDELAY = 1049184  # 0x00100260, R/W, sec, "TRIGGER DELAY"
    INTERNALTRIGGER_HANDLING = 1049200  # 0x00100270
    TRIGGERMULTIFRAME_COUNT = 1049216  # 0x00100280
    SYNCREADOUT_SYSTEMBLANK = (
        1049232  # 0x00100290, R/W, mode, "SYNC READOUT SYSTEM BLANK"
    )
    TRIGGERENABLE_ACTIVE = 1049616  # 0x00100410, R/W, mode,    "TRIGGER ENABLE ACTIVE"
    TRIGGERENABLE_POLARITY = 1049632  # 0x00100420
    TRIGGERNUMBER_FORFIRSTIMAGE = (
        1050640  # 0x00100810, R/O, long, "TRIGGER NUMBER FOR FIRST IMAGE"
    )
    TRIGGERNUMBER_FORNEXTIMAGE = (
        1050656  # 0x00100820, R/O, long,  "TRIGGER NUMBER FOR NEXT IMAGE"
    )
    NUMBEROF_OUTPUTTRIGGERCONNECTOR = 1835024  # 0x001C0010
    OUTPUTTRIGGER_CHANNELSYNC = (
        1835056  # 0x001C0030, R/W, mode,   "OUTPUT TRIGGER CHANNEL SYNC"
    )
    OUTPUTTRIGGER_PROGRAMABLESTART = (
        1835088  # 0x001C0050, R/W, mode,  "OUTPUT TRIGGER PROGRAMABLE START"
    )
    OUTPUTTRIGGER_SOURCE = 1835280  # 0x001C0110, R/W, mode,    "OUTPUT TRIGGER SOURCE"
    OUTPUTTRIGGER_POLARITY = (
        1835296  # 0x001C0120, R/W, mode,  "OUTPUT TRIGGER POLARITY"
    )
    OUTPUTTRIGGER_ACTIVE = 1835312  # 0x001C0130, R/W, mode,    "OUTPUT TRIGGER ACTIVE"
    OUTPUTTRIGGER_DELAY = 1835328  # 0x001C0140, R/W, sec,  "OUTPUT TRIGGER DELAY"
    OUTPUTTRIGGER_PERIOD = 1835344  # 0x001C0150, R/W, sec, "OUTPUT TRIGGER PERIOD"
    OUTPUTTRIGGER_KIND = 1835360  # 0x001C0160, R/W, mode,  "OUTPUT TRIGGER KIND"
    OUTPUTTRIGGER_BASESENSOR = (
        1835376  # 0x001C0170, R/W, mode,    "OUTPUT TRIGGER BASE SENSOR"
    )
    OUTPUTTRIGGER_PREHSYNCCOUNT = (
        1835408  # 0x001C0190, R/W, mode, "OUTPUT TRIGGER PRE HSYNC COUNT"
    )
    # - 0x001C10FF for 16 output trigger connector, reserved
    _OUTPUTTRIGGER = (
        256  # 0x00000100, the offset of ID for Nth OUTPUT TRIGGER parameter
    )
    MASTERPULSE_MODE = 1966112  # 0x001E0020, R/W, mode,    "MASTER PULSE MODE"
    MASTERPULSE_TRIGGERSOURCE = (
        1966128  # 0x001E0030, R/W, mode,   "MASTER PULSE TRIGGER SOURCE"
    )
    MASTERPULSE_INTERVAL = 1966144  # 0x001E0040, R/W, sec, "MASTER PULSE INTERVAL"
    MASTERPULSE_BURSTTIMES = (
        1966160  # 0x001E0050, R/W, long,  "MASTER PULSE BURST TIMES"
    )
    # Group: FEATURE
    # exposure period
    EXPOSURETIME = 2031888  # 0x001F0110, R/W, sec, "EXPOSURE TIME"
    EXPOSURETIME_CONTROL = 2031920  # 0x001F0130, R/W, mode,    "EXPOSURE TIME CONTROL"
    TRIGGER_FIRSTEXPOSURE = 2032128  # 0x001F0200, R/W, mode,   "TRIGGER FIRST EXPOSURE"
    TRIGGER_GLOBALEXPOSURE = (
        2032384  # 0x001F0300, R/W, mode,  "TRIGGER GLOBAL EXPOSURE"
    )
    FIRSTTRIGGER_BEHAVIOR = 2032400  # 0x001F0310, R/W, mode,   "FIRST TRIGGER BEHAVIOR"
    MULTIFRAME_EXPOSURE = 2035712  # 0x001F1000, R/W, sec,  "MULTI FRAME EXPOSURE TIME"
    # - 0x001F1FFF for 256 MULTI FRAME
    _MULTIFRAME = 16  # 0x00000010, the offset of ID for Nth MULTIFRAME
    # anti-blooming
    LIGHTMODE = 2097424  # 0x00200110, R/W, mode,   "LIGHT MODE"
    # 0x00200120 is reserved
    # sensitivity
    SENSITIVITYMODE = 2097680  # 0x00200210, R/W, mode, "SENSITIVITY MODE"
    SENSITIVITY = 2097696  # 0x00200220, R/W, long, "SENSITIVITY"
    DIRECTEMGAIN_MODE = 2097744  # 0x00200250, R/W, mode,   "DIRECT EM GAIN MODE"
    EMGAINWARNING_STATUS = 2097760  # 0x00200260
    EMGAINWARNING_LEVEL = 2097776  # 0x00200270, R/W, long, "EM GAIN WARNING LEVEL"
    EMGAINWARNING_ALARM = 2097792  # 0x00200280, R/W, mode, "EM GAIN WARNING ALARM"
    EMGAINPROTECT_MODE = 2097808  # 0x00200290, R/W, mode,  "EM GAIN PROTECT MODE"
    EMGAINPROTECT_AFTERFRAMES = (
        2097824  # 0x002002A0, R/W, long,   "EM GAIN PROTECT AFTER FRAMES"
    )
    MEASURED_SENSITIVITY = 2097840  # 0x002002B0, R/O, real,    "MEASURED SENSITIVITY"
    PHOTONIMAGINGMODE = 2097904  # 0x002002F0, R/W, mode,   "PHOTON IMAGING MODE"
    # sensor cooler
    SENSORTEMPERATURE = 2097936  # 0x00200310, R/O, celsius,"SENSOR TEMPERATURE"
    SENSORCOOLER = 2097952  # 0x00200320, R/W, mode,    "SENSOR COOLER"
    SENSORTEMPERATURETARGET = (
        2097968  # 0x00200330, R/W, celsius,"SENSOR TEMPERATURE TARGET"
    )
    SENSORCOOLERSTATUS = 2097984  # 0x00200340, R/O, mode,  "SENSOR COOLER STATUS"
    SENSORCOOLERFAN = 2098000  # 0x00200350, R/W, mode, "SENSOR COOLER FAN"
    SENSORTEMPERATURE_AVE = 2098016  # 0x00200360, R/O, celsius,"SENSOR TEMPERATURE AVE"
    SENSORTEMPERATURE_MIN = 2098032  # 0x00200370, R/O, celsius,"SENSOR TEMPERATURE MIN"
    SENSORTEMPERATURE_MAX = 2098048  # 0x00200380, R/O, celsius,"SENSOR TEMPERATURE MAX"
    SENSORTEMPERATURE_STATUS = (
        2098064  # 0x00200390, R/O, mode,    "SENSOR TEMPERATURE STATUS"
    )
    SENSORTEMPERATURE_PROTECT = (
        2098176  # 0x00200400, R/W, mode,   "SENSOR TEMPERATURE MODE"
    )
    # mechanical shutter
    MECHANICALSHUTTER = 2098192  # 0x00200410, R/W, mode,   "MECHANICAL SHUTTER"
    # contrast enhance
    CONTRASTGAIN = 3146016  # 0x00300120, R/W, long,    "CONTRAST GAIN"
    CONTRASTOFFSET = 3146032  # 0x00300130, R/W, long,  "CONTRAST OFFSET"
    # 0x00300140 is reserved
    HIGHDYNAMICRANGE_MODE = (
        3146064  # 0x00300150, R/W, mode,   "HIGH DYNAMIC RANGE MODE"
    )
    DIRECTGAIN_MODE = 3146080  # 0x00300160, R/W, mode, "DIRECT GAIN MODE"
    REALTIMEGAINCORRECT_MODE = (
        3146096  # 0x00300170, R/W,  mode,   "REALTIME GAIN CORRECT MODE"
    )
    REALTIMEGAINCORRECT_LEVEL = (
        3146112  # 0x00300180, R/W, mode,   "REALTIME GAIN CORRECT LEVEL"
    )
    REALTIMEGAINCORRECT_INTERVAL = (
        3146128  # 0x00300190, R/W,  mode,   "REALTIME GAIN CORRECT INTERVAL"
    )
    NUMBEROF_REALTIMEGAINCORRECTREGION = 3146144  # 0x003001A0
    # color features
    VIVIDCOLOR = 3146240  # 0x00300200, R/W, mode,  "VIVID COLOR"
    WHITEBALANCEMODE = 3146256  # 0x00300210, R/W, mode,    "WHITEBALANCE MODE"
    WHITEBALANCETEMPERATURE = (
        3146272  # 0x00300220, R/W, color-temp., "WHITEBALANCE TEMPERATURE"
    )
    WHITEBALANCEUSERPRESET = (
        3146288  # 0x00300230, R/W, long,  "WHITEBALANCE USER PRESET"
    )
    # 0x00300310 is reserved
    REALTIMEGAINCORRECTREGION_HPOS = (
        3149824  # 0x00301000, R/W,    long,   "REALTIME GAIN CORRECT REGION HPOS"
    )
    REALTIMEGAINCORRECTREGION_HSIZE = (
        3153920  # 0x00302000, R/W,   long,   "REALTIME GAIN CORRECT REGION HSIZE"
    )
    _REALTIMEGAINCORRECTIONREGION = 16  # 0x00000010, the offset of ID for Nth REALTIME GAIN CORRECT REGION parameter
    # Group: ALU
    # ALU
    INTERFRAMEALU_ENABLE = 3670032  # 0x00380010, R/W, mode,    "INTERFRAME ALU ENABLE"
    RECURSIVEFILTER = 3670288  # 0x00380110, R/W, mode, "RECURSIVE FILTER"
    RECURSIVEFILTERFRAMES = 3670304  # 0x00380120
    SPOTNOISEREDUCER = 3670320  # 0x00380130, R/W, mode,    "SPOT NOISE REDUCER"
    SUBTRACT = 3670544  # 0x00380210, R/W, mode,    "SUBTRACT"
    SUBTRACTIMAGEMEMORY = 3670560  # 0x00380220, R/W, mode, "SUBTRACT IMAGE MEMORY"
    STORESUBTRACTIMAGETOMEMORY = (
        3670576  # 0x00380230, W/O, mode,  "STORE SUBTRACT IMAGE TO MEMORY"
    )
    SUBTRACTOFFSET = 3670592  # 0x00380240, R/W, long   "SUBTRACT OFFSET"
    DARKCALIB_STABLEMAXINTENSITY = (
        3670608  # 0x00380250, R/W, long,    "DARKCALIB STABLE MAX INTENSITY"
    )
    SUBTRACT_DATASTATUS = 3670768  # 0x003802F0, R/W    mode,   "SUBTRACT DATA STATUS"
    SHADINGCALIB_DATASTATUS = (
        3670784  # 0x00380300, R/W    mode,   "SHADING CALIB DATA STATUS"
    )
    SHADINGCORRECTION = 3670800  # 0x00380310, R/W, mode,   "SHADING CORRECTION"
    SHADINGCALIBDATAMEMORY = (
        3670816  # 0x00380320, R/W, mode,  "SHADING CALIB DATA MEMORY"
    )
    STORESHADINGCALIBDATATOMEMORY = (
        3670832  # 0x00380330, W/O, mode,   "STORE SHADING DATA TO MEMORY"
    )
    SHADINGCALIB_METHOD = 3670848  # 0x00380340, R/W, mode, "SHADING CALIB METHOD"
    SHADINGCALIB_TARGET = 3670864  # 0x00380350, R/W, long, "SHADING CALIB TARGET"
    SHADINGCALIB_STABLEMININTENSITY = (
        3670880  # 0x00380360, R/W, long, "SHADING CALIB STABLE MIN INTENSITY"
    )
    SHADINGCALIB_SAMPLES = 3670896  # 0x00380370, R/W, long,    "SHADING CALIB SAMPLES"
    SHADINGCALIB_STABLESAMPLES = (
        3670912  # 0x00380380, R/W, long,  "SHADING CALIB STABLE SAMPLES"
    )
    SHADINGCALIB_STABLEMAXERRORPERCENT = (
        3670928  # 0x00380390, R/W, long,  "SHADING CALIB STABLE MAX ERROR PERCENT"
    )
    FRAMEAVERAGINGMODE = 3670944  # 0x003803A0, R/W, mode,  "FRAME AVERAGING MODE"
    FRAMEAVERAGINGFRAMES = 3670960  # 0x003803B0
    DARKCALIB_STABLESAMPLES = (
        3670976  # 0x003803C0, R/W, long, "DARKCALIB STABLE SAMPLES"
    )
    DARKCALIB_SAMPLES = 3670992  # 0x003803D0, R/W, long,   "DARKCALIB SAMPLES"
    DARKCALIB_TARGET = 3671008  # 0x003803E0, R/W, long,    "DARKCALIB TARGET"
    CAPTUREMODE = 3671056  # 0x00380410, R/W, mode, "CAPTURE MODE"
    LINEAVERAGING = 3671120  # 0x00380450, R/W, long,   "LINE AVERAGING"
    INTENSITYLUT_MODE = 3671312  # 0x00380510, R/W, mode,   "INTENSITY LUT MODE"
    INTENSITYLUT_PAGE = 3671328  # 0x00380520, R/W, long,   "INTENSITY LUT PAGE"
    INTENSITYLUT_WHITECLIP = (
        3671344  # 0x00380530, R/W, long,  "INTENSITY LUT WHITE CLIP"
    )
    INTENSITYLUT_BLACKCLIP = (
        3671360  # 0x00380540, R/W, long,  "INTENSITY LUT BLACK CLIP"
    )
    INTENSITY_GAMMA = 3671392  # 0x00380560, R/W, real, "INTENSITY GAMMA"
    SENSORGAPCORRECT_MODE = (
        3671584  # 0x00380620, R/W, long,   "SENSOR GAP CORRECT MODE"
    )
    ADVANCEDEDGEENHANCEMENT_MODE = (
        3671600  # 0x00380630, R/W, mode,    "ADVANCED EDGE ENHANCEMENT MODE"
    )
    ADVANCEDEDGEENHANCEMENT_LEVEL = (
        3671616  # 0x00380640, R/W, long,   "ADVANCED EDGE ENHANCEMENT LEVEL"
    )
    # TAP CALIBRATION
    TAPGAINCALIB_METHOD = 3673872  # 0x00380F10, R/W, mode, "TAP GAIN CALIB METHOD"
    TAPCALIB_BASEDATAMEMORY = 3673888  # 0x00380F20
    STORETAPCALIBDATATOMEMORY = 3673904  # 0x00380F30
    TAPCALIBDATAMEMORY = 3673920  # 0x00380F40, W/O, mode,  "TAP CALIB DATA MEMORY"
    NUMBEROF_TAPCALIB = 3674096  # 0x00380FF0, R/W, long,   "NUMBER OF TAP CALIB"
    TAPCALIB_GAIN = 3674112  # 0x00381000, R/W, mode,   "TAP CALIB GAIN"
    TAPCALIB_OFFSET = 3678208  # 0x00382000, R/W, mode, "TAP CALIB OFFSET"
    _TAPCALIB = 16  # 0x00000010, the offset of ID for Nth TAPCALIB
    # Group: READOUT
    # readout speed
    READOUTSPEED = 4194576  # 0x00400110, R/W, long,    "READOUT SPEED"
    # 0x00400120 is reserved
    READOUT_DIRECTION = 4194608  # 0x00400130, R/W, mode,   "READOUT DIRECTION"
    READOUT_UNIT = 4194624  # 0x00400140, R/O, mode,    "READOUT UNIT"
    SHUTTER_MODE = 4194640  # 0x00400150, R/W, mode,    "SHUTTER MODE"
    # sensor mode
    SENSORMODE = 4194832  # 0x00400210, R/W, mode,  "SENSOR MODE"
    SENSORMODE_LINEBUNDLEHEIGHT = (
        4194896  # 0x00400250, R/W, long, "SENSOR MODE LINE BUNDLEHEIGHT"
    )
    SENSORMODE_PANORAMICSTARTV = (
        4194944  # 0x00400280, R/W, long,  "SENSOR MODE PANORAMIC START V"
    )
    # other readout mode
    CCDMODE = 4195088  # 0x00400310, R/W, mode, "CCD MODE"
    EMCCD_CALIBRATIONMODE = (
        4195104  # 0x00400320, R/W, mode,   "EM CCD CALIBRATION MODE"
    )
    CMOSMODE = 4195152  # 0x00400350, R/W, mode,    "CMOS MODE"
    # output mode
    OUTPUT_INTENSITY = 4195344  # 0x00400410, R/W, mode,    "OUTPUT INTENSITY"
    OUTPUTDATA_OPERATION = 4195392  # 0x00400440, R/W, mode,    "OUTPUT DATA OPERATION"
    TESTPATTERN_KIND = 4195600  # 0x00400510, R/W, mode,    "TEST PATTERN KIND"
    TESTPATTERN_OPTION = 4195616  # 0x00400520, R/W, long,  "TEST PATTERN OPTION"
    EXTRACTION_MODE = 4195872  # 0x00400620
    # Group: ROI
    # binning and subarray
    BINNING = 4198672  # 0x00401110, R/W, mode, "BINNING"
    BINNING_INDEPENDENT = 4198688  # 0x00401120, R/W, mode, "BINNING INDEPENDENT"
    BINNING_HORZ = 4198704  # 0x00401130, R/W, long,    "BINNING HORZ"
    BINNING_VERT = 4198720  # 0x00401140, R/W, long,    "BINNING VERT"
    SUBARRAYHPOS = 4202768  # 0x00402110, R/W, long,    "SUBARRAY HPOS"
    SUBARRAYHSIZE = 4202784  # 0x00402120, R/W, long,   "SUBARRAY HSIZE"
    SUBARRAYVPOS = 4202800  # 0x00402130, R/W, long,    "SUBARRAY VPOS"
    SUBARRAYVSIZE = 4202816  # 0x00402140, R/W, long,   "SUBARRAY VSIZE"
    SUBARRAYMODE = 4202832  # 0x00402150, R/W, mode,    "SUBARRAY MODE"
    DIGITALBINNING_METHOD = 4202848  # 0x00402160, R/W, mode,   "DIGITALBINNING METHOD"
    DIGITALBINNING_HORZ = 4202864  # 0x00402170, R/W, long, "DIGITALBINNING HORZ"
    DIGITALBINNING_VERT = 4202880  # 0x00402180, R/W, long, "DIGITALBINNING VERT"
    # Group: TIMING
    # synchronous timing
    TIMING_READOUTTIME = 4206608  # 0x00403010, R/O, sec,   "TIMING READOUT TIME"
    TIMING_CYCLICTRIGGERPERIOD = (
        4206624  # 0x00403020, R/O, sec,   "TIMING CYCLIC TRIGGER PERIOD"
    )
    TIMING_MINTRIGGERBLANKING = (
        4206640  # 0x00403030, R/O, sec,    "TIMING MINIMUM TRIGGER BLANKING"
    )
    # 0x00403040 is reserved
    TIMING_MINTRIGGERINTERVAL = (
        4206672  # 0x00403050, R/O, sec,    "TIMING MINIMUM TRIGGER INTERVAL"
    )
    TIMING_EXPOSURE = 4206688  # 0x00403060, R/O, mode, "TIMING EXPOSURE"
    TIMING_INVALIDEXPOSUREPERIOD = (
        4206704  # 0x00403070, R/O, sec, "INVALID EXPOSURE PERIOD"
    )
    TIMING_FRAMESKIPNUMBER = (
        4206720  # 0x00403080, R/W, long,  "TIMING FRAME SKIP NUMBER"
    )
    TIMING_GLOBALEXPOSUREDELAY = (
        4206736  # 0x00403090, R/O, sec,   "TIMING GLOBAL EXPOSURE DELAY"
    )
    INTERNALFRAMERATE = 4208656  # 0x00403810, R/W, 1/sec,  "INTERNAL FRAME RATE"
    INTERNAL_FRAMEINTERVAL = (
        4208672  # 0x00403820, R/W, sec,   "INTERNAL FRAME INTERVAL"
    )
    INTERNALLINERATE = 4208688  # 0x00403830, R/W, 1/sec,   "INTERNAL LINE RATE"
    INTERNALLINESPEED = 4208704  # 0x00403840, R/W, m/sec,  "INTERNAL LINE SPEEED"
    INTERNAL_LINEINTERVAL = 4208720  # 0x00403850, R/W, sec,    "INTERNAL LINE INTERVAL"
    # system information
    TIMESTAMP_PRODUCER = 4262416  # 0x00410A10, R/O, mode,  "TIME STAMP PRODUCER"
    FRAMESTAMP_PRODUCER = 4262432  # 0x00410A20, R/O, mode, "FRAME STAMP PRODUCER"
    TRANSFERINFO_FRAMECOUNT = (
        4262672  # 0x00410B10, R/O, long, "TRANSFER INFO FRAME COUNT"
    )
    TRANSFERINFO_LOSTCOUNT = (
        4262673  # 0x00410B11, R/O, long,  "TRANSFER INFO LOST COUNT"
    )
    # Group: READOUT
    # image information
    # 0x00420110 is reserved
    COLORTYPE = 4325664  # 0x00420120, R/W, mode,   "COLORTYPE"
    BITSPERCHANNEL = 4325680  # 0x00420130, R/W, long,  "BIT PER CHANNEL"
    # 0x00420140 is reserved
    # 0x00420150 is reserved
    NUMBEROF_CHANNEL = 4325760  # 0x00420180, R/O, long,    "NUMBER OF CHANNEL"
    ACTIVE_CHANNELINDEX = 4325776  # 0x00420190, R/W, mode, "ACTIVE CHANNEL INDEX"
    NUMBEROF_VIEW = 4325824  # 0x004201C0, R/O, long,   "NUMBER OF VIEW"
    ACTIVE_VIEWINDEX = 4325840  # 0x004201D0, R/W, mode,    "ACTIVE VIEW INDEX"
    IMAGE_WIDTH = 4325904  # 0x00420210, R/O, long, "IMAGE WIDTH"
    IMAGE_HEIGHT = 4325920  # 0x00420220, R/O, long,    "IMAGE HEIGHT"
    IMAGE_ROWBYTES = 4325936  # 0x00420230, R/O, long,  "IMAGE ROWBYTES"
    IMAGE_FRAMEBYTES = 4325952  # 0x00420240, R/O, long,    "IMAGE FRAMEBYTES"
    IMAGE_TOPOFFSETBYTES = 4325968  # 0x00420250
    IMAGE_PIXELTYPE = 4326000  # 0x00420270, R/W, DCAM_PIXELTYPE,   "IMAGE PIXEL TYPE"
    IMAGE_CAMERASTAMP = 4326144  # 0x00420300, R/W, long,   "IMAGE CAMERA STAMP"
    RECORDFIXEDBYTES_PERFILE = (
        4326416  # 0x00420410, R/O,  long    "RECORD FIXED BYTES PER FILE"
    )
    RECORDFIXEDBYTES_PERSESSION = 4326432  # 0x00420420
    RECORDFIXEDBYTES_PERFRAME = (
        4326448  # 0x00420430, R/O, long    "RECORD FIXED BYTES PER FRAME"
    )
    # frame bundle
    FRAMEBUNDLE_MODE = 4329488  # 0x00421010, R/W, mode,    "FRAMEBUNDLE MODE"
    FRAMEBUNDLE_NUMBER = 4329504  # 0x00421020, R/W, long,  "FRAMEBUNDLE NUMBER"
    FRAMEBUNDLE_ROWBYTES = 4329520  # 0x00421030, R/O,  long,   "FRAMEBUNDLE ROWBYTES"
    FRAMEBUNDLE_FRAMESTEPBYTES = (
        4329536  # 0x00421040, R/O, long,  "FRAMEBUNDLE FRAME STEP BYTES"
    )
    # partial area
    NUMBEROF_PARTIALAREA = 4390928  # 0x00430010
    PARTIALAREA_HPOS = 4395008  # 0x00431000, R/W, long,    "PARTIAL AREA HPOS"
    PARTIALAREA_HSIZE = 4399104  # 0x00432000, R/W, long,   "PARTIAL AREA HSIZE"
    PARTIALAREA_VPOS = 4403200  # 0x00433000, R/W, long,    "PARTIAL AREA VPOS"
    PARTIALAREA_VSIZE = 4407296  # 0x00434000, R/W, long,   "PARTIAL AREA VSIZE"
    _PARTIALAREA = 16  # 0x00000010, the offset of ID for Nth PARTIAL AREA
    # multi line
    NUMBEROF_MULTILINE = 4517904  # 0x0044F010, R/W, long,  "NUMBER OF MULTI LINE"
    MULTILINE_VPOS = 4521984  # 0x00450000, R/W, long,  "MULTI LINE VPOS"
    MULTILINE_VSIZE = 4587520  # 0x00460000, R/W, long, "MULTI LINE VSIZE"
    _MULTILINE = 16  # 0x00000010, the offset of ID for Nth MULTI LINE
    # defect
    DEFECTCORRECT_MODE = 4653072  # 0x00470010, R/W, mode,  "DEFECT CORRECT MODE"
    NUMBEROF_DEFECTCORRECT = (
        4653088  # 0x00470020, R/W, long,  "NUMBER OF DEFECT CORRECT"
    )
    HOTPIXELCORRECT_LEVEL = (
        4653104  # 0x00470030, R/W, mode,   "HOT PIXEL CORRECT LEVEL"
    )
    DEFECTCORRECT_HPOS = 4657152  # 0x00471000, R/W, long,  "DEFECT CORRECT HPOS"
    DEFECTCORRECT_METHOD = 4665344  # 0x00473000, R/W, mode,    "DEFECT CORRECT METHOD"
    # - 0x0047FFFF for 256 DEFECT
    _DEFECTCORRECT = 16  # 0x00000010, the offset of ID for Nth DEFECT
    # Group: device buffer countrol
    DEVICEBUFFER_MODE = 4784128  # 0x00490000, R/W, mode,   "DEVICE BUFFER MODE"
    DEVICEBUFFER_FRAMECOUNTMAX = (
        4784160  # 0x00490020, R/O, long,  "DEVICE BUFFER FRAME COUNT MAX"
    )
    # Group: CALIBREGION
    CALIBREGION_MODE = 4203536  # 0x00402410, R/W, mode,    "CALIBRATE REGION MODE"
    NUMBEROF_CALIBREGION = 4203552  # 0x00402420
    CALIBREGION_HPOS = 4915200  # 0x004B0000, R/W, long,    "CALIBRATE REGION HPOS"
    CALIBREGION_HSIZE = 4919296  # 0x004B1000, R/W, long,   "CALIBRATE REGION HSIZE"
    # - 0x0048FFFF for 256 REGIONs at least
    _CALIBREGION = 16  # 0x00000010, the offset of ID for Nth REGION
    # Group: MASKREGION
    MASKREGION_MODE = 4203792  # 0x00402510, R/W, mode, "MASK REGION MODE"
    NUMBEROF_MASKREGION = 4203808  # 0x00402520, R/W, long, "NUMBER OF MASK REGION"
    MASKREGION_HPOS = 4980736  # 0x004C0000, R/W, long, "MASK REGION HPOS"
    MASKREGION_HSIZE = 4984832  # 0x004C1000, R/W, long,    "MASK REGION HSIZE"
    # - 0x0048FFFF for 256 REGIONs at least
    _MASKREGION = 16  # 0x00000010, the offset of ID for Nth REGION
    # Group: Camera Status
    CAMERASTATUS_INTENSITY = 5050640  # 0x004D1110, R/O, mode,  "CAMERASTATUS INTENSITY"
    CAMERASTATUS_INPUTTRIGGER = 5050656  # 0x004D1120
    CAMERASTATUS_CALIBRATION = (
        5050672  # 0x004D1130, R/O, mode,    "CAMERASTATUS CALIBRATION"
    )
    # Group: Back Focus Position
    BACKFOCUSPOS_TARGET = (
        8405008  # 0x00804010, R/W, micro-meter,"BACK FOCUS POSITION TARGET"
    )
    BACKFOCUSPOS_CURRENT = (
        8405024  # 0x00804020, R/O, micro-meter,"BACK FOCUS POSITION CURRENT"
    )
    BACKFOCUSPOS_LOADFROMMEMORY = 8405072  # 0x00804050
    BACKFOCUSPOS_STORETOMEMORY = (
        8405088  # 0x00804060, W/O, long, "BACK FOCUS POSITION STORE TO MEMORY"
    )
    # Group: MAICO
    CONFOCAL_SCANMODE = 9502736  # 0x00910010, R/W, mode,   "CONFOCAL SCAN MODE"
    CONFOCAL_SCANLINES = 9502752  # 0x00910020, R/W, long,  "CONFOCAL SCANLINES"
    CONFOCAL_ZOOM = 9502768  # 0x00910030, R/W, long,   "CONFOCAL ZOOM"
    SUBUNIT_IMAGEWIDTH = 9502944  # 0x009100e0, R/O, long,  "SUBUNIT IMAGE WIDTH
    NUMBEROF_SUBUNIT = 9502960  # 0x009100f0, R/O, long,    "NUMBER OF SUBUNIT"
    SUBUNIT_CONTROL = 9502976  # 0x00910100, R/W, mode, "SUBUNIT CONTROL"
    SUBUNIT_LASERPOWER = 9503232  # 0x00910200, R/W, long,  "SUBUNIT LASERPOWER"
    SUBUNIT_PMTGAIN = 9503488  # 0x00910300, R/W, real, "SUBUNIT PMTGAIN"
    SUBUNIT_PINHOLESIZE = 9503744  # 0x00910400, R/O, long, "SUBUNIT PINHOLE SIZE"
    SUBUNIT_WAVELENGTH = 9504000  # 0x00910500, R/O, long,  "SUBUNIT WAVELENGTH"
    SUBUNIT_TOPOFFSETBYTES = (
        9504256  # 0x00910600, R/O, long,  "SUBUNIT TOP OFFSET BYTES"
    )
    _SUBUNIT = 16  # 0x00000010, the offset of ID for Nth Subunit parameter
    # Group: SYSTEM
    # system property
    SYSTEM_ALIVE = 16711696  # 0x00FF0010, R/O, mode,   "SYSTEM ALIVE"
    CONVERSIONFACTOR_COEFF = (
        16769040  # 0x00FFE010, R/O, double,   "CONVERSION FACTOR COEFF"
    )
    CONVERSIONFACTOR_OFFSET = (
        16769056  # 0x00FFE020, R/O, double,  "CONVERSION FACTOR OFFSET"
    )


# ==== declare structures for DCAM-API functions ====


class DCAMAPI_INIT(Structure):
    _pack_ = 8
    _fields_ = [
        ("size", c_int32),
        ("iDeviceCount", c_int32),  # out
        ("reserved", c_int32),
        ("initoptionbytes", c_int32),
        ("initoption", POINTER(c_int32)),
        ("guid", c_void_p),  # const DCAM_GUID*
    ]

    def __init__(self):
        self.size = sizeof(DCAMAPI_INIT)


class DCAMDEV_OPEN(Structure):
    _pack_ = 8
    _fields_ = [("size", c_int32), ("index", c_int32), ("hdcam", c_void_p)]  # out

    def __init__(self):
        self.size = sizeof(DCAMDEV_OPEN)
        self.index = 0


class DCAMDEV_STRING(Structure):
    _pack_ = 8
    _fields_ = [
        ("size", c_int32),
        ("iString", c_int32),
        ("text", c_char_p),
        ("textbytes", c_int32),
    ]

    def __init__(self):
        self.size = sizeof(DCAMDEV_STRING)

    def alloctext(self, maxlen):
        textbuf = create_string_buffer(maxlen)
        self.text = addressof(textbuf)
        self.textbytes = sizeof(textbuf)


class DCAM_PROP:
    class ATTR(IntEnum):
        """
        Attributer flags.
        """

        HASRANGE = -2147483647  # 0x80000000
        HASSTEP = 0x40000000
        HASDEFAULT = 0x20000000
        HASVALUETEXT = 0x10000000
        HASCHANNEL = 0x08000000
        AUTOROUNDING = 0x00800000
        STEPPING_INCONSISTENT = 0x00400000
        DATASTREAM = 0x00200000
        HASRATIO = 0x00100000
        VOLATILE = 0x00080000
        WRITABLE = 0x00020000
        READABLE = 0x00010000
        HASVIEW = 0x00008000
        _SYSTEM = 0x00004000
        ACCESSREADY = 0x00002000
        ACCESSBUSY = 0x00001000
        ADVANCED = 0x00000800
        EFFECTIVE = 0x00000200

    class TYPE(IntEnum):
        """
        property types.
        """

        NONE = 0
        MODE = 1
        LONG = 2
        REAL = 3
        MASK = 15

    class ATTR2(IntEnum):
        """
        Attributer2 flags.
        """

    ARRAYBASE = 134217728  # 0x08000000
    ARRAYELEMENT = 67108864  # 0x04000000
    REAL32 = 33554432  # 0x02000000
    INITIALIZEIMPROPER = 1  # 0x00000001
    CHANNELSEPARATEDDATA = (
        262144  # 0x00040000, Channel 0 value is total of each channels.
    )


class DCAMPROP_OPTION(IntEnum):
    """
    options
    """

    PRIOR = -16777215  # 0xFF000000
    NEXT = 0x01000000
    NEAREST = 0x80000000
    SUPPORT = 0x00000000
    UPDATED = 0x00000001
    VOLATILE = 0x00000002
    ARRAYELEMENT = 0x00000004
    NONE = 0x00000000


class DCAMPROP_UNIT(IntEnum):
    """
    Unit of value
    """

    SECOND = 1
    CELSIUS = 2
    KELVIN = 3
    METERPERSECOND = 4
    PERSECOND = 5
    DEGREE = 6
    MICROMETER = 7
    NONE = 0


# property values


class DCAMPROP:
    class SENSORMODE(IntEnum):
        AREA = 1
        LINE = 3
        TDI = 4
        TDI_EXTENDED = 10
        PROGRESSIVE = 12
        SPLITVIEW = 14
        DUALLIGHTSHEET = 16
        PHOTONNUMBERRESOLVING = 18

    class SHUTTER_MODE(IntEnum):
        GLOBAL = 1
        ROLLING = 2

    class READOUTSPEED(IntEnum):
        SLOWEST = 1
        FASTEST = 0x7FFFFFFF

    class READOUT_DIRECTION(IntEnum):
        FORWARD = 1
        BACKWARD = 2
        BYTRIGGER = 3
        DIVERGE = 5

    class READOUT_UNIT(IntEnum):
        FRAME = 2
        BUNDLEDLINE = 3
        BUNDLEDFRAME = 4

    class CCDMODE(IntEnum):
        NORMALCCD = 1
        EMCCD = 2

    class CMOSMODE(IntEnum):
        NORMAL = 1
        NONDESTRUCTIVE = 2

    class OUTPUT_INTENSITY(IntEnum):
        NORMAL = 1
        TESTPATTERN = 2

    class OUTPUTDATA_OPERATION(IntEnum):
        RAW = 1
        ALIGNED = 2

    class TESTPATTERN_KIND(IntEnum):
        FLAT = 2
        IFLAT = 3
        HORZGRADATION = 4
        IHORZGRADATION = 5
        VERTGRADATION = 6
        IVERTGRADATION = 7
        LINE = 8
        ILINE = 9
        DIAGONAL = 10
        IDIAGONAL = 11
        FRAMECOUNT = 12

    class DIGITALBINNING_METHOD(IntEnum):
        MINIMUM = 1
        MAXIMUM = 2
        ODD = 3
        EVEN = 4
        SUM = 5
        AVERAGE = 6

    class TRIGGERSOURCE(IntEnum):
        INTERNAL = 1
        EXTERNAL = 2
        SOFTWARE = 3
        MASTERPULSE = 4

    class TRIGGERACTIVE(IntEnum):
        EDGE = 1
        LEVEL = 2
        SYNCREADOUT = 3
        POINT = 4

    class BUS_SPEED(IntEnum):
        SLOWEST = 1
        FASTEST = 0x7FFFFFFF

    class TRIGGER_MODE(IntEnum):
        NORMAL = 1
        PIV = 3
        START = 6

    class TRIGGERPOLARITY(IntEnum):
        NEGATIVE = 1
        POSITIVE = 2

    class TRIGGER_CONNECTOR(IntEnum):
        INTERFACE = 1
        BNC = 2
        MULTI = 3

    class INTERNALTRIGGER_HANDLING(IntEnum):
        SHORTEREXPOSURETIME = 1
        FASTERFRAMERATE = 2
        ABANDONWRONGFRAME = 3
        BURSTMODE = 4
        INDIVIDUALEXPOSURE = 7

    class SYNCREADOUT_SYSTEMBLANK(IntEnum):
        STANDARD = 1
        MINIMUM = 2

    class TRIGGERENABLE_ACTIVE(IntEnum):
        DENY = 1
        ALWAYS = 2
        LEVEL = 3
        START = 4

    class TRIGGERENABLE_POLARITY(IntEnum):
        NEGATIVE = 1
        POSITIVE = 2
        INTERLOCK = 3

    class OUTPUTTRIGGER_CHANNELSYNC(IntEnum):
        _1CHANNEL = 1
        _2CHANNELS = 2
        _3CHANNELS = 3

    class OUTPUTTRIGGER_PROGRAMABLESTART(IntEnum):
        FIRSTEXPOSURE = 1
        FIRSTREADOUT = 2

    class OUTPUTTRIGGER_SOURCE(IntEnum):
        EXPOSURE = 1
        READOUTEND = 2
        VSYNC = 3
        HSYNC = 4
        TRIGGER = 6

    class OUTPUTTRIGGER_POLARITY(IntEnum):
        NEGATIVE = 1
        POSITIVE = 2

    class OUTPUTTRIGGER_ACTIVE(IntEnum):
        EDGE = 1
        LEVEL = 2

    class OUTPUTTRIGGER_KIND(IntEnum):
        LOW = 1
        GLOBALEXPOSURE = 2
        PROGRAMABLE = 3
        TRIGGERREADY = 4
        HIGH = 5
        ANYROWEXPOSURE = 6

    class OUTPUTTRIGGER_BASESENSOR(IntEnum):
        VIEW1 = 1
        VIEW2 = 2
        ANYVIEW = 15
        ALLVIEWS = 16

    class EXPOSURETIME_CONTROL(IntEnum):
        OFF = 1
        NORMAL = 2

    class TRIGGER_FIRSTEXPOSURE(IntEnum):
        NEW = 1
        CURRENT = 2

    class TRIGGER_GLOBALEXPOSURE(IntEnum):
        NONE = 1
        ALWAYS = 2
        DELAYED = 3
        EMULATE = 4
        GLOBALRESET = 5

    class FIRSTTRIGGER_BEHAVIOR(IntEnum):
        STARTEXPOSURE = 1
        STARTREADOUT = 2

    class MASTERPULSE_MODE(IntEnum):
        CONTINUOUS = 1
        START = 2
        BURST = 3

    class MASTERPULSE_TRIGGERSOURCE(IntEnum):
        EXTERNAL = 1
        SOFTWARE = 2

    class MECHANICALSHUTTER(IntEnum):
        AUTO = 1
        CLOSE = 2
        OPEN = 3

    class LIGHTMODE(IntEnum):
        LOWLIGHT = 1
        HIGHLIGHT = 2

    class SENSITIVITYMODE(IntEnum):
        OFF = 1
        ON = 2
        INTERLOCK = 3

    class EMGAINWARNING_STATUS(IntEnum):
        NORMAL = 1
        WARNING = 2
        PROTECTED = 3

    class PHOTONIMAGINGMODE(IntEnum):
        _0 = 0
        _1 = 1
        _2 = 2
        _3 = 3

    class SENSORCOOLER(IntEnum):
        OFF = 1
        ON = 2
        MAX = 4

    class SENSORTEMPERATURE_STATUS(IntEnum):
        NORMAL = 0
        WARNING = 1
        PROTECTION = 2

    class SENSORCOOLERSTATUS(IntEnum):
        ERROR4 = -4
        ERROR3 = -3
        ERROR2 = -2
        ERROR1 = -1
        NONE = 0
        OFF = 1
        READY = 2
        BUSY = 3
        ALWAYS = 4
        WARNING = 5

    class REALTIMEGAINCORRECT_LEVEL(IntEnum):
        _1 = 1
        _2 = 2
        _3 = 3
        _4 = 4
        _5 = 5

    class WHITEBALANCEMODE(IntEnum):
        FLAT = 1
        AUTO = 2
        TEMPERATURE = 3
        USERPRESET = 4

    class DARKCALIB_TARGET(IntEnum):
        ALL = 1
        ANALOG = 2

    class SHADINGCALIB_METHOD(IntEnum):
        AVERAGE = 1
        MAXIMUM = 2
        USETARGET = 3

    class CAPTUREMODE(IntEnum):
        NORMAL = 1
        DARKCALIB = 2
        SHADINGCALIB = 3
        TAPGAINCALIB = 4
        BACKFOCUSCALIB = 5

    class INTERFRAMEALU_ENABLE(IntEnum):
        OFF = 1
        TRIGGERSOURCE_ALL = 2
        TRIGGERSOURCE_INTERNAL = 3

    class SHADINGCALIB_DATASTATUS(IntEnum):
        NONE = 1
        FORWARD = 2
        BACKWARD = 3
        BOTH = 4

    class TAPGAINCALIB_METHOD(IntEnum):
        AVE = 1
        MAX = 2
        MIN = 3

    class RECURSIVEFILTERFRAMES(IntEnum):
        _2 = 2
        _4 = 4
        _8 = 8
        _16 = 16
        _32 = 32
        _64 = 64

    class INTENSITYLUT_MODE(IntEnum):
        THROUGH = 1
        PAGE = 2
        CLIP = 3

    class BINNING(IntEnum):
        _1 = 1
        _2 = 2
        _4 = 4
        _8 = 8
        _16 = 16
        _1_2 = 102
        _2_4 = 204

    class COLORTYPE(IntEnum):
        BW = 0x00000001
        RGB = 0x00000002
        BGR = 0x00000003

    class BITSPERCHANNEL(IntEnum):
        _8 = 8
        _10 = 10
        _12 = 12
        _14 = 14
        _16 = 16

    class DEFECTCORRECT_MODE(IntEnum):
        OFF = 1
        ON = 2

    class DEFECTCORRECT_METHOD(IntEnum):
        CEILING = 3
        PREVIOUS = 4

    class HOTPIXELCORRECT_LEVEL(IntEnum):
        STANDARD = 1
        MINIMUM = 2
        AGGRESSIVE = 3

    class DEVICEBUFFER_MODE(IntEnum):
        THRU = 1
        SNAPSHOT = 2

    class SYSTEM_ALIVE(IntEnum):
        OFFLINE = 1
        ONLINE = 2
        ERROR = 3

    class TIMESTAMP_MODE(IntEnum):
        NONE = 1
        LINEBEFORELEFT = 2
        LINEOVERWRITELEFT = 3
        AREABEFORELEFT = 4
        AREAOVERWRITELEFT = 5

    class TIMING_EXPOSURE(IntEnum):
        AFTERREADOUT = 1
        OVERLAPREADOUT = 2
        ROLLING = 3
        ALWAYS = 4
        TDI = 5

    class TIMESTAMP_PRODUCER(IntEnum):
        NONE = 1
        DCAMMODULE = 2
        KERNELDRIVER = 3
        CAPTUREDEVICE = 4
        IMAGINGDEVICE = 5

    class FRAMESTAMP_PRODUCER(IntEnum):
        NONE = 1
        DCAMMODULE = 2
        KERNELDRIVER = 3
        CAPTUREDEVICE = 4
        IMAGINGDEVICE = 5

    class CAMERASTATUS_INTENSITY(IntEnum):
        GOOD = 1
        TOODARK = 2
        TOOBRIGHT = 3
        UNCARE = 4
        EMGAIN_PROTECTION = 5
        INCONSISTENT_OPTICS = 6
        NODATA = 7

    class CAMERASTATUS_INPUTTRIGGER(IntEnum):
        GOOD = 1
        NONE = 2
        TOOFREQUENT = 3

    class CAMERASTATUS_CALIBRATION(IntEnum):
        DONE = 1
        NOTYET = 2
        NOTRIGGER = 3
        TOOFREQUENTTRIGGER = 4
        OUTOFADJUSTABLERANGE = 5
        UNSUITABLETABLE = 6
        TOODARK = 7
        TOOBRIGHT = 8
        NOTDETECTOBJECT = 9

    class CONFOCAL_SCANMODE(IntEnum):
        SIMULTANEOUS = 1
        SEQUENTIAL = 2

    class SUBUNIT_CONTROL(IntEnum):
        NOTINSTALLED = 0
        OFF = 1
        ON = 2

    class SUBUNIT_PINHOLESIZE(IntEnum):
        ERROR = 1
        SMALL = 2
        MEDIUM = 3
        LARGE = 4

    class MODE(IntEnum):
        OFF = 1
        ON = 2


class DCAMPROP_ATTR(Structure):
    _pack_ = 8
    _fields_ = [
        ("cbSize", c_int32),
        ("iProp", c_int32),
        ("option", c_int32),
        ("iReserved1", c_int32),
        ("attribute", c_int32),
        ("iGroup", c_int32),
        ("iUnit", c_int32),
        ("attribute2", c_int32),
        ("valuemin", c_double),
        ("valuemax", c_double),
        ("valuestep", c_double),
        ("valuedefault", c_double),
        ("nMaxChannel", c_int32),
        ("iReserved3", c_int32),
        ("nMaxView", c_int32),
        ("iProp_NumberOfElement", c_int32),
        ("iProp_ArrayBase", c_int32),
        ("iPropStep_Element", c_int32),
    ]

    def __init__(self):
        self.cbSize = sizeof(DCAMPROP_ATTR)

    def is_effective(self):
        return True if self.attribute & DCAM_PROP.ATTR.EFFECTIVE else False

    def is_writable(self):
        return True if self.attribute & DCAM_PROP.ATTR.WRITABLE else False

    def is_readable(self):
        return True if self.attribute & DCAM_PROP.ATTR.READABLE else False

    def is_volatile(self):
        return True if self.attribute & DCAM_PROP.ATTR.VOLATILE else False

    def is_accessready(self):
        return True if self.attribute & DCAM_PROP.ATTR.ACCESSREADY else False

    def is_accessbusy(self):
        return True if self.attribute & DCAM_PROP.ATTR.ACCESSBUSY else False

    def is_datastream(self):
        return True if self.attribute & DCAM_PROP.ATTR.DATASTREAM else False

    def is_autorounding(self):
        return True if self.attribute & DCAM_PROP.ATTR.AUTOROUNDING else False

    def is_stepping_inconsistent(self):
        return True if self.attribute & DCAM_PROP.ATTR.STEPPING_INCONSISTENT else False

    def is_hasview(self):
        return True if self.attribute & DCAM_PROP.ATTR.HASVIEW else False

    def is_haschannel(self):
        return True if self.attribute & DCAM_PROP.ATTR.HASCHANNEL else False


class DCAMPROP_VALUETEXT(Structure):
    _pack_ = 8
    _fields_ = [
        ("cbSize", c_int32),
        ("iProp", c_int32),
        ("value", c_double),
        ("text", c_char_p),
        ("textbytes", c_int32),
    ]

    def __init__(self):
        self.cbSize = sizeof(DCAMPROP_VALUETEXT)

    def alloctext(self, maxlen):
        textbuf = create_string_buffer(maxlen)
        self.text = addressof(textbuf)
        self.textbytes = sizeof(textbuf)


class DCAM_TIMESTAMP(Structure):
    _pack_ = 8
    _fields_ = [("sec", c_uint32), ("microsec", c_int32)]

    def __init__(self):
        self.sec = 0
        self.microsec = 0


class DCAMCAP_TRANSFERINFO(Structure):
    _pack_ = 8
    _fields_ = [
        ("size", c_int32),
        ("iKind", c_int32),
        ("nNewestFrameIndex", c_int32),
        ("nFrameCount", c_int32),
    ]

    def __init__(self):
        self.size = sizeof(DCAMCAP_TRANSFERINFO)
        self.iKind = 0
        self.nNewestFrameIndex = -1
        self.nFrameCount = 0


class DCAMBUF_FRAME(Structure):
    _pack_ = 8
    _fields_ = [
        ("size", c_int32),
        ("iKind", c_int32),
        ("option", c_int32),
        ("iFrame", c_int32),
        ("buf", c_void_p),
        ("rowbytes", c_int32),
        ("type", c_int32),  # DCAM_PIXELTYPE
        ("width", c_int32),
        ("height", c_int32),
        ("left", c_int32),
        ("top", c_int32),
        ("timestamp", DCAM_TIMESTAMP),
        ("framestamp", c_int32),
        ("camerastamp", c_int32),
    ]

    def __init__(self):
        self.size = sizeof(DCAMBUF_FRAME)
        self.iKind = 0
        self.option = 0
        self.iFrame = 0
        self.buf = 0
        self.rowbytes = 0
        self.type = DCAM_PIXELTYPE.MONO16
        self.width = 0
        self.height = 0
        self.left = 0
        self.top = 0
        self.timestamp = DCAM_TIMESTAMP()
        self.framestamp = 0
        self.camerastamp = 0


class DCAMWAIT_OPEN(Structure):
    _pack_ = 8
    _fields_ = [
        ("size", c_int32),
        ("supportevent", c_int32),  # out
        ("hwait", c_void_p),  # out
        ("hdcam", c_void_p),
    ]

    def __init__(self):
        self.size = sizeof(DCAMWAIT_OPEN)


class DCAMWAIT_START(Structure):
    _pack_ = 8
    _fields_ = [
        ("size", c_int32),
        ("eventhappened", c_int32),  # out
        ("eventmask", c_int32),
        ("timeout", c_int32),
    ]

    def __init__(self):
        self.size = sizeof(DCAMWAIT_START)


if __platform_system == "Windows":

    class DCAMREC_OPEN(Structure):  # DCAMREC_OPENW
        _pack_ = 8
        _fields_ = [
            ("size", c_int32),  # [in] size of this structure.
            ("reserved", c_int32),  # [in]
            ("hrec", c_void_p),  # [out]
            ("path", c_wchar_p),  # [in] wchar_t*
            ("ext", c_wchar_p),  # [in] wchar_t*
            ("maxframepersession", c_int32),  # [in]
            ("userdatasize", c_int32),  # [in]
            ("userdatasize_session", c_int32),  # [in]
            ("userdatasize_file", c_int32),  # [in]
            ("usertextsize", c_int32),  # [in]
            ("usertextsize_session", c_int32),  # [in]
            ("usertextsize_file", c_int32),  # [in]
        ]

        def __init__(self):
            self.size = sizeof(DCAMREC_OPEN)
            # wtextbuf = create_unicode_buffer(256)
            # self.path = addressof(wtextbuf)
            self.ext = 0  # 'dcimg'.encode('UTF-16')
            self.maxframepersession = 0
            self.userdatasize_file = 0
            self.usertextsize_file = 0
            self.userdatasize_session = 0
            self.usertextsize_session = 0
            self.userdatasize = 0
            self.usertextsize = 0

        def setpath(self, filepath):
            self.path = filepath


# ==== assign aliases ====

dcamapi_init = __dll.dcamapi_init
dcamapi_init.argtypes = [POINTER(DCAMAPI_INIT)]
dcamapi_init.restype = DCAMERR
dcamapi_uninit = __dll.dcamapi_uninit
dcamapi_uninit.restype = DCAMERR
dcamdev_open = __dll.dcamdev_open
dcamdev_open.argtypes = [POINTER(DCAMDEV_OPEN)]
dcamdev_open.restype = DCAMERR
dcamdev_close = __dll.dcamdev_close
dcamdev_close.argtypes = [c_void_p]
dcamdev_close.restype = DCAMERR
dcamdev_getstring = __dll.dcamdev_getstring
dcamdev_getstring.argtypes = [c_void_p, POINTER(DCAMDEV_STRING)]
dcamdev_getstring.restype = DCAMERR
dcamprop_getattr = __dll.dcamprop_getattr
dcamprop_getattr.argtypes = [c_void_p, POINTER(DCAMPROP_ATTR)]
dcamprop_getattr.restype = DCAMERR
dcamprop_getvalue = __dll.dcamprop_getvalue
dcamprop_getvalue.argtypes = [c_void_p, c_int32, POINTER(c_double)]
dcamprop_getvalue.restype = DCAMERR
dcamprop_setvalue = __dll.dcamprop_setvalue
dcamprop_setvalue.argtypes = [c_void_p, c_int32, c_double]
dcamprop_setvalue.restype = DCAMERR
dcamprop_setgetvalue = __dll.dcamprop_setgetvalue
dcamprop_setgetvalue.argtypes = [c_void_p, c_int32, POINTER(c_double), c_int32]
dcamprop_setgetvalue.restype = DCAMERR
dcamprop_queryvalue = __dll.dcamprop_queryvalue
dcamprop_queryvalue.argtypes = [c_void_p, c_int32, POINTER(c_double), c_int32]
dcamprop_queryvalue.restype = DCAMERR
dcamprop_getnextid = __dll.dcamprop_getnextid
dcamprop_getnextid.argtypes = [c_void_p, POINTER(c_int32), c_int32]
dcamprop_getnextid.restype = DCAMERR
dcamprop_getname = __dll.dcamprop_getname
dcamprop_getname.argtypes = [c_void_p, c_int32, c_char_p, c_int32]
dcamprop_getname.restype = DCAMERR
dcamprop_getvaluetext = __dll.dcamprop_getvaluetext
dcamprop_getvaluetext.argtypes = [c_void_p, POINTER(DCAMPROP_VALUETEXT)]
dcamprop_getvaluetext.restype = DCAMERR
dcambuf_alloc = __dll.dcambuf_alloc
dcambuf_alloc.argtypes = [c_void_p, c_int32]
dcambuf_alloc.restype = DCAMERR
dcambuf_release = __dll.dcambuf_release
dcambuf_release.argtypes = [c_void_p, c_int32]
dcambuf_release.restype = DCAMERR
dcambuf_lockframe = __dll.dcambuf_lockframe
dcambuf_lockframe.argtypes = [c_void_p, POINTER(DCAMBUF_FRAME)]
dcambuf_lockframe.restype = DCAMERR
dcambuf_copyframe = __dll.dcambuf_copyframe
dcambuf_copyframe.argtypes = [c_void_p, POINTER(DCAMBUF_FRAME)]
dcambuf_copyframe.restype = DCAMERR
dcamcap_start = __dll.dcamcap_start
dcamcap_start.argtypes = [c_void_p, c_int32]
dcamcap_start.restype = DCAMERR
dcamcap_stop = __dll.dcamcap_stop
dcamcap_stop.argtypes = [c_void_p]
dcamcap_stop.restype = DCAMERR
dcamcap_status = __dll.dcamcap_status
dcamcap_status.argtypes = [c_void_p, POINTER(c_int32)]
dcamcap_status.restype = DCAMERR
dcamcap_transferinfo = __dll.dcamcap_transferinfo
dcamcap_transferinfo.argtypes = [c_void_p, POINTER(DCAMCAP_TRANSFERINFO)]
dcamcap_transferinfo.restype = DCAMERR
dcamcap_firetrigger = __dll.dcamcap_firetrigger
dcamcap_firetrigger.argtypes = [c_void_p, c_int32]
dcamcap_firetrigger.restype = DCAMERR

if __platform_system == "Windows":
    dcamcap_record = __dll.dcamcap_record
    dcamcap_record.argtypes = [c_void_p, c_void_p]
    dcamcap_record.restype = DCAMERR

dcamwait_open = __dll.dcamwait_open
dcamwait_open.argtypes = [POINTER(DCAMWAIT_OPEN)]
dcamwait_open.restype = DCAMERR
dcamwait_close = __dll.dcamwait_close
dcamwait_close.argtypes = [c_void_p]
dcamwait_close.restype = DCAMERR
dcamwait_start = __dll.dcamwait_start
dcamwait_start.argtypes = [c_void_p, POINTER(DCAMWAIT_START)]
dcamwait_start.restype = DCAMERR
dcamwait_abort = __dll.dcamwait_abort
dcamwait_abort.argtypes = [c_void_p]
dcamwait_abort.restype = DCAMERR

if __platform_system == "Windows":
    dcamrec_open = __dll.dcamrec_openW
    dcamrec_open.argtypes = [POINTER(DCAMREC_OPEN)]  # DCAMREC_OPENW
    dcamrec_open.restype = DCAMERR

    dcamrec_close = __dll.dcamrec_close
    dcamrec_close.argtypes = [c_void_p]
    dcamrec_close.restype = DCAMERR
