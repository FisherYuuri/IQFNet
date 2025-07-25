import torch

class DataPrefetcher(object):
    def __init__(self, loader):
        self.loader = iter(loader)
        self.stream = torch.cuda.Stream()
        self.preload()

    def preload(self):
        try:
            self.next_rgb, self.next_t, self.next_d, self.next_eg, self.next_gt,_,_ = next(self.loader)
        except StopIteration:
            self.next_rgb = None
            self.next_t = None
            self.next_d = None
            self.next_eg = None
            self.next_gt = None
            return

        with torch.cuda.stream(self.stream):
            self.next_rgb = self.next_rgb.cuda(non_blocking=True).float()
            self.next_t = self.next_t.cuda(non_blocking=True).float()
            self.next_d = self.next_d.cuda(non_blocking=True).float()
            self.next_eg = self.next_eg.cuda(non_blocking=True).float()
            self.next_gt = self.next_gt.cuda(non_blocking=True).float()
            #self.next_rgb = self.next_rgb #if need
            #self.next_t = self.next_t #if need
            #self.next_gt = self.next_gt  # if need

    def next(self):
        torch.cuda.current_stream().wait_stream(self.stream)
        rgb = self.next_rgb
        t = self.next_t
        d = self.next_d
        eg = self.next_eg
        gt = self.next_gt
        self.preload()
        return rgb, t, d, eg, gt

class VMDataPrefetcher(object):
    def __init__(self, loader):
        self.loader = iter(loader)
        self.stream = torch.cuda.Stream()
        self.preload()

    def preload(self):
        try:
            self.next_rgb, self.next_m, self.next_gt,_,_ = next(self.loader)
        except StopIteration:
            self.next_rgb = None
            self.next_m = None
            self.next_gt = None
            return

        with torch.cuda.stream(self.stream):
            self.next_rgb = self.next_rgb.cuda(non_blocking=True).float()
            self.next_m = self.next_m.cuda(non_blocking=True).float()
            self.next_gt = self.next_gt.cuda(non_blocking=True).float()

    def next(self):
        torch.cuda.current_stream().wait_stream(self.stream)
        rgb = self.next_rgb
        m = self.next_m
        gt = self.next_gt
        self.preload()
        return rgb, m, gt
