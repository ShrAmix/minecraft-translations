# 💰 Як налаштувати донат-посилання

Цей файл описує як підключити всі популярні платформи для донатів.
Після налаштування — заміни посилання-заглушки в `README.md`.

---

## 1. Buy Me a Coffee (найпростіше)

**Сайт:** https://buymeacoffee.com

1. Реєструєшся → вказуєш нікнейм (наприклад `yourname`)
2. Твоє посилання: `https://buymeacoffee.com/yourname`
3. Підтримує PayPal і картки — донатери з усього світу можуть платити
4. Комісія: ~5% + комісія платіжної системи
5. Виведення: на PayPal або банківський рахунок

**Вставити в README:**
```md
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-donate-yellow)](https://buymeacoffee.com/yourname)
```

---

## 2. Ko-fi (без комісії на разові донати)

**Сайт:** https://ko-fi.com

1. Реєструєшся → нікнейм → підключаєш PayPal або Stripe
2. Твоє посилання: `https://ko-fi.com/yourname`
3. **0% комісії** на разові донати (Ko-fi заробляє тільки на підписках)
4. Виведення: через PayPal або Stripe

**Вставити в README:**
```md
[![Ko-fi](https://img.shields.io/badge/Ko--fi-donate-blue)](https://ko-fi.com/yourname)
```

---

## 3. PayPal.me (пряме посилання)

**Сайт:** https://paypal.me

1. Треба мати обліковий запис PayPal (реєстрація на paypal.com)
2. Заходиш на paypal.me → Create your PayPal.Me link
3. Вводиш нікнейм → отримуєш: `https://paypal.me/yourname`
4. Можна одразу вказати суму: `https://paypal.me/yourname/5` (5 USD)
5. Гроші приходять на PayPal-рахунок, звідти — на банківську картку

> ⚠️ PayPal не завжди доступний в Україні напряму.
> Якщо є проблеми — використовуй Ko-fi, він підтримує PayPal як вихід.

---

## 4. Monobank (для українців)

Найпростіший варіант для тих хто грає з України.

**Варіант А — номер картки:**
Просто вказуєш номер картки в README. Переказ через будь-який банкінг.

**Варіант Б — посилання "Monobank Jar" (банка):**
1. В додатку Monobank → «Створити банку»
2. Встановлюєш назву, мету, фото
3. Копіюєш посилання на банку (вигляд: `https://send.monobank.ua/jar/XXXXXXXX`)
4. Вставляєш в README

**Варіант В — Monobank картка як QR:**
В додатку → картка → поділитись → QR-код.
Можна додати QR як картинку в репозиторій.

---

## 5. GitHub Sponsors (якщо хочеш все в одному місці)

**Сайт:** https://github.com/sponsors

1. Заходиш на github.com → Settings → Sponsorship
2. Заповнюєш анкету (потрібна верифікація — займає кілька днів)
3. Після схвалення на твоєму профілі з'являється кнопка "Sponsor"
4. Виведення через Stripe (потрібна картка що підтримує Stripe)

> Це найпрестижніший варіант для open-source, але потребує верифікації.

---

## Що вибрати?

| Ситуація | Рекомендація |
|----------|-------------|
| Хочеш найпростіше | **Buy Me a Coffee** |
| Хочеш без комісії | **Ko-fi** |
| Для гравців з України | **Monobank Jar** |
| Хочеш міжнародні перекази | **PayPal.me** + **Ko-fi** |
| Повноцінна підтримка | Всі чотири разом |

---

## Шаблон для README (вставити після налаштування)

```md
## 💛 Підтримати переклади

| Платформа | Посилання |
|-----------|-----------|
| ☕ Buy Me a Coffee | [buymeacoffee.com/yourname](https://buymeacoffee.com/yourname) |
| 💙 Ko-fi | [ko-fi.com/yourname](https://ko-fi.com/yourname) |
| 💸 PayPal | [paypal.me/yourname](https://paypal.me/yourname) |
| 💳 Monobank | [send.monobank.ua/jar/XXXXXXXX](https://send.monobank.ua/jar/XXXXXXXX) |
```
