# Lists all models and required patches
# Copyright (C) 2020-2021, Dhinak G, Mykola Grymalyuk
SupportedSMBIOS = [
    # MacBook
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBook8,1",
    # MacBook Air
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookAir4,1",
    "MacBookAir4,2",
    "MacBookAir5,1",
    "MacBookAir5,2",
    "MacBookAir6,1",
    "MacBookAir6,2",
    # MacBook Pro
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro7,1",
    "MacBookPro8,1",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "MacBookPro9,1",
    "MacBookPro9,2",
    "MacBookPro10,1",
    "MacBookPro10,2",
    "MacBookPro11,1",
    "MacBookPro11,2",
    "MacBookPro11,3",
    # Mac Mini
    "Macmini3,1",
    "Macmini4,1",
    "Macmini5,1",
    "Macmini5,2",
    "Macmini5,3",
    "Macmini6,1",
    "Macmini6,2",
    # iMac
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "iMac12,1",
    "iMac12,2",
    "iMac13,1",
    "iMac13,2",
    "iMac13,3",
    "iMac14,1",
    "iMac14,2",
    "iMac14,3",
    "iMac14,4",
    "iMac15,1",
    # Mac Pro
    "MacPro3,1",
    "MacPro4,1",
    "MacPro5,1",
    # Xserve
    "Xserve2,1",
    "Xserve3,1",
    "Dortania1,1",
]

# CPU patches

MissingSSE42 = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro7,1",
    "Macmini3,1",
    "Macmini4,1",
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "MacPro3,1",
    "Xserve2,1",
    "Dortania1,1",
]

SSEEmulator = ["MacPro3,1", "Xserve2,1", "Dortania1,1"]

DualSocket = ["MacPro3,1", "MacPro4,1", "MacPro5,1", "Xserve2,1", "Xserve3,1", "Dortania1,1"]

pciSSDT = ["MacBookPro6,1", "MacBookPro6,2", "iMac11,1", "iMac11,2", "iMac11,3", "Dortania1,1"]

# Ethernet patches

EthernetNvidia = [
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "Macmini3,1",
    "iMac9,1",
    "iMac10,1",
    "Dortania1,1",
]
EthernetMarvell = ["MacBook4,1", "MacBookPro4,1", "iMac7,1", "iMac8,1", "Dortania1,1"]
EthernetBroadcom = [
    "MacBookAir4,1",
    "MacBookAir4,2",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro7,1",
    "MacBookPro8,1",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "Macmini4,1",
    "Macmini5,1",
    "Macmini5,2",
    "Macmini5,3",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "iMac12,1",
    "iMac12,2",
    "Dortania1,1",
]

# Wifi patches

WifiAtheros = ["iMac10,1", "iMac11,1", "iMac11,2", "iMac11,3", "iMac12,1", "iMac12,2", "MacPro3,1", "MacPro4,1", "Dortania1,1"]

WifiBCM94328 = ["MacBook4,1", "MacBookAir2,1", "MacBookPro4,1", "iMac7,1", "iMac8,1", "Dortania1,1"]

WifiBCM94322 = [
    "MacBook5,1",
    "MacBook5,2",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro7,1",
    "Macmini3,1",
    "iMac9,1",
    "MacPro5,1",
    "Dortania1,1",
]

WifiBCM94331 = [
    "MacBook6,1",  # PciRoot(0x0)/Pci(0x15,0x0)/Pci(0x0,0x0)
    "MacBook7,1",  # PciRoot(0x0)/Pci(0x15,0x0)/Pci(0x0,0x0)
    "MacBookAir4,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookAir4,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookAir5,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookAir5,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro6,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro6,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro8,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro8,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro8,3",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro9,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro9,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro10,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "MacBookPro10,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "Macmini4,1",  # PciRoot(0x0)/Pci(0x15,0x0)/Pci(0x0,0x0)
    "Macmini5,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "Macmini5,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "Macmini5,3",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "Macmini6,1",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "Macmini6,2",  # PciRoot(0x0)/Pci(0x1C,0x1)/Pci(0x0,0x0)
    "iMac13,1",  # PciRoot(0x0)/Pci(0x1C,0x3)/Pci(0x0,0x0)
    "iMac13,2",  # PciRoot(0x0)/Pci(0x1C,0x3)/Pci(0x0,0x0)
    "iMac13,3",  # PciRoot(0x0)/Pci(0x1C,0x3)/Pci(0x0,0x0)
    "Dortania1,1",
]

