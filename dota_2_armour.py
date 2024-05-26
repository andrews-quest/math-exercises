import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

HP = 700
DMG = 62

arm_vals = []

dmg_factor_vals = []
dmg_factor_wrong_vals = []

dmg_done_vals = []
dmg_done_wrong_vals = []

hits_to_kill_vals = []
hits_to_kill_wrong_vals = []

ehp_vals = []
ehp_wrong_vals = []
ehp_numerator = []
ehp_denominator_right = []
ehp_denominator_wrong = []



def dmg_factor(armour):
    return 1-(0.06*armour)/(1+0.06*abs(armour))

def dmg_factor_wrong(armour):
    return 1-(0.06*armour)/(1+0.06*armour)

for armour in range(-50, 50):
    arm_vals.append(armour)
    dmg_factor_vals.append(dmg_factor(armour))
    dmg_factor_wrong_vals.append(dmg_factor_wrong(armour))
    dmg_done_vals.append(DMG * dmg_factor(armour))
    hits_to_kill_vals.append(HP / dmg_done_vals[-1])
    # hits_to_kill_wrong_vals.append(HP / dmg_done_wrong_vals[-1])
    ehp_vals.append(HP / dmg_factor(armour))
    ehp_wrong_vals.append(HP / dmg_factor_wrong(armour))
    ehp_numerator.append(0.06*(armour))
    ehp_denominator_right.append(1+0.06*abs(armour))
    ehp_denominator_wrong.append(1+0.06*armour)

plt.style.use('seaborn-v0_8-dark')
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
ax[0][0].set_ylim(-2, 2)
# ax[0][0].set_aspect('equal', 'box')
ax[0][0].plot(arm_vals, dmg_factor_vals, label="Damage factor", color="#FF8855")
ax[0][0].plot(arm_vals, dmg_factor_wrong_vals, label="Damage factor - wrong", color="#FF22AA")
ax[0][0].plot(arm_vals, ehp_numerator, label="EHP - numberator", color="#040F13")
ax[0][0].plot(arm_vals, ehp_denominator_wrong, label="EHP - wrong denominator", color="#11A011")
ax[0][0].plot(arm_vals, ehp_denominator_right, label="EHP - true denominator", color="#BB0011", linestyle="--")
ax[0][0].plot(arm_vals, [1 for i in range(-50,50)], color="#0000FF", linestyle="--")
ax[0][0].plot(arm_vals, [0 for i in range(-50,50)], color="#0000FF",  linestyle="--")

ax[0][1].plot(arm_vals, dmg_done_vals, label="Damage done", color="#FF0000")
ax[0][1].plot(arm_vals, [DMG for i in range(-50,50)], color="#0000FF")
ax[0][1].plot(arm_vals, [0 for i in range(-50,50)], color="#0000FF")

ax[1][0].plot(arm_vals, hits_to_kill_vals, label="Hits to kill", color="#01FF08")
# ax[1][0].plot(arm_vals, hits_to_kill_wrong_vals, label="Hits to kill - wrong", color="#A1FF06")
ax[1][0].plot(arm_vals, [HP/DMG for i in range(-50,50)], color="#0000FF")
ax[1][0].plot(arm_vals, [0 for i in range(-50,50)], color="#0000FF")

ax[1][1].plot(arm_vals, ehp_vals, label="EHP", color="#00AAFF")
ax[1][1].plot(arm_vals, ehp_wrong_vals, label="EHP - wrong", color="#11AA11")
ax[1][1].plot(arm_vals, [HP for i in range(-50,50)], color="#0000FF")
ax[1][1].plot(arm_vals, [0 for i in range(-50,50)], color="#0000FF")

for a in ax:
    a[0].legend()
    a[1].legend()
    # a.set_aspect()
plt.tight_layout()
plt.show()

