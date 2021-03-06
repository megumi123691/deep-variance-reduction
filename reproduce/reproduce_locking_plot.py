# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
import os
import sys
import run

transform_locking = [True, False]

try:
    pindex = int(sys.argv[1])
    print(f"problem index {pindex}")
except:
    pindex = 0

locking = transform_locking[pindex]
runargs = {
    'transform_locking': locking,
    'problem': 'cifar10',
    'architecture': 'default',
    'method': "svrg",
    'logfname': 'reproduce-transform-locking-{}'.format(locking),
    'momentum': 0.9,
    'decay': 0.0001,
    'lr': 0.1,
    'lr_reduction': "150-225",
    'batch_size': 128,
    'epochs': 3,
    'log_diagnostics': True,
    'log_diagnostics_every_epoch': True,
    'log_diagnostics_deciles': True,
    }

run.run(runargs)
