# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:12:23 2020

@author: Amin
"""

from ..Utils import Simulator
from .dNMF import dNMF

def demix_simulated_video():
    video,positions,traces = Simulator.generate_quadratic_video(K=20,T=30,sz=[100,100,5],\
                                        varfact=9,traj_variances=[0.0001,0.0001,0.0000001],\
                                        density=.9,bg_noise=.0001)
    dnmf, dvideo = dNMF.optimize_sequential(video,initial_p=positions[:,:,0],radius=10,step_S=.0,\
                                            gamma=.0,sigma_inv=.1,lr=.000001,n_iter=40,c_iter=2,use_gpu=False,\
                                            dscale=(1,1,1,1),batchsize=13,overlap=3)
    
    return dnmf, dvideo