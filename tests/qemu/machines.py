# flake8: noqa E131

import pathlib
from runners import TestLeaveAllDefault

parameters = {
	"pci_emulation" : {
		'test_class' : TestLeaveAllDefault,
		'arguments' : [
			'/usr/bin/qemu-system-x86_64',
			'-name', '"archinstall-test"',
			'-display', 'none',
			'-monitor', 'none',
			'-nographic',
			'-m', '4096',
			'-smp', '4,sockets=1,dies=1,cores=4,threads=1',
			'-usb', '-device', 'usb-host,vendorid=0x1050,productid=0x0407',
			'-pidfile', f'{pathlib.Path(__file__).parent}/archinstall-test.pid',
			'-cpu', 'host,topoext,kvm=off,hv_relaxed,hv_spinlocks=0x1fff,hv_vapic,hv_time',
			'-enable-kvm',
			'-object', 'rng-random,filename=/dev/urandom,id=rng0',
			'-device', 'virtio-rng-pci,rng=rng0',
			'-usbdevice', 'mouse',
			'-global', 'driver=cfi.pflash01,property=secure,value=on',
			'-machine', 'type=q35,accel=kvm,kernel_irqchip=on',
			'-smbios', '"type=0,vendor=American Megatrends Inc.,version=P4.60,date=08/03/2021,release=08.03.2021"',
			'-smbios', '"type=1,manufacturer=Inet_AB,product=To Be Filled By O.E.M.,version=To Be Filled By O.E.M.,serial=245797,uuid=4154a2b8-7b7f-0000-0000-000000000000,sku=To Be Filled By O.E.M.,family=To Be Filled By O.E.M."',
			'-smbios', '"type=2,manufacturer=ASRock,product=X570 Taichi,version=,serial=M80-D00000012340asset=,location="',
			'-smbios', '"type=3,manufacturer=To Be Filled By O.E.M.,version=To Be Filled By O.E.M.,serial=214345,asset=To Be Filled By O.E.M.,sku=To Be Filled By O.E.M."',
			'-smbios', '"type=4,sock_pfx=AM4,manufacturer=Advanced Micro Devices,, Inc.,version=AMD Ryzen 9 5900X 12-Core Processor,serial=Unknown,asset=Unknown,part=Unknown"',
			'-smbios', '"type=17,loc_pfx=DIMM 1,bank=P0 CHANNEL A,manufacturer=Unknown,serial=00000000,asset=Not Specified,part=CMK64GX4M2E3200C16,speed=2133"',
			'-smbios', '"type=17,loc_pfx=DIMM 1,bank=P0 CHANNEL B,manufacturer=Unknown,serial=00000000,asset=Not Specified,part=CMK64GX4M2E3200C16,speed=2133"',
			'-device', 'intel-iommu,device-iotlb=on,caching-mode=on',
			'-device', 'pcie-root-port,port=0xe,chassis=8,id=pci.8,bus=pcie.0,multifunction=on,addr=0x6',
			'-device', 'virtio-keyboard-pci,id=input1,bus=pci.8,addr=0x0',
			'-device', 'pcie-root-port,port=0xf,chassis=9,id=pci.9,bus=pcie.0,addr=0x6.0x1',
			'-device', 'pcie-root-port,port=0x11,chassis=13,id=pci.13,bus=pcie.0,addr=0x6.0x3',
			'-drive', 'if=pflash,format=raw,readonly=on,file=/usr/share/ovmf/x64/OVMF_CODE.secboot.fd',
			'-drive', f'if=pflash,format=raw,file={pathlib.Path(__file__).parent}/OVMF_VARS.fd',
			# '-tpmdev', 'passthrough,id=tpm0,path=/dev/tpm0,cancel-path=/tmp/foo-cancel2',
			# '-device', 'tpm-tis,tpmdev=tpm0',
			'-object', 'iothread,id=iothread1',
				'-device', 'virtio-scsi-pci,bus=pcie.0,id=scsi2,addr=0x8',
				'-device', 'virtio-scsi-pci,iothread=iothread1,id=scsi0,num_queues=8,bus=pci.13,addr=0x0',
					'-device', '"scsi-hd,serial=S5GBAD12345ABCE,drive=libvirt-1-format,bus=scsi2.0,id=scsi0-0-0-0,channel=0,scsi-id=0,lun=0,device_id=drive-scsi0-0-0-0,bootindex=2,write-cache=on"',
						'-blockdev', '\'{"driver":"file","filename":"./archtest.img","aio":"threads","node-name":"libvirt-1-storage","cache":{"direct":true,"no-flush":false},"auto-read-only":true,"discard":"unmap"}\'',
						'-blockdev', '\'{"node-name":"libvirt-1-format","read-only":false,"discard":"unmap","cache":{"direct":true,"no-flush":false},"driver":"qcow2","file":"libvirt-1-storage","backing":null}\'',
			'-device', 'pcie-root-port,multifunction=on,bus=pcie.0,id=port9-0,addr=0x9,chassis=0',
				'-device', 'virtio-net-pci,mac=FE:00:00:00:00:01,id=network0,netdev=network0.0,status=on,bus=port9-0',
					'-netdev', 'tap,ifname=tap0,id=network0.0,script=no,downscript=no',
			'-audiodev', 'pipewire,id=win11',
				'-device', 'ich9-intel-hda,id=sound0,bus=pcie.0,addr=0x1b',
				'-device', 'hda-micro,audiodev=win11',
		]
	}
}