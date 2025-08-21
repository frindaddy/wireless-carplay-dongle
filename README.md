# wireless-carplay-dongle

As of 8/20/2025 this won't work without a MFi chip to enable iAP2 authentication.
The iPhone needs to authenticate that the accessory it is connecting to is, in fact, an authenticated Apple accessory before it sends any sort of CarPlay packets.
See `Carplay Spec --> carplay.pdf --> 23.2.5.2` for more info. The iPhone must authenticate before it advertises the CarPlay Control Bonjour service and begins sending CarPlay data (which we want to forward to the CarPlay head)

There might be a way to get around this using BLE iAP2 authentication, but as of now I'm not convinced.