# Audio

LegacyAudio = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookAir4,1",
    "MacBookAir4,2",
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro7,1",
    "MacBookPro8,1",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "Macmini3,1",
    "Macmini4,1",
    "Macmini5,1",
    "Macmini5,2",
    "Macmini5,3",
    # "iMac7,1",
    # "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "iMac12,1",
    "iMac12,2",
    "MacPro3,1",
    "Dortania1,1",
]

nvidiaHDEF = [
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro7,1",
    "Macmini3,1",
    "Macmini4,1",
    "iMac9,1",
    "iMac10,1",
]

# GPU

ModernGPU = [
    "MacBookAir5,1",  # Intel 4000
    "MacBookAir5,2",  # Intel 4000
    "MacBookPro9,1",  # Intel 4000 + Nvidia 650M
    "MacBookPro9,2",  # Intel 4000
    "MacBookPro10,1",  # Intel 4000 + Nvidia 650M
    "MacBookPro10,2",  # Intel 4000
    "Macmini6,1",  # Intel 4000
    "Macmini6,2",  # Intel 4000
    "iMac13,1",  # Intel 4000
    "iMac13,3",  # Intel 4000
]

LegacyGPU = [
    "MacBook4,1",  # GMA X3100
    "MacBook5,1",  # Nvidia 9000
    "MacBook5,2",  # Nvidia 9000
    "MacBook6,1",  # Nvidia 9000
    "MacBook7,1",  # Nvidia 300
    "MacBookAir2,1",  # Nvidia 9000
    "MacBookAir3,1",  # Nvidia 300
    "MacBookAir3,2",  # Nvidia 300
    "MacBookAir4,1",  # Intel 3000
    "MacBookAir4,2",  # Intel 3000
    "MacBookPro4,1",  # Nvidia 8000
    "MacBookPro5,1",  # Nvidia 9000
    "MacBookPro5,2",  # Nvidia 9000
    "MacBookPro5,3",  # Nvidia 9000
    "MacBookPro5,4",  # Nvidia 9000
    "MacBookPro5,5",  # Nvidia 9000
    "MacBookPro6,1",  # Intel 100 + Nvidia 300
    "MacBookPro6,2",  # Intel 100 + Nvidia 300
    "MacBookPro7,1",  # Nvidia 300
    "MacBookPro8,1",  # Intel 3000
    "MacBookPro8,2",  # Intel 3000 + AMD 6000
    "MacBookPro8,3",  # Intel 3000 + AMD 6000
    "Macmini3,1",  # Nvidia 9000
    "Macmini4,1",  # Nvidia 300
    "Macmini5,1",  # Intel 3000
    "Macmini5,2",  # AMD 6000
    "Macmini5,3",  # Intel 3000
    "iMac7,1",  # AMD 2000
    "iMac8,1",  # Nvidia and AMD 2400
    "iMac9,1",  # Nvidia 9000
    "iMac10,1",  # Nvidia 9000 and AMD 4000
    "iMac11,1",  # AMD 4000
    "iMac11,2",  # AMD 4000 and 5000
    "iMac11,3",  # AMD 5000
    "iMac12,1",  # AMD 6000
    "iMac12,2",  # AMD 6000
    "Dortania1,1",  # RTX 3080
]

LegacyGPUNvidia = [
    "MacBook5,1",  # Nvidia 9000
    "MacBook5,2",  # Nvidia 9000
    "MacBook6,1",  # Nvidia 9000
    "MacBook7,1",  # Nvidia 300
    "MacBookAir2,1",  # Nvidia 9000
    "MacBookAir3,1",  # Nvidia 300
    "MacBookAir3,2",  # Nvidia 300
    "MacBookPro4,1",  # Nvidia 8000
    "MacBookPro5,1",  # Nvidia 9000
    "MacBookPro5,2",  # Nvidia 9000
    "MacBookPro5,3",  # Nvidia 9000
    "MacBookPro5,4",  # Nvidia 9000
    "MacBookPro5,5",  # Nvidia 9000
    "MacBookPro6,1",  # Intel 100 + Nvidia 300
    "MacBookPro6,2",  # Intel 100 + Nvidia 300
    "MacBookPro7,1",  # Nvidia 300
    "Macmini3,1",  # Nvidia 9000
    "Macmini4,1",  # Nvidia 300
    "iMac9,1",  # Nvidia 9000
    # "iMac10,1", # Nvidia 9000 and AMD 4000
]

