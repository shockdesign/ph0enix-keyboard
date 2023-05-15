import storage
import usb_cdc
import usb_midi

storage.disable_usb_drive()  # disable CIRCUITPY
usb_cdc.disable()            # disable REPL
usb_midi.disable()           # disable MIDI
