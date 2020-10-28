import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks
import bisect
import peakutils




df_fhr = pd.read_csv('FHRDataCol.csv', header = None)
df_ua = pd.read_csv('UADataCol.csv', header = None)


fs = 4.0
cutoff = 0.05
order = 2
nyq = 0.5 * fs

def butter_lowpass_filter(data, cutoff, fs, order):
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b,a,data)
    return y

for idx in range(200,300):

    data = df_fhr[idx]

    x = []
    for i in range(8000):
        x.append(i)
    ua = df_ua[idx]
    y = butter_lowpass_filter(data, cutoff, fs, order)
    
    # baseline stores starting point as key and baseline heart rate as value
    baseline = {}
    count = 1
    for i in range(5600):
        minute_avg = []
        for j in range(i, i+ 2400, 240):
            minute_avg.append(sum(y[j:j+240])/240)
        bounded = False
        if max(minute_avg) - min(minute_avg) < 25:
            bounded = True
        else:
            bounded = False
        if bounded == True:
            if i-1 in baseline:
                count += 1
                baseline[i] = (baseline[i-1]*(count-1) + (sum(y[i:i+2400])/2400))/count

                del baseline[i-1]
            else:
                count = 1
                baseline[i] = sum(y[i:i+2400])/2400
    baseline_data = []
    for key in baseline:
        temp1 = int(baseline[key]) // 5
        temp2 = baseline[key] % 5
        if 5.0 - temp2 < temp2: #up:
            baseline[key] = temp1 * 5 + 5
        else:
            baseline[key] = temp1 * 5
    key = list(baseline.keys())
    for i in range(8000):
        idx = bisect.bisect_left(key,i)
        if idx < len(key):
            baseline_data.append(baseline[key[idx]])
        else:
            baseline_data.append(baseline[key[-1]])



    # baseline_varia stores starting point
    baseline_varia = []

    for i in range(7760):
        temp = list(y[i:i+240].copy())
        temp_baseline = baseline_data[i:i+240].copy()
        avg_temp = sum(temp)/240
        max_idx = 0
        min_idx = 0

        if max(temp) - min(temp) >= 6 and max(temp) - min(temp) < 25 and temp_baseline[temp.index(max(temp))] < max(temp) and temp_baseline[temp.index(min(temp))] > min(temp):

            for j in range(240):
                if temp[j] == max(temp):
                    temp[j] = avg_temp
                    max_idx = j
                if temp[j] == min(temp):
                    temp[j] = avg_temp
                    min_idx = j
        if max(temp) - min(temp) >= 25 or max(temp) - min(temp) < 6 or temp_baseline[temp.index(max(temp))] > max(temp) or temp_baseline[temp.index(min(temp))] < min(temp):
            continue
        else:
            baseline_varia.append(i)
            i += max(max_idx,min_idx) - 1

    baseline_varia_y = []
    for val in baseline_varia:
        baseline_varia_y.append(y[val])




    # acceleration stores the starting point
    acceleration = []
    peak_point = []

    for i in range(7520):
        temp = y[i:i+480].copy()
        temp_peak = peakutils.peak.indexes(temp,thres = 0.4 , min_dist = 480)
        if len(temp_peak) != 0:
            temp_peak = temp_peak[0]
        else:
            continue
        if temp_peak + i in peak_point:
            continue
        else:
            if temp_peak < 120 and y[temp_peak+i] > baseline_data[temp_peak+i] + 15:
                peak_point.append(temp_peak+i)
                acceleration.append(i)

    # for val in acceleration:
    #     for i in range(120):
    #         if val + i not in acceleration:
    #             acceleration.append(val+i)
    #         else:
    #             continue
    accel_y = []
    # for i in range(8000):
    #     accel_y.append(i)
    for val in acceleration:
        accel_y.append(y[val])
    
    # baseline FHR is a period of 10min, 600s, 2400 data
    # baseline FHR variability 2 cycles per minute, 240 data
    # acceleration: one point to peak for less than 30s, 120 data
    # and duration less than 2min, 480 data
    # decceleration: tbd


    z = butter_lowpass_filter(ua, cutoff, fs, order)


    decceleration = []
    inverse_y = []
    inverse_y_temp = []
    for val in y:
        inverse_y_temp.append(val*(-1))
    inverse_y = np.asarray(inverse_y_temp)

    inver_y_peaks = peakutils.peak.indexes(inverse_y, thres=0.5, min_dist=120)
    z_peak = peakutils.peak.indexes(z, thres=0.4, min_dist=120)

    early_dec = []
    late_dec = []
    var_dec = []
    checked = False
    for val in inver_y_peaks:
        checked = False
        if val < 120 and abs(baseline_data[0] - y[0])<5:
            var_dec.append(val)
            continue
        if abs(baseline_data[val-119] - y[val-119])<5:
            var_dec.append(val)
            continue
        if abs(baseline_data[val-119] - y[val-119])>5:
            for i in range(-10,10):
                if (val+i) in z_peak and checked is False:# early
                    early_dec.append(val)
                    checked = True
                    break
            for i in range(-140,-100):
                if (val+i) in z_peak and checked is False:
                    late_dec.append(val)
                    checked = True
                    break
            continue
    early_y = []
    for val in early_dec:
        early_y.append(z[val])

    late_y = []
    for val in late_dec:
        late_y.append(z[val])
    
    var_dy = []
    for val in var_dec:
        var_dy.append(z[val])
    





    #plt.grid()
    plt.scatter(x,data,s=1, color = 'tomato', label = 'Original FHR')
    plt.plot(y,color = 'red', label = 'Filtered FHR')
    plt.plot(baseline_data, color = 'black', label = 'Baseline FHR')
    plt.scatter(baseline_varia, baseline_varia_y, s=5, color = 'blueviolet', label = 'Baseline Variable')
    plt.scatter(acceleration, accel_y,s=15, color = 'green', label = 'Acceleration')
    plt.scatter(x, ua, s=2, color = 'cyan', label = 'Original UA')
    plt.plot(z,color = 'blue', label = 'Filtered UA')
    plt.vlines(early_dec, [0]*len(early_dec),[200]*len(early_dec), linestyles = 'dotted',label = 'Early Dec', color = 'green')
    plt.vlines(late_dec, [0]*len(late_dec),[200]*len(late_dec),linestyles = 'dotted',label = 'Late Dec', color = 'yellow')
    plt.vlines(var_dec, [0]*len(var_dec),[200]*len(var_dec),linestyles = 'dotted',label = 'Variable Dec', color = 'violet')

    plt.legend(loc='best')
    plt.show()