LegacyGPUAMD = [
    "MacBookPro8,2",  # Intel 3000 + AMD 6000
    "MacBookPro8,3",  # Intel 3000 + AMD 6000
    "Macmini5,2",  # AMD 6000
    "iMac7,1",  # AMD 2000
    # "iMac8,1", # Nvidia and AMD 2000
    # "iMac10,1", # Nvidia 9000 and AMD 4000
    "iMac11,1",  # AMD 4000
    "iMac11,2",  # AMD 4000 and 5000
    "iMac11,3",  # AMD 5000
    "iMac12,1",  # AMD 6000
    "iMac12,2",  # AMD 6000
]

LegacyGPUAMDIntelGen2 = [
    "MacBookPro8,2",  # Intel 3000 + AMD 6000
    "MacBookPro8,3",  # Intel 3000 + AMD 6000
    "Macmini5,2",  # AMD 6000
    "iMac12,1",  # AMD 6000
    "iMac12,2",  # AMD 6000
]

LegacyGPUIntelGen1 = [
    "MacBookPro6,1",  # Intel 100 + Nvidia 300
    "MacBookPro6,2",  # Intel 100 + Nvidia 300
]

LegacyGPUIntelGen2 = [
    "MacBookAir4,1",  # Intel 3000
    "MacBookAir4,2",  # Intel 3000
    "MacBookPro8,1",  # Intel 3000
    "MacBookPro8,2",  # Intel 3000 + AMD 6000
    "MacBookPro8,3",  # Intel 3000 + AMD 6000
    "Macmini5,1",  # Intel 3000
    "Macmini5,3",  # Intel 3000
]

LegacyBrightness = [
    "MacBook5,2",
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
]

LegacyHID = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro7,1",
    "Macmini3,1",
    "Macmini4,1",
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "MacPro3,1",
    "Dortania1,1",
]

NVMePatch = ["MacPro3,1", "MacPro4,1", "Xserve3,1", "Dortania1,1"]

XhciSupport = [
    "MacBookAir5,1",
    "MacBookAir5,2",
    "MacBookAir6,1",
    "MacBookAir6,2",
    "MacBookAir7,1",
    "MacBookAir7,2",
    "MacBookPro9,1",
    "MacBookPro9,2",
    "MacBookPro10,1",
    "MacBookPro10,2",
    "MacBookPro11,1",
    "MacBookPro11,2",
    "MacBookPro11,3",
    "MacBookPro11,4",
    "MacBookPro11,5",
    "MacBookPro12,1",
    "Macmini6,1",
    "Macmini6,2",
    "Macmini7,1",
    "iMac13,1",
    "iMac13,2",
    "iMac13,3",
    "iMac14,1",
    "iMac14,2",
    "iMac14,3",
    "iMac15,1",
    "iMac16,1",
    "iMac16,2",
    "MacPro6,1",
    "Dortania1,1",
]

SidecarPatch = [
    "MacBook8,1",
    "MacBookAir5,1",
    "MacBookAir5,2",
    "MacBookAir6,1",
    "MacBookAir6,2",
    "MacBookAir7,1",
    "MacBookAir7,2",
    "MacBookPro9,1",
    "MacBookPro9,2",
    "MacBookPro10,1",
    "MacBookPro10,2",
    "MacBookPro11,1",
    "MacBookPro11,2",
    "MacBookPro11,3",
    "MacBookPro11,4",
    "MacBookPro11,5",
    "MacBookPro12,1",
    "MacBookPro13,1",
    "MacBookPro13,2",
    "MacBookPro13,3",
    "MacBookPro14,1",
    "MacBookPro14,2",
    "MacBookPro14,3",
    "Macmini6,1",
    "Macmini6,2",
    "Macmini7,1",
    "Macmini8,1",
    "iMac13,1",
    "iMac13,2",
    "iMac13,3",
    "iMac14,1",
    "iMac14,2",
    "iMac14,3",
    "iMac15,1",
    "iMac16,1",
    "iMac16,2",
    "iMac17,1",
    "iMac18,1",
    "MacPro5,1",
    "MacPro6,1",
    "Dortania1,1",
]

DualGPUPatch = [
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "Macmini5,2",
    "iMac12,1",
    "iMac12,2",
    "iMac13,1",
    "iMac13,2",
    "iMac14,2",
    "iMac14,3",
    "Dortania1,1",
]

DualGPUPatchRetina = [
    "MacBookPro10,1",
    "MacBookPro11,3",
]

