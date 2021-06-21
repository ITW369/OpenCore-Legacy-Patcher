# OpenCore Legacy Patcher changelog

## 0.2.0
- Refactor device probe logic
- Implement PatcherSupportPkg v0.0.8
  - Reduces binary sizes depending on OS
  - Deprecates Apple-Binaries-OCLP
- Fix full screen and Airplay to Mac support for Intel HD4000 iGPUs in Monterey
- Automatically set `CMIO_Unit_Input_ASC.DoNotUseOpenCL` on TeraScale 2 GPUs
- Fix Country Code detection on Wireless Cards
- Add Windows detection and prompt during installation
- Fix Google Fonts rendering for Intel HD4000 iGPUs in Monterey
- Increment Binaries
  - Lilu 1.5.4 rolling (f69a972 - 06-20-2021)
  - RestrictEvents 1.0.3 rolling (3773ce2 - 06-20-2021)
  - SidecarFixup 1.0.2 rolling (2c29166 - 06-21-2021)
- Allow AirPlay to Mac support on Skylake - Coffeelake Macs

## 0.1.9
- Fix incorrect AMFI and SIP detection

## 0.1.8
- Fix Kernel Panic in Big Sur and Monterey
- Increment binaries:
  - Lilu (1.5.4 rolling - 06-15-2021)

## 0.1.7
- Add FireWire Boot Support for Catalina and newer
- Add NVMe firmware support for older models (ie. MacPro3,1)
  - OpenCore must be stored on a bootable volume (ie. USB or SATA)
- Fix Thunderbolt Ethernet support on MacBookAir4,x
- Fix XHCI hangs on pre-2012 Machines
  - XHCI boot support dropped due to instability
- Add beta macOS Monterey Support
  - Fix iMac13,x sleep support
  - Add support for following models:
    - iMac14,4
    - iMac15,1
    - MacBook8,1
    - MacBookAir6,1
    - MacBookAir6,2
    - MacBookPro11,1
    - MacBookPro11,2
    - MacBookPro11,3
- Increment binaries:
  - OpenCore (0.7.0 release - 06-07-2021)
  - AirportBrcmFixup (2.1.3 rolling - 06-08-2021)
  - AppleALC (1.6.2 rolling - 06-08-2021)
  - CPUFriend (1.2.4 rolling - 06-08-2021)
  - Lilu (1.5.4 rolling - 06-11-2021)
  - NVMeFix (1.0.9 rolling - 06-12-2021)
  - WhateverGreen (1.5.1 rolling - 06-08-2021)
  - RestrictEvents (1.0.3 rolling - 06-11-2021)
  - Apple Binaries (0.0.18 release - 06-12-2021)
  - MouSSE (0.95 release - 06-08-2021)
  - SidecarFixup (1.0.2 rolling - 06-11-2021)
- Fix SSE4,2 Emulation
- Fix Sidecar and CPU renaming support in macOS Monterey
- Add AirPlay support to older Models
- Add Intel HD4000 Acceleration
  - Big thanks to Jackluke, EduCovas, DhinakG, MykolaG!
- Add DebugEnhancer for better macOS Monterey logs
  - DebugEnhancer (1.0.3 rolling - 06-08-2021)
- Add TeraScale 2 Graphics Acceleration to Big Sur
  - User configurable, those prone to seizures are recommended to avoid or have another setup the machine due to initial colour strobing before forcing Million Colours on the display with SwitchResX or ResXtreme

## 0.1.6
- Add XHCI UEFI Driver for 3rd Party USB 3.0 Controllers
  - Allows for Boot Support from OpenCore' Picker
- Fix UEFI output on MacPro3,1 with PC GPUs
- Increment binaries:
  - OpenCore 4e0ff2d (0.7.0 rolling - 05-23-2021)
  - Apple Binaries 59a52a3 (0.0.8 release - 05-24-2021)
