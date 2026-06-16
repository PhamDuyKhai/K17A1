import subprocess
import pandas as pd
import time
import os

INTERFACE = "ens33"

OUTPUT_FILE = "Packet_Network_Data.csv"

FIELDS = [
    "frame.time_epoch",
    "ip.src",
    "ip.dst",
    "tcp.srcport",
    "tcp.dstport",
    "tcp.len",
    "frame.len"
]

cmd = [
    "sudo",
    "tshark",
    "-i",
    INTERFACE,
    "-Y",
    "tcp",
    "-T",
    "fields"
]

for field in FIELDS:
    cmd.extend(["-e", field])

cmd.extend([
    "-E", "header=y",
    "-E", "separator=,",
    "-a", "duration:120"
])

print("Bat dau capture packet...")

with open(OUTPUT_FILE, "w") as outfile:

    process = subprocess.Popen(
        cmd,
        stdout=outfile,
        stderr=subprocess.DEVNULL
    )

    process.wait()

print("Da tao Packet_Network_Data.csv")