IntelNvidiaDRM = [
    "iMac13,1",
    "iMac13,2",
    "iMac14,2",
    "iMac14,3",
]

HiDPIpicker = ["MacBook8,1", "MacBookPro10,1", "MacBookPro10,2", "MacBookPro11,1", "MacBookPro11,2", "MacBookPro11,3", "iMac15,1", "Dortania1,1"]

IDEPatch = ["MacBook4,1", "MacBookPro4,1", "iMac7,1", "iMac8,1", "MacPro3,1", "Xserve2,1", "Dortania1,1"]

# 11" Air
MacBookAir61 = [
    "MacBookAir3,1",
    "MacBookAir4,1",
    "MacBookAir5,1",
    "MacBookAir6,1",
]

# Classic MacBook and 13" Air
MacBookAir62 = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookAir3,2",
    "MacBookAir4,2",
    "MacBookAir5,2",
    "MacBookAir6,2",
]

# Retina MacBook
MacBook81 = [
    "MacBook8,1",
]

# MacBook Pro 13"

MacBookPro111 = [
    "MacBookPro5,5",
    "MacBookPro7,1",
    "MacBookPro8,1",
    "MacBookPro9,2",
    "MacBookPro10,2",
    "MacBookPro11,1",
]

# MacBook Pro 15" (iGPU)

MacBookPro112 = ["MacBookPro11,2"]

# MacBook Pro 15" and 17" (dGPU)

MacBookPro113 = [
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "MacBookPro9,1",
    "MacBookPro10,1",
    "MacBookPro11,3",
]

# Mac Mini

Macmini71 = ["Macmini3,1", "Macmini4,1", "Macmini5,1", "Macmini5,2", "Macmini5,3", "Macmini6,1", "Macmini6,2"]
# iMacPro = dGPU only iMacs
iMacPro11 = [
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "iMac12,1",
    "iMac12,2",
]

# iMac = AMD and Nvidia GPU with iGPU
iMac151 = [
    "iMac13,2",
    "iMac14,2",
    "iMac14,3",
    "iMac15,1",
]
# iMac = Intel iGPU
iMac144 = ["iMac13,1", "iMac14,1", "iMac14,4"]

# Mac Pro and Xserve
MacPro71 = ["MacPro3,1", "MacPro4,1", "MacPro5,1", "Xserve2,1", "Xserve3,1", "Dortania1,1"]

XXerve = [
    "Xserve3,1",
]

iXac = [
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "iMac12,1",
    "iMac12,2",
    "iMac13,1",
    "iMac13,2",
    "iMac13,3",
    "iMac14,1",
    "iMac14,2",
    "iMac14,3",
]

XacBookNormal = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
]

XacBookAir = [
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookAir4,1",
    "MacBookAir4,2",
    "MacBookAir5,1",
    "MacBookAir5,2",
]

XacBookPro = [
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro7,1",
    "MacBookPro8,1",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "MacBookPro9,1",
    "MacBookPro9,2",
    "MacBookPro10,1",
    "MacBookPro10,2",
]

XacPro = [
    "MacPro3,1",
    "MacPro4,1",
    "MacPro5,1",
]

Xacmini = [
    "Macmini3,1",
    "Macmini4,1",
    "Macmini5,1",
    "Macmini5,2",
    "Macmini5,3",
    "Macmini6,1",
    "Macmini6,2",
]

ControllerTypes = [
    "",
    "-EHCI",
    "-EHC1",
    "-EHC2",
    "-XHC1",
    "-OHC1",
    "-OHC2",
    "-UHC1",
    "-UHC2",
    "-UHC3",
    "-UHC4",
    "-InternalHub-EHC1",
    "-InternalHub-EHC1-InternalHub",
    "-InternalHub-EHC2",
    "-InternalHub",
]

upgradableMXMGPUs = ["iMac10,1", "iMac11,1", "iMac11,2", "iMac11,3", "iMac12,1", "iMac12,2", "Xserve3,1", "Dortania1,1"]

NightShift = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookAir4,1",
    "MacBookAir4,2",
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro7,1",
    "MacBookPro8,1",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "Macmini3,1",
    "Macmini4,1",
    "Macmini5,1",
    "Macmini5,2",
    "Macmini5,3",
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "iMac12,1",
    "iMac12,2",
    "MacPro3,1",
    "MacPro4,1",
    "MacPro5,1",
    "Xserve2,1",
    "Xserve3,1",
    "Dortania1,1",
]