- Allow legacy macOS Booting
- Fix Photos app distortion on legacy GPUs
- Fix device tree renaming on Mac Pros and Xserves
- Ensure no Acceleration Patches applied when no compatible GPU found
- Allow custom SMBIOS overriding
- Fix incorrectly setting CPU override for non-Minimal SMBIOS spoofs
- Support Minimal SMBIOS spoofing on El Capitan era Macs
- Fix GPU Switching on MacBookPro6,x

## 0.1.5
- Fix crashing when Wireless module not present
- Add iMac10,1 default dGPU pathing
- Add agdpmod=vit9696 to all Nvidia Metal iMacs
  - Fixes external display support on Nvidia iMac12,x
- Remove reliance on AppleBacklightFixup
- Support space in path when downloading Root Patches
- Enable PanicNoKextDump by default
- Expand AppleGraphicsPowerManagement and AppleGraphicsDeviceControl Override support
- Fix MacBookPro8,2/3 Brightness Control
  - dGPU must be disabled via NVRAM or deMUXed
- Increment binaries:
  - Apple Binaries 478f6a6 (0.0.7 release - 05-16-2021)
- Add SeedUtil option to Advanced Patcher Settings

## 0.1.4
- Fix Device Path formatting on 2012+ iMacs

## 0.1.3
- Fix internal PCIe devices reporting as external
  - Opt for `built-in` when device path is detectable
  - Innie 0ccd95e (1.3.0 release - 01-16-2021)
- Fix MacBookPro5,4 audio support
- Increment binaries
  - AppleALC 58b57ee (1.6.1 rolling - 05-07-2021)
  - Apple Binaries 74bd80f (0.0.6 release - 05-09-2021)
- Support custom CPU names in About This Mac
- Fix NightShift accidentally disabling on Minimal SMBIOS configs
- Fix iMac9,1 audio support
- Heavily expand Graphics ID list
- Fix iMac7,1 and iMac8,1 audio support
- Work-around Bluetooth Kernel Panic on Apple's Bluetooth 2.0 Controllers (USB 05AC:8206)
  - Affects iMac7,1 and MacPro3,1
- Fix iMac external display support
- Fix NVMe properties not applying when OpenCore is installed

## 0.1.2
- Fix IDE support on 2008 era MacBooks, iMacs and Xserves
- Fix reduced output speeds on BCM94360 series Wifi cards
- Fix accidentally disabling non-existent iGPU in iMac11,2
- Remove USB ACPI Patching requirement for Minimal SMBIOS setups
- Probe hardware for Backlight pathing on iMac10,1, iMac11,x and iMac12,x with Metal GPUs
- Add Windows UEFI Audio support to Sandy and Ivy Bridge Macs
- Add 3rd Party NVMe Power Management Patches
  - NVMeFix fafc52d (1.0.7 release - 05-03-2021)
- Strip unused ACPI and Kernel entries during build
- Allow native Macs to use OpenCore
  - Better 3rd party NVMe support
  - Better Wireless networking support
- Fix MacBook6,1 audio support
- Increment binaries
  - OpenCore 65cc81b (0.6.9 release - 05-03-2021)
  - Lilu c77722d (1.5.3 release - 05-03-2021)
  - AppleALC 84850d0 (1.6.0 rolling - 04-30-2021)
  - RestrictEvents 9e2bb0f (1.0.1 release - 05-03-2021)
- Allow CPUFriend on all El-Capitan Era Macs
- Fix UEFI 2.0 Application support on upgraded Nvidia GPUs
- Add experimental Sidecar support
  - Requires Mac with Metal Intel iGPU and the iPad to be directly plugged in, wireless highly unstable
  - SidecarFixup efdf11c (1.0.0 release - 05-02-2021)

## 0.1.1
- Fix iMac11,3 GFX0 pathing
- Add MouSSE support to iMac10,1 with Metal AMD GPU
- Fix iMac11,1 and iMac11,3 Nvidia boot issues after PRAM reset
- Fix DRM support on Nvidia-only configurations
  - Support optional setting between DRM and QuickSync support on iMacs13,x and iMac14,x
- Add public beta support for Legacy GPU Acceleration (v0.0.4)
  - Note ATI/AMD TeraScale 2 unsupported (HD 5/6000)
