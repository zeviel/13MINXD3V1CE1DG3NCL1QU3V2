from hmac import new
from os import urandom
from hashlib import sha1
from pyfiglet import figlet_format
from progress.bar import IncrementalBar
from colored import fore, style, attr; attr(0)
print(fore.DARK_GREEN_SEA + style.BOLD)
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(figlet_format("13MINXD3V1CE1DG3NCL1QU3V2", font="smslant", width=64))

def device_Id_generator(identifier: str):
	return ("32" + identifier.hex() + new(bytes.fromhex("76b4a156aaccade137b8b1e77b435a81971fbd3e"), b"\x32" + identifier, sha1).hexdigest()).upper()

def generation_process(count: int):
    progress_bar = IncrementalBar("Generated", max=count)
    with open("device_Ids.txt", "a") as device_Ids:
    	for i in range(count):
    		device_Id = device_Id_generator(identifier=urandom(20))
    		device_Ids.write(f"{device_Id}\n")
    		progress_bar.next()
    	progress_bar.finish()
    	print(f"-- Generated {count} deviceIDs...")
    
generation_process(count=int(input("How much deviceID generate >> ")))
