# Trilha original (sem direito autoral): pad grave em lá menor + pulso suave, 15,2 s.
import numpy as np, wave, sys
SR=44100; T=15.2; t=np.arange(int(SR*T))/SR
def note(f): return 440*2**((f-69)/12)
def pad(freqs,a,b):
    y=np.zeros_like(t); m=(t>=a)&(t<b); tt=t[m]-a; d=b-a
    env=np.minimum(1,tt/1.2)*np.minimum(1,(d-tt)/1.0)
    for f in freqs:
        for det in(-.25,.25):
            ff=f+det; y[m]+=env*(np.sin(2*np.pi*ff*tt)+.3*np.sin(2*np.pi*2*ff*tt))/len(freqs)
    return y
prog=[([45,52,57,60],0,4.2),([41,48,53,57],3.8,8.0),([48,55,60,64],7.6,11.8),([43,50,55,59],11.4,15.2)]
y=sum(pad([note(n) for n in c],a,b) for c,a,b in prog)
# pulso grave a 72 bpm
bp=60/72; k=np.zeros_like(t)
for s in np.arange(0.4,T,bp):
    m=(t>=s)&(t<s+.5); tt=t[m]-s
    k[m]+=np.sin(2*np.pi*(55*np.exp(-tt*6)+38)*tt)*np.exp(-tt*7)
# notas soltas agudas, espaçadas
pl=np.zeros_like(t)
for s,n in [(1.2,76),(3.6,72),(5.9,74),(8.3,71),(10.6,72),(12.9,69)]:
    m=(t>=s)&(t<s+2.5); tt=t[m]-s
    pl[m]+=np.sin(2*np.pi*note(n)*tt)*np.exp(-tt*2.2)*.35
mix=.55*y+.5*k+pl
mix*=np.minimum(1,t/1.0)*np.minimum(1,(T-t)/1.2)
mix/=np.abs(mix).max()*1.12
d=(mix*32767).astype(np.int16)
with wave.open(sys.argv[1],'wb') as w:
    w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes(d.tobytes())