- Add better kmutil crash handling
- Fix build crashing when no wifi card is present
- Allow Legacy Acceleration Patches on Mac Pros and Xserves
- Fix USB kernel panics on iMac7,1
- Fix AppleALC support in Mojave
- Fix TeraScale 1 GPU detection
- Enable Graphics Acceleration on legacy GPUs by default
- Fix incorrectly disabling SIP/SMB on Metal GPUs
- Fix error output when rebuilding kernel cache fails
- Fix Acceleration Linking for Intel Ironlake iGPUs

## 0.1.0
- Fix crash on iMacs with Metal GPUs

## 0.0.23
- Fix MacBookPro4,1 15" and 17" audio support
- Fix iMac7,1 24" and iMac9,1 24" audio support
- Fix Macmini4,1 audio support
- Increment binaries
  - AppleALC 1a3e5cb (1.6.0 rolling - 04-14-2021)
- Enhance Wifi model detection
- Hide OpenShell.efi by default
- Add Brightness Control patches for legacy Nvidia, AMD and Intel GPUs
  - Models with brightness control issues in Catalina partially supported
- Add user configurable Bootstrap setting
- Enhance GPU Detection logic
- Increment AppleBackLightFixup v1.0.1
  - Add panel type F10T9cde
- Enhance HDMI audio support on Mac Pros and Xserves
- Strip unused kext entries during build
- Add gfxutil support for better DeviceProperty path detection
- Add basic CLI support
- Disable SIP and SecureBootModel by default on legacy GPUs

## 0.0.22
- Add ExFat support for models missing driver
  - Aids BootCamp support for EFI based installs on 2010 and older Macs
- Fix CPU Boosting on 2011 and older Macs
- Add basic support for Xserve2,1
- Add AppleALC support(99b3662 - 1.6.0 rolling - 04-09-2021), remove AppleHDA patching requirement
- Add BCM94322 and BCM94321 chipset support

## 0.0.21
- Fix botched images in OpenCanopy
- Add support for 3rd party OpenCore usage detection during building
  - Mainly for users transitioning from Ausdauersportler's OpenCore configuration

## 0.0.20
- Fix CPU Calculation on early MCP79 chipsets (ie. iMac9,1, MacBook5,x)
- Increment binaries
  - OpenCore c528597 (0.6.8 release - 2021-04-05)
  - Lilu 3ef7ca1 (1.5.2 release - 2021-04-05)
  - WhateverGreen afcd687 (1.4.9 release - 2021-04-05)
- Move Apple binaries to dedicated repo and allow custom repos
  - Reduces App size 1/5th compared to 0.0.19
- Fix OpenCanopy support on iMac7,1 and 8,1
- Set iGPU-less iMacs to iMacPro1,1
  - Additionally fixes Bluetooth on older iMacs with BRCM2046 modules
- Add MacBook4,1 support
- Create dedicated RestrictEvents build for MacBookPro9,1
- Fix Mac Pro and Xserve output issues

## 0.0.19
- Add SMC-Spoof.kext to avoid triggering `smcupdater`
- Add Root Volume patching for older machines
  - AppleHDA Patch for 2011 and older (Excluding MacPro4,1+)
- Fix CPU Speed reporting
- Increment binaries
  - OpenCore 9cd61bb (0.6.8 rolling - 2021-03-27)
- Add Mavericks and newer .app support
- Refactor USB map building, fixes USB 3.0 displaying as USB 2.0
- Fix blackscreen on MacBookPro9,1
- Update RestrictEvents with custom build (1.0.1)
  - Blocks `/usr/libexec/displaypolicyd` on MacBookPro9,1 to ensure smooth GPU switching
- Add custom SD Card icon
- Add automatic codesiging and notarization
- Fix crashing when CD is present
- Add custom SSD icon
- Fix Broadcom Ethernet on older 2009-2011 Macs

## 0.0.18
- Disable Vault by default due to breaking installations
- Move BOOTx64.efi to System/Library/CoreServices/ to support GPT BootCamp installs
- Disable verbose by default, still configurable by end-user
- Remove `AppleInternal`(0x10) from SIP value
- Add Mac Pro DRM patches for Metal GPUs
- Force `Moderate` SMBIOS replacement for models without native APFS support
- Re-enable legacy BCM94322 networking patches
- Add custom drive icons for external drives

