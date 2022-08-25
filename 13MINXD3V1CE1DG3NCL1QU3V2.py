from hmac import new
from os import urandom
from hashlib import sha1
from pyfiglet import figlet_format
from progress.bar import IncrementalBar
print("""Script by zeviel
Github : https://github.com/zeviel""")
print(figlet_format("13MINXD3V1CE1DG3NCL1QU3V2", font="smslant", width=64))

def generate_device_id(identifier: str):
	return ("32" + identifier.hex() + new(bytes.fromhex("76b4a156aaccade137b8b1e77b435a81971fbd3e"), b"\x32" + identifier, sha1).hexdigest()).upper()

def generation_process(count: int):
    progress_bar = IncrementalBar("Generated", max=count)
    with open("device_ids.txt", "a") as file:
    	for i in range(count):
    		device_id = generate_device_id(urandom(20))
    		file.write(f"{device_id}\n")
    		progress_bar.next()
    	progress_bar.finish()
    	print(f"-- Generated {count} deviceIDs...")
    
generation_process(int(input("How much deviceID generate >> ")))
