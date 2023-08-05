import os
import time
import pandas as pd
import schedule
import numpy as np


def read_last_OD_values(pe):
    def strtoint(s):
        try:
            return float(s)
        except:
            return None

    df=pd.read_csv(pe.OD_measurement.od_file, index_col=0)
    lastvalues = [0,0,0,0,0,0,0]
    for t in range(7):
        try:
            ODvalues=list(strtoint(s) for s in df.iloc[:, t])
            ODvalues=[od for od in ODvalues if od]
            lastvalues[t]=ODvalues[-1]
        except:
            pass
    return np.array(lastvalues)


def make_dilution(pe, tube, death_volume=0, peace_volume=0, extra_vacuum=5):
    pe.mix(30)   # Mixer speed > 30 while pumping may lead to power failure!
    if death_volume>0:
        pe.Pumps.pump_death(tube, death_volume)
    if peace_volume>0:
        pe.Pumps.pump_peace(tube, peace_volume)
    pe.Pumps.pump_vacuum(tube, death_volume+peace_volume)
    pe.mix(0)
    pe.Pumps.pump_vacuum(tube, extra_vacuum)
    pe.mix(30)


def write_parameters_drug_doses(pe, doses=(0, 0, 0, 0, 0, 0, 0)):
    assert len(doses) == 7
    with open(os.path.join(pe.name, "parameters_dose.csv"), "w+") as f:
        f.write(",".join([str(d) for d in doses]))


def read_parameters_drug_doses(pe):
    df = pd.read_csv(os.path.join(pe.name, "parameters_dose.csv"), header=None)
    drug_doses = np.array(df.values.ravel()).astype(float)
    pe.drug_doses = drug_doses
    return drug_doses


def write_parameters_OD_thresholds(pe, OD_thresholds=(0, 0, 0, 0, 0, 0, 0)):
    OD_thresholds = np.array(OD_thresholds).astype(float)
    assert len(OD_thresholds) == 7
    with open(os.path.join(pe.name, "parameters_OD_thresholds.csv"), "w+") as f:
        f.write(",".join([str(thr) for thr in OD_thresholds]))


def read_parameters_OD_thresholds(pe):
    OD_thresholds = pd.read_csv(os.path.join(pe.name, "parameters_OD_thresholds.csv"), header=None).values[0]
    OD_thresholds = np.array(OD_thresholds.ravel()).astype(float)
    pe.OD_thresholds = OD_thresholds
    return OD_thresholds


def dilute_if_necessary(pe, total_dilution_volume=10):
    OD_thresholds = read_parameters_OD_thresholds(pe)  # 7 OD thresholds
    drug_doses = read_parameters_drug_doses(pe)  # 7 death volumes
    death_volumes = total_dilution_volume * drug_doses/100
    peace_volumes = total_dilution_volume - death_volumes
    for tube in range(7):
        if OD_thresholds[tube] > 0.15 and pe.tubes_status_active[tube]:
            if pe.last_OD_values[tube] > OD_thresholds[tube]:
                make_dilution(pe, tube,
                              death_volume=death_volumes[tube],
                              peace_volume=peace_volumes[tube],
                              extra_vacuum=5)


def pause_mixers_and_measure_OD(pe, mixer_speed):
    pe.mix(mixer_speed)
    time.sleep(2)
    pe.mix(0)
    time.sleep(3)
    for t in range(7):
        pe.last_OD_values[t] = pe.OD_measurement.measure_OD(t)
    pe.mix(mixer_speed)


def start_experiment(pe, total_dilution_volume=10, mixer_speed=30, active_tubes=()):
    schedule.clear()
    pe.tubes_status_active = [i in active_tubes for i in range(7)]
    print("Starting Experiment loop")
    print("Active tubes: ", dict(zip(range(7), pe.tubes_status_active)))

    pe.mix(mixer_speed)
    try:
        pe.last_OD_values = read_last_OD_values(pe)
    except FileNotFoundError:
        pe.last_OD_values = [0]*7
    print("Last OD values: ", dict(zip(range(7), pe.last_OD_values)))

    try:
        pe.drug_doses = read_parameters_drug_doses(pe)
    except FileNotFoundError:
        write_parameters_drug_doses(pe)
        read_parameters_drug_doses(pe)
    print("Death doses:", dict(zip(range(7), pe.drug_doses)))

    try:
        pe.OD_thresholds = read_parameters_OD_thresholds(pe)
    except FileNotFoundError:
        write_parameters_OD_thresholds(pe)
        read_parameters_OD_thresholds(pe)
    print("OD thresholds:", dict(zip(range(7), pe.OD_thresholds)))

    schedule.every().minute.at(":00").do(pause_mixers_and_measure_OD, pe,
                                         mixer_speed=mixer_speed)
    schedule.every().minute.at(":15").do(dilute_if_necessary, pe,
                                         total_dilution_volume=total_dilution_volume)

    while True:
        if not os.path.exists(os.path.join(pe.name, "stop.status")):
            schedule.run_pending()
            time.sleep(1)
        else:
            print("Loop aborted with stop.status file")
            break