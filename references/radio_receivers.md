# Radio Receivers 

### Tuned Radio Frequency (TRF) Receiver

The general design principle of a T R F receiver is shown in the block diagram below

![TRF.png](https://github.com/sabSAThai/Advitiya/blob/master/images/TRF.png)

- The radio frequency waves picked up by the aerial are first fed to the tuned input circuit of the
receiver this circuit being coupled to the aerial.
- The input circuit tuned to the frequency of the incoming signal, provides a certain amount of amplification and also gives some preliminary selectivity, separating the signal of a desired radio station from the signals of numerous other stations simultaneously picked up by the receiving aerial.
- The radio frequency voltage built up across the tuned circuit at the input of the receiver is then
applied to the first stage of RF amplification. The RF amplifier usually consists of not more than
two stages.
- Having passed through the RE amplifier, the amplified RF signal reaches the detector stage where
it is rectified.
- The low frequency (audio frequency) signal developed at the output of the detector is, next,
amplified in AF amplifier stages. The output of AF amplifier feeds the loudspeaker or a pair of
earphones.



### Superheterodyne Receiver 

A superheterodyne receiver is a type of radio receiver that uses frequency mixing to convert a received signal to a fixed intermediate frequency (IF) which can be more conveniently processed than the original carrier frequency. 

This form of receiver is based around the idea of mixing signals in a non-linear fashion. This idea was first noticed when beats were detected between two signals. 

![hetero_receiver.png](https://github.com/sabSAThai/Advitiya/blob/master/images/hetero_receiver.png)

**RF amplifier stage**
The radio waves from various broadcasting stations are intercepted by the
receiving aerial and are coupled to this stage. This stage selects the desired radio wave (using a
tuned circuit) and raises the strength of the wave to the desired level.

**Mixer stage**
The amplified output of RF amplifier is fed to the mixer stage where it is combined
with the output of a local oscillator. The two frequencies beat together and produce an intermediate
frequency (IF). 

**Local Oscillator**
The locally generated oscillations in a superhetrodyne receiver are usually of a frequency higher than the frequency of the incoming signals.

**IF amplifier stage**  
The output of mixer is always 455 kHz and is fed to fixed tuned IF amplifiers.
These amplifiers are tuned to one frequency (i.e. 455 kHz) and render nice amplification.

**Detector Stage**
Here, the audio signal is extracted from the IF output. Usually, diode detector circuit is used
because of its low distortion and excellent audio fidelity.

![AM_diode.png](https://github.com/sabSAThai/Advitiya/blob/master/images/AM_diode.png)

The rectified modulated wave contains radio frequency and the signal and cannot be fed to the
speaker for sound reproduction. The RF Component is filtered by the capacitor C shunted
across the speaker. The result is that the RF components are by-passed by the capacitor C and the signal is passed on to the speaker for sound reproduction. 

**AF amplifier stage**
The audio signal output of detector stage is fed to a multistage audio
amplifier. Here, the signal is amplified until it is sufficiently strong to drive the speaker.


#### Advantages of a Superheterodyne Receiver over T.R.F

- The Superhetrodyne receiver is having good sensitivity. This is because of the fact that the
signal, after the frequency conversion is amplified at a single and convenient, frequency for
amplification.
-  The selectivity is good as the IF amplifier stages use tuned stages with good selectivity and
required bandwidth.
- Continuous tuning is limited to the three tuned circuits namely the R.F. amplifier, Mixer
(frequency converter) and the local oscillator. 
-  The fidelity of the receiver will be better as the band with of the I. F amplifier is of the required
value.
- The R.F amplifier stage improves signal to noise ratio, reduces I.E interference and it offers a
better coupling between antenna and the input of the receiver


