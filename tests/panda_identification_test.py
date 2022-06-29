#!/usr/bin/env python3
import os
import time
import random
import contextlib

from panda_jungle import PandaJungle
from panda import Panda

PANDA_UNDER_TEST = Panda.HW_TYPE_BLACK_PANDA

panda_jungle = PandaJungle()

def silent_panda_connect():
  with open(os.devnull, "w") as devnull:
    with contextlib.redirect_stdout(devnull):
        while True:
            try:
                panda = Panda()
                break
            except:
                time.sleep(1)
  return panda

def reboot_panda(harness_orientation=PandaJungle.HARNESS_ORIENTATION_NONE, ignition=False):
  print(f"Restarting panda with harness orientation: {harness_orientation} and ignition: {ignition}")
  panda_jungle.set_panda_power(False)
  panda_jungle.set_harness_orientation(harness_orientation)
  panda_jungle.set_ignition(ignition)
  time.sleep(2)
  panda_jungle.set_panda_power(True)
  time.sleep(2)

count = 0
if __name__ == "__main__":
  while True:
    ignition = random.randint(0, 1)
    harness_orientation = random.randint(0, 2)
    reboot_panda(harness_orientation, ignition)

    p = silent_panda_connect()
    assert p.get_type() == PANDA_UNDER_TEST
    assert p.health()['car_harness_status'] == harness_orientation
    if harness_orientation != PandaJungle.HARNESS_ORIENTATION_NONE:
      assert p.health()['ignition_line'] == ignition

    count += 1
    print(f"Passed {count} loops")