## 0.0.17
- Fix build detection breaking on older OS

## 0.0.16
- Move Serial selection to Patcher Settings
- Add new SMBIOS patching options:
  - Minimal:  Only update board ID and BIOSVersion, keep original serials
  - Moderate: Update entire SMBIOS, keep original serials
  - Advanced: Update entire SMBIOS, generate new serials
- Fix crash on MacBookPro4,1
- Fix External Display Support on MacBookPro10,1
- Inject Patcher version into NVRAM for easier debugging
- Add user-configurable ShowPicker
- Add user-configurable Vaulting, enabled by default
- Add user-configurable SIP and SecureBootModel
- Fix USB Maps not working on "Minimal" SMBIOS
- Fix GPU vendor user-configuration
- Fix custom EFI Boot icon in Mac Boot Picker
- Enable UserInterfaceTheme to ensure DefaultBackgroundColor is respected
- Enable `amfi_get_out_of_my_way=1` when SIP is disabled

## 0.0.15
- Add user-configurable OpenCore DEBUG builds
- Add user-configurable Wifi and GPU patches
- Fix ThirdPartyDrives model detection
- Add HW_BID injection to fix boot.efi error

## 0.0.14
- Enable ThirdPartyDrives to aid with hibernation on 3rd party SATA drives
- Increment OpenCore 7bb41aa (0.6.8 rolling, 2021-03-06)
- Add ForceBooterSignature to resolve hibernation issues
- Add NightShiftEnabler (1.1.0 release e1639f9)
- Add user-configurable verbose and debug settings
- Add GopPassThrough quirk for UGA-based systems

## 0.0.13
- Add CPUFriend support to resolve X86PlatformPlugin clashes
    - (1.2.3 c388a62 release)
- Fix crash with MacBookAir5,x
- Fix hibernation support
- Remove Wireless patches for BCM4328/4321(14e4:4328) due to boot issues

## 0.0.12
- Convert OpenCore-Patcher binary to OpenCore-Patcher.app
- Add Backlight patches for modded Nvidia GPUs in iMac10,x-12,x
- Fix sleep for iMac12,x with upgraded GPUs

## 0.0.11
- Re-add OpenCore GUI
- Rewrite in py3
- Add OpenCore-Patcher binary for releases avoiding local python requirement
- Increment binaries
    - OpenCore cbd2fa3 (0.6.7 release)
    - WhateverGreen 2e19d1b (1.4.8 release)
- Rework SMBIOS allowing both original and custom serials(Should resolve all iMessage issues)
- Support upgraded GPU detection in iMac10,x-12,x
- Add Wifi card upgrade detection

## 0.0.10
- Increment binaries
    - OpenCore 43f5339 (0.6.6 release)
    - Lilu d107554 (1.5.1 release)
    - WhateverGreen 9e53d8a (1.4.7 release)
- Add IDE support to MacPro3,1
- Set SecureBootModel to iMac Pro(should aid in booting older OSes with OpenCore)
- Update MacBookPro SMBIOS

## 0.0.9
- Resolve firmware install issues bricking Macs

## 0.0.8
- Fix USB Map
- Add HiDPI patch

## 0.0.7
- Add MacPro3,1 to HID patch
- Fix missing SSDT-CPBG patch
- Fix BlacklistAppleUpdate
- Add RestrictEvents kext

## 0.0.6
- Fix macserial crashing

## 0.0.5
- Enable hibernation support
- Work around USB Map failing
- Add checks whether booting with OpenCore
- Fix MouSSE injection

## 0.0.4
- Add basic audio support for legacy chipsets
- Add patch for dual GPU machines

## 0.0.3
- Fix Wireless patch logic

## 0.0.2
- Expand IOHIDFamily Patch to all Nvidia chipsets
- Fix Airdrop 1.0 support
- Add El Capitan era wireless cards

## 0.0.1
- Initial developer preview
