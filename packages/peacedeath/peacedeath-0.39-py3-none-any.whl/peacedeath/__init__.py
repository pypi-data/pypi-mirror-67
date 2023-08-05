from peacedeath.valves import Valves
from peacedeath.photodiodes import Photodiodes
from peacedeath.od_measurement import ODmeasurement
from peacedeath.pumps import Pumps
from peacedeath import pm
from peacedeath.experiment import start_experiment, write_parameters_OD_thresholds, write_parameters_drug_doses, \
    read_parameters_OD_thresholds, read_parameters_drug_doses
import pandas as pd
import numpy as np
import os
import time


class Experiment:
    def __init__(self, name="NewExperiment", connect=True, device_serial="auto", fit_calibration_functions=True):
        """
        :param name: Experiment name with no spaces, e.g. starting date
        :param device_serial: board serial number or "auto" to auto-connect
        """
        assert " " not in name
        self.name = name
        if not os.path.exists(self.name):
            os.mkdir(self.name)
        if connect:
            self.dev = self.connect_device(device_serial=device_serial)
            self.Valves = Valves(self)
            self.Photodiodes = Photodiodes(self)
            self.Pumps = Pumps(self)
        else:
            self.dev = None
            self.hub = None
            print("Not connected to device")
        self.OD_measurement = ODmeasurement(self, fit_calibration_functions=fit_calibration_functions)

    def mix(self, speed=70, period=3000):
        if 0 < speed < 30:
            speed = 30
        if speed > 100:
            speed = 100

        if speed > 0:
            state = 1
        else:
            state = 0

        pulseWidth = int(period * speed / 100)
        period = int(period)
        self.dev.request(pm.dev_msg.SetMixerStateRequest(state=state, period=period, pulseWidth=pulseWidth))

        # log
        try:
            with open(os.path.join(self.name, "log_mixer.csv"), "a") as f:
                f.write(time.ctime() + ",%d\n" % speed)
        except FileNotFoundError:
            with open(os.path.join(self.name, "log_mixer.csv"), "w+") as f:
                f.write("time, speed \n")
                f.write(time.ctime() + ",%d\n" % speed)

    def connect_device(self, device_serial="auto"):
        # hub = pm.PMHub.local()
        self.hub = pm.PMHub("tcp://localhost:5555")
        if device_serial == "auto":
            dev = self.hub.get_devices()[0]
            self.dev = dev
            return dev

    def test_device(self):
        print("Testing OD measurement...")
        for t in range(7):
            self.Photodiodes.measure_current(t, 1, 10)
        print("Testing mixers...")
        for speed in [30, 50, 100]:
            self.mix(speed)
            time.sleep(1)
        self.mix(0)
        print("Testing valves...")
        for t in range(7):
            self.Valves.open_valve(t)
            self.Valves.close_valve(t)
        print("Testing pumps...")
        self.Pumps.pump_peace(6, 0.1)
        self.Pumps.pump_death(6, 0.1)
        self.Pumps.pump_vacuum(6, 0.1)

    def start_experiment(self, total_dilution_volume=10, mixer_speed=30, active_tubes=()):
        start_experiment(self, total_dilution_volume=total_dilution_volume,
                         mixer_speed=mixer_speed, active_tubes=active_tubes)

    def write_parameters_drug_doses(self, drug_doses=(0, 0, 0, 0, 0, 0, 0)):
        write_parameters_drug_doses(self, drug_doses=drug_doses)

    def read_parameters_drug_doses(self):
        return read_parameters_drug_doses(self)

    def write_parameters_OD_thresholds(self, OD_thresholds=(0, 0, 0, 0, 0, 0, 0)):
        write_parameters_OD_thresholds(self, OD_thresholds=OD_thresholds)

    def read_parameters_OD_thresholds(self):
        return read_parameters_OD_thresholds(self)
