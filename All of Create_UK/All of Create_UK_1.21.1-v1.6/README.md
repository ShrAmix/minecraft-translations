# All of Create — Українська локалізація | v1.6 / 1.21.1

Переклад зборки **All of Create** версії 1.6 для Minecraft 1.21.1.

---

## 📁 Структура перекладу

```
All of Create_UK_1.21.1-v1.6/
├── quests/                        ← Квести (FTB Quests)
│   ├── chapters/                  ← 18 файлів розділів з текстом завдань
│   │   ├── create.snbt            ← Основний розділ Create (~2500 рядків)
│   │   ├── new_age.snbt
│   │   ├── welcome.snbt
│   │   └── ... (ще 15 файлів)
│   ├── lang/
│   │   └── en_us.snbt             ← Централізовані назви/описи квестів
│   ├── chapter_groups.snbt        ← Назви груп розділів
│   └── data.snbt
└── resourcepacks/                 ← Переклади модів (назви предметів, блоків, підказки)
    ├── boatload/                  ← Boatload (човни)
    ├── cmpackagecouriers/         ← Create: More Package Couriers
    ├── create_blaze_burner_fuels/ ← Create: Blaze Burner Fuels
    ├── create_chocolate_fountain/ ← Create: Chocolate Fountain
    ├── create_pattern_schematics/ ← Create: Pattern Schematics
    ├── create_sa/                 ← Create: Stuff & Additions (~15000 рядків!)
    ├── create_train_parts/        ← Create: Train Parts
    ├── create_vibrant_vaults/     ← Create: Vibrant Vaults
    ├── createtransmission/        ← Create: Transmission
    ├── handcrafted/               ← Handcrafted (меблі)
    ├── idas/                      ← IDAS
    ├── sliceanddice/              ← Slice & Dice
    ├── trading_floor/             ← Trading Floor
    └── tradingpost/               ← Trading Post
```

---

## 🔧 Як встановити

### Квести
Скопіюй вміст папки `quests/` в:
```
[Папка зборки]/config/ftbquests/quests/
```
(з заміною файлів)

### Переклади модів
Для кожної папки в `resourcepacks/` — це окремий ресурс-пак.
Скопіюй їх в:
```
[Папка зборки]/resourcepacks/
```
Потім увімкни їх у грі: **Options → Resource Packs**

---

## 📊 Пріоритет перекладу

| Файл | Розмір | Пріоритет |
|------|--------|-----------|
| `quests/lang/en_us.snbt` | 640 рядків | 🔴 Спочатку це |
| `quests/chapters/create.snbt` | ~2500 рядків | 🔴 Основний розділ |
| `resourcepacks/create_sa/` | ~15000 рядків | 🟡 Великий мод |
| `resourcepacks/create_vibrant_vaults/` | ~1300 рядків | 🟡 |
| `resourcepacks/handcrafted/` | ~23000 рядків | 🟠 Меблі (не критично) |
| Інші квест-файли | по 200-700 рядків | 🔴 |

---

## ⚠️ Важливо при перекладі

- У `.snbt` файлах не чіпай ключі (id, uuid), змінюй тільки текст у лапках після `title:`, `description:`, `subtitle:`
- У `.json` файлах не чіпай ключі зліва від `:`, змінюй тільки значення справа
- Формат кольорів у квестах: `&6Текст&r` — не видаляй ці коди
