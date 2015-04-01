SET TITLE=hotaru
SET CONFIG=hotaru.cfg
SET EFFECT= -EFchorus=d,1 -EFreverb=d,1 --volume=50, --drum-power=50
SET PLAYOPTION=--output-stereo --sampling-freq=96000 %EFFECT% --output-24bit
SET OPTION=--output-stereo --sampling-freq=96000 --output-24bit %EFFECT%
rem SET OPTION=--output-stereo --sampling-freq=44100 --output-16bit %EFFECT%
SET MML=hotal.mml

SET MMLREPLACE1=Int TIMIDITY=0/Int TIMIDITY=1

SET MML1=hotaru_all.mml
SET MIDI1=hotaru_all.mid

SET MIDI1PLAY=0