UGAtoGOP = [
    "MacBook4,1",
    "MacBookPro4,1",
    "iMac7,1",
    "iMac8,1",
    "MacPro3,1",
    "Xserve2,1",
]

SATAPatch = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookAir3,2",
    "MacBookAir4,1",
    "MacBookAir4,2",
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro7,1",
    "MacBookPro8,1",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "MacBookPro9,1",
    "MacBookPro9,2",
    "Macmini3,1",
    "Macmini4,1",
    "Macmini5,1",
    "Macmini5,2",
    "Macmini5,3",
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "iMac11,1",
    "iMac11,2",
    "iMac11,3",
    "iMac12,1",
    "iMac12,2",
    "MacPro3,1",
    "MacPro4,1",
    "MacPro5,1",
    "Xserve2,1",
    "Xserve3,1",
    "Dortania1,1",
]

NoAPFSsupport = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBookAir2,1",
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "Macmini3,1",
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "MacPro3,1",
    "MacPro4,1",
    "Xserve2,1",
    "Xserve3,1",
    "Dortania1,1",
]

NoRootPatch11 = [
    "MacBookAir5,1",
    "MacBookAir5,2",
    "MacBookPro9,1",
    "MacBookPro9,2",
    "MacBookPro10,1",
    "MacBookPro10,2",
    "Macmini6,1",
    "Macmini6,2",
    "iMac13,1",
    "iMac13,2",
    "iMac13,3",
    "iMac14,1",
    "iMac14,2",
    "iMac14,3",
    "MacPro4,1",
    "MacPro5,1",
    "Xserve3,1",
]

NoExFat = [
    "MacBook4,1",
    "MacBook5,1",
    "MacBook5,2",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir2,1",
    "MacBookPro4,1",
    "MacBookPro5,1",
    "MacBookPro5,2",
    "MacBookPro5,3",
    "MacBookPro5,4",
    "MacBookPro5,5",
    "MacBookPro6,1",
    "MacBookPro6,2",
    "MacBookPro7,1",
    "Macmini3,1",
    "iMac7,1",
    "iMac8,1",
    "iMac9,1",
    "iMac10,1",
    "iMac11,1",
    "MacPro3,1",
    "MacPro4,1",
    "MacPro5,1",
    "Xserve2,1",
    "Xserve3,1",
    "Dortania1,1",
]

SandyIGPU = [
    "MacBookAir4,1",
    "MacBookAir4,2",
    "MacBookPro8,1",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "Macmini5,1",
    "Macmini5,2",
    "Macmini5,3",
]

windows_audio = [
    "MacBookAir4,1",
    "MacBookAir4,2",
    "MacBookAir5,1",
    "MacBookAir5,2",
    "MacBookPro8,1",
    "MacBookPro8,2",
    "MacBookPro8,3",
    "MacBookPro9,1",
    "MacBookPro9,2",
    "MacBookPro10,1",
    "MacBookPro10,2",
    "Macmini5,1",
    "Macmini5,2",
    "Macmini5,3",
    "Macmini6,1",
    "Macmini6,2",
    "iMac12,1",
    "iMac12,2",
    "iMac13,1",
    "iMac13,2",
    "iMac13,3",
]

NoAGPMSupport = ["MacBook4,1", "MacBookPro4,1", "iMac7,1", "iMac8,1", "MacPro3,1", "Xserve2,1"]

AGDPSupport = [
    "MacBookPro9,1",
    "MacBookPro10,1",
    "iMac13,1",
    "iMac13,2",
    "iMac14,1",
    "iMac14,2",
    "iMac14,3",
    "iMac14,4",
    "iMac15,1",
    # TODO: Uncomment when dropped from macOS
    # "iMac17,1",
    # "iMac18,2",
    # "iMac18,3",
    # "iMac19,1",
    # "iMac19,2",
    # "iMac20,1",
    # "iMac20,2",
    # "iMacPro1,1",
    # "MacPro6,1",
]

AMCSupport = [
    "MacBookPro8,2",
    "MacBookPro8,3",
    # "MacBookPro9,1",
    # "MacBookPro10,1"
]

NoFireWireSupport = [
    "MacBook5,1",
    "MacBook6,1",
    "MacBook7,1",
    "MacBookAir1,1",
    "MacBookAir2,1",
    "MacBookAir3,1",
    "MacBookAir3,2",
]

RecoveryIgnore = ["Update", "VM", "Recovery", "Preboot"]
