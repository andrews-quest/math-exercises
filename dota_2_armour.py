import matplotlib.pyplot as plt
import numpy as np

HP = 700
DMG = 62

arm_vals = []
dmg_factor_vals = []
dmg_done_vals = []
hits_to_kill_vals = []



def dmg_factor(armour):
    return (1-((0.06*armour)/(1+00.6*armour)))

for armour in range(0, 50):
    arm_vals.append(armour)
    dmg_factor_vals.append(dmg_factor(armour))
    dmg_done_vals.append(DMG * dmg_factor(armour))
    hits_to_kill_vals.append(HP / dmg_done_vals[-1])

# plt.style.use('seaborn')
fig, ax = plt.subplots(nrows=1, ncols= 3, figsize=(15,5))
ax[0].plot(arm_vals, dmg_factor_vals, label="Damage factor", color="#FF8855")
ax[1].plot(arm_vals, dmg_done_vals, label="Damage done", color="#FF0000")
ax[2].plot(arm_vals, hits_to_kill_vals, label="Hits to kill", color="#01FF08")

for a in ax:
    a.legend()
    # a.set_aspect(1)
plt.tight_layout()
plt.show()

