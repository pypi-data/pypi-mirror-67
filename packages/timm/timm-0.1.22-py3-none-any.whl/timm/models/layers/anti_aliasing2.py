import torch
from torch import nn as nn
from torch.nn import functional as F


@torch.jit.script
def downsample_conv_jit(input: torch.Tensor, filter: torch.Tensor):
    input_pad = F.pad(input, (1, 1, 1, 1), 'reflect')
    return F.conv2d(input_pad, filter, stride=2, padding=0, groups=input.shape[1])


def downsample_conv(input: torch.Tensor, filter: torch.Tensor):
    input_pad = F.pad(input, (1, 1, 1, 1), 'reflect')
    return F.conv2d(input_pad, filter, stride=2, padding=0, groups=input.shape[1])


class AntiAliasDownsampleLayer2(nn.Module):
    def __init__(self, remove_aa_jit: bool = False, filt_size: int = 3, stride: int = 2, channels: int = 0):
        super(AntiAliasDownsampleLayer2, self).__init__()
        self.stride = stride
        self.filt_size = filt_size
        self.channels = channels
        self.use_jit = not remove_aa_jit

        assert self.filt_size == 3
        assert stride == 2
        a = torch.tensor([1., 2., 1.])
        filt = (a[:, None] * a[None, :])
        filt = filt / torch.sum(filt)
        self.register_buffer('filt', filt[None, None, :, :].repeat((self.channels, 1, 1, 1)))
        self._register_state_dict_hook(self._hk)
        self._register_load_state_dict_pre_hook(self._hkp)

    def _hk(self, module, state_dict, prefix, *args):
        del state_dict['filt']

    def _hkp(self, state_dict, prefix, *args):
        state_dict[prefix + 'filt'] = self.filt

    def forward(self, x):
        if self.use_jit:
            return downsample_conv_jit(x, self.filter)
        else:
            return downsample_conv(x, self.filter)