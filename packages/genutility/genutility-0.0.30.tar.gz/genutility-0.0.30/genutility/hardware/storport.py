from __future__ import absolute_import, division, print_function, unicode_literals

FILE_DEVICE_SCSI = 0x0000001b

IOCTL_SCSI_EXECUTE_IN = (FILE_DEVICE_SCSI << 16) + 0x0011
IOCTL_SCSI_EXECUTE_OUT = (FILE_DEVICE_SCSI << 16) + 0x0012
IOCTL_SCSI_EXECUTE_NONE = (FILE_DEVICE_SCSI << 16) + 0x0013

# SMART support in atapi

IOCTL_SCSI_MINIPORT_SMART_VERSION = (FILE_DEVICE_SCSI << 16) + 0x0500
IOCTL_SCSI_MINIPORT_IDENTIFY = (FILE_DEVICE_SCSI << 16) + 0x0501
IOCTL_SCSI_MINIPORT_READ_SMART_ATTRIBS = (FILE_DEVICE_SCSI << 16) + 0x0502
IOCTL_SCSI_MINIPORT_READ_SMART_THRESHOLDS = (FILE_DEVICE_SCSI << 16) + 0x0503
IOCTL_SCSI_MINIPORT_ENABLE_SMART = (FILE_DEVICE_SCSI << 16) + 0x0504
IOCTL_SCSI_MINIPORT_DISABLE_SMART = (FILE_DEVICE_SCSI << 16) + 0x0505
IOCTL_SCSI_MINIPORT_RETURN_STATUS = (FILE_DEVICE_SCSI << 16) + 0x0506
IOCTL_SCSI_MINIPORT_ENABLE_DISABLE_AUTOSAVE = (FILE_DEVICE_SCSI << 16) + 0x0507
IOCTL_SCSI_MINIPORT_SAVE_ATTRIBUTE_VALUES = (FILE_DEVICE_SCSI << 16) + 0x0508
IOCTL_SCSI_MINIPORT_EXECUTE_OFFLINE_DIAGS = (FILE_DEVICE_SCSI << 16) + 0x0509
IOCTL_SCSI_MINIPORT_ENABLE_DISABLE_AUTO_OFFLINE = (FILE_DEVICE_SCSI << 16) + 0x050a
IOCTL_SCSI_MINIPORT_READ_SMART_LOG = (FILE_DEVICE_SCSI << 16) + 0x050b
IOCTL_SCSI_MINIPORT_WRITE_SMART_LOG = (FILE_DEVICE_SCSI << 16) + 0x050c
