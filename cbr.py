import ollama
import asyncio
import edge_tts
import pygame
import os
import re

# Inisialisasi Audio Player
pygame.mixer.init()

async def speak(text):
    """Fungsi untuk mengubah teks ke suara dan memutarnya"""
    VOICE = "id-ID-GadisNeural" # Suara perempuan Indonesia yang jernih
    OUTPUT_FILE = "temp_voice.mp3"
    
    # Bersihkan teks dari markdown seperti **
    clean_text = re.sub(r'[^\w\s.,!?]', '', text)
    
    if clean_text.strip():
        communicate = edge_tts.Communicate(clean_text, VOICE)
        await communicate.save(OUTPUT_FILE)
        
        # Putar audionya
        pygame.mixer.music.load(OUTPUT_FILE)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)
        
        pygame.mixer.music.unload() 

async def main():
    while True:
        try:
            prompt = input("\nMasukkan prompt: ")

            if prompt.startswith("!think"):
                model = "aira-step-6-fcpu"
            elif prompt.startswith("!deepl"):
                model = "aira-step-6-xcpu"
            else:
                model = "aira-step-6-cpu"

            stream = ollama.chat(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                stream=True
            )

            GRAY = "\033[90m"
            RESET = "\033[0m"
            is_thinking = False
            buffer = ""

            for chunk in stream:
                msg = chunk.get('message', {})

                think_text = msg.get('thinking', '')
                content_text = msg.get('content', '')

                buffer += content_text

                # tampilkan thinking kalau ada
                if think_text:
                    if not is_thinking:
                        print(f"{GRAY}Thinking... \n", end='', flush=True)
                        is_thinking = True
                    print(f"{GRAY}{think_text}{RESET}", end='', flush=True)

                # tampilkan jawaban biasa
                if content_text:
                    if is_thinking:
                        print(f"{RESET}\n[Done Thinking]\n", end='', flush=True)
                        is_thinking = False
                    print(content_text, end='', flush=True)

                # Trigger bicara jika ketemu akhir kalimat
                if any(punc in content_text for punc in ".,:;!?\n"):
                    sentences = re.split(r'(?<=[.:;!?\n])', buffer)
                    for i in range(len(sentences) - 1):
                        sentence = sentences[i].strip()
                        if sentence:
                            await speak(sentence)
                    buffer = sentences[-1]

            if buffer.strip():
                await speak(buffer.strip())


        except KeyboardInterrupt:
            print("\n[Stream interrupted/stoped by user]")
            break

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        if os.path.exists("temp_voice.mp3"):
            os.remove("temp_voice.mp3")