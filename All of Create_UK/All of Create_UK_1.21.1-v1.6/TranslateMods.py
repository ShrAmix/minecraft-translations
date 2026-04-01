import os
import json
import time
import sys
import re  # <--- ОСЬ ЦЕЙ РЯДОК БУВ ПРОПУЩЕНИЙ
from google import genai
from google.genai import types
# --- НАЛАШТУВАННЯ ---
API_KEY = "AIzaSyCNuqHE4EQboCa-GcJHobyHR-c77HZgUjM"  # Встав свій ключ
TARGET_LANG = "Ukrainian"
ASSETS_PATH = "." # Працює в поточній папці та ВСІХ її підпапках
HISTORY_FILE = "quest_translated_history.log"
MODEL_ID = "gemini-3.1-flash-lite-preview" 

client = genai.Client(api_key=API_KEY)

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f)
    return set()

def save_to_history(filepath):
    with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{filepath}\n")

def contains_cyrillic(text):
    """Швидка локальна перевірка, чи є в тексті українські літери."""
    return bool(re.search('[а-яА-ЯіІїЇєЄґҐ]', str(text)))

def is_already_translated_locally(quest_data):
    """Перевіряє, чи є український текст у файлі, щоб не витрачати запити API."""
    data_str = json.dumps(quest_data, ensure_ascii=False)
    return contains_cyrillic(data_str)

def translate_quest(quest_data):
    """Відправляє квест до ШІ з інструкцією повернути статус, якщо вже перекладено."""
    sys_instr = f"""You are a Minecraft RPG Quest localizer. Target Language: {TARGET_LANG}.
    CRITICAL RULES:
    1. Translate ONLY narrative text: 'text' fields inside 'title' and 'description', dialogues, and readable text inside NBT strings (like 'Name' or 'Lore').
    2. DO NOT translate JSON keys, item IDs (e.g., 'minecraft:iron_chestplate'), or commands (starting with '/').
    3. Keep exact JSON structure and formatting.
    4. IF the narrative text is ALREADY in {TARGET_LANG}, return EXACTLY this JSON: {{"status": "already_translated"}}
    5. Otherwise, return ONLY the translated JSON."""
    
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=json.dumps(quest_data, ensure_ascii=False),
            config=types.GenerateContentConfig(
                system_instruction=sys_instr,
                response_mime_type="application/json",
                temperature=0.1
            )
        )
        return json.loads(response.text)
    except Exception as e:
        err_msg = str(e)
        if "429" in err_msg or "503" in err_msg:
            wait_time = 60 if "429" in err_msg else 15
            reason = "ЛІМІТ" if "429" in err_msg else "ПЕРЕВАНТАЖЕННЯ"
            print(f"\n   ⏳ {reason}. Сплю {wait_time} сек...")
            time.sleep(wait_time)
            return "RETRY"
        print(f"\n   🔴 Помилка API: {err_msg[:150]}")
        return None

def main():
    history = load_history()
    
    # Збираємо файли з УСІХ підпапок (рекурсивно)
    targets = []
    for root, dirs, files in os.walk(ASSETS_PATH):
        for file in files:
            if file.endswith('.json'):
                targets.append(os.path.join(root, file))
    
    print(f"🌟 Старт Квест-Локалізатора. Модель: {MODEL_ID} | Знайдено файлів: {len(targets)}")

    for path in targets:
        # Робимо гарний відносний шлях для логів (напр., quests/quest_0000/root.json)
        rel_path = os.path.relpath(path, ASSETS_PATH).replace("\\", "/")
        
        if rel_path in history: 
            continue

        print(f"\n📜 КВЕСТ: [{rel_path}]")
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                quest_data = json.load(f, strict=False)
        except Exception as e:
            print(f"   ❌ Файл битий! Пропускаю. (Error: {e})")
            continue
            
        # 1. Швидка локальна перевірка (економить ліміти!)
        if is_already_translated_locally(quest_data):
            print(f"   ⏩ Пропускаю: вже містить український текст (локальна перевірка).")
            save_to_history(rel_path)
            continue
        
        # 2. Відправка до ШІ
        while True:
            print(f"   ⏳ Перекладаю...", end="\r")
            res = translate_quest(quest_data)
            
            if res == "RETRY":
                continue 
            
            elif res:
                # Перевірка на відповідь ШІ про те, що файл вже перекладено
                if res.get("status") == "already_translated":
                    print(f"   ⏩ Пропускаю: ШІ підтвердив, що текст вже перекладено.")
                    save_to_history(rel_path)
                    time.sleep(1)
                    break

                # Зберігаємо файл (ПЕРЕЗАПИСУЄМО ОРИГІНАЛ)
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(res, f, indent=4, ensure_ascii=False)
                
                save_to_history(rel_path)
                print(f"   ✅ Готово! Файл перезаписано.")
                time.sleep(1.5) # Пауза для стабільності
                break
            else:
                print(f"   🛑 Помилка. Пропускаю цей квест.")
                break

if __name__ == "__main__":
    main()