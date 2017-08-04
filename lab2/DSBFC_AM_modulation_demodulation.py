#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Dsbfc Am Modulation Demodulation
# Generated: Fri Aug  4 14:34:29 2017
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class DSBFC_AM_modulation_demodulation(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Dsbfc Am Modulation Demodulation")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 320000

        ##################################################
        # Blocks
        ##################################################
        self.lab2_part1 = self.lab2_part1 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.lab2_part1.AddPage(grc_wxgui.Panel(self.lab2_part1), "scope")
        self.lab2_part1.AddPage(grc_wxgui.Panel(self.lab2_part1), "fft")
        self.lab2_part1.AddPage(grc_wxgui.Panel(self.lab2_part1), "fft1")
        self.Add(self.lab2_part1)
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_f(
        	self.lab2_part1.GetPage(0).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.lab2_part1.GetPage(0).Add(self.wxgui_scopesink2_0_0.win)
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_c(
        	self.lab2_part1.GetPage(2).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.lab2_part1.GetPage(2).Add(self.wxgui_fftsink2_1.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.lab2_part1.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.lab2_part1.GetPage(1).Add(self.wxgui_fftsink2_0.win)
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 30000, 100, firdes.WIN_HAMMING, 6.76))
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(32, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.5, ))
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vcc((1, ))
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 100000, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 10000, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.dc_blocker_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.wxgui_fftsink2_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.wxgui_scopesink2_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_const_vxx_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 30000, 100, firdes.WIN_HAMMING, 6.76))
        self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_1.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = DSBFC_AM_modulation_demodulation()
    tb.Start(True)
    tb.Wait()

