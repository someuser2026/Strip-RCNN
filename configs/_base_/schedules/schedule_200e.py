# evaluation
evaluation = dict(interval=1, metric='mAP')
# optimizer
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=dict(max_norm=35, norm_type=2))
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=1.0 / 3,
    step=[20, 40, 60])
runner = dict(type='EpochBasedRunner', max_epochs=200)
checkpoint_config = dict(interval=20, max_keep_ckpts=2)
# evaluation = dict(save_best = True)
