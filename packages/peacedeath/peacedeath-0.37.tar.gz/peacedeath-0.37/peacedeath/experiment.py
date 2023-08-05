import os
import time
import pandas as pd
import schedule


def read_thresholds_from_file(pe):
    df=pd.read_csv(os.path.join(pe.name,"thresholds.csv"),header=None)
    return df.values.ravel()

def read_last_OD_values(pe):
    def strtoint(s):
        try:
            return float(s)
        except:
            return None

    df=pd.read_csv(pe.OD_measurement.od_file,index_col=0)
    lastvalues = [0,0,0,0,0,0,0]
    for t in range(7):
        try:
            ODvalues=list(strtoint(s) for s in df.iloc[:,t])
            ODvalues=[od for od in ODvalues if od]
            lastvalues[t]=ODvalues[-1]
        except:
            pass
    return np.array(lastvalues)

def read_death_volumes(pe):
    df=pd.read_csv(os.path.join(pe.name,"death_volumes.csv"),header=None)
    return df.values.ravel()

def make_dilution(pe,tube,death_volume=0, peace_volume=0,extra_vacuum=5):
    pe.mix(30)
    if death_volume>0:
        pe.Pumps.pump_death(tube, death_volume)
    if peace_volume>0:
        pe.Pumps.pump_peace(tube, peace_volume)
    pe.Pumps.pump_vacuum(tube, death_volume+peace_volume)
    pe.mix(0)
    pe.Pumps.pump_vacuum(tube, extra_vacuum)
    pe.mix(30)

def dilute_if_necessary(total_dilution_volume=10):
    # thresholds = read_thresholds_from_file()  # 7 OD thresholds
    # lastODvalues = read_last_OD_values()  # 7 OD values
    # death_volumes = read_death_volumes()  # 7 death volumes
    # peace_volumes = total_dilution_volume - death_volumes
    for tube in range(7):
        if lastODvalues[tube] > thresholds[tube]:
            make_dilution(tube,
                          death_volume = death_volumes[tube],
                          peace_volume = peace_volumes[tube],
                          extra_vacuum = 5)

def pause_mixers_and_measure_OD(pe,mixer_speed):
    pe.mix(mixer_speed)
    time.sleep(2)
    pe.mix(0)
    time.sleep(3)
    for t in range(7):
        pe.lastODvalues[t]=pe.OD_measurement.measure_OD(t)
    pe.mix(mixer_speed)

def start_experiment(pe,total_dilution_volume=10,mixer_speed=30,active_tubes=[0,1,2,3,4,5,6]):
    schedule.clear()
    print("Starting Experiment loop")
    pe.lastODvalues = np.array([None]*7)
    pe.mix(30)
    schedule.every().minute.at(":00").do(pause_mixers_and_measure_OD(pe,mixer_speed=mixer_speed))
    schedule.every().minute.at(":15").do(dilute_if_necessary)

    while True:
        if not os.path.exists(os.path.join(pe.name, "stop.status")):
            schedule.run_pending()
            time.sleep(1)
        else:
            print("Loop aborted with stop.status file")
            break