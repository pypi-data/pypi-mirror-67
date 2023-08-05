from peacedeath.valves import Valves
from peacedeath.photodiodes import Photodiodes
from peacedeath.od_measurement import ODmeasurement
from peacedeath.pumps import Pumps
from peacedeath import pm
import pandas as pd
import numpy as np
import os

class Experiment:
    def __init__(self, name="NewExperiment", connect=True, device_serial="auto",fit_calibration_functions=True):
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
        assert 30 <= speed <= 100 or speed == 0
        if speed > 0:
            state = 1
        else:
            state = 0
        pulseWidth = int(period*speed/100)
        period = int(period)
        self.dev.request(pm.dev_msg.SetMixerStateRequest(state=state, period=period, pulseWidth=pulseWidth))
        return

    def connect_device(self, device_serial="auto"):
        # hub = pm.PMHub.local()
        self.hub = pm.PMHub("tcp://localhost:5555")
        if device_serial == "auto":
            dev = self.hub.get_devices()[0]
            self.dev = dev
            return dev
    def test_device(self):
        for t in range(7):
            self.Photodiodes.measure_current(t,3,20)

    def read_ODthresholds_from_file(self):
        ODthresholds = pd.read_csv(os.path.join(self.name, "OD_thresholds.csv"), header=None).values[0]
        ODthresholds = np.array(ODthresholds.ravel()).astype(float)
        return ODthresholds

