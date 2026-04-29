# AI-TTS (CBR)

This is a <b>C</b>hat<b>B</b>ot <b>R</b>ealtime with using Python code, library ollama and liblrary edge_tts. And don't forget to `pip install ollama`, `pip install edge_tts`, install ollama and create `aira-step-6-cpu`, `aira-step-6-fcpu` and `aira-step-6-xcpu` on cmd prompt with `ollama create aira-step-6-[cpu/fcpu/xcpu] -f [your path]/aira-step-6-cpu/aira-step-6-[cpu/fcpu/xcpu]`, or u can change the models to your own models on the code.
Use this command on first prompt for using The Function,<br>
The Function:<br>
• !think [your prompt]<br>
for thinking models (using models aira-step-6-fcpu)<br>
• !deepl [your prompt]<br>
for deep thinking models (using models aira-step-6-xcpu).<br><br>

<b>NB:</b>
<b>`aira-step-6-xcpu`</b> smartes than <b>`aira-step-6-fcpu`</b>,
<b>`aira-step-6-fcpu`</b> smartes than <b>`aira-step-6-cpu`</b><br>
if the models can't create, you must `ollama pull llama3.2:1b`, `ollama pull qwen3:4b`, `ollama pull qwen3:8b`

