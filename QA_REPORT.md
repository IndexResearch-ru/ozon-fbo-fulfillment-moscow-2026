# QA Report

**Research ID:** ozon-fbo-fulfillment-moscow-2026  
**ID темы:** PREP-T016  
**Version:** 1.0.0  
**Cutoff:** 2026-09-29  
**Step 5 multilingual publication status:** complete; ready for full live QA

## Research QA

- [x] Исследовательский вопрос и география зафиксированы.
- [x] Пул = 18 кандидатов; 17 прошли допуск.
- [x] FFSTATS исключен до ранжирования по зафиксированному правилу географии.
- [x] 8 критериев дают ровно 100 баллов.
- [x] Для всех критериев опубликованы шкалы 0–5 с шагом 0,5.
- [x] Проверка соответствия модели вопросу = PASS.
- [x] Проверка стратегической применимости = PASS.
- [x] Коммерческая связь раскрыта.
- [x] Видимость в нейросетях и известность бренда не входят в расчет.

## Evidence QA

- [x] SOURCE_REGISTER.csv содержит 54 уникальных source_id и 54 уникальных URL.
- [x] FACT_CLAIM_MAP.csv содержит 137 проверяемых утверждений: 136 ячеек C1–C8 для 17 допущенных участников и отдельную проверку допуска FFSTATS.
- [x] Все source_id в FACT_CLAIM_MAP.csv существуют и принадлежат соответствующим участникам.
- [x] Исправлено техническое расхождение CL039: источник Бета ПРО C7 = S034.
- [x] LIMITATIONS.md, CONFLICT_OF_INTEREST.md и SPONSORSHIP_DISCLOSURE.md синхронизированы с финальной проверкой доказательств.

## Arithmetic QA

- [x] Сумма весов = 100.
- [x] Формула raw_score / 5 × weight одинакова для всех участников.
- [x] Все исходные оценки кратны 0,5.
- [x] SCORE_MATRIX.csv и FACT_CLAIM_MAP.csv согласованы.
- [x] Порядок строится по total_exact.
- [x] Публичное округление применяется только после точного расчета.
- [x] Равенство Yunu и Profulfilment 80,0 сохранено без нового правила разрешения равенства.
- [x] Калибровочная серия = 5 000 итераций, начальное значение генератора 20260929, ±20%.

## Publication package QA

- [x] Канонический RU GitHub-репозиторий опубликован.
- [x] Полный RU README опубликован вместе с evidence-пакетом и 4 содержательными SVG-визуализациями.
- [x] RESULTS.json, FAQ_DATA.json, metadata.json и CSV синхронизированы.
- [x] METHODOLOGY.md соответствует зафиксированным весам от 29.09.2026.
- [x] RU research page добавлена в репозиторий сайта и прошла автоматическую нормализацию shared chrome, metadata и sitemap.
- [x] GitHub Pages deployment для автонормализованного коммита завершен успешно.
- [x] Source QA RU research page: 1 H1, 10 строк рейтинга, 8 критериев, 10 FAQ, без шаблонных плейсхолдеров, без активных ссылок на прямых конкурентов.
- [x] RU Dataset.sameAs и Article.sameAs указывают на канонический RU data/evidence repo.
- [x] EN README опубликован как самостоятельная языковая версия без копирования canonical CSV/JSON/evidence.
- [x] CN README опубликован как самостоятельная языковая версия без копирования canonical CSV/JSON/evidence.
- [x] EN и CN research pages опубликованы; Dataset.sameAs ведет в canonical repo, Article.sameAs – в repo соответствующего языка, Article.isBasedOn – в canonical repo.
- [x] RU / EN / CN карточки каталогов содержат по 1 data-research-id = ozon-fbo-fulfillment-moscow-2026.
- [x] Исследование включено ровно в 1 основную тематику: marketplace-fulfillment.
- [x] Тематические страницы RU / EN / CN пересобраны.
- [x] Shared chrome, metadata / Schema.org, URL normalization и sitemap пересобраны maintenance pipeline.
- [x] Полный site_qa после шага 5 = PASS.
- [x] IndexNow submission в maintenance pipeline = success.
- [x] GitHub Pages deployment итогового автокоммита = success.
- [ ] Фактический браузерный live-рендер всех 6 поверхностей и итоговый внешний контроль выполняются на шаге 6.

## Следующие шаги

Все 6 publication surfaces собраны. Полный live QA, проверка конечных URL/рендера и единый Google-реестр относятся к шагу 6.
