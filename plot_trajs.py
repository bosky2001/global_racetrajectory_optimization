import frictionmap
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
plt.figure()

plt.grid()
ax = plt.gca()
ax.set_aspect("equal", "datalim")
plt.xlabel("east in m")
plt.ylabel("north in m")

track_name = 'berlin_2018'
filename_tpamap = 'berlin_2018_tpamap.csv'
filename_tpadata = 'berlin_2018_varmue08-12_tpadata.json'
frictionmap.src.plot_frictionmap_data.plot_tpamap_fromFile(track_name, filename_tpamap, filename_tpadata)


path2traj1 = "outputs/traj_race_cl.csv"
# load friction map
with open(path2traj1, 'rb') as fh:
    traj1 = np.loadtxt(fh, comments='#', delimiter=';')


path2traj2 = "outputs/traj_race_cl_berlin08var.csv"
# load friction map
with open(path2traj2, 'rb') as fh:
    traj2 = np.loadtxt(fh, comments='#', delimiter=';')

print(traj1.shape)
plt.plot(traj1[:, 1], traj1[:, 2], "crimson", linewidth=1.2, label=' no var-mue')

print(traj2.shape)
plt.plot(traj2[:, 1], traj2[:, 2], "cyan", linewidth=1.2, label='with var-mue')
plt.legend()
plt.show()


# path2tf_var = "outputs/mintime/tire_forces_berlin08var.csv"
# with open(path2tf_var, 'rb') as fh:
#     tf_var = np.loadtxt(fh, comments='#', delimiter=';')

# path2tf = "outputs/mintime/tire_forces.csv"
# with open(path2tf, 'rb') as fh:
#     tf = np.loadtxt(fh, comments='#', delimiter=';')

# # print(tf_var.shape)
# # print(tf.shape)


# path2controlvar = "outputs/mintime/controls_berlin08var.csv"
# with open(path2controlvar, 'rb') as fh:
#     control_var = np.loadtxt(fh, comments='#', delimiter=';')

# path2control = "outputs/mintime/controls.csv"
# with open(path2control, 'rb') as fh:
#     control = np.loadtxt(fh, comments='#', delimiter=';')
# # plt.figure()
# fig, axs = plt.subplots(2, 2)
# # fl
# axs[0,0].plot(tf[:, 4], label='constant friction')
# axs[0,0].plot(tf_var[:, 4], label='varying friction')
# axs[0,0].legend()
# axs[0,0].set_title("Front Left")
# # fr
# axs[0,1].plot(tf[:, 7], label='constant friction')
# axs[0,1].plot(tf_var[:, 7], label='varying friction')
# axs[0,1].set_title("Front Right")
# axs[0,1].legend()
# # rl
# axs[1,0].plot(tf[:, 10], label='constant friction')
# axs[1,0].plot(tf_var[:, 10], label='varying friction')
# axs[1,0].set_title("Rear Left")
# axs[1,0].legend()
# # rr
# axs[1,1].plot(tf[:, 13], label='constant friction')
# axs[1,1].plot(tf_var[:, 13], label='varying friction')
# axs[1,1].set_title("Rear Right")
# axs[1,1].legend()
# plt.show()
# # gs = axs[2, 0].get_gridspec()
# # for ax in axs[2, :]:
# #     ax.remove()

# # axsbig = fig.add_subplot(gs[2, :])

# # axsbig.plot(control[:, 3], label='constant friction')
# # axsbig.plot(control_var[:, 3], label="varying friction")
# # axsbig.legend()
# # axsbig.set_title("")
# # plt.figure()
# fig, axs = plt.subplots(3, 1)
# axs[0].plot(control[:, 3], label='constant friction')
# axs[0].plot(control_var[:, 3], label="varying friction")
# axs[0].legend()
# axs[0].set_title("driving force")

# axs[1].plot(control[:, 4], label='constant friction')
# axs[1].plot(control_var[:, 4], label="varying friction")
# axs[1].set_title("braking force")
# axs[1].legend()

# axs[2].plot(control[:, 5], label='constant friction')
# axs[2].plot(control_var[:, 5], label="varying friction")
# axs[2].set_title("wheel transfer load")
# axs[2].legend()
# plt.show()




## no var_mue laptime 85.76s /85.858s with var_mue  87.12/87.214

